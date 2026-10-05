---
title: "【定義・定理・公式】高校数学基本事項 - 数学Ⅱ - 対数関数"
status: "published"
published_at: "2018-10-13 17:55:19"
path: "/basics-of-high-school-math/basics-h2-5-2/"
---

## 対数




<strong>対数</strong>：$a>0$，$a \neq 1$，$M>0$ のとき $a^p=M$ $\Leftrightarrow$ $p= \log_aM$ すなわち $\log_aa^p =p$，$a^{\log_aM}=M$




$a>0$，$a \neq 1$ とするとき，任意の正の数 $M$ に対して，$a^p=M$ となる実数 $p$ がただ1つ定まる。この $p$ の値を $\boldsymbol{\log_aM}$ で表し，$a$ を<strong>底</strong>とする $M$ の<strong>対数</strong>という。また，$M$ をこの対数の<strong>真数</strong>という。なお，$a^p>0$ であるから，<strong>真数</strong> $\boldsymbol{M}$ <strong>は正の数</strong>でなければならない。









## 対数の性質




【定理】




<strong>対数の性質</strong>




$a>0$，$b>0$，$c>0$，$a \neq 1$，$b \neq 1$，$c \neq 1$，$M>0$，$N>0$，$k$ は実数のとき


<ul>
	<li>$\log_aa=1$</li>
	<li>$\log_a1=0$</li>
	<li>$\log_a \frac{1}{a} =-1$</li>
	<li>$\log_aMN= \log_aM + \log_aN$</li>
	<li>$\log_a \displaystyle \frac{M}{N} = \log_aN - \log_aN$　特に　$\log_a \displaystyle \frac{1}{N} =- \log_aN$</li>
	<li>$\log_aM^k=k \log_aM$　特に　$\log_a \sqrt[n]{M} = \displaystyle \frac{1}{n} \log_aM$</li>
	<li><strong>底の変換公式</strong>：$\log_ab = \displaystyle \frac{\log_cb}{\log_ca}$　特に　$\log_ab = \displaystyle \frac{1}{\log_ba}$</li>
</ul>







## 対数関数




【定義】




$a$ を<strong>底</strong>とする $x$ の<strong>対数関数</strong>：$y= \log_ax$ ( $a>0$，$a \neq 1$ )









## 対数関数のグラフ




<strong>指数関数のグラフの特徴・性質</strong>


<ul>
	<li>曲線</li>
	<li>対数関数 $y= \log_ax$ のグラフは，指数関数 $y=a^x$ のグラフと直線 $y=x$ に関して対象</li>
	<li>点 $(1,0)$，$(a,1)$ を通る</li>
	<li>$y$ 軸が漸近線</li>
	<li>$0&lt;a&lt;1$ のとき減少関数：$0&lt;p&lt;q$ $\Leftrightarrow$ $\log_ap&gt; \log_aq$</li>
	<li>$1&lt;a$ のとき増加関数：$0&lt;p&lt;q$ $\Leftrightarrow$ $\log_ap&lt; \log_aq$</li>
	<li>定義域は正の数全体，値域は実数全体</li>
</ul>







## 対数方程式・対数不等式




$a>0$，$a=1$ とし，$b$ は正の定数とする


<ul>
	<li>方程式 $\log_ax=\log_ab$ の解は $x=b$</li>
	<li>不等式 $\log_ax&gt;\log_ab$ の解は $0&lt;a&lt;1$ のとき $0&lt;x&lt;b$，$1&lt;a$ のとき$b&lt;x$</li>
	<li>不等式 $\log_ax&lt;\log_ab$ の解は $0&lt;a&lt;1$ のとき $b&lt;x$，$1&lt;a$ のとき$0&lt;x&lt;b$</li>
</ul>







## 桁数・小数首位と常用対数




【定義】




<strong>常用対数</strong>：底が10の対数




<strong>小数首位</strong>：$0<M<1$ である小数 $M$ の初めて $0$ でない数字が現れる位


<p style="padding-left: 30px;">自然対数 $N$ が $n$ 桁 $\Leftrightarrow$ $10^{n-1} \leqq N&lt;10^n$ $\Leftrightarrow$ $n-1 \leqq \log_{10}N&lt;n$</p>
<p style="padding-left: 30px;">小数首位が小数第 $n$ 位 $\Leftrightarrow$ $\frac{1}{10^n} \leqq M&lt; \frac{1}{10^{n-1}}$ $\frac{}{}\Leftrightarrow$ $-n \leqq \log_{10}M &lt;-n+1$</p>
