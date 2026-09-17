# Mathrao 2.0

Astro + TypeScript の静的な数学教材サイトです。旧WordPressから救出した原稿309件を、原本のMarkdownとFront Matterを保ったまま `src/content/legacy/` に収めています。公開306件だけを旧URLに生成し、下書き3件は生成しません。数学的内容・カリキュラム・読みやすさのレビューは未実施です。

## ローカルで起動

Node.js 22.12以上とpnpmを用意します。

```sh
pnpm install
pnpm dev
pnpm check
pnpm build
```

通常は `http://localhost:4321/` で確認できます。旧記事の例は `/basics-of-high-school-math/basics-hb-4-6/` です。表示確認用のサンプル教材も残しています。

## 原稿と移行ルール

- `src/content/legacy/`: 救出Markdownをバイト単位で保存。WP ID 1125も1件のみ。旧WordPressのID、状態、日付、URL、親子関係、カテゴリ等は原本Front Matterに保持。
- `src/pages/[...legacy].astro`: 公開状態の原稿だけを `legacy_path` に静的生成。下書きは生成対象外。
- `src/lib/legacyMarkdown.ts`: 描画時に旧サイト内リンクと静的素材URLをローカルパスへ対応付け、数式のHTMLエンティティと旧 `eqnarray` をKaTeX表示用に変換。`overrule` は解説枠、`wpex` は読める開閉枠として表示します。原本ファイルは変更しません。旧広告iframeの自動読み込みは止めて要確認表示にします。
- 長い数式は共通表示で式の領域だけ横スクロール可能にします。原文の式と改行位置は変えず、短い式は通常表示にします。
- `public/images/`: 旧 `public_html` 内で原稿から参照された画像・PDFだけを照合して収録。PHP、テーマ、プラグイン、WordPressのキャッシュは含めません。
- `migration/`: 原稿の索引、素材対応表、旧スラッグ候補、移行と内容レビューの状態。
- `migration/errata.json`: Mathrao 2.0で表示時だけ適用する校訂台帳。WP ID、原文、校訂後、理由、確認状態を1箇所ごとに記録。原本Markdownは編集しません。対象の文字列が記事中にちょうど1回現れないとビルドを停止します。
- `public/_redirects`: 確認できた旧slug4件のCloudflare Pages用301設定。ローカルのAstroプレビューではCloudflareの転送動作を再現しません。
- `reports/`: 原稿上に残る旧記法の分析と、互換表示後の検証結果。数学的内容、旧リンク、広告停止後の書籍表示には人間の確認が必要です。

救出元の `mathrao-rescue/`、`mathrao_inventory.csv` はこのリポジトリの親ディレクトリに置き、旧 `public_html` の場所を明示して再実行できます。入力は読み取り専用です。

```sh
python scripts/migrate_legacy.py --asset-root "/path/to/old/public_html"
pnpm check
pnpm build
python scripts/validate_legacy.py --asset-root "/path/to/old/public_html"
node scripts/check_math.mjs
node scripts/check_rendered_math.mjs
```

`--audit-only` は原稿・素材の照合だけを行います。Python 3の標準ライブラリを利用します。移行元のSQLやZIP、旧WordPressのPHPはリポジトリに投入しません。

新規教材は `src/content/lessons/` にMarkdownを追加します。数式はKaTeXで表示します。旧原稿の内容を変更する前にレビュー状態を確認してください。
`pnpm build` はAstroの内容キャッシュを再生成し、校訂台帳の変更を確実に反映します。
