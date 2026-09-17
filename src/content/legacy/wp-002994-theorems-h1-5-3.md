---
title: "【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 分散・標準偏差・共分散・相関係数"
wp_id: 2994
content_type: "page"
status: "publish"
published_at: "2020-05-03 18:28:05"
wp_date: "2020-05-03 18:28:05"
modified_at: "2020-05-03 18:33:04"
legacy_url: "http://mathrao.com/theorems-proof-of-high-school-math/theorems-h1-5-3/"
legacy_path: "/theorems-proof-of-high-school-math/theorems-h1-5-3/"
legacy_slug: "theorems-h1-5-3"
former_slugs: []
parent_wp_id: 2564
parent_title: "【定理・公式・証明】高校数学定理・公式一覧"
hierarchy: ["【定理・公式・証明】高校数学定理・公式一覧", "【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 分散・標準偏差・共分散・相関係数"]
category: []
tags: []
mathrao_section: "定理・公式・証明"
mathrao_grade: null
mathrao_course: "数学I"
source_content_sha256: "aaf9b6318ed24217250117986e875d5b1fa7db74b524e62d7afa060ceb7239a5"
---

## 分散①と標準偏差


<div class="info-box">$n$ 個の値からなるデータ $x_{1}$ ， $x_{2}$ ，・・・，$x_{n}$ の平均値を $\overline{x}$ とする。このデータの分散を $s_{x}^2$ ，標準偏差を $s_{x}$ とすると，



$\displaystyle s_{x}^2 =\frac{(x_{1} - \overline{x} )^2 +・・・+(x_{n} - \overline{x})^2}{n}$ ， $s_{x}= \sqrt{s_{x}^2}$


</div>


[overrule]説明




$n$ 個の値それぞれと平均値 $\overline{x}$ の差 $x_1 - \overline{x}$ ， $x_{2} - \overline{x}$ ，・・・， $x_{n} - \overline{x}$ をそれぞれの平均値からの偏差という。




偏差の２乗の平均値を分散といい， $s_{x}$ で表す。また，分散の正の平方根を標準偏差といい， $s_{x}$ で表す。




このとき分散は，




$\displaystyle s_{x}^2 = \frac{x_{1} - \overline{x})^2 + ・・・ + (x_{n} -x^2)}{n}$




また，この正の平方根が標準偏差なので，




$s_{x} = \sqrt{s_{x}^2}$




となる。




この分散と標準偏差の数学的な意味は，データの平均値からの「散らばりの度合い」と表す。例えば，〈図１〉と〈図２〉のような，２つのデータの平均値が同じ値でも，平均値からの差が小さいデータと大きいデータとでは，集合の意味が異なる。このようにデータの平均値からの「ばらつき具合」の指標として標準偏差や分散がある。[/overrule]




&nbsp;




## 共分散①と相関係数


<div class="info-box">２つの変数 $x$ ， $y$ からなるデータとして， $n$ 個の値の組( $x_{1}$ ,$y_{1}$ )，( $x_{2}$ , $y_{2}$ )，・・・，( $x_{n}$ , $y_{n}$ )がある。$x$ の偏差と $y$ の偏差の積の平均を共分散といい， $s_{xy}$ で表すと，



$\displaystyle s_{xy}= \frac{1}{n} \{(x_{1} - \overline{x} )(y_{1} - \overline{y} )+ ・・・ +(x_{n} - \overline{x} )(y_{n} - \overline{y} ) \}$




また，共分散 $s_{xy}$ を $x$ の標準偏差 $s_{x}$ と $y$ の標準偏差 $s_{y}$ の積 $s_{x} s_{y}$ で割った値を $x$ ， $y$ の相関係数といい， $r$で表すと，




$\displaystyle r=\frac{s_{xy}}{s_{x} \cdot s_{y}}$


</div>


[overrule]説明




・共分散




２つの変数 $x$ ， $y$ からなるデータとして， $n$ 個の値の組 ( $x_{i}$ , $y_{i}$ ) ( $i=1,2,・・・,n$ )と $x$ ， $y$ の平均値 $\overline{x}$ ， $\overline{y}$ に対して， $x$ の偏差と $y$の偏差の積の平均値を共分散といい， $s_{xy}$ で表すと，




$\displaystyle s_{xy} =\frac{1}{n} \{ (x_{1} -\overline{x} )( y_{1} - \overline{y}) +・・・+(x_{n} - \overline{x} )( y_{n} - \overline{y} ) \}$




となる。




また，右図のように領域を定める。




