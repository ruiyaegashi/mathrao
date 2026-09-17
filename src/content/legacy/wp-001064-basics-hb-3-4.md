---
title: "【定義・定理・公式】高校数学基本事項 - 数学B - 漸化式"
wp_id: 1064
content_type: "page"
status: "publish"
published_at: "2018-10-16 19:34:15"
wp_date: "2018-10-16 19:34:15"
modified_at: "2018-10-16 19:34:15"
legacy_url: "http://mathrao.com/basics-of-high-school-math/basics-hb-3-4/"
legacy_path: "/basics-of-high-school-math/basics-hb-3-4/"
legacy_slug: "basics-hb-3-4"
former_slugs: []
parent_wp_id: 448
parent_title: "【定義・定理・公式】高校数学基本事項一覧"
hierarchy: ["【定義・定理・公式】高校数学基本事項一覧", "【定義・定理・公式】高校数学基本事項 - 数学B - 漸化式"]
category: []
tags: []
mathrao_section: "高校数学"
mathrao_grade: null
mathrao_course: "数学B"
source_content_sha256: "510a8d6a0efb867b4ae2c3406d2e15a82460f10854601bf364dece51b0b54778"
---

## 漸化式と数列




【定義】




<strong>漸化式</strong>：数列において，その前の項から次の項をただ1通りに定める規則を示す等式




<strong>隣接2項間の漸化式</strong>：隣り合う2つの項からなる漸化式




<strong>隣接3項間の漸化式</strong>：隣り合う3つの項からなる漸化式




&nbsp;




## 特性方程式




【定義】




<strong>特性方程式</strong>：隣接2項間の漸化式において，$a_{n+1}$，$a_n$ の代わりに $\alpha$ とおいた方程式


<p style="padding-left: 30px;">※特性方程式の解を用いて漸化式を変形することができる。</p>


&nbsp;




## 種々の漸化式




$p$，$q$ を実数とする。




### <strong>隣接2項間の漸化式</strong>




$a_1=a$，$a_{n+1}=pa_n+q$


<p style="padding-left: 30px;">$p=1$ のとき</p>
<p style="padding-left: 60px;">数列 $\{a_n\}$ は等差数列であり $a_n=a+(n-1)q$</p>
<p style="padding-left: 30px;">$p\neq1$ かつ $q=0$ のとき</p>
<p style="padding-left: 60px;">数列 $\{a_n\}$ は等比数列であり $a_n=ap^{n-1}$</p>
<p style="padding-left: 30px;">$p\neq1$ かつ $q\neq0$</p>
<p style="padding-left: 60px;">①特性方程式 $x=px+q$ の解 $\alpha$ を用いて $a_{n+1}-\alpha=p(a_n-\alpha)$ と変形</p>
<p style="padding-left: 60px;">②$a_{n+1}=pa_n+q$，$a_{n+2}=pa_{n+1}+q$ より $a_{n+2}-a_{n+1}=p(a_{n+1}-a_n)$ を導く</p>


$a_1=a$，$a_{n+1}=pa_n+f(n)$


<p style="padding-left: 30px;">$p=1$ のとき</p>
<p style="padding-left: 60px;">$f(n)$ を階差数列とする数列であり $a_n=a+\displaystyle\sum_{k=1}^{n-1}f(k)$ ( $n\geqq2$ )</p>
<p style="padding-left: 30px;">$p\neq1$，$f(n)$ が $n$ の1次式のとき</p>
<p style="padding-left: 60px;">①$a_{n+1}=pa_n+q$，$a_{n+2}=pa_{n+1}+q$ より $a_{n+2}-a_{n+1}=p(a_{n+1}-a_n)$ を導く</p>
<p style="padding-left: 60px;">②$a_{n+1}-g(n+1)=p{a_n-g(n)}$ と変形</p>


特殊な形の漸化式


<p style="padding-left: 30px;">逆数をとって $\frac{1}{a_n}=b_n$ とおく</p>
<p style="padding-left: 30px;">$f(n)a_n=b_n$，$\frac{a_n}{f(n)}=b_n$ とおく</p>
<p style="padding-left: 30px;">対数をとって $\log_ca_n=b_n$ とおく</p>


### <strong>隣接3項間の漸化式</strong>




$pa_{n+2}+qa_{n+1}+ra_n=0$




特性方程式 $px^2+qx+r=0$ の2解 $\alpha$，$\beta$ を用いて2式を導く


<ul>
	<li>$a_{n+2}-\alpha a_{n+1}=\beta(a_{n+1}-\alpha a_n)$</li>
	<li>$a_{n+2}-\beta a_{n+1}=\alpha(a_{n+1}-\beta a_n)$</li>
</ul>
<p style="padding-left: 30px;">$\alpha$，$\beta$ のうち一方が $1$ のとき</p>
<p style="padding-left: 60px;">$\alpha=1$ とし，$a_{n+1}-a_n=b_n$ とおくと $b_{n+1}=\beta b_n$</p>
<p style="padding-left: 30px;">$\alpha\neq1$ かつ $\beta\neq1$ かつ $\alpha\neq\beta$ のとき</p>
<p style="padding-left: 60px;">数列 $\{a_{n+1}-\alpha a_n\}$ の一般項 $c_n$，数列 $\{a_{n+1}-\beta a_n\}$ の一般項 $d_n$ を求める。</p>
<p style="padding-left: 30px;">$\alpha=\beta$ かつ $\alpha\neq1$ のとき</p>
<p style="padding-left: 60px;">数列 $\{a_{n+1}-\alpha a_n\}$ の一般項を求め，$f(n)a_n=b_n$，$\frac{a_n}{f(n)}=b_n$ とおく</p>


### <strong>2つの数列の漸化式</strong>




$a_{n+1}=pa_n+qb_n$，$b_{n+1}=ra_n+sb_n$




2式


<ul>
	<li>$a_{n+1}+\alpha_1b_{n+1}=\beta_1(a_n+\alpha_1b_n)$</li>
	<li>$a_{n+1}+\alpha_2b_{n+1}=\beta_2(a_n+\alpha_2b_n)$</li>
</ul>


を導く，または，代入によって $\{a_n\}$ または $\{b_n\}$ だけの漸化式を導き，隣接3項間に落とし込む。
