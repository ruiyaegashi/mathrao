---
title: "【定義・定理・公式】高校数学基本事項 - 数学Ⅲ - 不定積分"
status: "published"
published_at: "2018-10-24 18:15:38"
path: "/basics-of-high-school-math/basics-h3-7-1/"
---

## 不定積分とその基本性質




【定義】




<strong>不定積分</strong>




$F'(x)=f(x)$ のとき


<p style="padding-left: 30px;">$\displaystyle\int f(x)dx=F(x)+C$ ( $C$ は積分定数)</p>


<strong>原始関数</strong>：不定積分の定義における $F(x)$




【定理】




<strong>不定積分の基本性質</strong>




$k$，$l$ を定数とする。


<ul>
	<li><strong>定数倍</strong>：$\displaystyle\int kf(x)dx=k\displaystyle\int f(x)dx$</li>
	<li><strong>和</strong>：$\displaystyle\int\{f(x)+g(x)\}dx=\displaystyle\int f(x)dx+\displaystyle\int g(x) dx$</li>
	<li><strong>差</strong>：$\displaystyle\int\{f(x)-g(x)\}dx=\displaystyle\int f(x)dx-\displaystyle\int g(x) dx$</li>
	<li>$\displaystyle\int\{kf(x)+lg(x)\}dx=k\displaystyle\int f(x)dx+l\displaystyle\int g(x) dx$</li>
</ul>







## 基本的な不定積分




$C$ を積分定数とする。




<strong>関数</strong> $\boldsymbol{y=x^\alpha}$


<ul>
	<li>$\alpha\neq -1$ のとき $\displaystyle\int x^\alpha dx=\displaystyle\frac{1}{\alpha+1}x^{\alpha+1}+C$</li>
	<li>$\alpha=-1$ のとき $\displaystyle\int \displaystyle\frac{1}{x}dx=\log|x|+C$</li>
</ul>


<strong>関数</strong> $\boldsymbol{y=ax+b}$




$F'(x)=f(x)=ax+b$，$a\neq 0$ とする


<ul>
	<li>$\displaystyle\int f(ax+b)dx=\displaystyle\frac{1}{a}F(ax+b)+C$</li>
</ul>


<strong>三角関数</strong>


<ul>
	<li>$\displaystyle\int\sin xdx=-\cos x+C$</li>
	<li>$\displaystyle\int\cos xdx=\sin x+C$</li>
	<li>$\displaystyle\int\displaystyle\frac{1}{\cos^2x}dx=\tan x+C$</li>
	<li>$\displaystyle\int\displaystyle\frac{1}{\sin^2x}dx=-\frac{1}{\tan x}+C$</li>
</ul>


<strong>指数関数</strong>


<ul>
	<li>$\displaystyle\int e^xdx=e^x+C$</li>
	<li>$\displaystyle\int a^xdx=\displaystyle\frac{a^x}{\log a}+C$</li>
</ul>







## 置換積分法


<ul>
	<li>$\displaystyle\int f(x)dx=\displaystyle\int f(g(t))g'(t)dt$ ( $x=g(t)$ )</li>
	<li>$\displaystyle\int f(g(x))g'(x)dx=\displaystyle\int f(u)du$ ( $g(x)=u$ )</li>
	<li>$\displaystyle\int\displaystyle\frac{g'(x)}{g(x)}dx=\log|g(x)|+C$ ( $C$ は積分定数)</li>
</ul>







## 部分積分法


<ul>
	<li>$\displaystyle\int f(x)g'(x)=f(x)g(x)-\displaystyle\int f'(x)g(x)dx$</li>
	<li>$g'(x)=1$ とすると $\displaystyle\int f(x)dx=xf(x)-\displaystyle\int xf'(x)dx$</li>
</ul>
