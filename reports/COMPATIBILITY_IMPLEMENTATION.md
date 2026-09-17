# Mathrao 2.0 互換表示の実装・再検証

救出Markdown 309件はすべて原本とバイト一致。数学的内容、現行課程、文章は修正していない。commit、push、deployもしていない。

## 実装

- レンダリング時に旧 `eqnarray` をKaTeX対応の `array` に置換するか、連立式を囲むだけの外側の `eqnarray` を外す。元の数式セルと演算子は維持。分析済み31箇所に適用し、追加発見したWP 714の区切りなしの数式にも表示用の区切りを付与。
- `overrule` 55対を内容が常時読める控えめな解説枠に変換。`wpex` は公開中の1対を開閉可能な `<details>` として表示。下書きのもう1対はサイトに生成しない。
- Amazon広告iframe120個は従来どおり自動読込を停止。原稿中の広告コードはそのまま保持。
- `_wp_old_slug` 4件から `public/_redirects` を追加。旧pathと公開pathの衝突・転送先・ビルドコピーを検査。

## 全件検証

| 項目 | 結果 |
|---|---:|
| Astro check | エラー0、警告0 |
| 静的ビルド | 成功、全308ページ |
| 原稿・公開・下書き | 309・306・3 |
| 公開旧pathの生成 | 306/306、重複0 |
| 下書きの生成 | 0 |
| 原稿と救出元のバイト差 | 0 |
| 静的HTMLのKaTeXエラー表示 | 0 |
| ビルド後のHTML内数式をKaTeXへ渡した検査 | 4,986箇所、エラー0 |
| ビルドに残る `eqnarray` | 0 |
| 未解決 `overrule` / `wpex` | 0 |
| 表示した解説枠・公開開閉枠 | 55・1 |
| broken internal links / missing assets | 0 / 0 |
| 旧mathrao.comへの画像・PDF依存 | 0 |
| 旧slug 301ルール / 設定検査の問題 | 4 / 0 |

`reports/math-validation.json` の31件は**原稿をそのままKaTeXへ渡した場合**の歴史的なエラー記録。互換処理後の検査は `reports/rendered-math-validation.json` と `reports/legacy-validation.json` を参照。Cloudflare Pages上の301応答は未デプロイのため未確認。

WP 1125の `/basics-of-high-school-math/basics-hb-4-6/` はローカルHTTP 200。ブラウザでKaTeX数式37箇所・エラー0、`/images/hanseisuhosei.png` の読み込み（幅600px）を確認した。画像自体もHTTP 200。

## 人間の目視確認を残す4箇所

| WP ID・URL | 原稿行 | 確認対象 |
|---|---:|---|
| 2586 `/theorems-proof-of-high-school-math/theorems-h1-1-2/` | 27 | 絶対値の区分的定義で、数式内の「のとき」の日本語の字形・行間。 |
| 2763 `/theorems-proof-of-high-school-math/theorems-h1-3-3/` | 62 | ①〜③の丸数字の字形・不等式との対応。KaTeXの字形警告は残る。 |
| 2994 `/theorems-proof-of-high-school-math/theorems-h1-5-3/` | 140 | 四領域の長い日本語を含む数式の折り返しと可読性。 |
| 3233 `/theorems-proof-of-high-school-math/theorems-ha-4-2/` | 31 | `\\ / \\! / \\` で表した平行関係が意図した見た目か。`\\parallel` への変更は未実施。 |

いずれも互換処理後はKaTeX構文エラー0。数学的な原稿修正はしていない。

## 広告停止後の内容

7記事とも記事本文は表示され、広告iframeは0。WP 24、57、1388、1390は広告以外の見出し・本文が十分に残る。**WP 1568、1739、1741** の参考書紹介3記事は文章と分類見出しは読めるが、商品画像のみで識別していた個別の本が `[旧埋め込み：要確認]` となり、どの説明がどの本を指すか分かりにくい箇所がある。書誌情報の復元・静的な代替表現は別工程で人間が判断する。

## その他残件

