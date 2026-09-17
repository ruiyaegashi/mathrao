---
title: "【定義・定理・公式】高校数学基本事項 - 数学B - 位置ベクトル，ベクトルと図形"
wp_id: 1027
content_type: "page"
status: "publish"
published_at: "2018-10-15 01:23:55"
wp_date: "2018-10-15 01:23:55"
modified_at: "2018-10-15 17:04:10"
legacy_url: "http://mathrao.com/basics-of-high-school-math/basics-hb-2-3/"
legacy_path: "/basics-of-high-school-math/basics-hb-2-3/"
legacy_slug: "basics-hb-2-3"
former_slugs: []
parent_wp_id: 448
parent_title: "【定義・定理・公式】高校数学基本事項一覧"
hierarchy: ["【定義・定理・公式】高校数学基本事項一覧", "【定義・定理・公式】高校数学基本事項 - 数学B - 位置ベクトル，ベクトルと図形"]
category: []
tags: []
mathrao_section: "高校数学"
mathrao_grade: null
mathrao_course: "数学B"
source_content_sha256: "51b6b9d5a43c9ffaee056edfc08446ff3c381e962af8678de5a5d3dca3799e81"
---

## 分点・重心の位置ベクトル




<strong>分点の位置ベクトル</strong>




2点 $\mathrm{A}(\vec{a})$，$\mathrm{B}(\vec{b})$ を結ぶ線分 $\mathrm{AB}$ を $m:n$ に内分する点 $\mathrm{P}(\vec{p})$ と外分する点 $\mathrm{Q}(\vec{q})$，および，線分 $\mathrm{AB}$ の中点 $\mathrm{R}(\vec{r})$ は $\vec{a}=(a_1,a_2,a_3)$，$\vec{b}=(b_1,b_2,b_3)$ とすると


<ul>
	<li>$\vec{p}=\displaystyle\frac{n\vec{a}+m\vec{b}}{m+n}$　$\mathrm{P}\displaystyle\left(\frac{na_1+mb_1}{m+n},\frac{na_2+mb_2}{m+n},\frac{na_3+mb_3}{m+n}\right)$</li>
	<li>$\vec{q}=\displaystyle\frac{-n\vec{a}+m\vec{b}}{m-n}$　$\mathrm{Q}\displaystyle\left(\frac{-na_1+mb_1}{m-n},\frac{-na_2+mb_2}{m-n},\frac{-na_3+mb_3}{m-n}\right)$</li>
	<li>$\vec{r}=\displaystyle\frac{\vec{a}+\vec{b}}{2}$　$\mathrm{R}\displaystyle\left(\frac{a_1+b_1}{2},\frac{a_2+b_2}{2},\frac{a_3+b_3}{2}\right)$</li>
</ul>


<strong>三角形の重心の位置ベクトル</strong>




3点 $\mathrm{A}(\vec{a})$，$\mathrm{B}(\vec{b})$，$\mathrm{C}(\vec{c})$ を頂点とする $\triangle \mathrm{ABC}$ の重心 $\mathrm{G}(\vec{g})$ は $\vec{a}=(a_1,a_2,a_3)$，$\vec{b}=(b_1,b_2,b_3)$，$\vec{c}=(c_1,c_2,c_3)$ とすると


<p style="padding-left: 30px;">$\vec{g}=\displaystyle\frac{\vec{a}+\vec{b}+\vec{c}}{3}$　$\mathrm{G}\displaystyle\left(\frac{a_1+b_1+c_1}{3},\frac{a_2+b_2+c_3}{3},\frac{a_3+b_3+c_3}{3}\right)$</p>


<strong>共点条件</strong>(異なる3本以上の直線が1点で交わるための条件)




点の一致は位置ベクトルの一致から示す。




例)




3点 $\mathrm{P}$，$\mathrm{Q}$，$\mathrm{R}$ の一致は $\overrightarrow{OP}=\overrightarrow{OQ}=\overrightarrow{OR}$ から示す。




&nbsp;




<strong>共線条件</strong>(異なる3個以上の点が同じ直線上にあるための条件)


<ul>
	<li>点 $\mathrm{C}$ が直線 $\mathrm{AB}$ 上にある $\Leftrightarrow$ $\overrightarrow{AC}=k\overrightarrow{AB}$ となる実数 $k$ がある</li>
	<li>点 $\mathrm{P}$ が直線 $\mathrm{AB}$ 上にある $\Leftrightarrow$ $\overrightarrow{OP}=s\overrightarrow{OA}+t\overrightarrow{OB}$，$s+t=1$ となる実数 $s$，$t$ がある</li>
</ul>


<strong>共面条件</strong>(異なる4個以上の点が同じ平面上にあるための条件)




一直線上にない3点 $\mathrm{A}(\vec{a})$，$\mathrm{B}(\vec{b})$，$\mathrm{C}(\vec{c})$ の定める平面 $\mathrm{ABC}$ がある。


<p style="padding-left: 30px;">点 $\mathrm{P}(\vec{p})$ が平面 $\mathrm{ABC}$ 上にある $\Leftrightarrow$ $\overrightarrow{CP}=s\overrightarrow{CA}+t\overrightarrow{CB}$ となる実数 $s$，$t$ がある $\Leftrightarrow$ $\vec{p}=s\vec{a}+t\vec{b}+u\vec{c}$，$s+t+u=1$ となる実数 $s$，$t$，$u$ がある</p>
