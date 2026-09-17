---
title: "【定義・定理・公式】高校数学基本事項 - 数学A - いろいろな確率，確率の乗法定理"
wp_id: 783
content_type: "page"
status: "publish"
published_at: "2018-09-23 18:50:39"
wp_date: "2018-09-23 18:50:39"
modified_at: "2018-09-23 18:50:39"
legacy_url: "http://mathrao.com/basics-of-high-school-math/basics-ha-1-5/"
legacy_path: "/basics-of-high-school-math/basics-ha-1-5/"
legacy_slug: "basics-ha-1-5"
former_slugs: []
parent_wp_id: 448
parent_title: "【定義・定理・公式】高校数学基本事項一覧"
hierarchy: ["【定義・定理・公式】高校数学基本事項一覧", "【定義・定理・公式】高校数学基本事項 - 数学A - いろいろな確率，確率の乗法定理"]
category: []
tags: []
mathrao_section: "高校数学"
mathrao_grade: null
mathrao_course: "数学A"
source_content_sha256: "f9e8a25061ade35c467cdcd726880ff626a8c06be0f20623fd29c157ae481fd2"
---

## 独立な試行の確率




【定義】




<strong>独立</strong>：いくつかの試行において，どの試行の結果も他の試行の結果に影響を与えないこと


<p style="padding-left: 30px;">※2つの試行SとTが独立であるとき，Sで事象 $A$ が起こり，かつ，Tで事象 $B$ が起こる確率 $p$ は</p>
<p style="padding-left: 60px;">$p=P(A) \times P(B)$</p>
<p style="padding-left: 30px;">※独立な3つ以上の試行についても，同様の等式が成り立つ。</p>


&nbsp;




## 反復試行の確率




【定義】




<strong>反復試行</strong>：同じ条件のもとでの試行の繰り返し


<p style="padding-left: 30px;">※1つの試行を何回か繰り返すとき，これらの試行は互いに独立である。</p>
<p style="padding-left: 30px;">※1回の試行で事象 $A$ の起こる確率を $p$ とすると，この試行を $n$ 回繰り返し行うとき $A$ がちょうど $r$ 回起こる確率は</p>
<p style="padding-left: 60px;">${}_n \mathrm{ C }_rp^r(1-p)^{n-r}$</p>


&nbsp;




## 条件付き確率と乗法定理




【定義】




<strong>$\boldsymbol{A}$ が起こったときの $\boldsymbol{B}$ が起こる条件付き確率( $P_A(B)$ )</strong>：1つの試行における2つの事象 $A$，$B$ について，事象 $A$ が起こったとして，そのときに事象 $B$ の起こる確率


<p style="padding-left: 30px;">$P(A) \neq 0$ のとき $P_A(B)= \displaystyle \frac{P(A \cap B)}{P(A)}$</p>


【定理】




<strong>乗法定理</strong>




2つの事象 $A$，$B$ がともに起こる確率 $P(A \cap B)$ は


<p style="padding-left: 30px;">$P(A \cap B)=P(A)P_A(B)$</p>
