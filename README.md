# Mathrao

Mathraoは数学の公開記事を扱うAstro静的サイト。実装と現在の運用方法はこのservice repositoryの`main`で管理する。

## 構成

- 公開サイト: https://mathrao.com
- Cloudflare Pages: project `mathrao`、Production branch `main`
- 記事: `src/content/articles/` のMarkdown。公開URLはファイル名ではなくfrontmatterの`path`を使用する
- 数式: KaTeX
- 静的媒体: 非公開R2 bucket `mathrao-media`をPages Functionsの`MEDIA` bindingで参照し、`/media/<basename>`のGET/HEADとして配信。該当Functions経路は`public/_routes.json`の`/media/*`に限定
- 記事・書籍ページは静的生成。ブラウザー側から楽天APIへ直接接続しない
- 旧WordPress、XServerのWeb origin、MySQLへの実行時依存はない

公開記事frontmatter: `title`、`status: "published"`、`published_at`、`path`、必要な場合だけ`featured_image`。下書きでは公開`path`を省略できる。

## 楽天書籍の掲載・公開

- 採用対象は`src/data/rakuten-book-selections.json`。2026-10-15の本番公開で5記事に91 ISBN（88選定グループ）。変更するときは実際の採用内容を再確認する
- 楽天の商品情報は`scripts/refresh_rakuten_books.mjs`がGitHub Actions内で取得し、`src/generated/rakuten-books.json`へ一時生成する。生成商品データ・認証情報はGitへコミットしない
- 書籍取得、ISBN一致検査、Astroビルド、広告開示・書籍カード検査、Cloudflare Pages直接公開、公開HTTP検査、旧成功Productionの削除・結果照合までを`.github/workflows/rakuten-books.yml`の1本で行う
- 類の更新・削除指示と変更内容の承認を受けてから、`main`への該当コミットを起点に自動実行する。更新はコミット件名を`[mathrao-books:update]`で、削除は`[mathrao-books:remove]`で始める。定期実行・Actions画面での反復手動実行は設けない
- ISBN変更がない再取得は、承認済み`main`のファイル内容を変えない起動コミットでも実行できる。削除は選定JSONから**指定ISBNのみを除く**変更を要し、Workflowが前コミットとの差分を検査する
- CloudflareのGit連携は維持するが、`source.config.production_deployments_enabled=false`により通常のGit pushによる本番自動ビルド・公開を停止。承認済みWorkflowの`pages deploy dist --project-name=mathrao --branch=main`でProductionを公開する。Git連携にスキップ履歴が作られることと、実際に公開されることは区別する
- Previewは作業ブランチで同一ブランチの旧版を整理する。Productionでは新しい本番公開とHTTP検査の後、現在公開中のデプロイIDを保護し、**古い成功済みProductionだけを自動削除**する。失敗・スキップ済みの履歴は削除対象外。削除後は現行IDの維持と旧成功版の消失を照合し、不一致・API失敗なら停止する
- 独自の7日失効・自動更新・定期実行は設けていない。楽天の提供条件・保存期限の遵守は更新・削除時に確認する

BODの現行操作手順: `ruiyaegashi/YDI/Directives/Mathrao書籍更新.md` と `Mathrao書籍削除.md`。

## 広告と本番確認

AdSenseの読み込みコードは`src/layouts/BaseLayout.astro`、販売者情報は`public/ads.txt`、楽天書籍の広告開示とリンクは`src/components/RakutenBookCard.astro`。既存Amazonリンク・開示文も維持する。

2026-10-15に楽天91件のProduction公開・公開HTML検証・`mathrao.com`代表HTTP/書籍導線・媒体GET/HEAD/404検証を完了。AdSenseの実画面はBODが確認してSTEP31完了を承認した。技術的に全広告枠が毎回埋まると保証するものではない。

## 検証と復旧

- 開発時: `corepack pnpm install --frozen-lockfile` → `pnpm run check` → `pnpm run build`。書籍の実公開は通常のローカルビルドだけで代替しない
- 本番トラブル時は、`main`の内容、Actionsの実行・検証結果、Cloudflare Pagesの現在のProduction、`mathrao.com`の外部HTTPを別々に確認する。GitHub mainだけから公開中の内容を決めつけない
- 商品削除は新規版の公開だけで完了とはしない。旧成功Productionの消失と現在公開中のIDを確認する。Actionsが削除後照合で失敗した場合は成功と扱わず、**追加の公開・削除を行う前に読み取り専用で実際の状態を確認**し、確認不能・残存・異常ならBODへ報告して停止する
- `/media/*`以外の静的ページは不要なFunctions呼び出しを避ける。R2の存在・HTTP GET/HEAD・404を分けて確認する
