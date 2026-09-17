---
title: "【定理・公式・証明】高校数学定理・公式 – 数学A –  $n$ 進法"
wp_id: 3191
content_type: "page"
status: "publish"
published_at: "2020-06-09 09:59:40"
wp_date: "2020-06-09 09:59:40"
modified_at: "2020-06-09 10:00:10"
legacy_url: "http://mathrao.com/theorems-proof-of-high-school-math/theorems-ha-3-12/"
legacy_path: "/theorems-proof-of-high-school-math/theorems-ha-3-12/"
legacy_slug: "theorems-ha-3-12"
former_slugs: []
parent_wp_id: 2564
parent_title: "【定理・公式・証明】高校数学定理・公式一覧"
hierarchy: ["【定理・公式・証明】高校数学定理・公式一覧", "【定理・公式・証明】高校数学定理・公式 – 数学A –  $n$ 進法"]
category: []
tags: []
mathrao_section: "定理・公式・証明"
mathrao_grade: null
mathrao_course: "数学A"
source_content_sha256: "3756b0d64bccca3dea918d9695a1c37d4a6c86bc0c02145988707f0c93a81d6a"
---

## $n$ 進法①


<div class="info-box">$n$ 進法で表された整数 $N=a_{m} a_{m-1} \cdots a_{1} a_{0(n)}$ を10進法で表すと，



$N=a_{m} \times n^m +a_{m-1} \times n^{m-1} + \cdots + a_{2} \times n^2 +a_{1} \times n^1 + a_{0} \times 1$




となる。( $a_{k}$ は $N$ の位を表し， $0 \leqq a_{k} \leqq n-1 , a_{m} \neq 0$ )


</div>


[overrule]説明




例えば，5進法で表された数 $1234_{(5)}$ を10進法で表すことを考える。




10進法では各位は上記のようになり，10進法で表された数1234は，




$1234=1 \times 10^{3} +2 \times 10^{2} +3 \times 10^{1} +4 \times 1$




と表すことができる。これと同様に，5進法では各位は上記のようになり，5進法で表された数 $1234_{(5)}$ は，




$1234_{(5)} =1 \times 5^3 +2 \times 5^2 +3 \times 5^1 +4 \times 1$




と表すことができる。①の右辺は，




$1 \times 5^3 +2 \times 5^2 +3 \times 5^1 +4 \times 1=194$




であるから， $1234_{(5)}$ を10進法で表すと，194である。




同様にして， $n$ 進法で表された数




$N=a_{m} a_{m-1} \cdots a_{1} a_{0(n)}$




(ただし， $a_{k}$ は $n^k$ の位( $k=0,1,2, \cdots , m$ )を表し， $0 \leqq a_{k} \leqq n-1 , a_{m} \neq 0$ )




を10進法で表すときは，




$N=a_{m} \times n^m +a_{m-1} + \cdots + a_{2} \times n^2 +a_{1} +a_{0} \times 1$




と計算するとよい。[/overrule]




## $n$ 進法②


<div class="info-box">10進法で表された整数 $N$ を $n$ 進法で表すときは， $N$ を $n$ で割り，その商を $n$ で割り，またその商を $n$ で割り $\cdots$ ということを商が0になるまで繰り返し，得られた余りを1の位から順に並べる。</div>
<div>[overrule]説明</div>
<div>10進法で表された数 $194$ を5進法で表すときは，右の図のようにまず $194$ を5で割り，その商を5で割り，またその商を5で割り $\cdots$ ということを商が0になるまで繰り返し，得られる余りを図のようにしたから順に読むとよい。これより， $194=1234$ が得られる。なぜこの方法で良いのか説明する。</div>
<div>$194= 1 \times 5^3 +2 \times 5^2 + 3 \times 5 +4=5 \times (1 \times 5^2 +2 \times 5 +3) +4$</div>
<div>なので， $194$ を5進法で表したときの1の位4は，$194$ を5で割った余りである。</div>
<div>また，$194$ を5で割った商を $A$ とすると，</div>
<div>$A=1 \times 5^2 +2 \times 5 +3=5 \times (1 \times 5+2) +3$</div>
<div>なので，194を5進法で表したときの1の位4は，194を5で割った余りである。</div>
<div>また， $A$ を5で割った商を $B$ とすると，</div>
<div>$B=5 \times 1 +2$</div>
<div>なので，194を5進法で表したときの $5^2$ の位2は， $B$ を5で割った余りである。</div>
<div>また， $B$ を5で割った商を $C$ とすると，</div>
<div>$C=5 \times 0+1$</div>
<div>なので，194を5進法で表したときの $5^3$ の位1は， $C$ を5で割った余りである。</div>
<div>同様に，10進法で表された正の整数 $N$ が $n$ 進法で $N=a_{m} a_{m-1} \cdots a_{2} a_{1} a_{0(n)}$ ( $k=0,1,2, \cdots ,m$ において， $a_{k}$ は $n^k$ の位を表す)と表されるとき， $N$ を $n$ で割った余りが $a_{0}$ ，その商を $n$ で割った余りが $a_{1}$ ，またその商を $n$ で割った余りが $a_{2}$ ， $\cdots$ となるから， $N$ を $n$ 進法で表すときは，まず $N$ を $n$ で割り，その商を $n$ で割り，またその商を $n$ で割り $\cdots$ ということを商が0になるまで繰り返し，得られる余りを1の位から順に並べる(〈図1〉のような筆算では下から読む)とよい。[/overrule]</div>
<div> </div>


## $n$ 進法③


