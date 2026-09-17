---
title: "【定義・定理・公式】高校数学基本事項 - 数学A - 確率と種々の定理"
wp_id: 780
content_type: "page"
status: "publish"
published_at: "2018-09-23 18:37:54"
wp_date: "2018-09-23 18:37:54"
modified_at: "2018-10-13 15:42:08"
legacy_url: "http://mathrao.com/basics-of-high-school-math/basics-ha-1-4/"
legacy_path: "/basics-of-high-school-math/basics-ha-1-4/"
legacy_slug: "basics-ha-1-4"
former_slugs: []
parent_wp_id: 448
parent_title: "【定義・定理・公式】高校数学基本事項一覧"
hierarchy: ["【定義・定理・公式】高校数学基本事項一覧", "【定義・定理・公式】高校数学基本事項 - 数学A - 確率と種々の定理"]
category: []
tags: []
mathrao_section: "高校数学"
mathrao_grade: null
mathrao_course: "数学A"
source_content_sha256: "8a9225d79c1aa7d4961e2244c13d8d6b5e7703620539190a078cfc190c39b74d"
---

## 事象と確率




【定義】




<strong>試行</strong>：同じ条件のもとで繰り返すことができる実験や観測




<strong>事象</strong>：試行の結果として起こる事柄




<strong>全事象</strong>：1つの試行において起こりうる結果全体を集合 $U$ で表すとき，$U$ 自身で表される事象




<strong>根元事象</strong>：$U$ のただ1つの要素からなる集合で表される事象




<strong>空事象</strong>：空集合 $\varnothing$ で表される決して起こらない事象




<strong>事象 $\boldsymbol{A}$ の確率( $\boldsymbol{P(A)}$ )</strong>：1つの試行において，ある事象 $A$ の起こることが期待される割合


<p style="padding-left: 30px;">※全事象 $U$ のどの根元事象も同様に確からしいとき</p>
<p style="padding-left: 60px;">$P(A)= \displaystyle \frac{n(A)}{n(U)} = \frac{事象 A の起こる場合の数}{起こりうる全ての場合の数}$</p>


$A$ と $B$ の<strong>積事象</strong>( $A \cap B$ )：$A$ と $B$ がともに起こる事象




$A$ と $B$ の<strong>和事象</strong>( $A \cup B$ )：$A$ または $B$ が起こる事象




$A$ と $B$ が互いに<strong>排反(事象)</strong>：2つの事象 $A$，$B$ が決して同時に起こらない，すなわち，$A \cap B= \varnothing$ であること




&nbsp;




## 確率の基本性質




【定理】




<strong>確率の基本性質</strong>




どのような事象 $A$ についても $0 \leqq P(A) \leqq 1$




特に，$P( \varnothing )=0$，$P(U)=1$




<strong>確率の加法定理</strong>




事象 $A$，$B$ が互いには違反であるとき


<p style="padding-left: 30px;">$P(A \cup B)=P(A)+P(B)$</p>


&nbsp;




## 一般の和事象の確率




3つの事象 $A$，$B$，$C$ について


<p style="padding-left: 30px;">$P(A \cup B)=P(A)+P(B)-P(A \cap B)$</p>
<p style="padding-left: 30px;">$P(A \cup B \cup C)=P(A)+P(B)+P(C)-P(A \cap B)-P(B \cap C)-P(C \cap A)+P(A \cap B \cap C)$</p>


&nbsp;




## 余事象とその確率




【定義】




<strong>余事象( $\overline{A}$ )</strong>：事象 $A$ に対して，$A$ が起こらない事象


<p style="padding-left: 30px;">※余事象の確率は $P( \overline{A} ) =1-P(A)$</p>
