#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT_OLD = ROOT / "src/content/legacy"
CONTENT_NEW = ROOT / "src/content/articles"

SHORTCODE_RE = re.compile(r"\[(\/)?(overrule|wpex)(?:\s+[^\]]*)?\]", re.I)
LOCAL_HOST_RE = re.compile(r"(?:(?:https?:)?//)(?:www\.)?mathrao\.com(?=/)", re.I)
EMBED_RE = re.compile(
    r"<(?:iframe|object|embed|script|form)\b[^>]*>(?:[\s\S]*?</(?:iframe|object|embed|script|form)\s*>)?",
    re.I,
)
EQN_RE = re.compile(r"\\begin\{eqnarray\}([\s\S]*?)\\end\{eqnarray\}")

ERRATA = {
    2582: [
        ("+a^2b+b^3+c^2a-ab^2", "+a^2b+b^3+bc^2-ab^2"),
        ("+b^2c+c^4-cba", "+b^2c+c^3-cba"),
    ],
    3022: [
        ("x_{1} + x_{2} + x_{n}", r"x_{1} + x_{2} + \cdots + x_{n}"),
        (r"\ ( \gt 0 )", ""),
    ],
}

CURRENT_ARTICLE = ""

def split_frontmatter(text: str) -> tuple[list[str], str]:
    if not text.startswith("---\n"):
        raise RuntimeError("frontmatter start missing")
    marker = "\n---\n"
    pos = text.find(marker, 4)
    if pos < 0:
        raise RuntimeError("frontmatter end missing")
    return text[4:pos].splitlines(), text[pos + len(marker):]

