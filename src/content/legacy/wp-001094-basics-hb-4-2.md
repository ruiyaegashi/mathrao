---
title: "【定義・定理・公式】高校数学基本事項 - 数学B - 確率変数の和と積，二項分布"
wp_id: 1094
content_type: "page"
status: "publish"
published_at: "2018-10-19 14:26:07"
wp_date: "2018-10-19 14:26:07"
modified_at: "2018-10-19 14:26:07"
legacy_url: "http://mathrao.com/basics-of-high-school-math/basics-hb-4-2/"
legacy_path: "/basics-of-high-school-math/basics-hb-4-2/"
legacy_slug: "basics-hb-4-2"
former_slugs: []
parent_wp_id: 448
parent_title: "【定義・定理・公式】高校数学基本事項一覧"
hierarchy: ["【定義・定理・公式】高校数学基本事項一覧", "【定義・定理・公式】高校数学基本事項 - 数学B - 確率変数の和と積，二項分布"]
category: []
tags: []
mathrao_section: "高校数学"
mathrao_grade: null
mathrao_course: "数学B"
source_content_sha256: "be5e683386b0da288cb2c8475d7ae44e61bb72513b2a1bf53572e9a9c16538a7"
---

## 同時分布




【定義】




<strong>同時分布</strong>




ある試行によって $X$，$Y$ の値が定まるとき，$X=a$ かつ $Y=b$ である確率を $P(X=a,Y=b)$ と表す。




ある試行によって $X$，$Y$，$Z$ の値が定まるとき，$X=a$ かつ $Y=b$ かつ $Z=c$ である確率を $P(X=a,Y=b,Z=c)$ と表す。




2つの確率変数 $X$，$Y$ について，$X$ のとる値が $x_1,x_2,……,x_n$，$Y$ のとる値が $y_1,y_2,……,y_m$ のとき，$P(X=x_i,Y=y_j)=p_ij$ とおくと，$X$，$Y$ の確率分布は下図のように表され，この対応を $X$，$Y$ の<strong>同時分布</strong>という。




$\begin{array}{|c|cccc|c|}\hline&amp;y_1&amp;y_2&amp;\cdots\cdots&amp;y_m&amp;計\\\hline x_1&amp;p_{11}&amp;p_{12}&amp;\cdots\cdots&amp;p_{1m}&amp;p_1\\x_2&amp;p_{21}&amp;p_{22}&amp;\cdots\cdots&amp;p_{2m}&amp;p_2\\\vdots&amp;\vdots&amp;\vdots&amp;\cdots\cdots&amp;\vdots&amp;\vdots\\\vdots&amp;\vdots&amp;\vdots&amp;\cdots\cdots&amp;\vdots&amp;\vdots\\x_n&amp;p_{n1}&amp;p_{n2}&amp;\cdots\cdots&amp;p_{nm}&amp;p_n\\\hline 計&amp;q_1&amp;q_2&amp;\cdots\cdots&amp;q_m&amp;1\\\hline\end{array}$




&nbsp;




## 確率変数の独立・従属




【定義】




<strong>独立</strong>




2つの変数 $X$，$Y$ があって，$X$ のとる値 $a$ と，$Y$ のとる値 $b$ に対して，


<p style="padding-left: 30px;">$P(X=a,Y=b)=P(X=a)P(Y=b)$</p>


が $a$，$b$ のとり方に関係なく常に成り立つとき，確率変数 $X$，$Y$ は互いに<strong>独立</strong>であるという。


<p style="padding-left: 30px;">※3つ以上の確率変数が互いに独立であることも同様に定義される。</p>


<strong>従属</strong>




2つの事象 $A$，$B$ が独立でないとき，$A$ と $B$ は従属であるという。


<p style="padding-left: 30px;">※3つ以上の確率変数が従属であることも同様に定義される。</p>


&nbsp;




## 事象の独立・従属


<p style="padding-left: 30px;">2つの事象 $A$ と $B$ が互いに独立<br />
$\Leftrightarrow$ $P_A(B)=P(B)$<br />
$\Leftrightarrow$ $P_B(A)=P(A)$<br />
$\Leftrightarrow$ $P(A\cap B)=P(A)P(B)$</p>


&nbsp;




## 期待値・分散の性質




【定理】




<strong>期待値の性質</strong>


<ul>
	<li>$E(X+Y)=E(X)+E(Y)$</li>
	<li>$E(aX+bY)=aE(X)+bE(Y)$ ($a$，$b$ は定数)</li>
	<li>2つの確率変数 $X$，$Y$ が互いに独立であるとき $E(XY)=E(X)E(Y)$</li>
</ul>
<p style="padding-left: 30px;">※3つ以上の確率変数の和の期待値についても同様の等式が成り立つ。</p>


<strong>分散の性質</strong>




2つの確率変数 $X$，$Y$ が互いに独立であるとき


<ul>
	<li>$V(X+Y)=V(X)+V(Y)$</li>
	<li>$V(aX+bY)=a^2V(X)+b^2V(Y)$ ($a$，$b$ は定数)</li>
</ul>
<p style="padding-left: 30px;">※互いに独立な3つ以上の確率変数の和の分散についても同様の等式が成り立つ。</p>


&nbsp;




## 二項分布




1回の試行で事象 $A$ の怒る確率を $p$ とすると，この試行を $n$ 回行う反復試行において，$A$ がちょうど $r$ 回起こる確率は


<p style="padding-left: 30px;">${}_n\mathrm{C}_rp^rq^{n-r}$ (ただし $q=1-p$ )</p>


【定義】




<strong>二項分布</strong>




$n$ 回の反復試行において，事象 $A$ の起こる回数を $X$ とすると，$X$ は確率変数で，その確率分布を<strong>二項分布</strong>といい，$\boldsymbol{B(n,p)}$ で表す。また，確率変数 $X$ は二項分布 $B(n,p)$ に従うという。




【定理】




<strong>確率変数 $X$ が二項分布 $B(n,p)$ に従うときの期待値・分散・標準偏差</strong>




確率変数 $X$ が二項分布 $B(n,p)$ に従うとき，$q=1-p$ とすると


<ul>
	<li>期待値：$E(X)=np$</li>
	<li>分散：$V(X)=npq$</li>
	<li>標準偏差：$\sigma(X)=\sqrt{npq}$</li>
</ul>
