---
title: "【定義・定理・公式】高校数学基本事項 - 数学Ⅲ - 定積分の置換積分法，部分積分法"
status: "published"
published_at: "2018-10-24 18:53:21"
path: "/basics-of-high-school-math/basics-h3-7-4/"
---

## 定積分の置換積分法




閉区間 $[a,b]$ で関数 $f(x)$ が連続であるとし，$x$ が微分可能な関数 $g(t)$ を用いて $x=g(t)$ と表されているとする。$t$ が $\alpha$ から $\beta$ まで変化するとき $x$ が $a$ から $b$ まで変化するならば，次の公式が成り立つ。


<ul>
	<li>$\displaystyle\int_{a}^{b}f(x)dx=\displaystyle\int_{\alpha}^{\beta}f(g(t))g'(t)dt$ ( $x=g(t)$，$a=g(\alpha)$，$b=g(\beta)$ )</li>
	<li>$\displaystyle\int_{a}^{b}f(g(x))g'(x)dx=\displaystyle\int_{\alpha}^{\beta}f(t)dt$ ( $g(x)=t$，$g(a)=\alpha$，$g(b)=\beta$ )</li>
</ul>







## 偶関数・奇関数の定積分




<strong>偶関数</strong>




$f(-x)=f(x)$ のとき


<p style="padding-left: 30px;">$\displaystyle\int_{-a}^{a}f(x)dx=2\displaystyle\int_{0}^{a}f(x)dx$</p>


<strong>奇関数</strong>




$f(-x)=-f(x)$ のとき


<p style="padding-left: 30px;">$\displaystyle\int_{-a}^{a}f(x)dx=0$</p>







## 定積分の部分積分法


<p style="padding-left: 30px;">$\displaystyle\int_{a}^{b}f(x)g'(x)dx=\left[f(x)g(x)\right]_{a}^{b}-\displaystyle\int_{a}^{b}f'(x)g(x)dx$</p>
<p style="padding-left: 30px;">$g'(x)=1$ のとき $\displaystyle\int_{a}^{b}f(x)dx=\left[xf(x)\right]_{a}^{b}-\displaystyle\int_{a}^{b}xf'(x)dx$</p>
