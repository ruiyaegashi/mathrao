---
title: "【定義・定理・公式】高校数学基本事項 - 数学Ⅲ - 無限級数"
status: "published"
published_at: "2018-10-23 18:31:12"
path: "/basics-of-high-school-math/basics-h3-4-2/"
---

## 無限級数




【定義】




<strong>級数</strong>：数列の各項を順に加法記号(+)で結んだ式




<strong>無限級数</strong>：無限数列 $\{a_n\}$ の級数 $\displaystyle\sum_{n=1}^{\infty}a_n=a_1+a_2+a_3+\cdots\cdots+a_n+\cdots\cdots$




<strong>無限等比級数</strong>：無限等比数列 $\{ar^{n-1}\}$ の級数 $\displaystyle\sum_{n=1}^{\infty}ar^{n-1}=a+ar+ar^2+\cdots\cdots+ar^{n-1}+\cdots\cdots$









## 無限級数の収束・発散




無限数列 $\{a_n\}$ の部分和を $S_n=\displaystyle\sum_{k=1}^{n}a_k$，部分和の数列を $\{S_n\}$ とすると，無限級数 $\displaystyle\sum_{n=1}^{\infty}a_n$ について，


<p style="padding-left: 30px;">数列 $\{S_n\}$ が収束して，$\displaystyle\lim_{n\to\infty}S_n=\displaystyle\lim_{n\to\infty}\displaystyle\sum_{k=1}^{n}a_k=S$ のとき，$\displaystyle\sum_{n=1}^{\infty}a_n$ は収束し，和は $S$ である。</p>
<p style="padding-left: 30px;">数列 $\{S_n\}$ が発散するとき，$\displaystyle\sum_{n=1}^{\infty}a_n$ は発散する。</p>







## 無限等比級数




無限等比級数 $\displaystyle\sum_{n=1}^{\infty}ar^{n-1}$ について


<p style="padding-left: 30px;">$a\neq 0$ のとき</p>
<p style="padding-left: 60px;">$|r|&lt;1$ ならば収束し，$\displaystyle\sum_{n=1}^{\infty}ar^{n-1}=\frac{a}{1-r}$</p>
<p style="padding-left: 60px;">$|r|\geqq 1$ ならば発散する</p>
<p style="padding-left: 30px;">$a=0$ のとき</p>
<p style="padding-left: 60px;">常に収束し，その和は $0$</p>







## 循環小数を分数で表す




循環小数は初項と公比が$a=r=0.(循環節)$ の無限等比級数と考えることができるため，収束の公式 $\displaystyle\frac{a}{1-r}$ を使えば分数で表すことができる。









## 無限級数の和の性質




【定理】




<strong>無限級数の和の性質</strong>




$\displaystyle\sum_{n=1}^{\infty}a_n$，$\displaystyle\sum_{n=1}^{\infty}b_n$ が収束する無限級数で，$\displaystyle\sum_{n=1}^{\infty}a_n=S$，$\displaystyle\sum_{n=1}^{\infty}b_n=T$，$k$，$l$ は定数とする。


<ul>
	<li>定数倍：$\displaystyle\sum_{n=1}^{\infty}ka_n=kS$</li>
	<li>和：$\displaystyle\sum_{n=1}^{\infty}(a_n+b_n)=S+T$</li>
	<li>差：$\displaystyle\sum_{n=1}^{\infty}(a_n-b_n)=S-T$</li>
	<li>$\displaystyle\sum_{n=1}^{\infty}(ka_n+lb_n)=kS+lT$</li>
</ul>







## 無限級数の収束・発散条件


<ul>
	<li>無限級数 $\displaystyle\sum_{n=1}^{\infty}a_n$ が収束する $\Rightarrow$ $\displaystyle\lim_{n\to\infty}a_n=0$</li>
	<li>数列 $\{a_n\}$ が $0$ に収束しない $\Rightarrow$ 無限級数 $\displaystyle\sum_{n=1}^{\infty}a_n$ は発散する</li>
</ul>
<p style="padding-left: 30px;">※上記の2つは互いに他の待遇であり，ともに逆は不成立。</p>
