---
title: "【定義・定理・公式】高校数学基本事項 - 数学B - ベクトルの演算"
wp_id: 983
content_type: "page"
status: "publish"
published_at: "2018-10-14 16:39:08"
wp_date: "2018-10-14 16:39:08"
modified_at: "2018-10-15 17:05:08"
legacy_url: "http://mathrao.com/basics-of-high-school-math/basics-hb-1-1/"
legacy_path: "/basics-of-high-school-math/basics-hb-1-1/"
legacy_slug: "basics-hb-1-1"
former_slugs: []
parent_wp_id: 448
parent_title: "【定義・定理・公式】高校数学基本事項一覧"
hierarchy: ["【定義・定理・公式】高校数学基本事項一覧", "【定義・定理・公式】高校数学基本事項 - 数学B - ベクトルの演算"]
category: []
tags: []
mathrao_section: "高校数学"
mathrao_grade: null
mathrao_course: "数学B"
source_content_sha256: "5b9b05d05cdbc9ea3af5f0fce0c86af1be62e28bdc50f47b6757b7c005975dac"
---

## 有向線分とベクトル




【定義】




<strong>有向線分</strong>：向きを指定した線分




<strong>始点</strong>：有向線分 $\mathrm{AB}$ における点 $\mathrm{A}$




<strong>終点</strong>：有向線分 $\mathrm{AB}$ における点 $\mathrm{B}$




<strong>有向線分の大きさ(長さ)</strong>：有向線分 $\mathrm{AB}$ における線分 $\mathrm{AB}$ の長さ




<strong>ベクトル</strong>：その位置を問題にしないで，向きと大きさだけで定まる量


<p style="padding-left: 30px;">※有向線分 $\mathrm{AB}$ で表されるベクトルを $\overrightarrow{AB}$，ベクトル $\overrightarrow{AB}$ の大きさを $\left| \overrightarrow{AB} \right|$ と書く。また，1つの文字を用いて $\vec{a}$，$| \vec{a} |$ と表すこともある。</p>
<p style="padding-left: 30px;">※2つのベクトル $\vec{a}$，$\vec{b}$ が等しい( $\vec{a} = \vec{b}$ ) $\Leftrightarrow$ $\vec{a}$，$\vec{b}$ の向きが同じで大きさが等しい：ベクトルの相等</p>


<strong>単位ベクトル</strong>：大きさが $1$ であるベクトル




<strong>逆ベクトル</strong>：大きさが等しく，向きが反対であるベクトル


<p style="padding-left: 30px;">※$\vec{a}$ に対して，$-\vec{a}$ で表される。</p>


<strong>零ベクトル( $\vec{0}$ )</strong>：大きさが $0$ のベクトル


<p style="padding-left: 30px;">※零ベクトルの向きは考えない。</p>


<strong>1次独立</strong>：2つのベクトル $\vec{a}$，$\vec{b}$ が，$\vec{a}\neq\vec{0}$，$\vec{b}\neq\vec{0}$，$\vec{a}\nparallel\vec{b}$ を満たすこと




&nbsp;




## ベクトルの演算




$\vec{a}$，$\vec{b}$，実数 $k$，$l$ に対して


<ul>
	<li>ベクトルの加法：$\vec{a}+\vec{b}$</li>
	<li>ベクトルの減法：$\vec{a}-\vec{b}$</li>
	<li>ベクトルの実数倍：$k \vec{a}$<br />
※大きさは $| \vec{a} |$ の $k$ 倍，向きは $k&gt;0$ のときは同じで，$k&lt;0$ のときは反対<br />
※ $k=0$ のとき $k \vec{a} =0 \vec{a} = \vec{0}$</li>
</ul>


【法則】




<strong>交換法則</strong>


<p style="padding-left: 30px;">$\vec{a}+\vec{b}=\vec{b}+\vec{a}$</p>


<strong>結合法則</strong>


<p style="padding-left: 30px;">$(\vec{a}+\vec{b})+\vec{c}=\vec{a}+(\vec{b}+\vec{c})$</p>


【定理】




<strong>逆ベクトルと零ベクトルの性質</strong>


<ul>
	<li>$\vec{a}+(-\vec{a})=\vec{0}$</li>
	<li>$\vec{a}+\vec{0}=\vec{a}$</li>
</ul>


<strong>ベクトルの実数倍の性質</strong>


<ul>
	<li>$k(l\vec{a})=(kl)\vec{a}$</li>
	<li>$(k+l)\vec{a}=k\vec{a}+l\vec{a}$</li>
	<li>$k(\vec{a}+\vec{b})=k\vec{a}+k\vec{b}$</li>
</ul>


&nbsp;




## ベクトルの平行




【定義】




<strong>ベクトルが平行</strong>( $\vec{a}/\!/\vec{b}$ )：$\vec{0}$ でない2つのベクトル $\vec{a}$，$\vec{b}$ の向きが同じ，または，反対であること




$\vec{a}\neq\vec{0}$ のとき，$\vec{a}$ と平行な単位ベクトル： $\displaystyle \frac{\vec{a}}{|\vec{a}|}$，$\displaystyle -\frac{\vec{a}}{|\vec{a}|}$




&nbsp;




## ベクトルの平行条件




$\vec{a}\neq\vec{0}$，$\vec{b}\neq\vec{0}$ のとき


<p style="padding-left: 30px;">$\vec{a}/\!/\vec{b}$ $\Leftrightarrow$ $\vec{b}=k\vec{a}$ となる実数 $k$ が存在する</p>


&nbsp;




## ベクトルの分解




1次独立な2つのベクトル $\vec{a}$，$\vec{b}$ に対して，任意のベクトル $\vec{p}$ は実数 $s$，$t$ を用いて次の形にただ1通りに表される。


<p style="padding-left: 30px;">$\vec{p}=s\vec{a}+t\vec{b}$</p>


このことから，$k$，$l$，$m$，$n$ を実数として次の性質が成り立つ。


<p style="padding-left: 30px;">$k\vec{a}+l\vec{b}=m\vec{a}+n\vec{b}$ $\Leftrightarrow$ $k=m$ かつ $l=n$</p>
<p style="padding-left: 30px;">特に $k\vec{a}+l\vec{b}=\vec{0}$ $\Leftrightarrow$ $k=l=0$</p>
