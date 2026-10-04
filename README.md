# Mathrao

Mathrao is a small Astro site that keeps the rescued mathematics articles online.

## Production requirements

1. Existing articles remain available, including their images and files.
2. Markdown lives in GitHub. Images and other binary files live in Cloudflare R2.
3. New articles can continue to be added as Markdown.

The production site intentionally does not keep WordPress compatibility, migration tooling, affiliate features, analytics, category navigation, or other legacy infrastructure.

## Content

Existing articles are under `src/content/legacy/`. New articles may be added to the same collection.

A new article needs at least:

```yaml
---
title: "Article title"
published_at: "2026-10-04 12:00:00"
path: "/article-path/"
status: publish
---
```

Math rendering and the small set of legacy shortcodes needed by rescued articles remain part of article rendering because they are content semantics, not site design.

## Media cutover

The current branch temporarily retains `public/images/` while the final R2 set is assembled and verified.

Before merge, the final media step will:

- copy the 23 currently referenced images/PDFs to R2
- rescue the 68 unique featured-image files from the old backup
- rescue the original top logo `images/logo_wide.png`
- switch article media references to `/media/*`
- remove `public/images/`

Do not delete the local media until R2 verification passes.

## Local check

```console
pnpm install --frozen-lockfile
pnpm run check
pnpm run build
```
