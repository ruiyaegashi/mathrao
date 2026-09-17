---
title: "【定義・定理・公式】高校数学基本事項 - 数学A - 集合の要素の個数，場合の数，順列"
wp_id: 768
content_type: "page"
status: "publish"
published_at: "2018-09-23 17:34:59"
wp_date: "2018-09-23 17:34:59"
modified_at: "2019-05-12 20:57:34"
legacy_url: "http://mathrao.com/basics-of-high-school-math/basics-ha-1-1/"
legacy_path: "/basics-of-high-school-math/basics-ha-1-1/"
legacy_slug: "basics-ha-1-1"
former_slugs: []
parent_wp_id: 448
parent_title: "【定義・定理・公式】高校数学基本事項一覧"
hierarchy: ["【定義・定理・公式】高校数学基本事項一覧", "【定義・定理・公式】高校数学基本事項 - 数学A - 集合の要素の個数，場合の数，順列"]
category: []
tags: []
mathrao_section: "高校数学"
mathrao_grade: null
mathrao_course: "数学A"
source_content_sha256: "01732e9afa963a056b836b915eaf79b738f582566c6ede74da8631d18505f90a"
---

## 集合の要素の個数




【定義】




<strong>有限集合</strong>：要素の個数が有限である集合




【定理】




<strong>個数定理</strong>




$A$，$B$ は有限集合で，$n(P)$ を有限集合 $P$ の要素の個数とすると




和集合の要素の個数


<ul>
	<li>$n(A \cup B)=n(A)+n(B)-n(A \cap B)$</li>
	<li>$A \cap B= \varnothing$ のとき $n(A \cup B)=n(A)+n(B)$</li>
</ul>


補集合の要素の個数


<ul>
	<li>$n( \overline{A} )=n(U)-n(A)$</li>
</ul>


&nbsp;




## 場合の数




すべての場合をもれなく書き出し，重複することなく数え上げる。




<strong>樹形図(tree)</strong>：次々と枝分かれしていく図で表す方法




<strong>辞書式配列法</strong>：辞書の単語のようにアルファベット順に並べる方法




&nbsp;




## 法則




【法則】




<strong>和の法則</strong>




2つの事柄AとBの起こり方に重複はないとする。Aの起こり方が $a$ 通りあり，Bの起こり方が $b$ 通りあれば，AまたはBの起こる場合は，$a+b$ 通りある。




<strong>積の法則</strong>




事柄Aの起こり方が $a$ 通りあり，そのどの場合に対しても，事柄Bの起こり方が $b$ 通りあれば，Aが起こり，そしてBが起こる場合は $a \times b$ 通りある。


<p style="padding-left: 30px;">※和の法則・積の法則は事柄が3つ以上でも同様に成り立つ</p>


&nbsp;




## 順列




【定義】




<strong>順列</strong>：いくつかのものを順に1列に並べるとき，その並びの1つ1つのこと




<strong>階乗( $n!$ )</strong>：$n$ に1ずつ小さくした数を次々と1になるまでかけたもの


<p style="padding-left: 30px;">$n!=n(n-1)(n-2)……3 \cdot 2 \cdot 1$</p>
<p style="padding-left: 30px;">$0!=1$</p>


<strong>$\boldsymbol{n}$ 個から $\boldsymbol{r}$ 個取る順列</strong>：異なる $n$ 個のものから異なる $r$ 個を取り出して並べる順列


<p style="padding-left: 30px;">※$\boldsymbol{n}$ 個から $\boldsymbol{r}$ 個取る順列の総数を ${}_n \mathrm{ P }_r$ で表す</p>
<p style="padding-left: 60px;">${}_n \mathrm{ P }_r=n(n-1)(n-2)……(n-r+1)= \displaystyle \frac{n!}{(n-r)!}$ ( $r \leqq n$ )</p>
<p style="padding-left: 60px;">${}_n \mathrm{ P }_n=n(n-1)(n-2)……3 \cdot 2 \cdot 1=n!$</p>
<p style="padding-left: 60px;">${}_n \mathrm{ P }_0=1$</p>