<div class="info-box">$n$ 進法で表された少数 $c=0.a_{1} a_{2} a_{3} \cdots a_{m(n)}$ を10進法で表すと，



$\displaystyle c=a_{1} \times \frac{1}{n} + a_{2} \times \frac{1}{n^2} + a_{3} \times \frac{1}{n^3} + \cdots + a_{m} \times \frac{1}{n^m}$




となる。( $a_{k}$ は $c$ の少数第 $k$ 位を表し， $0 \leqq a_{k} \leqq n-1,a_{m} \neq 0$ )


</div>


[overrule]説明




例えば，5進法で表された少数 $0.1234_{(5)}$ を10進法で表すことを考える。




10進法では，各位は上記のようになり，10進法で表された小数 0.1234 は，




$\displaystyle 0.1234=1 \times \frac{1}{10} +2 \times \frac{1}{10^2} +3 \times \frac{1}{10^3} +4 \times \frac{1}{10^4}$




と表すことができる。これと同様に，5進法では，各位は上記のようになり，5進法で表された小数 $0.1234_{(5)}$ は，




$\displaystyle 0.1234= 1 \times \frac{1}{5} +2 \times \frac{1}{5^2} +3 \times \frac{1}{5^3} +4 \times \frac{1}{5^4}$




と表すことができ，①の右辺は $\displaystyle \frac{1}{5} + \frac{2}{25} + \frac{3}{125} + \frac{4}{625} = \frac{194}{625} = 0.3104$ であるから， $0.1234_{(5)}$ を10進法で表すと， $0.3104$ である。




同様にして， $n$ 進法で表された小数 $c=0.a_{1} a_{2} a_{3} \cdots a_{m-1} a_{m(n)}$ (ただし、 $a_{k}$ は $c$ の小数第 $k$ 位を表し， $0 \leqq a_{k} \leqq n-1,a_{m}\neq 0$ )




を10進法で表すときは、 $\displaystyle c=a_{1} \times \frac{1}{n} +a_{2} \times \frac{1}{n^2} +a_{3} \times \frac{1}{n^3} + \cdots +a_{m} \times \frac{1}{n^m}$ と計算するとよい。[/overrule]




&nbsp;




## $n$ 進法④


<div class="info-box">10進法で表された小数 $c$ を $n$ 進法で表すときは， $c$ を $n$ 倍して得られる数の整数部分を取り出し，残った小数部分を $n$ 倍して得られる数の整数部分を取り出し，また残った小数部分を $n$ 倍して得られる数の整数部分を取り出し…と繰り返して，取り出した整数部分を小数第一位から順に並べる。</div>


[overrule]説明




10進法で表された小数 $0.3104$ を5進法で表すときは，〈図１〉のように小数を5倍した数の整数部分を取り出し，残った小数部分を5倍して得られる数の整数部分を取り出し…ということを繰り返して，得られた整数部分を小数第一位から順に並べればよい。




なぜこの方法で良いのかを説明する。




$0.3104$を5進数で表すとは，




$0.3104=0.a_{1} a_{2} a_{3} \cdots {}_{(5)}$ すなわち， $\displaystyle 0.3104=a_{1} \times \frac{1}{5} +a_{2} \times \frac{1}{5^2} +a_{3} \times \frac{1}{5^3} + \cdots$




を満たす $a_{1} ,a_{2} ,a_{3} \cdots$ を求めることである。(ただし，各$a_{k}$ は0以上4以下の整数)




①の両辺を5倍すると，




$\displaystyle 1.552=a_{1} + a_{2} \times \frac{1}{5} +a_{3} \times \frac{1}{5^2} +a_{4} \times \frac{1}{5^3}+ \cdots$




であるから，整数部分を比較し， $a_{1} =1$ ，小数部分を比較し，




$\displaystyle 0.552=a_{2} \times \frac{1}{5} +a_{3} \times \frac{1}{5^2} +a_{4} \times \frac{1}{5^3} \cdots$




この式の両辺を5倍すると，




$\displaystyle 2.76=a_{2} +a_{3} \times \frac{1}{5} +a_{4} \times \frac{1}{5^2}$ + \cdots$




であるから，




$\displaystyle a_{2} =2,0.76=a_{3} \times \frac{1}{5}+ a_{4} \times \frac{1}{5^2} + \cdots$




この式の両辺を5倍すると，




$\displaystyle 3.8=a_{3} +a_{4} \times \frac{1}{5} +a_{5} \times \frac{1}{5^2} + \cdots$




であるから，




$\displaystyle a_{3}=3,0.8=a_{4} \times \frac{1}{5} +a_{5} \times \frac{1}{5^2} + \cdots$




この式の両辺を5倍すると，




$\displaystyle 4=a_{4} +a_{5} \times \frac{1}{5} + \cdots$




であるから，




$\displaystyle a_{4} =4$




このようにして，$0.3104=0.1234_{(5)}$ であることが分かる。




同様にして，1より小さい数 $c$ を $n$ 進法で表すときは，




$c=0.a_{1} a_{2} a_{3} \cdots {}_{(n)}$ (ただし， $k=1,2,3, \cdots$ において， $a_{k}$ は $\displaystyle \frac{1}{n^k}$ の位を表す)




という形をイメージし， $c$ を $n$ 倍したときに得られる数の整数部分 $a_{1}$ ，その小数部分を $n$ 倍したときに得られる数の整数部分 $a_{2}$ ，またその小数部分を $n$ 倍したときに得られる数の整数部分 $a_{3}$ ，…を順に求め， $\frac{1}{n}$ の位から順に並べるとよい。[/overrule]
