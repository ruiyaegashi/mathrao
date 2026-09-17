# Mathrao 2.0 公開前要確認事項の原因分析

原稿309件は変更していない。以下は `reports/math-validation.json` と救出Markdown、静的出力の照合結果。行番号は救出Markdownの行番号。

## KaTeX：31箇所・12記事

31箇所すべての直接原因は、旧MathJax/LaTeXの `\begin{eqnarray}…\end{eqnarray}` をKaTeXが認識しないこと（`No such environment: eqnarray`）。[KaTeXの対応環境](https://katex.org/docs/supported)には `array`、`aligned` 等がある。
太字の静的エラー対象は19箇所・10記事。残り12箇所はHTML内の数式で、ブラウザの自動描画段階に同じ構文エラーを持つ。

| WP ID・原稿行 | 静的HTML | 意図 | 判定・推奨互換表現 |
|---|---|---|---|
| 2582:58#1 | HTML内 | 二つの二項式の分配・展開 | **自動修正可**。HTMLエンティティを表示用に復号し、外側のみ `\begin{array}{rcl}…\end{array}` にする。`&=&` の3列を維持。 |
| 2582:59#2 | HTML内 | 三つの二項式の分配・展開 | **自動修正可**。HTMLエンティティを表示用に復号し、外側のみ `\begin{array}{rcl}…\end{array}` にする。`&=&` の3列を維持。 |
| 2582:71#3 | HTML内 | 二項式の分配 | **自動修正可**。HTMLエンティティを表示用に復号し、外側のみ `\begin{array}{rcl}…\end{array}` にする。`&=&` の3列を維持。 |
| 2582:103#4 | HTML内 | 和の平方 | **自動修正可**。HTMLエンティティを表示用に復号し、外側のみ `\begin{array}{rcl}…\end{array}` にする。`&=&` の3列を維持。 |
| 2582:109#5 | HTML内 | 平方差 | **自動修正可**。HTMLエンティティを表示用に復号し、外側のみ `\begin{array}{rcl}…\end{array}` にする。`&=&` の3列を維持。 |
| 2582:116#6 | HTML内 | 和の立方 | **自動修正可**。HTMLエンティティを表示用に復号し、外側のみ `\begin{array}{rcl}…\end{array}` にする。`&=&` の3列を維持。 |
| 2582:122#7 | HTML内 | 立方和 | **自動修正可**。HTMLエンティティを表示用に復号し、外側のみ `\begin{array}{rcl}…\end{array}` にする。`&=&` の3列を維持。 |
| 2582:128#8 | HTML内 | 三項の平方 | **自動修正可**。HTMLエンティティを表示用に復号し、外側のみ `\begin{array}{rcl}…\end{array}` にする。`&=&` の3列を維持。 |
| 2582:134#9 | HTML内 | 立方和の因数分解の展開 | **要数学内容確認**。HTMLエンティティを表示用に復号し、外側のみ `\begin{array}{rcl}…\end{array}` にする。`&=&` の3列を維持。 中間式の `c^4` 等に代数上の疑義があり、式本文は自動訂正不可。 |
| 2582:148#10 | HTML内 | 立方和の変形 | **自動修正可**。HTMLエンティティを表示用に復号し、外側のみ `\begin{array}{rcl}…\end{array}` にする。`&=&` の3列を維持。 |
| 2582:155#11 | HTML内 | 平方和の変形 | **自動修正可**。HTMLエンティティを表示用に復号し、外側のみ `\begin{array}{rcl}…\end{array}` にする。`&=&` の3列を維持。 |
| 2586:27#1 | HTML内 | 絶対値の区分的定義 | **人間確認後修正**。外側の `\begin{eqnarray}` と `\end{eqnarray}` だけ外し、内側の `\left\{\begin{array}{l}…\end{array}\right.` を維持。 数式中の日本語を目視。 |
| 2651:161#1 | **エラー表示** | 判別式による解の種類の列挙 | **自動修正可**。外側の `\begin{eqnarray}` と `\end{eqnarray}` だけ外し、内側の `\left\{\begin{array}{l}…\end{array}\right.` を維持。 |
| 2711:67#1 | **エラー表示** | 放物線の平行移動と逆変換 | **自動修正可**。外側の `\begin{eqnarray}` と `\end{eqnarray}` だけ外し、内側の `\left\{\begin{array}{l}…\end{array}\right.` を維持。 |
| 2711:67#2 | **エラー表示** | 放物線の平行移動と逆変換 | **自動修正可**。外側の `\begin{eqnarray}` と `\end{eqnarray}` だけ外し、内側の `\left\{\begin{array}{l}…\end{array}\right.` を維持。 |
| 2711:140#3 | **エラー表示** | x軸対称移動と逆変換 | **自動修正可**。外側の `\begin{eqnarray}` と `\end{eqnarray}` だけ外し、内側の `\left\{\begin{array}{l}…\end{array}\right.` を維持。 |
| 2711:140#4 | **エラー表示** | x軸対称移動と逆変換 | **自動修正可**。外側の `\begin{eqnarray}` と `\end{eqnarray}` だけ外し、内側の `\left\{\begin{array}{l}…\end{array}\right.` を維持。 |
| 2711:208#5 | **エラー表示** | y軸対称移動と逆変換 | **自動修正可**。外側の `\begin{eqnarray}` と `\end{eqnarray}` だけ外し、内側の `\left\{\begin{array}{l}…\end{array}\right.` を維持。 |
| 2711:208#6 | **エラー表示** | y軸対称移動と逆変換 | **自動修正可**。外側の `\begin{eqnarray}` と `\end{eqnarray}` だけ外し、内側の `\left\{\begin{array}{l}…\end{array}\right.` を維持。 |
| 2711:281#7 | **エラー表示** | 原点対称移動と逆変換 | **自動修正可**。外側の `\begin{eqnarray}` と `\end{eqnarray}` だけ外し、内側の `\left\{\begin{array}{l}…\end{array}\right.` を維持。 |
| 2711:281#8 | **エラー表示** | 原点対称移動と逆変換 | **自動修正可**。外側の `\begin{eqnarray}` と `\end{eqnarray}` だけ外し、内側の `\left\{\begin{array}{l}…\end{array}\right.` を維持。 |
| 2737:132#1 | **エラー表示** | 余弦定理の三辺それぞれの式 | **自動修正可**。外側の `\begin{eqnarray}` と `\end{eqnarray}` だけ外し、内側の `\left\{\begin{array}{l}…\end{array}\right.` を維持。 |
| 2737:185#2 | **エラー表示** | 余弦定理の残り二辺の式 | **自動修正可**。外側の `\begin{eqnarray}` と `\end{eqnarray}` だけ外し、内側の `\left\{\begin{array}{l}…\end{array}\right.` を維持。 |
| 2763:52#1 | **エラー表示** | 三角形の成立条件の連立表示 | **自動修正可**。外側の `\begin{eqnarray}` と `\end{eqnarray}` だけ外し、内側の `\left\{\begin{array}{l}…\end{array}\right.` を維持。 |
| 2763:62#2 | **エラー表示** | 三角形の不等式を①〜③と対応付けた連立表示 | **人間確認後修正**。外側の `\begin{eqnarray}` と `\end{eqnarray}` だけ外し、内側の `\left\{\begin{array}{l}…\end{array}\right.` を維持。 ①〜③はKaTeXの字形警告あり。表示を目視。 |
| 2797:54#1 | **エラー表示** | 内心による三つの小三角形の面積 | **自動修正可**。外側の `\begin{eqnarray}` と `\end{eqnarray}` だけ外し、内側の `\left\{\begin{array}{l}…\end{array}\right.` を維持。 |
| 2849:49#1 | **エラー表示** | 面積比に用いる二つの面積式 | **自動修正可**。外側の `\begin{eqnarray}` と `\end{eqnarray}` だけ外し、内側の `\left\{\begin{array}{l}…\end{array}\right.` を維持。 |
| 2994:140#1 | **エラー表示** | 平均からの偏差の符号による四領域 | **人間確認後修正**。外側の `\begin{eqnarray}` と `\end{eqnarray}` だけ外し、内側の `\left\{\begin{array}{l}…\end{array}\right.` を維持。 数式中の日本語を目視。 |
| 3022:115#1 | **エラー表示** | 平均と分散の式の列挙 | **要数学内容確認**。外側の `\begin{eqnarray}` と `\end{eqnarray}` だけ外し、内側の `\left\{\begin{array}{l}…\end{array}\right.` を維持。 平均の総和に中間項の省略記号がなく、内容確認を要する。 |
| 3147:99#1 | **エラー表示** | 合同式の差を倍数で表す連立式 | **自動修正可**。外側の `\begin{eqnarray}` と `\end{eqnarray}` だけ外し、内側の `\left\{\begin{array}{l}…\end{array}\right.` を維持。 |
| 3233:31#1 | **エラー表示** | 中点連結定理の平行関係と長さの式 | **人間確認後修正**。外側の `\begin{eqnarray}` と `\end{eqnarray}` だけ外し、内側の `\left\{\begin{array}{l}…\end{array}\right.` を維持。 `\ / \! / \` は平行記号の見た目を模した可能性。`\parallel` への変更は目視後。 |

上記の提案を原稿に適用せず、メモリ上で31箇所すべて `katex.renderToString(..., throwOnError: true)` を通した。これは**構文の検査のみ**であり、数式の正誤や見た目の保証ではない。静的エラー対象のWP IDは 2651、2711、2737、2763、2797、2849、2994、3022、3147、3233。

### 各箇所の原記法とエラー全文

#### WP 2582 行58 #1 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 - 数学Ⅰ - 展開公式・因数分解公式 +α
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-1-1/`
- 表示段階: raw HTML内。ブラウザ自動描画時にエラー
- 意図: 二つの二項式の分配・展開
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲ (a+b)(c+d) &=&…`
- 原稿上の記法:

```text
\begin{eqnarray} (a+b)(c+d) &amp;=&amp; (a+b)C \\ &amp;=&amp; aC+bC \\ &amp;=&amp; a(c+d)+b(c+d) \\ &amp;=&amp; ac+ad+bc+bd \end{eqnarray}
```

#### WP 2582 行59 #2 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 - 数学Ⅰ - 展開公式・因数分解公式 +α
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-1-1/`
- 表示段階: raw HTML内。ブラウザ自動描画時にエラー
- 意図: 三つの二項式の分配・展開
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲ (a+b)(c+d)(e+f…`
- 原稿上の記法:

```text
\begin{eqnarray} (a+b)(c+d)(e+f) &amp;=&amp; (a+b)CE \\ &amp;=&amp; aCE+bCE \\ &amp;=&amp; aE(c+d)+bE(c+d) \\ &amp;=&amp;  acE+adE+bcE+bdE \\ &amp;=&amp; ac(e+f)+ad(e+f)+bc(e+f)+bd(e+f) \\ &amp;=&amp; ace+acf+ade+adf+bce+bcf+bde+bdf \end{eqnarray}
```

#### WP 2582 行71 #3 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 - 数学Ⅰ - 展開公式・因数分解公式 +α
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-1-1/`
- 表示段階: raw HTML内。ブラウザ自動描画時にエラー
- 意図: 二項式の分配
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲ (a+b)(c+d) &=&…`
- 原稿上の記法:

```text
\begin{eqnarray} (a+b)(c+d) &amp;=&amp; a(c+d)+b(c+d) \\ &amp;=&amp; ac+ad+bc+bd \end{eqnarray}
```

#### WP 2582 行103 #4 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 - 数学Ⅰ - 展開公式・因数分解公式 +α
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-1-1/`
- 表示段階: raw HTML内。ブラウザ自動描画時にエラー
- 意図: 和の平方
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲ (a+b)^2 &=& (a…`
- 原稿上の記法:

```text
\begin{eqnarray} (a+b)^2 &amp;=&amp; (a+b)(a+b) \\ &amp;=&amp; a(a+b)+b(a+b) \\ &amp;=&amp; a^2+ab+ab+b^2 \\ &amp;=&amp; a^2+2ab+b^2 \end{eqnarray}
```

#### WP 2582 行109 #5 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 - 数学Ⅰ - 展開公式・因数分解公式 +α
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-1-1/`
- 表示段階: raw HTML内。ブラウザ自動描画時にエラー
- 意図: 平方差
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲ (a+b)(a-b) &=&…`
- 原稿上の記法:

```text
\begin{eqnarray} (a+b)(a-b) &amp;=&amp; a(a-b)+b(a-b) \\ &amp;=&amp; a^2-ab+ab-b^2 \\ &amp;=&amp; a^2-b^2 \end{eqnarray}
```

#### WP 2582 行116 #6 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 - 数学Ⅰ - 展開公式・因数分解公式 +α
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-1-1/`
- 表示段階: raw HTML内。ブラウザ自動描画時にエラー
- 意図: 和の立方
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲ (a+b)^3 &=& (a…`
- 原稿上の記法:

```text
\begin{eqnarray} (a+b)^3 &amp;=&amp; (a+b)(a+b)^2 \\ &amp;=&amp; (a+b)(a^2+2ab+b^2) \\ &amp;=&amp; a(a^2+2ab+b^2)+b(a^2+2ab+b^2) \\ &amp;=&amp; a^3+2a^2b+ab^2+a^2b+2ab^2+b^3 \\ &amp;=&amp; a^3+3a^2b+3ab^2+b^3 \end{eqnarray}
```

#### WP 2582 行122 #7 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 - 数学Ⅰ - 展開公式・因数分解公式 +α
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-1-1/`
- 表示段階: raw HTML内。ブラウザ自動描画時にエラー
- 意図: 立方和
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲ (a+b)(a^2-ab+b…`
- 原稿上の記法:

```text
\begin{eqnarray} (a+b)(a^2-ab+b^2) &amp;=&amp; a(a^2-ab+b^2)+b(a^2-ab+b^2) \\ &amp;=&amp; a^3-a^2b+ab^2+a^2b-ab^2+b^3 \\ &amp;=&amp; a^3+b^3 \end{eqnarray}
```

#### WP 2582 行128 #8 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 - 数学Ⅰ - 展開公式・因数分解公式 +α
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-1-1/`
- 表示段階: raw HTML内。ブラウザ自動描画時にエラー
- 意図: 三項の平方
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲ (a+b+c)^2 &=& …`
- 原稿上の記法:

```text
\begin{eqnarray} (a+b+c)^2 &amp;=&amp; (a+b+c)(a+b+c) \\ &amp;=&amp; a(a+b+c)+b(a+b+c)+c(a+b+c) \\ &amp;=&amp; a^2+ab+ca+ab+b^2+bc+ca+bc+c^2 \\ &amp;=&amp; a^2+b^2+c^2+2ab+2bc+2ca \end{eqnarray}
```

#### WP 2582 行134 #9 — 要数学内容確認

- 記事: 【定理・公式・証明】高校数学定理・公式 - 数学Ⅰ - 展開公式・因数分解公式 +α
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-1-1/`
- 表示段階: raw HTML内。ブラウザ自動描画時にエラー
- 意図: 立方和の因数分解の展開
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲ (a+b+c)(a^2+b^…`
- 原稿上の記法:

```text
\begin{eqnarray} (a+b+c)(a^2+b^2+c^2-ab-bc-ca) &amp;=&amp; a(a^2+b^2+c^2-ab-bc-ca)+b(a^2+b^2+c^2-ab-bc-ca)+c(a^2+b^2+c^2-ab-bc-ca) \\ &amp;=&amp; a^3+ab^2+c^2a-a^2b-abc-ca^2+a^2b+b^3+c^2a-ab^2-b^2c-abc+ca^2+b^2c+c^4-cba-bc^2-c^2a \\ &amp;=&amp; a^3+b^3+c^3-3abc \end{eqnarray}
```

#### WP 2582 行148 #10 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 - 数学Ⅰ - 展開公式・因数分解公式 +α
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-1-1/`
- 表示段階: raw HTML内。ブラウザ自動描画時にエラー
- 意図: 立方和の変形
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲ a^3+b^3 &=& (a…`
- 原稿上の記法:

```text
\begin{eqnarray} a^3+b^3 &amp;=&amp; (a+b)^3-3a^2b-3ab^2 \\ &amp;=&amp; (a+b)^3-3ab(a+b) \end{eqnarray}
```

#### WP 2582 行155 #11 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 - 数学Ⅰ - 展開公式・因数分解公式 +α
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-1-1/`
- 表示段階: raw HTML内。ブラウザ自動描画時にエラー
- 意図: 平方和の変形
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲ a^2+b^2+c^2 &=…`
- 原稿上の記法:

```text
\begin{eqnarray} a^2+b^2+c^2 &amp;=&amp; (a+b+c)^2-2ab-2bc-2ca \\ &amp;=&amp; (a+b+c)^2-2(ab+bc+ca) \end{eqnarray}
```

#### WP 2586 行27 #1 — 人間確認後修正

- 記事: 【定理・公式・証明】高校数学定理・公式 - 数学Ⅰ - 絶対値の性質・方程式・不等式
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-1-2/`
- 表示段階: raw HTML内。ブラウザ自動描画時にエラー
- 意図: 絶対値の区分的定義
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 27: …le |a| = \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲  \left\{    \b…`
- 原稿上の記法:

```text
\displaystyle |a| = \begin{eqnarray}  \left\{    \begin{array}{l}     a \ (a \geqq0のとき) \\      -a \ (a \lt0のとき)    \end{array}  \right.\end{eqnarray}
```

#### WP 2651 行161 #1 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 2次方程式の解・重解・解の個数
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-2-2/`
- 表示段階: 静的HTMLでエラー表示
- 意図: 判別式による解の種類の列挙
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲  \left\{    \b…`
- 原稿上の記法:

```text
\begin{eqnarray}  \left\{    \begin{array}{l}     D \gt 0のとき，異なる2つの実数解をもつ \\      D=0のとき，ただ1つの実数解(重解)をもつ  \\  D \lt 0のとき，実数解をもたない   \end{array}  \right.\end{eqnarray}
```

#### WP 2711 行67 #1 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 関数の平行移動・対称移動
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-2-3/`
- 表示段階: 静的HTMLでエラー表示
- 意図: 放物線の平行移動と逆変換
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲  \left\{    \b…`
- 原稿上の記法:

```text
\begin{eqnarray}  \left\{    \begin{array}{l}   X=x+p    \\      Y=y+q    \end{array}  \right.\end{eqnarray}
```

#### WP 2711 行67 #2 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 関数の平行移動・対称移動
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-2-3/`
- 表示段階: 静的HTMLでエラー表示
- 意図: 放物線の平行移動と逆変換
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲  \left\{    \b…`
- 原稿上の記法:

```text
\begin{eqnarray}  \left\{    \begin{array}{l}      x=X-p \\      y=Y-q    \end{array}  \right.\end{eqnarray}
```

#### WP 2711 行140 #3 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 関数の平行移動・対称移動
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-2-3/`
- 表示段階: 静的HTMLでエラー表示
- 意図: x軸対称移動と逆変換
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲  \left\{    \b…`
- 原稿上の記法:

```text
\begin{eqnarray}  \left\{    \begin{array}{l}   X=x    \\      Y=-y    \end{array}  \right.\end{eqnarray}
```

#### WP 2711 行140 #4 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 関数の平行移動・対称移動
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-2-3/`
- 表示段階: 静的HTMLでエラー表示
- 意図: x軸対称移動と逆変換
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲  \left\{    \b…`
- 原稿上の記法:

```text
\begin{eqnarray}  \left\{    \begin{array}{l}      x=X \\      y=-Y    \end{array}  \right.\end{eqnarray}
```

#### WP 2711 行208 #5 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 関数の平行移動・対称移動
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-2-3/`
- 表示段階: 静的HTMLでエラー表示
- 意図: y軸対称移動と逆変換
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲  \left\{    \b…`
- 原稿上の記法:

```text
\begin{eqnarray}  \left\{    \begin{array}{l}   X=-x    \\      Y=y    \end{array}  \right.\end{eqnarray}
```

#### WP 2711 行208 #6 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 関数の平行移動・対称移動
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-2-3/`
- 表示段階: 静的HTMLでエラー表示
- 意図: y軸対称移動と逆変換
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲  \left\{    \b…`
- 原稿上の記法:

```text
\begin{eqnarray}  \left\{    \begin{array}{l}      x=-X \\      y=Y    \end{array}  \right.\end{eqnarray}
```

#### WP 2711 行281 #7 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 関数の平行移動・対称移動
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-2-3/`
- 表示段階: 静的HTMLでエラー表示
- 意図: 原点対称移動と逆変換
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲  \left\{    \b…`
- 原稿上の記法:

```text
\begin{eqnarray}  \left\{    \begin{array}{l}     X=-x  \\      Y=-y    \end{array}  \right.\end{eqnarray}
```

#### WP 2711 行281 #8 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 関数の平行移動・対称移動
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-2-3/`
- 表示段階: 静的HTMLでエラー表示
- 意図: 原点対称移動と逆変換
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲  \left\{    \b…`
- 原稿上の記法:

```text
\begin{eqnarray}  \left\{    \begin{array}{l}      x=-X \\      y=-Y    \end{array}  \right.\end{eqnarray}
```

#### WP 2737 行132 #1 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 正弦定理・余弦定理
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-3-1/`
- 表示段階: 静的HTMLでエラー表示
- 意図: 余弦定理の三辺それぞれの式
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲  \left\{    \b…`
- 原稿上の記法:

```text
\begin{eqnarray}  \left\{    \begin{array}{l}      a^2 =b^2 + c^2 -2bc \cos A \\      b^2 =c^2 +a^2 -2ca \cos B  \\ c^2 =a^2 +b^2 -2ab \cos C    \end{array}  \right.\end{eqnarray}
```

#### WP 2737 行185 #2 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 正弦定理・余弦定理
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-3-1/`
- 表示段階: 静的HTMLでエラー表示
- 意図: 余弦定理の残り二辺の式
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲  \left\{    \b…`
- 原稿上の記法:

```text
\begin{eqnarray}  \left\{    \begin{array}{l}     b^2 =c^2 +a^2 -2ca \cos B \\     c^2 =a^2 +b^2 -2ab \cos C    \end{array}  \right.\end{eqnarray}
```

#### WP 2763 行52 #1 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 三角形の成立条件・辺と角の大小関係
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-3-3/`
- 表示段階: 静的HTMLでエラー表示
- 意図: 三角形の成立条件の連立表示
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲  \left\{    \b…`
- 原稿上の記法:

```text
\begin{eqnarray}  \left\{    \begin{array}{l}      a \lt b+c \\     b \lt c+a  \\ c \lt a+b    \end{array}  \right.\end{eqnarray}
```

#### WP 2763 行62 #2 — 人間確認後修正

- 記事: 【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 三角形の成立条件・辺と角の大小関係
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-3-3/`
- 表示段階: 静的HTMLでエラー表示
- 意図: 三角形の不等式を①〜③と対応付けた連立表示
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲  \left\{    \b…`
- 原稿上の記法:

```text
\begin{eqnarray}  \left\{    \begin{array}{ll}      a \lt b+c  &amp; …①  \\     b-c \lt a &amp; …②    \\ c-b \lt a &amp; …③      \end{array}  \right.\end{eqnarray}
```

#### WP 2797 行54 #1 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 三角形の内接円の半径
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-3-5/`
- 表示段階: 静的HTMLでエラー表示
- 意図: 内心による三つの小三角形の面積
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲  \left\{    \b…`
- 原稿上の記法:

```text
\begin{eqnarray}  \left\{    \begin{array}{l}     \displaystyle \triangle \mathrm{ IAB } = \frac{1}{2} cr \\   \displaystyle \triangle \mathrm{ IBC } = \frac{1}{2} ar  \\ \displaystyle \triangle \mathrm{ ICA } = \frac{1}{2} br   \end{array}  \right.\end{eqnarray}
```

#### WP 2849 行49 #1 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 面積比
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-3-9/`
- 表示段階: 静的HTMLでエラー表示
- 意図: 面積比に用いる二つの面積式
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲  \left\{    \b…`
- 原稿上の記法:

```text
\begin{eqnarray}  \left\{    \begin{array}{l}     \displaystyle \triangle \mathrm{ ABD } = \frac{1}{2} \cdot \mathrm{ BD } \cdot \mathrm{ AH } = \frac{1}{2} \cdot \frac{m}{m+n} \mathrm{ BC } \cdot \mathrm{ AH } \\     \displaystyle \triangle \mathrm{ ACD } = \frac{1}{2} \cdot \mathrm{ CD } \cdot \mathrm{ AH } = \frac{1}{2} \cdot \frac{n}{m+n} \mathrm{ BC } \cdot \mathrm{ AH }    \end{array}  \right.\end{eqnarray}
```

#### WP 2994 行140 #1 — 人間確認後修正

- 記事: 【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 分散・標準偏差・共分散・相関係数
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-5-3/`
- 表示段階: 静的HTMLでエラー表示
- 意図: 平均からの偏差の符号による四領域
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲ \left\{ \begin…`
- 原稿上の記法:

```text
\begin{eqnarray} \left\{ \begin{array}{l} x_{i} - \overline{x} \gt 0,y_{i} - \overline{y} \gt 0 となる( x_{i} , y_{i} ) を含む領域を領域1 \\ x_{i} - \overline{x} \lt 0 , y_{i} - \overline{y} \gt 0 となる ( x_{i} , y_{i} ) を含む領域を領域2 \\ x_{i} - \overline{x} \lt 0 , y_{i} - \overline{y} \lt 0 となる ( x_{i} , y_{i} ) を含む領域を領域3 \\ x_{i} - \overline{x} \gt 0 , y_{i} - \overline{y} \lt 0 となる ( x_{i} , y_{i} ) を含む領域を領域4 \end{array} \right. \end{eqnarray}
```

#### WP 3022 行115 #1 — 要数学内容確認

- 記事: 【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 平均・分散・共分散・標準偏差における変量の変換
- legacy path: `/theorems-proof-of-high-school-math/theorems-h1-5-4/`
- 表示段階: 静的HTMLでエラー表示
- 意図: 平均と分散の式の列挙
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲ \left\{ \begin…`
- 原稿上の記法:

```text
\begin{eqnarray} \left\{ \begin{array}{l} \displaystyle \overline{x} = \frac{1}{n} (x_{1} + x_{2} + x_{n} ) \\ \displaystyle s_{x}^2= \frac{1}{n} \{ (x_{1} - \overline{x} )^2 + (x_{2} - \overline{x} )^2 + \cdots + (x_{n} - \overline{x} ) ^2 \} \ ( \gt 0 ) \end{array} \right. \end{eqnarray}
```

#### WP 3147 行99 #1 — 自動修正可

- 記事: 【定理・公式・証明】高校数学定理・公式 – 数学A – 合同式
- legacy path: `/theorems-proof-of-high-school-math/theorems-ha-3-9/`
- 表示段階: 静的HTMLでエラー表示
- 意図: 合同式の差を倍数で表す連立式
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲ \left \{ \begi…`
- 原稿上の記法:

```text
\begin{eqnarray} \left \{ \begin{array}{l} a-b=mk \\ b-c=ml \end{array} \right. \end{eqnarray}
```

#### WP 3233 行31 #1 — 人間確認後修正

- 記事: 【定理・公式・証明】高校数学定理・公式 – 数学A – 中点連結定理
- legacy path: `/theorems-proof-of-high-school-math/theorems-ha-4-2/`
- 表示段階: 静的HTMLでエラー表示
- 意図: 中点連結定理の平行関係と長さの式
- KaTeXエラー: `KaTeX parse error: No such environment: eqnarray at position 7: \begin{̲e̲q̲n̲a̲r̲r̲a̲y̲}̲ \left \{ \begi…`
- 原稿上の記法:

```text
\begin{eqnarray} \left \{ \begin{array}{l} \mathrm{DE} \ / \! / \ \mathrm{BC} \\ \displaystyle \mathrm{DE} = \frac{1}{2} \mathrm{BC} \end{array} \right. \end{eqnarray}
```
## WordPressショートコード

- `[overrule]…[/overrule]`: 開始・終了各55個、31記事。例として WP 2586 では `info-box` の後の「【解説】」全体、WP 2711 では「説明①」から始まる解説を囲む。短い一段落の例（WP 2649）もある。内容を非表示にするための `more/less` 属性はない。**解説・補足を通常本文と区別する枠**という推定が最も堅いが、旧テーマの正確な色・余白・折り畳み有無は原稿だけでは特定できない。WP 2586 などはショートコードがHTMLの `<span>` に分断されているため、単純なMarkdown文字列置換は危険。
- 推奨: 原稿外の表示処理で対を構文として認識し、囲まれた本文を常時表示する `<aside class="legacy-overrule">` 相当の軽い解説枠にする。見出しや数式・表をそのままレンダリングし、対応が不明な対やHTML境界をまたぐ対は元記法のまま要確認とする。色や旧サイト固有の動作を決め打ちしない。
- `[wpex more="…" less="…"]…[/wpex]`: 2対。公開 WP 1620 は「定理の詳細(性質・公式・名無し・系・原理)／閉じる」、下書き WP 2535 は「見る／閉じる」で三角比の大きな表を囲む。表示と非表示を切り替える意図は属性・内容から明瞭で、[WordPress.org の Expander サポート欄](https://wordpress.org/support/plugin/expander/)にも `wpex` の開閉に関する項目がある。ただし当時の具体的な導入プラグイン・CSSはこの原稿だけでは確定しない。
- 推奨: Astroのレンダリング層で囲まれた本文を `<details><summary>more属性の文言</summary>…</details>` にする。標準では閉じ、開いたときの「閉じる」は必要なら末尾の操作ボタンで実現する。表・数式・見出しを含むため、Markdown処理前に安全なブロックの対応関係を解析し、HTML構造の正当性・キーボード操作・目視を確認する。下書きWP 2535は引き続き非公開。

現在は原記法が残っており、互換表示はまだ実装していない。

## 旧埋め込み：7記事

7記事の埋め込みは**すべて** `rcm-fe.amazon-adsystem.com` の書籍広告iframe、計120個。動画や自サイトの教材埋め込みはこの7記事には見つからない。現行のAstro表示では自動読込せず `[旧埋め込み：要確認]` に置換し、原稿にはURL・商品識別子を保持している。

| WP ID・旧path | 原稿上の対象 | 現状と推奨 |
|---|---:|---|
| 24「小中高の算数・数学は人生で何の役に立つの？なんで勉強しなきゃいけないの？」 `/math-is-useful/` | Amazon広告13 | 広告の自動読込は停止。書籍紹介の文脈・代替リンクを人間が確認する。 |
| 57「【しくじり先生】中田塾：ピタゴラスのしくじりから学ぶ「勉強する理由」【しくじり偉人伝】」 `/shikujiri-pythagoras/` | Amazon広告2 | 同上。記事名は動画を連想させるが、検出したiframeは広告。 |
| 1388「受験勉強の「不安」と「焦り」に打ち勝ちたいなら「小さな成功」をつかめ」 `/how-to-overcome-impatience-and-anxiety/` | Amazon広告2 | 同上。 |
| 1390「「地頭」っぽいものを鍛えれば勉強が加速していく」 `/improving-natural-abilities/` | Amazon広告3 | 同上。 |
| 1568「高校数学の種類別おすすめ学習参考書①」 `/recommended-study-aid-books-of-mathematics-1/` | Amazon広告28 | 書籍一覧への影響が大きい。書名・ISBN等と静的リンクへの代替を確認するまでプレースホルダーを維持。 |
| 1739「高校数学の種類別おすすめ学習参考書②」 `/recommended-study-aid-books-of-mathematics-2/` | Amazon広告54 | 同上。 |
| 1741「高校数学の種類別おすすめ学習参考書③」 `/recommended-study-aid-books-of-mathematics-3/` | Amazon広告18 | 同上。 |

静的サイトでは広告iframeを自動復活させない。必要な書誌情報を原稿周辺から確認し、広告のない静的な書籍名・出版社等の表現を別工程で検討する。商品・紹介内容の変更は今回しない。

## 未収録記事への旧mathrao.comリンク：4箇所

リンク先は4箇所とも `http://mathrao.com/recommended-study-aid-books-of-mathematics/`。救出台帳309件の `legacy_path` に一致する記事はない。一方、末尾に `-1/`、`-2/`、`-3/` を付けた公開3記事（WP 1568、1739、1741）は存在する。元のURLが削除・改名・一覧用ページだったかはバックアップだけでは断定できない。

| リンク元WP ID・path | 原稿行 | 確認結果・推奨 |
|---|---|---|
| 1563 `/kinds-of-study-aid-books-of-mathematics/` | 29、345 | 両方とも未収録の同一URL。3分割記事との関係を人間が確認し、適切な案内先を決める。 |
| 1566 `/how-to-use-study-aid-books-of-mathematics/` | 29、329 | 同上。 |

現在の表示はリンクを原文のまま保持している。削除・推測による書き換えや、3記事のいずれかへの無根拠な転送はしない。

## `_wp_old_slug` のリダイレクト候補

Front Matterの旧slug履歴から確認できた4候補。仮定したルート直下の旧pathはいずれも現在の306公開pathと衝突しない。ただし旧URLの実際の階層・過去のアクセスログは未確認。

| 旧path候補 | 現在の公開path | WP ID |
|---|---|---:|
| `/firstofall/` | `/first-of-all/` | 15 |
| `/early-to-bed-and-early-to-rise/` | `/the-early-bird-catches-the-worm/` | 1463 |
| `/brush-up-your-junior-high-study/` | `/brush-up-your-past-study/` | 1510 |
| `/how-to-make-a-daily-schedule/` | `/how-to-make-a-weekly-schedule/` | 1813 |

`migration/slug-aliases.json` の214件は現存記事の短いslugから旧階層pathを参照する本文内リンクの対応で、**旧slug履歴4件とは別物**。214件を一律の301候補とみなさない。

提案: 4件の出典と旧階層を確認してから、リポジトリで管理する `public/_redirects` に `旧path 現行path 301` を1行ずつ生成する。生成前に公開path・素材pathとの衝突、重複、転送ループを検査する。Cloudflare Pagesの[_redirects仕様](https://developers.cloudflare.com/pages/configuration/redirects/)では静的ルールを最大2,000件扱え、ファイルは公開アセットディレクトリに置ける。現行の静的Astro構成と相性がよい。仮URLでステータスとLocationを検査してから本番へ適用する。今回は `_redirects` もCloudflare設定も作成・変更しない。

## 残件の判断順

1. **自動修正して安全**: `eqnarray` の外側だけを表示時に互換変換する25箇所。特に `array` の三列配置・内側の連立式を保存し、原文ハッシュと変換対象件数を検査する。現時点では試案のみ。
2. **人間が表示だけ確認**: 数式4箇所（WP 2586:27、2763:62、2994:140、3233:31）で日本語・丸数字・平行記号風の字形を確認。`overrule` 55対、`wpex` 2対の枠と開閉を実装後に画面確認する。旧slug4件は元の階層と衝突検査後に転送確認。
3. **数学的内容を人間が確認**: WP 2582:134 の展開途中に `c^4` 等の疑義、WP 3022:115 の平均式で中間項が省略された可能性。構文の互換変換が通っても式本文は機械的に直さない。
4. **公開後対応でも問題ない候補**: Amazon広告iframe120個の復活は不要。7記事のプレースホルダーは現在も自動読込を抑止。ただし参考書紹介3記事は書誌情報が欠けて見えるため公開前に見た目を確認する。未収録記事への旧リンク4箇所は公開前に少なくとも未解決として明示し、転送先の判断自体は内容整理の後工程に回せる。

公開の可否そのものは数式エラー表示と欠けた書籍紹介の見た目を確認して判断する。ここでは原稿、移行コード、リダイレクト設定、外部サービスを変更していない。
