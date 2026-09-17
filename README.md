# Mathrao 2.0

日本語の数学教材をMarkdownで管理するための、最小限のAstroサイトです。現在の教材は表示確認用サンプル1件のみです。旧WordPressから救出した309件はまだ取り込んでいません。

## ローカルで起動

Node.js 22.12以上とpnpmを用意してください。

```sh
pnpm install
pnpm dev
```

ターミナルに表示されるローカルURL（通常は `http://localhost:4321/`）を開きます。

```sh
pnpm check  # TypeScript・Astroの検査
pnpm build  # 静的サイトを dist/ に生成
```

## 教材を書く

`src/content/lessons/` にMarkdownファイルを追加します。ファイル名が教材URLになります。Front Matterには最低限 `title` を指定してください。

```md
---
title: "教材タイトル"
description: "一覧に表示する短い説明"
---

# 教材タイトル

インライン数式は $x^2$、独立した数式は次のように書けます。

$$
x^2 + 2x + 1 = (x+1)^2
$$
```

MarkdownはAstroのコンテンツコレクションで読み込み、数式はKaTeXで表示します。表示確認用の `sample.md` は本番教材ではありません。

旧Mathraoからは現在、WP ID 1125の1件だけを `src/content/legacy/` に原文のまま追加しています。旧URL `/basics-of-high-school-math/basics-hb-4-6/` で表示し、WordPressの情報は原稿のFront Matterに保持しています。旧記事中のHTML内数式も表示するため、このページではKaTeXの自動描画を使います。

## 構成

- `src/content/lessons/`：Markdown教材
- `src/content/legacy/`：旧WordPress原稿（現在はテスト移植1件）
- `src/content.config.ts`：教材Front Matterの型と読み込み設定
- `src/pages/`：一覧ページと教材ページ
- `src/layouts/`：共通のHTMLと最小限のスタイル
- `astro.config.ts`：MarkdownとKaTeXの設定

現在は静的出力です。Cloudflareへのデプロイ設定、DNS変更、旧URLの転送設定は行っていません。旧WordPress由来のHTMLやショートコードを取り込む際は、表示と安全性を別途確認します。
