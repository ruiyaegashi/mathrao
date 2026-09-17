---
title: "【定義・定理・公式】高校数学基本事項 - 数学B - 確率分布"
wp_id: 1070
content_type: "page"
status: "publish"
published_at: "2018-10-19 13:49:55"
wp_date: "2018-10-19 13:49:55"
modified_at: "2018-10-19 13:49:55"
legacy_url: "http://mathrao.com/basics-of-high-school-math/basics-hb-4-1/"
legacy_path: "/basics-of-high-school-math/basics-hb-4-1/"
legacy_slug: "basics-hb-4-1"
former_slugs: []
parent_wp_id: 448
parent_title: "【定義・定理・公式】高校数学基本事項一覧"
hierarchy: ["【定義・定理・公式】高校数学基本事項一覧", "【定義・定理・公式】高校数学基本事項 - 数学B - 確率分布"]
category: []
tags: []
mathrao_section: "高校数学"
mathrao_grade: null
mathrao_course: "数学B"
source_content_sha256: "3f9a7c8f33a3ba4cce71e41d0b19b8bc43dc8ca41aaa843ae23640f7f215a5b5"
---

## 確率変数と確率分布




【定義】




<strong>確率変数</strong>：ある試行において，試行の結果によってその値が定まり，各値に対応して確率が定まるような変数




<strong>確率分布</strong>




一般に，確率変数 $X$ のとりうる値が $x_1,x_2,……,x_n$ であり，それぞれの値をとる確率が $p_1,p_2,……,p_n$ であるとき，次が成り立つ。


<ul>
	<li>$p_1\geqq0,p_2\geqq0,……,p_n\geqq0$</li>
	<li>$p_1+p_2+……+p_n=1$</li>
</ul>


また，以下のような確率変数 $X$ のとりうる値とその値をとる確率の対応関係を<strong>確率分布</strong>または<strong>分布</strong>といい，確率変数 $X$ はこの分布に<strong>従う</strong>という。




$\begin{array}{|c|cccc|c|}\hline X&amp;x_1&amp;x_2&amp;……&amp;x_n&amp;計\\\hline P&amp;p_1&amp;p_2&amp;……&amp;p_n&amp;1\\\hline\end{array}$


<p style="padding-left: 30px;">※確率変数 $X$ が値 $a$ をとる確率を $P(X=a)$ で，$X$ が $a$ 以上 $b$ 以下の値をとる確率を $P(a\leqq X \leqq b)$ で表す。</p>


&nbsp;




## 確率変数の期待値




【定義】




<strong>期待値</strong>




$\begin{array}{|c|cccc|c|}\hline X&amp;x_1&amp;x_2&amp;……&amp;x_n&amp;計\\\hline P&amp;p_1&amp;p_2&amp;……&amp;p_n&amp;1\\\hline\end{array}$




確率変数 $X$ の分布が上図で与えられているとき，<strong>期待値</strong> $E(X)$ は


<p style="padding-left: 30px;">$E(X)=x_1p_1+x_2p_2+……+x_np_n=\displaystyle\sum_{k=1}^{n}x_kp_k$</p>
<p style="padding-left: 30px;">※期待値は平均ともいい，$E(X)$ または $m$ で表す。</p>


&nbsp;




## 確率変数の分散と標準偏差




【定義】




<strong>分散・標準偏差</strong>




$\begin{array}{|c|cccc|c|}\hline X&amp;x_1&amp;x_2&amp;……&amp;x_n&amp;計\\\hline P&amp;p_1&amp;p_2&amp;……&amp;p_n&amp;1\\\hline\end{array}$




確率変数 $X$ の分布が上図で与えられているとき，$X$ の期待値を $m$ とすると，分散 $V(X)$，標準偏差 $\sigma(X)$ は


<p style="padding-left: 30px;"><br />
$\begin{array}{rl}V(X)&amp;=E((X-m)^2)\\ &amp;=(x_1-m)^2p_1+(x_2-m)^2p_2+……+(x_n-m)^2p_n\\ &amp;=\displaystyle\sum_{k=1}^{n}(x_k-m)^2p_k\\ &amp;=E(X^2)-\{E(X)\}^2\end{array}$</p>
<p style="padding-left: 30px;">$\sigma(X)=\sqrt{V(X)}$</p>


&nbsp;




## 確率変数の演算




$X$ を確率変数，$a$，$b$ を定数とするとき


<ul>
	<li>期待値：$E(aX+b)=aE(X)+b$</li>
	<li>分散：$V(aX+b)=a^2V(X)$</li>
	<li>標準偏差：$\sigma(aX+b)=|a|\sigma(X)$</li>
</ul>
