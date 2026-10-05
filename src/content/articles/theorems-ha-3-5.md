---
title: "【定理・公式・証明】高校数学定理・公式 – 数学A – 正の約数の個数・総和"
status: "published"
published_at: "2020-05-11 23:50:28"
path: "/theorems-proof-of-high-school-math/theorems-ha-3-5/"
---

## 正の約数の個数


<div class="info-box">$p,q,r, \cdots$ を素数， $a,b,c, \cdots$ を正の整数とする。自然数 $n$ が $n=p^a q^b r^c \cdots$ と素因数分解されるとき， $n$ の正の約数の個数は



$(a+1) (b+1) (c+1) \cdots$ (個)$




である。


</div>


<aside class="article-note">

説明




0でない実数 $t$ について，$t^0 =1$ と表す。




例えば，360の正の約数の個数を求めてみよう。$360=2^3 \cdot 3^2 \cdot 5^1$ であり，360の正の約数である$1,40,60$ はそれぞれ，




$1=2^0 \cdot 3^0 \cdot 5^0$ ， $40=2^3 \cdot 3^0 \cdot 5^1$ ， $60=2^2 \cdot 3^1 \cdot 5^1$




のように表すことができる。




このように，360のすべての正の約数は，




$2^x \cdot 3^y \cdot 5^z$ $(x=0,1,2,3;y=0,1,2;z=0,1)$




と表すことができ，




$x$ の値が $(3+1)$ 通り， $y$ の値が $(2+1)$ 通り， $z$ の値が $(1+1)$ 通り




であるから，360の正の約数の個数は，




$(3+1)(2+1)(1+1)=24$ (個)




である。




このように， $n$ が $n=p^a q^b r^c \cdots$ と素因数分解できるとき， $n$ の正の約数は，




$p^x \cdot q^y \cdot r^z \cdot \cdots$ $(x=0,1,2, \cdots ,a;y=0,1,2, \cdots ,b;z=0,1,2, \cdots ,c; \cdots)$




と表すことができ， $n$ の正の約数の個数は




$(a+1)(b+1)(c+1) \cdots$ (個)




である。

</aside>









## 正の約数の総和


<div class="info-box">$p,q,r \cdots$ を素数， $a,b,c, \cdots$ を正の整数とする。 $n=p^a q^b r^c \cdots$ のとき， $n$ の約数の総和は



$(1+p+ \cdots + p^a )(1+q+ \cdots + q^b )(1+r+ \cdots + r^c ) \cdots$




である。


</div>


<aside class="article-note">

説明




例えば，60の正の約数の総和を求める。 $60=2^2 \cdot 3^1 \cdot 5^1$ より，60の正の約数は，




$2^x \cdot 3^y \cdot 5^z$ $(x=0,1,2;y=0,1;z=0,1)$




と表せる。




$z=0$ のとき




$z=1$ のとき




$①+②$ より，60の正の約数の総和は，




$(2^0 +2^1 +2^2 )(3^0 +3^1)5^0 +(2^0 +2^1 +2^2)(3^0 +3^1 )5^1 =(2^0 +2^1 +2^2 )(3^0 +3^1 )(5^0 +5^1 )$




このように，正の整数 $n$ が $n=p^a q^b r^c \cdots$ と素因数分解できるとき， $n$ の正の約数の総和は，




$(1+p+ \cdots +p^a )(1+q+ \cdots q^b )(1+r+ \cdots + r^c) \cdots$




である。


</aside>