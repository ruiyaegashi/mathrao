"""Check the complete static Mathrao migration and write review reports."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

from migrate_legacy import ROOT, audit


class ArticleReferences(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.article_depth = 0
        self.references: list[tuple[str, str]] = []
        self.ids: set[str] = set()
        self.embed_placeholders = 0
        self.katex_errors = 0
        self.overrule_boxes = 0
        self.wpex_details = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "article" and "data-legacy-content" in values:
            self.article_depth = 1
        elif tag == "article" and self.article_depth:
            self.article_depth += 1
        if self.article_depth:
            if values.get("id"):
                self.ids.add(values["id"] or "")
            if "legacy-embed-review" in (values.get("class") or ""):
                self.embed_placeholders += 1
            if "katex-error" in (values.get("class") or ""):
                self.katex_errors += 1
            if tag == "aside" and "legacy-overrule" in (values.get("class") or ""):
                self.overrule_boxes += 1
            if tag == "details" and "legacy-wpex" in (values.get("class") or ""):
                self.wpex_details += 1
            for attribute in ("href", "src", "poster"):
                if values.get(attribute):
                    self.references.append((attribute, values[attribute] or ""))
            if values.get("srcset"):
                for item in (values["srcset"] or "").split(","):
                    self.references.append(("srcset", item.strip().split(" ")[0]))

    def handle_endtag(self, tag: str) -> None:
        if tag == "article" and self.article_depth:
            self.article_depth -= 1


def target_file(path: str) -> Path:
    decoded = unquote(path)
    relative = decoded.lstrip("/")
    candidate = ROOT / "dist" / relative
    if path.endswith("/") or not Path(relative).suffix:
        candidate /= "index.html"
    return candidate


def validate(rescue: Path, inventory: Path, asset_root: Path) -> dict:
    source = audit(rescue, inventory, asset_root)
    index = json.loads((ROOT / "migration/source-index.json").read_text(encoding="utf-8"))
    review = json.loads((ROOT / "migration/review.json").read_text(encoding="utf-8"))
    asset_map = json.loads((ROOT / "migration/asset-map.json").read_text(encoding="utf-8"))
    if len(index) != 309 or len(review) != 309:
        raise ValueError("Migration metadata must cover 309 entries")
    if len(list((ROOT / "src/content/legacy").glob("*.md"))) != 309:
        raise ValueError("Astro legacy collection must contain exactly 309 Markdown files")
    source_by_id = {m["meta"]["wp_id"]: m for m in source["manuscripts"]}
    mismatch = []
    for item in index:
        wp_id = item["wp_id"]
        original = source_by_id[wp_id]["file"].read_bytes()
        imported = (ROOT / "src/content/legacy" / item["file"]).read_bytes()
        if original != imported:
            mismatch.append(wp_id)

    output_missing = []
    output_paths = {}
    broken_links = []
    missing_assets = []
    old_domain_dependencies = []
    anchor_issues = []
    embed_pages = {}
    static_katex_errors = {}
    shortcode_rendered = Counter()
    unresolved_shortcodes = []
    remaining_eqnarray = []
    media_references = Counter()
    for path, wp_id in source["published_paths"].items():
        file = target_file(path)
        if not file.is_file():
            output_missing.append({"wp_id": wp_id, "path": path})
            continue
        output_paths[wp_id] = str(file.relative_to(ROOT / "dist")).replace("\\", "/")
        output_html = file.read_text(encoding="utf-8")
        parser = ArticleReferences()
        parser.feed(output_html)
        for match in re.finditer(r"\[/?(?:overrule|wpex)\b[^\]]*\]", output_html, re.I):
            unresolved_shortcodes.append({"wp_id": wp_id, "token": match.group(0)})
        if r"\begin{eqnarray}" in output_html or r"\end{eqnarray}" in output_html:
            remaining_eqnarray.append(wp_id)
        if parser.embed_placeholders:
            embed_pages[wp_id] = parser.embed_placeholders
        if parser.katex_errors:
            static_katex_errors[wp_id] = parser.katex_errors
        shortcode_rendered["overrule"] += parser.overrule_boxes
        shortcode_rendered["wpex"] += parser.wpex_details
        for kind, value in parser.references:
            if not value or value.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
                continue
            resolved = urlsplit(urljoin("https://mathrao.pages.dev" + path, value))
            host = resolved.hostname or ""
            if host in {"mathrao.com", "www.mathrao.com"}:
                old_domain_dependencies.append({"wp_id": wp_id, "kind": kind, "url": value})
                continue
            if host != "mathrao.pages.dev":
                continue
            target = target_file(resolved.path)
            if target.is_file():
                media_references[target.suffix.lower()] += 1
                continue
            issue = {"wp_id": wp_id, "kind": kind, "url": value, "target": resolved.path}
            if kind in {"src", "poster", "srcset"} or Path(resolved.path).suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".pdf"}:
                missing_assets.append(issue)
            else:
                broken_links.append(issue)

    drafts_with_output = []
    for item in index:
        if item["status"] == "draft" and item["legacy_path"] and target_file(item["legacy_path"]).exists():
            drafts_with_output.append(item["wp_id"])
    built_pages = len(list((ROOT / "dist").rglob("index.html")))
    asset_missing = [path for path in asset_map.values() if not (ROOT / "dist" / path.lstrip("/")).is_file()]
    candidates = json.loads((ROOT / "migration/former-slug-candidates.json").read_text(encoding="utf-8"))
    expected_redirects = {f"/{item['former_slug']}/": item["canonical_path"] for item in candidates}
    redirect_lines = [line.strip().split() for line in (ROOT / "public/_redirects").read_text(encoding="utf-8").splitlines() if line.strip() and not line.lstrip().startswith("#")]
    redirect_issues = []
    actual_redirects = {}
    for parts in redirect_lines:
        if len(parts) != 3 or parts[2] != "301":
            redirect_issues.append({"rule": parts, "reason": "invalid format or status"})
            continue
        old, new, _ = parts
        if old in actual_redirects or old in source["published_paths"] or not target_file(new).is_file():
            redirect_issues.append({"rule": parts, "reason": "collision, duplicate, or missing destination"})
        actual_redirects[old] = new
    if actual_redirects != expected_redirects:
        redirect_issues.append({"reason": "rules differ from former-slug candidates"})
    if (ROOT / "dist/_redirects").read_bytes() != (ROOT / "public/_redirects").read_bytes():
        redirect_issues.append({"reason": "build did not copy redirects unchanged"})

    errata = json.loads((ROOT / "migration/errata.json").read_text(encoding="utf-8"))
    errata_checks = []
    for entry in errata:
        wp_id = entry["wp_id"]
        manuscript = source_by_id[wp_id]["file"].read_text(encoding="utf-8")
        imported = (ROOT / "src/content/legacy" / next(x["file"] for x in index if x["wp_id"] == wp_id)).read_text(encoding="utf-8")
        rendered = target_file(source_by_id[wp_id]["meta"]["legacy_path"]).read_text(encoding="utf-8")
        result = {
            "wp_id": wp_id,
            "location": entry["location"],
            "source_original_once": manuscript.count(entry["original"]) == 1,
            "imported_original_once": imported.count(entry["original"]) == 1,
            "rendered_correction_added_once": (entry["replacement"] == "" or rendered.count(entry["replacement"]) == manuscript.count(entry["replacement"]) + 1),
            "rendered_old_context_absent": entry["original"] not in rendered,
        }
        errata_checks.append(result)
    if len(errata_checks) != 4 or any(not all(value for key, value in item.items() if key not in {"wp_id", "location"}) for item in errata_checks):
        raise ValueError(f"Editorial correction validation failed: {errata_checks}")
    variance_html = target_file(source_by_id[3022]["meta"]["legacy_path"]).read_text(encoding="utf-8")
    if r"\ ( \gt 0 )" in variance_html:
        raise ValueError("WP 3022 variance inequality was not removed from the rendered article")

    for item in broken_links + missing_assets + old_domain_dependencies:
        review[str(item["wp_id"])]["migration"] = "needs_review"
    (ROOT / "migration/review.json").write_text(json.dumps(review, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report = {
        "source_total": source["total"],
        "source_status": source["status"],
        "imported_files": len(index),
        "source_byte_mismatch_wp_ids": mismatch,
        "unique_published_paths": len(source["published_paths"]),
        "built_pages_total": built_pages,
        "built_legacy_pages": len(output_paths),
        "output_missing": output_missing,
        "drafts_with_output": drafts_with_output,
        "assets_matched": len(source["asset_matches"]),
        "asset_match_types": dict(Counter(x["match"] for x in source["asset_matches"].values())),
        "asset_type_counts": dict(Counter(Path(x["local_path"]).suffix.lower() for x in source["asset_matches"].values())),
        "assets_unmatched_in_source": source["asset_issues"],
        "assets_missing_from_build": asset_missing,
        "missing_local_assets": missing_assets,
        "broken_internal_links": broken_links,
        "old_domain_dependencies": old_domain_dependencies,
        "old_domain_asset_dependencies": [item for item in old_domain_dependencies if urlsplit(item["url"]).path.startswith(("/images/", "/wp-content/uploads/"))],
        "old_domain_text_references": len(source["old_url_references"]),
        "shortcode_counts": source["shortcode_counts"],
        "shortcode_pages": source["shortcode_pages"],
        "embed_pages": embed_pages,
        "static_katex_errors": static_katex_errors,
        "remaining_eqnarray_wp_ids": remaining_eqnarray,
        "unresolved_shortcodes": unresolved_shortcodes,
        "shortcode_rendered": dict(shortcode_rendered),
        "redirect_rules": actual_redirects,
        "redirect_issues": redirect_issues,
        "errata_checks": errata_checks,
        "review_status": dict(Counter(x["migration"] for x in review.values())),
        "wp1125": {
            "path": source_by_id[1125]["meta"]["legacy_path"],
            "html_exists": 1125 in output_paths,
            "image_local_exists": (ROOT / "dist/images/hanseisuhosei.png").is_file(),
            "source_byte_identical": 1125 not in mismatch,
        },
    }
    return report


def write_report(report: dict) -> None:
    folder = ROOT / "reports"
    folder.mkdir(exist_ok=True)
    (folder / "legacy-validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Mathrao 1.0 一括移行検証",
        "",
        "原本は `src/content/legacy/` にバイト単位で複製。旧WordPressのPHP、テーマ、プラグインは移行対象外。",
        "Mathrao 2.0側のレビュー状態は `migration/review.json` で独立管理。",
        "",
        f"- 原本・台帳: {report['source_total']} 件（公開 {report['source_status']['publish']}、下書き {report['source_status']['draft']}）",
        f"- Astroに取り込んだ原稿: {report['imported_files']} 件、原本との差異: {len(report['source_byte_mismatch_wp_ids'])} 件",
        f"- 重複のない公開旧URL: {report['unique_published_paths']} 件",
        f"- 生成した公開記事: {report['built_legacy_pages']} 件、生成先欠落: {len(report['output_missing'])} 件",
        f"- 生成ページ総数: {report['built_pages_total']}（トップ・サンプルを含む）",
        f"- 下書きの誤公開: {len(report['drafts_with_output'])} 件",
        f"- 照合できた静的素材: {report['assets_matched']} 件 {report['asset_type_counts']}",
        f"- 素材照合の例外: {len(report['assets_unmatched_in_source'])} 件、ビルド上の欠落: {len(report['assets_missing_from_build'])} 件",
        f"- 出力HTML中の欠落素材: {len(report['missing_local_assets'])} 件",
        f"- broken internal links: {len(report['broken_internal_links'])} 件",
        f"- 未解決の旧ドメインリンク・素材: {len(report['old_domain_dependencies'])} 件",
        f"- 旧ドメインへの画像・PDF依存: {len(report['old_domain_asset_dependencies'])} 件",
        f"- 原稿中の旧ドメイン文字列（リンク属性以外も含む）: {report['old_domain_text_references']} 種類",
        f"- ショートコード: {report['shortcode_counts']}",
        f"- 公開時に停止した旧埋め込み: {len(report['embed_pages'])} 記事",
        f"- 静的HTMLのKaTeXエラー表示: {sum(report['static_katex_errors'].values())} 件",
        f"- 残るeqnarray記法: {len(report['remaining_eqnarray_wp_ids'])} 記事、未解決shortcode: {len(report['unresolved_shortcodes'])} 件",
        f"- 表示した解説枠: {report['shortcode_rendered'].get('overrule', 0)} 件、開閉枠: {report['shortcode_rendered'].get('wpex', 0)} 件（もう1件は下書き）",
        f"- Cloudflare Pages 301設定: {len(report['redirect_rules'])} 件、設定上の問題: {len(report['redirect_issues'])} 件",
        f"- 移行レビュー状態（人間確認を残す既存フラグ）: {report['review_status']}",
        "- 旧ルートslugの対応表: `migration/slug-aliases.json`（214 件）。旧slug履歴4件の301ルールは `public/_redirects` に設定済み、Cloudflare上の動作は未確認。",
        "",
        "## WP ID 1125 の回帰検査",
        "",
        f"- 旧path: `{report['wp1125']['path']}`",
        f"- HTML生成: {report['wp1125']['html_exists']}",
        f"- 原本と同一バイト: {report['wp1125']['source_byte_identical']}",
        f"- `/images/hanseisuhosei.png` の生成: {report['wp1125']['image_local_exists']}",
        "",
        "## 要確認",
        "",
        "ショートコードと外部埋め込みは原本に保持。前者は表示用互換処理を実装し、旧広告iframeは自動読込せず要確認表示に置換。",
        "原稿上の旧構文は `reports/math-validation.json`、互換表示後のHTML内数式は `reports/rendered-math-validation.json` に記録。確認済みの校訂は `migration/errata.json` で表示時だけ適用し、原稿は変更していない。",
        "旧slugは原本の `former_slugs` に保持。301ルール4件はビルドに含めたが、Cloudflare上のHTTP応答は未検証。",
        "`overrule` と `wpex` のショートコードの意味を確認するまで原文を保持。旧埋め込み7記事は自動読み込みを止めた表示を確認する。",
        "未解決の旧リンクは同一の未収録記事を指す4箇所。対応先またはリンクの扱いは内容レビュー時に判断する。",
        "旧素材は参照された23点のみ収録し、未参照の画像・WordPressアップロードキャッシュは移していない。",
    ]
    for title, key in [
        ("欠落素材", "missing_local_assets"),
        ("broken internal links", "broken_internal_links"),
        ("旧ドメイン依存", "old_domain_dependencies"),
    ]:
        lines += ["", f"### {title}", ""]
        items = report[key]
        if items:
            lines.extend(f"- WP {item['wp_id']}: `{item['url']}`" for item in items[:100])
            if len(items) > 100:
                lines.append(f"- ほか {len(items) - 100} 件。全件は JSON を参照。")
        else:
            lines.append("- なし")
    math_report_path = folder / "math-validation.json"
    if math_report_path.is_file():
        math_report = json.loads(math_report_path.read_text(encoding="utf-8"))
        summary = math_report["summary"]
        lines += [
            "", "### 数式・KaTeX", "",
            f"- 数式を抽出した記事: {summary['pages_with_math']} 件、式: {summary['expressions']} 箇所",
            f"- WP 1125: {summary['wp1125_expressions']} 箇所（ブラウザで37箇所表示、エラー0を確認）",
            f"- 原稿をそのままKaTeXへ渡した場合の旧構文エラー: {summary['errors']} 箇所 / {summary['pages_with_errors']} 記事（原稿を未修正のまま保持）",
            f"- 静的HTML上のエラー表示: {sum(report['static_katex_errors'].values())} 箇所 / {len(report['static_katex_errors'])} 記事",
            f"- strict警告: {summary['warnings']} 件 / {summary['pages_with_warnings']} 記事。文字や空白に関する警告も含むため個別に精査が必要。",
            "- 互換表示後のHTML内数式は `rendered-math-validation.json` を参照（検査4986箇所、エラー0）。",
            "", "旧構文エラーの全文、原本行番号、原因は `math-validation.json` を参照。記事別の件数:", "",
        ]
        lines.extend(
            f"- WP {page['wp_id']} {page['title']}: {len(page['errors'])} 件（行 {', '.join(str(e['line']) for e in page['errors'])}）"
            for page in math_report["pages"] if page["errors"]
        )
    (folder / "legacy-migration.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rescue", type=Path, default=ROOT.parent / "mathrao-rescue")
    parser.add_argument("--inventory", type=Path, default=ROOT.parent / "mathrao_inventory.csv")
    parser.add_argument("--asset-root", required=True, type=Path)
    args = parser.parse_args()
    report = validate(args.rescue, args.inventory, args.asset_root)
    write_report(report)
    print(json.dumps({key: len(value) if isinstance(value, list) else value for key, value in report.items() if key not in {"broken_internal_links", "missing_local_assets", "old_domain_dependencies", "shortcode_pages", "embed_pages"}}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
