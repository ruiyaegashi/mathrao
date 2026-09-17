---
title: "【定理・公式・証明】高校数学定理・公式 – 数学A – 事象の独立・独立な試行・反復試行の確率"
wp_id: 3087
content_type: "page"
status: "publish"
published_at: "2020-05-10 22:58:32"
wp_date: "2020-05-10 22:58:32"
modified_at: "2020-05-10 22:58:32"
legacy_url: "http://mathrao.com/theorems-proof-of-high-school-math/theorems-ha-2-3/"
legacy_path: "/theorems-proof-of-high-school-math/theorems-ha-2-3/"
legacy_slug: "theorems-ha-2-3"
former_slugs: []
parent_wp_id: 2564
parent_title: "【定理・公式・証明】高校数学定理・公式一覧"
hierarchy: ["【定理・公式・証明】高校数学定理・公式一覧", "【定理・公式・証明】高校数学定理・公式 – 数学A – 事象の独立・独立な試行・反復試行の確率"]
category: []
tags: []
mathrao_section: "定理・公式・証明"
mathrao_grade: null
mathrao_course: "数学A"
source_content_sha256: "939de108f0189d60cc4d0ced24fa401e29c5c86f2efbb6471b5835467ed479d2"
---

## 独立な試行


<div class="info-box">独立な試行 $S,T$ において試行 $S$ において事象 $A$ が起こり，なおかつ試行 $T$ において事象 $B$ が起こる確率は，



$P(A) \times P(B)$


</div>
<div class="blank-box bb-green">証明



2つの試行 $S,T$ において， $A$ の思考が $T$ の結果には影響せず，また $T$ の試行も $S$ の結果に影響を与えないとき， $S$ と $T$ は独立な試行であるという。




例えば，




$S:硬貨を一枚投げる$ $T:サイコロを1回ふる$




とすると， $S$ と $T$ は独立である。




試行 $S,T$ における全事象をそれぞれ $U,V$ とすると，




$\displaystyle P(A) = \frac{n(A)}{n(U)},P(B)= \frac{n(B)}{n(V)}$




一方，試行 $S,T$ を行うとき，起こりうるすべての場合の数は，




$n(U) \times n(V)$ (通り)




であり，これは同様に確からしい。




このうち $S$ において事象 $A$ が起こり，なおかつ $T$ において事象 $B$ が起こるのは，




$n(A) \times n(B)$ (通り)




であるから， $S$ において事象 $A$ が起こり、なおかつ  $T$ において事象 $B$ が起こる確率は，




$\displaystyle \frac{n(A) \times n(B)}{n(U) \times n(V)}$




であり，




$\displaystyle \frac{n(A) \times n(B)}{n(U) \times n(V)} = \frac{n(A)}{n(U)} \times \frac{n(B)}{n(V)} = P(A) \times P(B)$




であるから， $S$ において事象 $A$ が起こり，なおかつ $T$ において事象 $B$ が起こる確率は




$P(A) \times P(B)$


</div>


&nbsp;




## 反復試行の確率


<div class="info-box">事象 $A$ の起こる確率が $p$ である試行を $n$ 回繰り返すとき，事象 $A$ がちょうど $r$ 回( $r=0,1,2, \cdots ,n$ )起こる確率は，



$_{n} C_{r} p^r (1-p)^{n-r}$ (ただし， $p^0= (1-p)^0 =1$ )


</div>


[overrule]説明




例題




赤球が2個，白球が1個入った袋から球を1個取り，色を見て元に戻すことを5回繰り返す。このとき，赤球をちょうど3回取り出す確率を求めよ。




赤を取る $\cdots$ 〇　(確率 $\displaystyle \frac{2}{3}$ ) ， 白を取る $\cdots$ ✕ (確率 $\displaystyle \frac{1}{3}$ )




と表す。5回のうち赤球を3回取り出すとき，球の取り出し方にはいくつかのパターンがあり，互いに排反である。取り出し方と，それぞれの確率は次図のようになる。




図のように，5回のうち，赤球を3回取り出す方法は $_{5} C_{3} =10$ 通り ((i)から(x))あり，求める確率は，




(i)または (ii)または $\cdots$ または(x)




が起こる確率であるから，




$\displaystyle \left( \frac{2}{3} \right) ^3 \left( \frac{1}{3} \right) ^2 + \left( \frac{2}{3} \right) ^3 \left( \frac{1}{3} \right) ^2 + \cdots +\left( \frac{2}{3} \right) ^3 \left( \frac{1}{3} \right) ^2 = _{5} C_{3} \left( \frac{2}{3} \right) ^3 \left( \frac{1}{3} \right) ^2 = \frac{80}{243}$ [/overrule]




&nbsp;




## 事象の独立


<div class="info-box">ある一つの試行 $S$ における事象 $A,B$ において， $A$ と $B$ が独立であるとは，



$P(A \cap B) = P(A)P(B)$




が成り立つことである。


</div>


[overrule]説明




(※)が成り立つとき，




$\displaystyle P_{A} (B)= \frac{P(A \cap B)}{P(A)} = \frac{P(A)P(B)}{P(A)} = P(B)$




$\displaystyle P_{A} (B)= \frac{P( \overline{A} \cap B)}{P( \overline{A} )} = \frac{P(B) -P(A \cap B)}{1-P(A)} = \frac{P(B)-P(A)P(B)}{1- P(A)}$




$\displaystyle \frac{P(B) \{1-P(A) \} }{1-P(A)} =P(B)$




であるから，




「 $A$ が起きたとわかった時に $B$ が起こる条件付確率」




も，




「 $A$ が怒らなかったとわかった時に $B$ が起こる条件付確率」




もともに「 $B$ が起こる確率」と等しいことが分かる。




同様にして， $P_{B} (A) =P _{ \overline{B} } (A) =P(A)$ も成り立つ。




このように，一方が起こった，あるいは起こらなかったと分かっても，もう一方の起こる確率に影響しないというのが， $A$ と $B$ が独立であるということである。




「独立」という言葉から，「独立な試行」と勘違いしたり，




「 $A$ と $B$ は同時には起こらない（＝ $A$ と $B$ が互いに排反）」




と勘違いしやすいので，注意しよう。[/overrule]
