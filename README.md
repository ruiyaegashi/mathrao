# Mathrao

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
