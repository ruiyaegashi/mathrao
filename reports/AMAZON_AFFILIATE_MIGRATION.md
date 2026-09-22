# Mathrao Amazonアソシエイト復旧設計

## 発掘結果

- 公開記事: 306
- Amazon表現を確認した記事: 10
- 旧商品出現: 120
- 一意な旧ASIN: 118
- 記事単位のASIN割当: 120（high）
- 解決前のAmazon短縮URL: 4（medium）
- 商品を割り当てていない記事: 299
- 旧アソシエイトタグ: `mathrao-22`（120箇所）

全306記事を `affiliate/mapping.json` に収録した。旧教材・参考書が明示された記事を優先し、一般の数学記事へ商品を一律追加していない。

## 実装方式

原稿Markdownとは別にWP ID→商品mappingを管理する。`display_status: approved` の商品だけを記事末尾に表示する。商品情報はCloudflare Pages FunctionがAmazon Creators APIから取得し、商品画像はAmazonのURLを参照する。価格・在庫は表示しない。

PA-API 5.0は2026-05-15に廃止されたためCreators APIを使用する。API認証情報はCloudflare Secretsだけに保存し、Git、Markdown、JSON、HTMLには保存しない。

## 未完了

- Creators APIで118 ASINの現在状態を確認
- 販売終了商品の後継・代替候補の選定
- 短縮URL4件の解決
- 商品単位の人間承認

認証情報がない現段階では全商品を `pending` とし、本番Mathraoに商品カードは出さない。