- 未収録の `/recommended-study-aid-books-of-mathematics/` への旧リンク4箇所（WP 1563、1566）は変更していない。
- WP 2582とWP 3022の式本文には数学的疑義が残る。下記の原文は表示用の `eqnarray` 互換処理以外、未修正。
- Cloudflare Pagesの301ルールはビルドに入っているが、本番側HTTP 301の動作確認はpush・deploy後の工程。
- `migration/review.json` の既存 `needs_review` 45件は、数学的・表示上の人間確認が終わるまで維持。

## 数学的疑義2箇所の原文と前後

### WP 2582 — 証明の⑥。中間展開に `c^4` 等があり、式の正しさは未判定。

原稿 94〜97 行（改行・記法を保持）:

```text
なお，上記公式の⑦～⑨は展開，因数分解ではありませんが，対称式・交代式(※後述)等において頻繁に用いられる変形なので押さえておきましょう。


<div class="blank-box bb-green"><strong>証明</strong>
```

原稿 125〜141 行（改行・記法を保持）:

```text
⑤


<p style="padding-left: 40px;">$\begin{eqnarray} (a+b+c)^2 &amp;=&amp; (a+b+c)(a+b+c) \\ &amp;=&amp; a(a+b+c)+b(a+b+c)+c(a+b+c) \\ &amp;=&amp; a^2+ab+ca+ab+b^2+bc+ca+bc+c^2 \\ &amp;=&amp; a^2+b^2+c^2+2ab+2bc+2ca \end{eqnarray}$</p>


⑥


<p style="padding-left: 40px;">$\begin{eqnarray} (a+b+c)(a^2+b^2+c^2-ab-bc-ca) &amp;=&amp; a(a^2+b^2+c^2-ab-bc-ca)+b(a^2+b^2+c^2-ab-bc-ca)+c(a^2+b^2+c^2-ab-bc-ca) \\ &amp;=&amp; a^3+ab^2+c^2a-a^2b-abc-ca^2+a^2b+b^3+c^2a-ab^2-b^2c-abc+ca^2+b^2c+c^4-cba-bc^2-c^2a \\ &amp;=&amp; a^3+b^3+c^3-3abc \end{eqnarray}$</p>


⑦


<p style="padding-left: 40px;">①より<br />
$a^2+b^2=(a+b)^2-2ab$</p>
```

### WP 3022 — 分散・標準偏差の変量変換の証明。平均式の `x_{1} + x_{2} + x_{n}` に中間項がない。

原稿 90〜102 行（改行・記法を保持）:

```text
## 分散・標準偏差における変量の変換


<div class="info-box">$n$ 個の値からなるデータ $x_{1} , x_{2} , \cdots , x_{n}$ の平均値を $\overline{x}$  ， 分散 $s_{x}^2$ ，標準偏差を $s_{x}$ とする。 $u_{i} = ax_{i} +b$ $(i=1,2, \cdots ,n)$ としたとき， $u_{i}$ の分散を $s_{1}^2$ ，標準偏差を $s_{u}$ とすると，



[Ⅰ] $s_{u}^2 = a^2 s_{x}^2$




[Ⅱ] $s_{u} = \vert a \vert s_{x}$
```

原稿 106〜120 行（改行・記法を保持）:

```text
<div class="blank-box bb-green">証明



$x$ の平均値 $\overline{x}$ ，分散 $s_{x}^2$ は，




$\begin{eqnarray} \left\{ \begin{array}{l} \displaystyle \overline{x} = \frac{1}{n} (x_{1} + x_{2} + x_{n} ) \\ \displaystyle s_{x}^2= \frac{1}{n} \{ (x_{1} - \overline{x} )^2 + (x_{2} - \overline{x} )^2 + \cdots + (x_{n} - \overline{x} ) ^2 \} \ ( \gt 0 ) \end{array} \right. \end{eqnarray}$




$u_{i} =ax_{i} +b$ のとき， $\overline{u} =a \overline{x} +b$ 。このとき，$u$ の分散 $u_{x}^2$ は，
```