def frontmatter_values(lines: list[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in lines:
        m = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2)
    return out

def scalar(raw: str | None):
    if raw is None or raw in {"", "null", "~"}:
        return None
    raw = raw.strip()
    if raw.startswith('"') and raw.endswith('"'):
        return json.loads(raw)
    if raw.startswith("'") and raw.endswith("'"):
        return raw[1:-1].replace("''", "'")
    return raw

def shortcode_label(token: str) -> str:
    m = re.search(r'\bmore\s*=\s*["\'“”‘’]([^"\'“”‘’]+)["\'“”‘’]', token, re.I)
    value = m.group(1) if m else "詳しく見る"
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def transform_shortcodes(body: str, stats: Counter, articles: dict[str, set[str]]) -> str:
    stack: list[str] = []
    out: list[str] = []
    for line in body.splitlines(keepends=True):
        matches = list(SHORTCODE_RE.finditer(line))
        if not matches:
            out.append(line)
            continue

        opens = [m for m in matches if not m.group(1)]
        closes = [m for m in matches if m.group(1)]

        for m in opens:
            name = m.group(2).lower()
            stats[f"{name}_open"] += 1
            articles[name].add(CURRENT_ARTICLE)
            if name == "overrule":
                out.append('<aside class="article-note">\n')
            else:
                out.append(f'<details class="article-details"><summary>{shortcode_label(m.group(0))}</summary>\n')
            stack.append(name)

        cleaned = SHORTCODE_RE.sub("", line)
        if cleaned.strip():
            out.append(cleaned)

        for m in closes:
            name = m.group(2).lower()
            stats[f"{name}_close"] += 1
            articles[name].add(CURRENT_ARTICLE)
            if not stack or stack[-1] != name:
                raise RuntimeError(f"shortcode nesting mismatch in {CURRENT_ARTICLE}: {m.group(0)}")
            stack.pop()
            out.append("</aside>\n" if name == "overrule" else "</details>\n")

    if stack:
        raise RuntimeError(f"unclosed shortcode in {CURRENT_ARTICLE}: {stack}")
    return "".join(out)

def normalize_eqnarray(body: str, stats: Counter, eqn_articles: set[str]) -> str:
    if "\\begin{eqnarray}" in body:
        eqn_articles.add(CURRENT_ARTICLE)

    def repl(m: re.Match[str]) -> str:
        whole = m.group(0)
        inner = m.group(1)
        if re.search(r"&(?:amp;)?\s*=\s*&(?:amp;)?", whole):
            stats["eqnarray_to_array_rcl"] += 1
            return r"\begin{array}{rcl}" + inner + r"\end{array}"
        if re.search(r"\\left\s*\\\{[\s\S]*?\\begin\{array\}", whole):
            stats["eqnarray_wrapper_removed"] += 1
            return inner
        return whole

    return EQN_RE.sub(repl, body)

def write_runtime_files() -> None:
    (ROOT / "src/content.config.ts").write_text(
"""import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const articles = defineCollection({
  loader: glob({ base: './src/content/articles', pattern: '**/*.md' }),
  schema: z.object({
    title: z.string(),
    status: z.enum(['published', 'draft']).default('published'),
    published_at: z.string().nullable().optional(),
    path: z.string().optional(),
    featured_image: z.string().optional(),
  }).refine((data) => data.status === 'draft' || Boolean(data.path), {
    message: 'published article requires path',
  }),
});

export const collections = { articles };
""",
        encoding="utf-8",
    )

    old_page = ROOT / "src/pages/[...legacy].astro"
    new_page = ROOT / "src/pages/[...path].astro"
    page = old_page.read_text(encoding="utf-8")
    page = page.replace("entry.data.status === 'publish'", "entry.data.status === 'published'")
    page = page.replace("params: { legacy: (entry.data.path ?? entry.data.legacy_path!).replace(/^\\/+|\\/+$/g, '') }",
                        "params: { path: entry.data.path!.replace(/^\\/+|\\/+$/g, '') }")
    new_page.write_text(page, encoding="utf-8")
    old_page.unlink()

    astro = (ROOT / "astro.config.ts").read_text(encoding="utf-8")
    astro = astro.replace("import { remarkLegacyMarkdown } from './src/lib/legacyMarkdown';\n", "")
    astro = astro.replace("remarkPlugins: [remarkMath, remarkLegacyMarkdown],", "remarkPlugins: [remarkMath],")
    (ROOT / "astro.config.ts").write_text(astro, encoding="utf-8")

    index_page = ROOT / "src/pages/index.astro"
    index_text = index_page.read_text(encoding="utf-8")
    index_text = index_text.replace("entry.data.status === 'publish'", "entry.data.status === 'published'")
    index_text = index_text.replace("entry.data.path ?? entry.data.legacy_path!", "entry.data.path!")
    index_page.write_text(index_text, encoding="utf-8")

    layout = (ROOT / "src/layouts/BaseLayout.astro").read_text(encoding="utf-8")
    layout = layout.replace(".legacy-overrule", ".article-note")
    layout = layout.replace(".legacy-wpex", ".article-details")
    (ROOT / "src/layouts/BaseLayout.astro").write_text(layout, encoding="utf-8")

    (ROOT / "functions/_middleware.js").write_text(
"""function objectHeaders(object) {
  const headers = new Headers();
  object.writeHttpMetadata(headers);
  headers.set('etag', object.httpEtag);
  headers.set('last-modified', object.uploaded.toUTCString());
  headers.set('cache-control', 'public, max-age=3600');
  return headers;
}

function decodePathname(url) {
  try {
    return decodeURIComponent(url.pathname);
  } catch {
    return null;
  }
}

export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const pathname = decodePathname(url);

  if (pathname === null || !pathname.startsWith('/media/')) return context.next();

  if (request.method !== 'GET' && request.method !== 'HEAD') {
    return new Response(null, {
      status: 405,
      headers: { Allow: 'GET, HEAD' },
    });
  }

  const key = pathname.slice('/media/'.length);
  if (!key || key.includes('/')) return new Response(null, { status: 404 });

  if (request.method === 'HEAD') {
    const object = await env.MEDIA.head(key);
    if (!object) return new Response(null, { status: 404 });
    const headers = objectHeaders(object);
    headers.set('content-length', String(object.size));
    return new Response(null, { headers });
  }

  const object = await env.MEDIA.get(key);
  if (!object) return new Response(null, { status: 404 });

  const headers = objectHeaders(object);
  headers.set('content-length', String(object.size));
  return new Response(object.body, { headers });
}
""",
        encoding="utf-8",
    )

    (ROOT / "README.md").write_text(
"""# Mathrao

Mathrao is a small static Astro site for mathematics articles.

## Architecture

- Article Markdown: GitHub under src/content/articles/
- Article routes: frontmatter path
- Binary media: Cloudflare R2 through /media/<basename>
- R2 binding: MEDIA
- Runtime database/API dependency: none

## Article frontmatter

Published articles use title, status=published, published_at, path, and optional featured_image.
Draft articles use title, status=draft, published_at, and may omit path.

Math rendering uses KaTeX. Article-specific note/detail markup is stored directly in the Markdown source.

## Media

Images, PDFs, and other binary files live in the mathrao-media R2 bucket and are referenced as /media/<basename>.
The application serves media with GET/HEAD only.

## Local check

Run pnpm install --frozen-lockfile, pnpm run check, and pnpm run build.
""",
        encoding="utf-8",
    )

    (ROOT / ".gitignore").write_text(
"""node_modules/
affiliate/products.generated.json
.dev.vars
.wrangler/
.astro/
dist/
.env
.env.*
!.env.example
.DS_Store
__pycache__/
*.py[cod]
.pytest_cache/
""",
        encoding="utf-8",
    )

    for path in [ROOT / "src/lib/legacyMarkdown.ts", ROOT / "src/data/errata.json"]:
        if path.exists():
            path.unlink()

    public_images = ROOT / "public/images"
    if public_images.exists():
        shutil.rmtree(public_images)

def transform() -> None:
    global CURRENT_ARTICLE

    files = sorted(CONTENT_OLD.glob("*.md"))
    if len(files) != 309:
        raise RuntimeError(f"article count mismatch before transform: {len(files)}")

    stats = Counter()
    shortcode_articles = {"overrule": set(), "wpex": set()}
    eqn_articles: set[str] = set()
    embed_articles: set[str] = set()
    url_header = 0
    url_body = 0
    output_names: set[str] = set()

    CONTENT_NEW.mkdir(parents=True, exist_ok=False)

    for old_path in files:
        CURRENT_ARTICLE = old_path.name
        text = old_path.read_text(encoding="utf-8")
        stats["local_url_all"] += len(LOCAL_HOST_RE.findall(text))

        fm_lines, body = split_frontmatter(text)
        fm = frontmatter_values(fm_lines)

        wp_m = re.match(r"^wp-(\d{6})-(.+)\.md$", old_path.name)
        if not wp_m:
            raise RuntimeError(f"unexpected filename: {old_path.name}")

        wp_id = int(wp_m.group(1))
        new_name = wp_m.group(2) + ".md"
        if new_name in output_names:
            raise RuntimeError(f"filename collision: {new_name}")
        output_names.add(new_name)

        status = scalar(fm.get("status"))
        if status not in {"publish", "draft"}:
            raise RuntimeError(f"unexpected status in {old_path.name}: {status}")
        stats[f"status_{status}"] += 1

        legacy_path = scalar(fm.get("legacy_path"))
        current_path = scalar(fm.get("path"))
        if current_path:
            stats["existing_path_nonempty"] += 1
        if legacy_path:
            stats["legacy_path_nonempty"] += 1
        if "featured_image" in fm and scalar(fm.get("featured_image")):
            stats["featured_image"] += 1

        url_header += len(LOCAL_HOST_RE.findall("\n".join(fm_lines)))
        url_body += len(LOCAL_HOST_RE.findall(body))

        if wp_id in ERRATA:
            for original, replacement in ERRATA[wp_id]:
                count = body.count(original)
                if count != 1:
                    raise RuntimeError(f"errata count mismatch wp={wp_id}: {original!r} -> {count}")
                body = body.replace(original, replacement)
                stats["errata_applied"] += 1

        if EMBED_RE.search(body):
            embed_articles.add(old_path.name)
        body, embed_count = EMBED_RE.subn('<span class="article-embed-placeholder">[旧埋め込み]</span>', body)
        stats["embed_replaced"] += embed_count

        body = normalize_eqnarray(body, stats, eqn_articles)

        body, url_count = LOCAL_HOST_RE.subn("", body)
        stats["body_local_url_normalized"] += url_count

        body, nbsp_count = re.subn(
            r"(?mi)^[ \\t]*(?:&nbsp;|&#160;|&#x0*a0;)[ \\t]*(?:\\r?\\n|$)",
            "",
            body,
        )
        stats["standalone_nbsp_removed"] += nbsp_count

        body = transform_shortcodes(body, stats, shortcode_articles)

        title_raw = fm.get("title")
        published_at_raw = fm.get("published_at")
        if title_raw is None or published_at_raw is None:
            raise RuntimeError(f"required frontmatter missing: {old_path.name}")

        out_fm = [
            "---",
            f"title: {title_raw}",
            f'status: "{"published" if status == "publish" else "draft"}"',
            f"published_at: {published_at_raw}",
        ]

        route = current_path or legacy_path
        if status == "publish":
            if not route:
                raise RuntimeError(f"published article without route: {old_path.name}")
            out_fm.append("path: " + json.dumps(route, ensure_ascii=False))
        elif route:
            out_fm.append("path: " + json.dumps(route, ensure_ascii=False))

        if "featured_image" in fm and scalar(fm.get("featured_image")):
            out_fm.append(f"featured_image: {fm['featured_image']}")

        out_text = "\n".join(out_fm) + "\n---\n" + body
        (CONTENT_NEW / new_name).write_text(out_text, encoding="utf-8")

    shutil.rmtree(CONTENT_OLD)

    if stats["status_publish"] != 306 or stats["status_draft"] != 3:
        raise RuntimeError(f"status accounting mismatch: {stats}")
    if stats["existing_path_nonempty"] != 0:
        raise RuntimeError(f"unexpected current path count: {stats['existing_path_nonempty']}")
    if stats["legacy_path_nonempty"] != 306:
        raise RuntimeError(f"legacy path count mismatch: {stats['legacy_path_nonempty']}")
    if stats["featured_image"] != 73:
        raise RuntimeError(f"featured image count mismatch: {stats['featured_image']}")
    if stats["local_url_all"] != 664:
        raise RuntimeError(f"absolute local URL accounting mismatch: {stats['local_url_all']}")
    if stats["errata_applied"] != 4:
        raise RuntimeError(f"errata accounting mismatch: {stats['errata_applied']}")
    if stats["overrule_open"] != 55 or stats["overrule_close"] != 55:
        raise RuntimeError(f"overrule accounting mismatch: {stats}")
    if len(shortcode_articles["overrule"]) != 31:
        raise RuntimeError(f"overrule article count mismatch: {len(shortcode_articles['overrule'])}")
    if stats["wpex_open"] != 2 or stats["wpex_close"] != 2:
        raise RuntimeError(f"wpex accounting mismatch: {stats}")
    if len(shortcode_articles["wpex"]) != 2:
        raise RuntimeError(f"wpex article count mismatch: {len(shortcode_articles['wpex'])}")
    if len(embed_articles) != 7:
        raise RuntimeError(f"embed article count mismatch: {len(embed_articles)}")
    if len(eqn_articles) != 13:
        raise RuntimeError(f"eqnarray article count mismatch: {len(eqn_articles)}")
    if len(output_names) != 309:
        raise RuntimeError(f"new filename uniqueness mismatch: {len(output_names)}")

    all_new = "\n".join(p.read_text(encoding="utf-8") for p in sorted(CONTENT_NEW.glob("*.md")))
    if SHORTCODE_RE.search(all_new):
        raise RuntimeError("shortcode residue remains")
    if "legacy-overrule" in all_new or "legacy-wpex" in all_new or "legacy-embed-review" in all_new:
        raise RuntimeError("generated class residue remains")
    if LOCAL_HOST_RE.search(all_new):
        raise RuntimeError("absolute local mathrao.com URL residue remains")

    write_runtime_files()

    report = {
        "articles": len(files),
        "published": stats["status_publish"],
        "draft": stats["status_draft"],
        "filenames_unique": len(output_names),
        "featured_image_articles": stats["featured_image"],
        "old_absolute_local_urls_total": stats["local_url_all"],
        "old_absolute_local_urls_frontmatter": url_header,
        "old_absolute_local_urls_body": url_body,
        "normalized_body_urls": stats["body_local_url_normalized"],
        "standalone_nbsp_removed": stats["standalone_nbsp_removed"],
        "errata_applied": stats["errata_applied"],
        "overrule_pairs": stats["overrule_open"],
        "overrule_articles": len(shortcode_articles["overrule"]),
        "wpex_pairs": stats["wpex_open"],
        "wpex_articles": len(shortcode_articles["wpex"]),
        "embed_articles": len(embed_articles),
        "embed_occurrences": stats["embed_replaced"],
        "eqnarray_articles": len(eqn_articles),
        "eqnarray_to_array_rcl": stats["eqnarray_to_array_rcl"],
        "eqnarray_wrapper_removed": stats["eqnarray_wrapper_removed"],
    }

    Path("/tmp/step59-summary.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))

CLASS_MAP = {
    "legacy-overrule": "article-note",
    "legacy-wpex": "article-details",
    "legacy-embed-review": "article-embed-placeholder",
}

class CanonicalHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tokens = []

    def handle_starttag(self, tag, attrs):
        norm = []
        for k, v in attrs:
            if k == "class" and v:
                v = " ".join(CLASS_MAP.get(c, c) for c in v.split())
            if v:
                v = LOCAL_HOST_RE.sub("", v)
                if k == "href":
                    v = re.sub(r"^(/_astro/.+)\.[A-Za-z0-9_-]{6,}\.css$", r"\1.<hash>.css", v)
                if k == "src":
                    v = re.sub(
                        r"^/_astro/_\.\.\.(?:legacy|path)_\.astro_astro_type_script_index_0_lang\.([A-Za-z0-9_-]+)\.js$",
                        r"/_astro/<route-page>.astro_astro_type_script_index_0_lang.\1.js",
                        v,
                    )
            norm.append((k, v))
        self.tokens.append(("start", tag, tuple(sorted(norm))))

    def handle_startendtag(self, tag, attrs):
        norm = []
        for k, v in attrs:
            if k == "class" and v:
                v = " ".join(CLASS_MAP.get(c, c) for c in v.split())
            if v:
                v = LOCAL_HOST_RE.sub("", v)
                if k == "href":
                    v = re.sub(r"^(/_astro/.+)\.[A-Za-z0-9_-]{6,}\.css$", r"\1.<hash>.css", v)
                if k == "src":
                    v = re.sub(
                        r"^/_astro/_\.\.\.(?:legacy|path)_\.astro_astro_type_script_index_0_lang\.([A-Za-z0-9_-]+)\.js$",
                        r"/_astro/<route-page>.astro_astro_type_script_index_0_lang.\1.js",
                        v,
                    )
            norm.append((k, v))
        self.tokens.append(("empty", tag, tuple(sorted(norm))))

    def handle_endtag(self, tag):
        self.tokens.append(("end", tag))

    def handle_data(self, data):
        data = LOCAL_HOST_RE.sub("", data)
        normalized = re.sub(r"\s+", " ", data).strip()
        if normalized:
            self.tokens.append(("text", normalized))

    def handle_comment(self, data):
        pass

def canonical(path: Path):
    parser = CanonicalHTML()
    parser.feed(path.read_text(encoding="utf-8"))
    parser.close()
    return parser.tokens

def compare(before: Path, after: Path) -> None:
    before_files = sorted(p.relative_to(before) for p in before.rglob("*.html"))
    after_files = sorted(p.relative_to(after) for p in after.rglob("*.html"))

    if before_files != after_files:
        only_before = sorted(set(before_files) - set(after_files))
        only_after = sorted(set(after_files) - set(before_files))
        raise RuntimeError(
            f"HTML route set changed: only_before={only_before[:10]} only_after={only_after[:10]}"
        )

    mismatches = []
    for rel in before_files:
        a = canonical(before / rel)
        b = canonical(after / rel)
        if a != b:
            first = next(
                (i for i, (x, y) in enumerate(zip(a, b)) if x != y),
                min(len(a), len(b)),
            )
            mismatches.append((str(rel), first, a[first:first+3], b[first:first+3]))
            if len(mismatches) >= 10:
                break

    if mismatches:
        raise RuntimeError("rendered DOM mismatch: " + json.dumps(mismatches, ensure_ascii=False))

    print(json.dumps({"html_routes": len(before_files), "canonical_dom_mismatch": 0}, ensure_ascii=False))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--compare", nargs=2, metavar=("BEFORE", "AFTER"))
    args = parser.parse_args()

    if args.compare:
        compare(Path(args.compare[0]), Path(args.compare[1]))
    else:
        transform()

if __name__ == "__main__":
    main()
