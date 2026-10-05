---
title: "【定義・定理・公式】高校数学基本事項 - 数学Ⅲ - 定積分とその基本性質"
status: "published"
published_at: "2018-10-24 18:45:58"
path: "/basics-of-high-school-math/basics-h3-7-3/"
---

## 定積分とその基本性質




【定義】




ある区間で連続な関数 $f(x)$ の不定積分の1つを $F(x)$ とするとき，区間に属する2つの実数 $a$，$b$ に対して


<p style="padding-left: 30px;">$\displaystyle\int_{a}^{b}f(x)dx=\left[F(x)\right]_{a}^{b}=F(a)-F(b)$</p>


【定理】




$k$，$l$ を定数とする。


<ul>
	<li>定積分の値は積分変数の文字に無関係：$\displaystyle\int_{a}^{b}f(x)dx=\displaystyle\int_{a}^{b}f(t)dt$</li>
	<li>定数倍：$\displaystyle\int_{a}^{b}kf(x)dx=k\displaystyle\int_{a}^{b}f(x)dx$</li>
	<li>和：$\displaystyle\int_{a}^{b}\{f(x)+g(x)\}dx=\displaystyle\int_{a}^{b}f(x)dx+\displaystyle\int_{a}^{b}g(x)dx$</li>
	<li>差：$\displaystyle\int_{a}^{b}\{f(x)-g(x)\}dx=\displaystyle\int_{a}^{b}f(x)dx-\displaystyle\int_{a}^{b}g(x)dx$</li>
	<li>$\displaystyle\int_{a}^{b}\{kf(x)+lg(x)\}dx=k\displaystyle\int_{a}^{b}f(x)dx+l\displaystyle\int_{a}^{b}g(x)dx$</li>
	<li>$\displaystyle\int_{a}^{b}f(x)dx=-\displaystyle\int_{b}^{a}f(x)dx$</li>
	<li>$\displaystyle\int_{a}^{a}f(x)dx=0$</li>
	<li>$\displaystyle\int_{a}^{b}f(x)dx=\displaystyle\int_{a}^{c}f(x)dx+\displaystyle\int_{c}^{b}f(x)dx$</li>
</ul>







## 絶対値のついた関数の定積分




$a\leqq x\leqq c$ のとき $f(x)\geqq 0$，$c\leqq x\leqq b$ のとき $f(x)\leqq 0$ $\Rightarrow$ $\displaystyle\int_{a}^{b}|f(x)|dx=\displaystyle\int_{a}^{c}f(x)dx+\displaystyle\int_{c}^{b}\{-f(x)\}dx$
