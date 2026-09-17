---
title: "【定義・定理・公式】高校数学基本事項 - 数学B - 【補足】1次独立と1次従属"
wp_id: 998
content_type: "page"
status: "publish"
published_at: "2018-10-14 16:58:24"
wp_date: "2018-10-14 16:58:24"
modified_at: "2018-10-15 17:05:01"
legacy_url: "http://mathrao.com/basics-of-high-school-math/basics-hb-1-2/"
legacy_path: "/basics-of-high-school-math/basics-hb-1-2/"
legacy_slug: "basics-hb-1-2"
former_slugs: []
parent_wp_id: 448
parent_title: "【定義・定理・公式】高校数学基本事項一覧"
hierarchy: ["【定義・定理・公式】高校数学基本事項一覧", "【定義・定理・公式】高校数学基本事項 - 数学B - 【補足】1次独立と1次従属"]
category: []
tags: []
mathrao_section: "高校数学"
mathrao_grade: null
mathrao_course: "数学B"
source_content_sha256: "e2e741b1f19cf3a7e8841dde7b790da9bfc7994295ba13b324aff0f79adc2240"
---

## 1次独立と1次従属




【定義】




<strong>1次結合</strong>




$n$ 個のベクトル $\vec{a_1}$，$\vec{a_2}$，……，$\vec{a_n}$ と実数 $x_1$，$x_2$，……，$x_ん$ を用いて，$x_1\vec{a_1}+x_2\vec{a_2}+……+x_n\vec{a_n}$ の形に表されたベクトルを $\vec{a_1}$，$\vec{a_2}$，……，$\vec{a_n}$ の1次結合という。




<strong>1次独立</strong>




$\vec{a_1}$，$\vec{a_2}$，……，$\vec{a_n}$ の1次結合について


<p style="padding-left: 30px;">$x_1\vec{a_1}+x_2\vec{a_2}+……+x_n\vec{a_n}=\vec{0}$ $\Rightarrow$ $x_1=x_2=……=x_n=0$</p>


が成り立つとき，$n$ 個のベクトル $\vec{a_1}$，$\vec{a_2}$，……，$\vec{a_n}$ は1次独立であるという。




<strong>1次従属</strong>




1次独立でないベクトルは1次従属である。




&nbsp;




## 平面・空間ベクトルの1次独立と1次従属




<strong>平面ベクトル</strong>




平面上で $\vec{a}\neq\vec{0}$，$\vec{b}\neq\vec{0}$，$\vec{a}\nparallel\vec{b}$ のとき，$s$，$t$ を実数とすると


<ul>
	<li>任意のベクトル $\vec{p}$ は $\vec{p}=s\vec{a}+t\vec{b}$ の形にただ1通りに表される。</li>
	<li>$s\vec{a}+t\vec{b}=\vec{0}$ $\Leftrightarrow$ $s=t=0$</li>
</ul>


が成り立つので，2つのベクトル $\vec{a}$，$\vec{b}$ について


<p style="padding-left: 30px;">$\vec{a}$，$\vec{b}$ が1次独立 $\Leftrightarrow$ $\vec{a}\neq\vec{0}$，$\vec{b}\neq\vec{0}$，$\vec{a}\nparallel\vec{b}$</p>


2つのベクトル $\vec{a}$，$\vec{b}$ が1次独立であるとき，3つ目のベクトル $\vec{c}$ をどのようにとっても，$\vec{a}$，$\vec{b}$，$\vec{c}$ は1次従属になる。




<strong>空間ベクトル</strong>




空間において同じ平面上にないベクトル $\vec{a}$，$\vec{b}$，$\vec{c}$ に対して，$s$，$t$，$u$ を実数とすると


<ul>
	<li>任意のベクトル $\vec{p}$ は $\vec{p}=s\vec{a}+t\vec{b}+u\vec{c}$ の形にただ1通りに表される。</li>
	<li>$s\vec{a}+t\vec{b}+u\vec{c}=\vec{0}$ $\Leftrightarrow$ $s=t=u=0$</li>
</ul>


が成り立つので，3つのベクトル $\vec{a}$，$\vec{b}$，\vec{c} について


<p style="padding-left: 30px;">$\vec{a}$，$\vec{b}$，\vec{c} が1次独立 $\Leftrightarrow$ $\vec{a}$，$\vec{b}$，\vec{c} が同一平面上にない</p>


3つのベクトル $\vec{a}$，$\vec{b}$，$\vec{c}$ が1次独立であるとき，4つ目のベクトル $\vec{d}$ をどのようにとっても，$\vec{a}$，$\vec{b}$，$\vec{c}$，$\vec{d}$ は1次従属になる。




&nbsp;




## まとめ




平面上では


<ul>
	<li>1次独立なベクトルを，最大で2つ定めることができる。</li>
	<li>任意のベクトルは，1次独立な2つのベクトルの1次結合で表される。</li>
</ul>


空間では


<ul>
	<li>1次独立なベクトルを，最大で3つ定めることができる。</li>
	<li>任意のベクトルは，1次独立な3つのベクトルの1次結合で表される。</li>
</ul>
