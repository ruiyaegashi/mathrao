---
title: "【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 2次方程式の解・重解・解の個数"
wp_id: 2651
content_type: "page"
status: "publish"
published_at: "2020-04-22 22:05:16"
wp_date: "2020-04-22 22:05:16"
modified_at: "2020-04-22 22:05:16"
legacy_url: "http://mathrao.com/theorems-proof-of-high-school-math/theorems-h1-2-2/"
legacy_path: "/theorems-proof-of-high-school-math/theorems-h1-2-2/"
legacy_slug: "theorems-h1-2-2"
former_slugs: []
parent_wp_id: 2564
parent_title: "【定理・公式・証明】高校数学定理・公式一覧"
hierarchy: ["【定理・公式・証明】高校数学定理・公式一覧", "【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 2次方程式の解・重解・解の個数"]
category: []
tags: []
mathrao_section: "定理・公式・証明"
mathrao_grade: null
mathrao_course: "数学I"
source_content_sha256: "4bcded795380db2cefc2f8f1293804bea0aec2a5ea5c4914afff81bf298ce312"
---

## 2次方程式の解(解の公式①)


<div class="info-box">$ax^2+bx+c=0$ $(a \neq 0)$　の解は，



$\displaystyle x=\frac{-b \pm \sqrt{b^2-4ac}}{2a}$


</div>
<div class="blank-box bb-green">証明



$ax^2+bx+c=0$




$\displaystyle a \left( x^2 + \frac{b}{a}x \right)+c=0$




$\displaystyle a \left \{ \left( x+ \frac{b}{2a} \right)^2 - \frac{b^2}{4a^2} \right \} +c=0$




$\displaystyle a \left(x+ \frac{b}{2a} \right)^2 - \frac{b^2}{4a} +c=0$




$\displaystyle a \left( x+ \frac{b}{2a} \right) ^2 - \frac{b^2-4ac}{4a}=0$




$\displaystyle a \left( x+ \frac{b}{2a} \right) ^2 = \frac{b^2 -4ac}{4a} $




$\displaystyle \left( x+ \frac{b}{2a} \right) ^2 = \frac{b^2 -4ac}{4a^2}$




$\displaystyle x+ \frac{b}{2a} = \pm \frac{ \sqrt{b^2 -4ac}}{2a}$




$\displaystyle x= \frac{-b \pm \sqrt{b^2 -4ac}}{2a}$


</div>


## 2次方程式の解(解の公式②)


<div class="info-box">$ax^2+2Bx+c=0$ $(a \neq 0)$ の解は，



$\displaystyle x= \frac{-B \pm \sqrt{B^2 -ac}}{a}$


</div>
<div class="blank-box bb-green">証明①



$ax^2+2Bx+c=0$




$\displaystyle a \left \{ \left(x+ \frac{B}{a} \right)^2 - \frac{B^2}{a^2} \right \} +c=0$




$\displaystyle a \left( x+ \frac{B}{a} \right)^2 - \frac{B^2-ac}{a} =0$




$\displaystyle \left( x+ \frac{B}{a} \right) ^2= \frac{B^2 -ac}{a^2}$




$\displaystyle x+ \frac{B}{a} = \pm \frac{ \sqrt {B^2 -ac}}{a}$




$\displaystyle x= \frac {-B \pm \sqrt{B^2 -ac}}{a}$


</div>
<div class="blank-box bb-green">証明②



$ax^2+2Bx+c=0$ の解は，解の公式①を利用して求めることもできる。




$\displaystyle x= \frac{-2B \pm \sqrt{(2B)^2 -4ac}}{2a}= \frac{-2B \pm \sqrt{4B^2-4ac}}{2a}$




$\displaystyle =\frac{-2B \pm \sqrt{4(B^2-ac)}}{2a} = \frac{-2B \pm 2 \sqrt{B^2 -ac}}{2a}$




$\displaystyle = \frac{-B \pm \sqrt{B^2 -ac}}{a}$


</div>


## 2次方程式の解の個数


<div class="info-box">2次方程式 $ax^2+bx+c=0 (a \neq 0)$ の実数解の個数は， $b^2 -4ac$ の符号により判別することができる。このとき， $b^2 -4ac$ をこの2次方程式の判別式といい， $D$ で表すと，次のことがいえる。



$\begin{eqnarray}  \left\{    \begin{array}{l}     D \gt 0のとき，異なる2つの実数解をもつ \\      D=0のとき，ただ1つの実数解(重解)をもつ  \\  D \lt 0のとき，実数解をもたない   \end{array}  \right.\end{eqnarray}$


</div>


[overrule]説明




2次方程式　$ax^2 +bx+c=0$ の解は，解の公式より，$\displaystyle x=\frac{-b \pm \sqrt{b^2 -4ac}}{2a}$ .




この $\sqrt{ \\ }$ の中の $b^2-4ac$ の部分が判別式であり，これをDとすると，




$D=5$ $( \gt 0)$ のとき，解が $\displaystyle x= \frac{-b \pm \sqrt{5}}{2a}$ となり，異なる2つの実数解をもつ。




$D=0$ のときは，解が $\displaystyle x= \frac{-b}{2a}$ となり，1つの実数解(重解)をもつ。




$D=-5(\lt 0)$ のときは，解が $\displaystyle x=\frac{-b \pm \sqrt{-5}}{2a}$ となり，実数解をもたない。




以上により，判別式 $D=b^2 -4ac$ の符号を調べることで，2次方程式の実数解の個数がわかる。[/overrule]




## 2次方程式の重解


<div class="info-box">2次方程式 $ax^2+bx+c=0$ が重解をもつとき，その重解は，



$\displaystyle x= \frac{-b}{2a}$


</div>


[overrule]説明①(解の公式を用いた説明)




2次方程式 $ax^2+bx+c=0$ の解は，解の公式から，




$\displaystyle x=\frac{-b \pm \sqrt{b^2 -4ac}}{2a} = \frac{-b \pm \sqrt{D}}{2a}$




この2次方程式が重解をもつとき，この方程式の判別式 $D$ は， $D=b^2-4ac=0$ となる。よって，この方程式の重解は，




$\displaystyle x= \frac{-b}{2a}$




説明② (グラフを利用した説明)




2次方程式 $ax^2+bx+c=0$ が重解をもつとき，2次関数 $y=ax^2+bx+c$ のグラフはx軸に接する。このとき，グラフの頂点のy座標は0となる。




$\displaystyle y=ax^2+bx+c=a \left( x+ \frac{b}{2a} \right) ^2 - \frac{b^2-4ac}{4a}$




より，




$\displaystyle (頂点のy座標)=- \frac{b^2-4ac}{4a} =0$




これより，2次方程式 $ax^2+bx+c=0$ の解は，




$\displaystyle a \left( x+ \frac{b}{2a} \right) ^2 =0$




$\displaystyle x= \frac{b}{2a}$[/overrule]




&nbsp;
