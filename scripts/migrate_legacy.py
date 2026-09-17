"""Import the rescued Mathrao manuscripts without changing their source bytes.

Usage:
  python scripts/migrate_legacy.py --asset-root PATH [--audit-only]

The rescue directory and inventory default to siblings of this repository.
Only referenced, recognized static assets are copied from the old WordPress
tree. No PHP, theme, plugin, or WordPress code is executed or copied.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
import shutil
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
URL_RE = re.compile(r"https?://(?:www\.)?mathrao\.com/[^\s\"'<>]*", re.I)
ATTR_RE = re.compile(r"\b(?:src|href|poster)\s*=\s*([\"'])(.*?)\1", re.I | re.S)
SHORTCODE_RE = re.compile(r"\[(/?)([A-Za-z][A-Za-z0-9_-]*)(?=[\s\]/])[^\]]*\]")
EMBED_RE = re.compile(r"<(?:iframe|embed|object|script|form)\b", re.I)
STATIC_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".avif", ".svg", ".pdf", ".mp3", ".mp4", ".webm", ".ico"}


def read_manuscript(path: Path) -> tuple[dict, str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"Missing front matter: {path}")
    end = next((i for i, line in enumerate(lines[1:], 1) if line.strip() == "---"), None)
    if end is None:
        raise ValueError(f"Unclosed front matter: {path}")
    metadata = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        if not sep:
            raise ValueError(f"Invalid front matter line in {path}: {line[:60]!r}")
        metadata[key] = json.loads(value.strip())
    return metadata, "".join(lines[end + 1 :]), text


def normalize_path(value: str) -> str:
    return unicodedata.normalize("NFC", unquote(value)).replace("\\", "/")


def safe_asset_path(url: str) -> str | None:
    parsed = urlsplit(html.unescape(url))
    if parsed.netloc and parsed.netloc.lower() not in {"mathrao.com", "www.mathrao.com"}:
        return None
    path = normalize_path(parsed.path)
    if not (path.startswith("/images/") or path.startswith("/wp-content/uploads/")):
        return None
    if any(part in {"", ".", ".."} for part in path[1:].split("/")):
        return None
    return path


def file_kind_ok(path: Path) -> bool:
    suffix = path.suffix.lower()
    if suffix not in STATIC_SUFFIXES:
        return False
    head = path.open("rb").read(32)
    if suffix == ".png":
        return head.startswith(b"\x89PNG\r\n\x1a\n")
    if suffix in {".jpg", ".jpeg"}:
        return head.startswith(b"\xff\xd8\xff")
    if suffix == ".gif":
        return head.startswith((b"GIF87a", b"GIF89a"))
    if suffix == ".webp":
        return head.startswith(b"RIFF") and head[8:12] == b"WEBP"
    if suffix == ".pdf":
        return head.startswith(b"%PDF-")
    if suffix == ".svg":
        # SVG can contain active code and is intentionally left for manual review.
        return False
    return suffix in {".avif", ".mp3", ".mp4", ".webm", ".ico"}


def get_asset_index(asset_root: Path) -> tuple[dict[str, Path], dict[str, list[str]]]:
    exact = {}
    folded = defaultdict(list)
    for subdir in ("images", "wp-content/uploads"):
        directory = asset_root / subdir
        if not directory.is_dir():
            continue
        for file in directory.rglob("*"):
            if not file.is_file() or file.is_symlink():
                continue
            relative = "/" + file.relative_to(asset_root).as_posix()
            exact[relative] = file
            folded[relative.casefold()].append(relative)
    return exact, folded


def audit(rescue: Path, inventory: Path, asset_root: Path | None) -> dict:
    rows = list(csv.DictReader(inventory.open(encoding="utf-8-sig", newline="")))
    by_id = {int(row["wp_id"]): row for row in rows}
    if len(rows) != 309 or len(by_id) != 309:
        raise ValueError("Inventory must have 309 unique WP IDs")
    files = sorted((rescue / "content").rglob("*.md"))
    if len(files) != 309:
        raise ValueError(f"Rescue has {len(files)} Markdown files, expected 309")
    manuscripts = []
    for file in files:
        meta, body, full = read_manuscript(file)
        wp_id = meta["wp_id"]
        if wp_id not in by_id:
            raise ValueError(f"WP ID {wp_id} absent from inventory")
        row = by_id[wp_id]
        if meta["status"] != row["wp_status"]:
            raise ValueError(f"Status mismatch for WP ID {wp_id}")
        if (meta["legacy_path"] or "") != row["old_path"]:
            raise ValueError(f"Legacy path mismatch for WP ID {wp_id}")
        manuscripts.append({"file": file, "meta": meta, "body": body, "full": full})
    if len({m["meta"]["wp_id"] for m in manuscripts}) != 309:
        raise ValueError("Duplicate WP ID in rescue")

    statuses = Counter(m["meta"]["status"] for m in manuscripts)
    if statuses != {"publish": 306, "draft": 3}:
        raise ValueError(f"Unexpected statuses: {statuses}")
    published = {m["meta"]["legacy_path"]: m["meta"]["wp_id"] for m in manuscripts if m["meta"]["status"] == "publish"}
    if len(published) != 306 or None in published:
        raise ValueError("Published paths are missing or duplicated")

    exact, folded = get_asset_index(asset_root) if asset_root else ({}, {})
    asset_matches = {}
    asset_issues = []
    content_issues = []
    external_assets = []
    all_old_urls = defaultdict(set)
    shortcode_counts = Counter()
    shortcode_pages = defaultdict(set)
    all_asset_references = defaultdict(set)

    def register_asset(value: str, wp_id: int) -> None:
        path = safe_asset_path(value)
        if not path:
            return
        all_asset_references[path].add(wp_id)
        candidates = folded.get(path.casefold(), [])
        actual = path if path in exact else candidates[0] if len(candidates) == 1 else None
        if actual and file_kind_ok(exact[actual]):
            asset_matches[path] = {
                "local_path": actual,
                "match": "exact" if path == actual else "normalized",
                "source": str(exact[actual]),
            }
        else:
            reason = "missing" if not actual else "unsupported_or_invalid_type"
            issue = {"wp_id": wp_id, "url": value, "reason": reason}
            if issue not in asset_issues:
                asset_issues.append(issue)

    for manuscript in manuscripts:
        meta, body = manuscript["meta"], manuscript["body"]
        wp_id = meta["wp_id"]
        for match in URL_RE.finditer(body):
            url = match.group(0).rstrip(".,;!?，。")
            all_old_urls[url].add(wp_id)
            register_asset(url, wp_id)
        for match in ATTR_RE.finditer(body):
            value = html.unescape(match.group(2))
            register_asset(value, wp_id)
            if value.startswith(("http://", "https://")) and not re.match(r"https?://(?:www\.)?mathrao\.com/", value, re.I):
                if re.search(r"\.(?:png|jpe?g|gif|webp|svg|pdf)(?:[?#]|$)", value, re.I):
                    external_assets.append({"wp_id": wp_id, "url": value})
        for match in SHORTCODE_RE.finditer(body):
            tag = match.group(2).lower()
            if tag in {"wpex", "overrule"}:
                shortcode_counts[tag] += 1
                shortcode_pages[tag].add(wp_id)
        if EMBED_RE.search(body):
            content_issues.append({"wp_id": wp_id, "kind": "embed_or_script", "title": meta["title"]})
    report = {
        "total": len(manuscripts),
        "status": dict(statuses),
        "published_paths": published,
        "manuscripts": manuscripts,
        "asset_matches": asset_matches,
        "asset_issues": asset_issues,
        "external_assets": external_assets,
        "old_url_references": {url: sorted(ids) for url, ids in all_old_urls.items()},
        "shortcode_counts": dict(shortcode_counts),
        "shortcode_pages": {tag: sorted(ids) for tag, ids in shortcode_pages.items()},
        "asset_reference_pages": {path: sorted(ids) for path, ids in all_asset_references.items()},
        "content_issues": content_issues,
    }
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rescue", type=Path, default=ROOT.parent / "mathrao-rescue")
    parser.add_argument("--inventory", type=Path, default=ROOT.parent / "mathrao_inventory.csv")
    parser.add_argument("--asset-root", type=Path)
    parser.add_argument("--audit-only", action="store_true")
    args = parser.parse_args()
    report = audit(args.rescue, args.inventory, args.asset_root)
    if not args.audit_only:
        if args.asset_root is None:
            parser.error("--asset-root is required for import")
        destination = ROOT / "src/content/legacy"
        destination.mkdir(parents=True, exist_ok=True)
        source_index = []
        for manuscript in report["manuscripts"]:
            source = manuscript["file"]
            target = destination / source.name
            source_bytes = source.read_bytes()
            if target.exists():
                if target.read_bytes() != source_bytes:
                    raise ValueError(f"Existing manuscript differs from rescue: {target}")
            else:
                target.write_bytes(source_bytes)
            meta = manuscript["meta"]
            source_index.append({
                "wp_id": meta["wp_id"],
                "file": source.name,
                "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
                "status": meta["status"],
                "legacy_path": meta["legacy_path"],
            })
        for match in report["asset_matches"].values():
            target = ROOT / "public" / match["local_path"].lstrip("/")
            target.parent.mkdir(parents=True, exist_ok=True)
            source = Path(match["source"])
            if target.exists():
                if target.read_bytes() != source.read_bytes():
                    raise ValueError(f"Existing asset differs from rescued file: {target}")
            else:
                shutil.copyfile(source, target)
        migration_dir = ROOT / "migration"
        migration_dir.mkdir(exist_ok=True)
        asset_map = {path: match["local_path"] for path, match in sorted(report["asset_matches"].items())}
        (migration_dir / "asset-map.json").write_text(json.dumps(asset_map, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (migration_dir / "source-index.json").write_text(json.dumps(sorted(source_index, key=lambda row: row["wp_id"]), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        aliases = defaultdict(list)
        former_slug_candidates = []
        for manuscript in report["manuscripts"]:
            meta = manuscript["meta"]
            if meta["status"] != "publish":
                continue
            canonical = meta["legacy_path"]
            if meta["legacy_slug"]:
                alias = f"/{meta['legacy_slug'].strip('/')}/"
                if alias != canonical and alias not in report["published_paths"]:
                    aliases[alias].append(canonical)
            for former in meta["former_slugs"]:
                former_slug_candidates.append({"wp_id": meta["wp_id"], "former_slug": former, "canonical_path": canonical})
        safe_aliases = {alias: paths[0] for alias, paths in aliases.items() if len(set(paths)) == 1}
        (migration_dir / "slug-aliases.json").write_text(json.dumps(safe_aliases, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (migration_dir / "former-slug-candidates.json").write_text(json.dumps(former_slug_candidates, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        review = {}
        flagged = {issue["wp_id"] for issue in report["asset_issues"] + report["content_issues"]}
        for ids in report["shortcode_pages"].values():
            flagged.update(ids)
        for manuscript in report["manuscripts"]:
            wp_id = manuscript["meta"]["wp_id"]
            review[str(wp_id)] = {
                "migration": "needs_review" if wp_id in flagged else "passed",
                "mathematical": "pending",
                "curriculum": "pending",
                "readability": "pending",
            }
        (migration_dir / "review.json").write_text(json.dumps(review, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "total": report["total"],
        "status": report["status"],
        "published_paths": len(report["published_paths"]),
        "asset_matches": len(report["asset_matches"]),
        "asset_match_types": dict(Counter(v["match"] for v in report["asset_matches"].values())),
        "asset_issues": len(report["asset_issues"]),
        "external_assets": len(report["external_assets"]),
        "old_url_references": len(report["old_url_references"]),
        "shortcode_counts": report["shortcode_counts"],
        "shortcode_pages": report["shortcode_pages"],
        "content_issues": report["content_issues"],
        "first_asset_issues": report["asset_issues"][:20],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
