---
title: "【定義・定理・公式】高校数学基本事項 - 数学B - 種々の数列"
status: "published"
published_at: "2018-10-15 17:59:25"
path: "/basics-of-high-school-math/basics-hb-3-3/"
---

## 和の記号 $\Sigma$，数列の和の公式




【定義】




$\displaystyle\sum_{k=1}^{n}a_k=a_1+a_2+……+a_n$




【定理】




<strong>和の公式</strong>


<ul>
	<li>定数の和：$\displaystyle\sum_{k=1}^{n}c=c+c+…+c=nc$ ( $c$ は定数)</li>
	<li>自然数の和：$\displaystyle\sum_{k=1}^{n}k=1+2+…+n=\frac{1}{2}n(n+1)$</li>
	<li>平方数の和：$\displaystyle\sum_{k=1}^{n}k^2=1^2+2^2+…+n^2=\frac{1}{6}n(n+1)(2n+1)$</li>
	<li>立法数の和：$\displaystyle\sum_{k=1}^{n}k^3=1^3+2^3+…+n^3=\left\{\frac{1}{2}n(n+1)\right\}^2$</li>
	<li>累乗の和：$\displaystyle\sum_{k=1}^{n}r^{k-1}=r^1+r^2+……+r^{n-1}=\frac{1-r^n}{1-r}=\frac{r^n-1}{r-1}$ ( $r\neq1$ )</li>
</ul>


$\boldsymbol{\Sigma}$ <strong>の性質</strong>




$p$，$q$ は $k$ に無関係な定数とする


<ul>
	<li>$\displaystyle\sum_{k=1}^{n}(a_k+b_k)=\displaystyle\sum_{k=1}^{n}a_k+\sum_{k=1}^{n}b_k$</li>
	<li>$\displaystyle\sum_{k=1}^{n}pa_k=p\sum_{k=1}^{n}a_k$</li>
	<li>$\displaystyle\sum_{k=1}^{n}(pa_k+qb_k)=p\sum_{k=1}^{n}a_k+q\sum_{k=1}^{n}b_k$</li>
</ul>







## 階差数列と一般項




一般に，数列 $\{a_n\}$ の隣り合う2項の差 $a_{n+1}-a_n=b_n$ ( $n$ は自然数)を項とする数列 $\{b_n\}$ を，数列 $\{a_n\}$ の<strong>階差数列</strong>という。




階差数列 $\{b_n\}$ を用いた数列 $\{a_n\}$ の一般項は


<p style="padding-left: 30px;">$n\geqq2$ のとき $a_n=a_1+\displaystyle\sum_{k=1}^{n-1}b_k</p>







## 和 $S_n$ と一般項 $a_n$ の関係




数列 $\{a_n\}$ の初項から第 $n$ 項までの和を $S_n$ とすると


<ul>
	<li>$a_1=S_1$</li>
	<li>$n\geqq2$ のとき $a_n=S_n-S_{n-1}$</li>
</ul>