$\begin{eqnarray} \left\{ \begin{array}{l} x_{i} - \overline{x} \gt 0,y_{i} - \overline{y} \gt 0 となる( x_{i} , y_{i} ) を含む領域を領域1 \\ x_{i} - \overline{x} \lt 0 , y_{i} - \overline{y} \gt 0 となる ( x_{i} , y_{i} ) を含む領域を領域2 \\ x_{i} - \overline{x} \lt 0 , y_{i} - \overline{y} \lt 0 となる ( x_{i} , y_{i} ) を含む領域を領域3 \\ x_{i} - \overline{x} \gt 0 , y_{i} - \overline{y} \lt 0 となる ( x_{i} , y_{i} ) を含む領域を領域4 \end{array} \right. \end{eqnarray}$




このとき，偏差の積 $(x_{i} - \overline{x} )( y_{i} , \overline{y} )$ の符号と $( x_{i} , y_{i} )$ を含む領域， $x$ ， $y$ の関係について，




となる。




このように， $x$ ， $y$ の偏差の積の平均値である共分散 $s_{xy}$ は符号やその大きさにより， $x$ ， $y$ の相関関係を表す値となる。




・相関係数




2つの変数 $x$ ， $y$ の相関の強さを表す指標を相関係数といい， $r$ で表すと，




$\displaystyle r= \frac{ s_{xy} }{s_{x} \cdot s_{y} }$




この式から，相関係数は共分散 $s_{xy}$ を標準偏差 $s_{x}$ ， $s_{y}$ で割った値であり， $x$ と $y$ の関係を-1から1の間で表す値となる。相関係数は-1に近いほど負の相関が強いといい，1に近いほど正の関係が強いという。[/overrule]




&nbsp;




## 【発展】分散②


<div class="info-box">$n$ 個の値からなるデータ $x_{1} , x_{2} , ・・・ , x_{n}$ の平均値を $\overline{x}$ 分散を $s_{x}^2$ とし，$n$ 個の値の2乗の平均を $\overline{x^2}$ とするとき，



$s_{x}^2 = \overline{x^2} -( \overline{x} )^2$


</div>
<div class="blank-box bb-green">証明



分散①の式を変形すると，




$\displaystyle s_{x}^2 = \frac{1}{n} \{ (x_{1} - \overline{x} )^2 +( x_{2} - \overline{x} )^2 +・・・+ (x_{n} - \overline{x} )^2 \}$




$\displaystyle = \frac{1}{n} \{ (x_{1}^2 +x_{2}^2 +・・・+ x_{n}^2 )-2 \overline{x} (x_{1} + x_{2} +・・・+ x_{n}) +n( \overline{x} )^2 \}$




$\displaystyle = \frac{1}{n} ( x_{1}^2 + x_{2}^2 +・・・+ x_{n}^2 ) -2 \overline{x} \frac{1}{n} (x_{1} + x_{2} +・・・+ x_{n} ) +( \overline{x} )^2$




$= \overline{x^2} -2 \overline{x} \cdot \overline{x} + ( \overline{x} )^2$




$= \overline{x^2} -2( \overline{x} )^2 +( \overline{x} )^2$




$= \overline{x^2} -( \overline{x} )^2$




このように，




$( x の分散)=(x^2 の平均値)-(x の平均値)^2$




となり， $x$ の分散は $x^2$ の平均値と $x$ の平均値の2乗の差から求めることもできる。


</div>


&nbsp;




## 【発展】共分散②


<div class="info-box">2つの変量 $x$ , $y$ からなるデータとして， $n$ 個の値の組 $(x_{1} , y_{1} ) , (x_{2} , y_{2} ) ,・・・, (x_{n} , y_{n} )$ がある。 $x$ , $y$ の平均値を $\overline{x}$ ， $\overline{y}$ とすると，共分散 $s_{xy}$ は，



$\displaystyle s_{xy} = \frac{1}{n} (x_{1} y_{1} + x_{2} y_{2} +・・・+ x_{n} y_{n}) - \overline{x} \cdot \overline{y}$




と表せる。


</div>
<div class="blank-box bb-green">証明



$x$ ， $y$ の平均値を $\overline{x}$ ， $\overline{y}$ とすると，




$\displaystyle \overline{x} = \frac{x_{1} + x_{2}+・・・+ x_{n}}{n}$ ， $\displaystyle \overline{y} = \frac{y_{1} + y_{2} +・・・+ y_{n}}{n}$




共分散の定義より，




$\displaystyle s_{xy} = \frac{(x_{1} - \overline{x} )(y_{1} - \overline{y}) + (x_{2} - \overline{x})(y_{2} - \overline{y})+・・・+ (x_{n} - \overline{x})(y_{n} - \overline{y}}{n})$




ここで， $i=1,2,・・・,n$ に対して，




$(x_{i} - \overline{x})(y_{i} - \overline{y}) =x_{i} y_{i} - x_{i} \overline{y} - \overline{x} y_{i} + \overline{x} \overline{y}$




と変形できるので，




$\displaystyle s_{xy}= \frac{(x_{1} y_{1} -x_{1} \overline{y} - \overline{x} y_{1} + \overline{x} \cdot \overline{y} )+ (x_{2} y_{2} -x_{2} \overline{y} - \overline{x} y_{2} + \overline{x} \cdot \overline{y})+・・・+(x_{n} y_{n} -x_{n} \overline{y} - \overline{x} y_{n} + \overline{x} \cdot \overline{y})}{n}$




$\displaystyle = \frac{(x_{1} y_{1} + x_{2} y_{2} +・・・+x_{n} y_{n}) - (x_{1} + x_{2} +・・・+ x_{n}) \overline{y} - (y_{1} + y_{2} +・・・+ x_{n}) - \overline{x} (y_{1} + y_{2} +・・・+ y_{n}) +n \overline{x} \cdot \overline{y}}{n}$




$\displaystyle = \frac{x_{1} y_{1} + x_{2} y_{2} +・・・+ x_{n} y_{n}}{n} - \frac{x_{1} + x_{2} +・・・+ x_{n}}{n} \overline{y} - \overline{x} \frac{y_{1} + y_{2} +・・・+ y_{n}}{n} + \overline{x} \cdot \overline{y}$




$\displaystyle = \frac{x_{1} y_{1} + x_{2} y_{2} +・・・+ x_{n} y_{n}}{n} - \overline{x} \cdot \overline{y} - \overline{x} \cdot \overline{y} + \overline{x} \cdot \overline{y}$




$\displaystyle =\frac{1}{n} (x_{1} y_{1} + x_{2} y_{2} +・・・+ x_{n} y_{n}) - \overline{x} \cdot \overline{y}$


</div>
