---
title: "【定義・定理・公式】高校数学基本事項 - 数学B - ベクトル方程式"
wp_id: 1012
content_type: "page"
status: "publish"
published_at: "2018-10-14 23:43:32"
wp_date: "2018-10-14 23:43:32"
modified_at: "2018-10-15 17:04:31"
legacy_url: "http://mathrao.com/basics-of-high-school-math/basics-hb-1-6/"
legacy_path: "/basics-of-high-school-math/basics-hb-1-6/"
legacy_slug: "basics-hb-1-6"
former_slugs: []
parent_wp_id: 448
parent_title: "【定義・定理・公式】高校数学基本事項一覧"
hierarchy: ["【定義・定理・公式】高校数学基本事項一覧", "【定義・定理・公式】高校数学基本事項 - 数学B - ベクトル方程式"]
category: []
tags: []
mathrao_section: "高校数学"
mathrao_grade: null
mathrao_course: "数学B"
source_content_sha256: "0cc27e930c88bfecd97b653f594c701949835e0e0375b1efb7fcfb70e3ba2194"
---

## 直線のベクトル方程式




直線上の任意の点 $\mathrm{P}(\vec{p})$ について，$s$，$t$ を実数の変数とする。




<strong>1定点と方向ベクトル</strong>




定点 $\mathrm{A}(\vec{a})$ を通り，$\vec{0}$ でないベクトル $\vec{d}$ に平行な直線のベクトル方程式


<p style="padding-left: 30px;">$\vec{p}=\vec{a}+t\vec{d}$</p>


※$\vec{d}$ を直線の<strong>方向ベクトル</strong>，$t$ を<strong>媒介変数</strong>という。




<strong>媒介変数表示</strong>




$\vec{p}=(x,y)$，$\vec{a}=(x_1,y_1)$，$\vec{d}=(l,m)$ とすると


<p style="padding-left: 30px;">$\left \{ \begin{array}{l}x=x_1+lt\\y=y_1+mt \end{array} \right.$ </p>


<strong>2定点</strong>




異なる2点 $\mathrm{A}(\vec{a})$，$\mathrm{B}(\vec{b})$ を通る直線のベクトル方程式


<p style="padding-left: 30px;">$\vec{p}=(1-t)\vec{a}+t\vec{b}$</p>
<p style="padding-left: 30px;">$\vec{p}=s\vec{a}+t\vec{b}$ ( $s+t=1$ )</p>


<strong>1定点と法線ベクトル</strong>




定点 $\mathrm{A}(\vec{a})$ を通り，$\vec{0}$ でないベクトル $\vec{n}$ に垂直な直線のベクトル方程式


<p style="padding-left: 30px;">$\vec{n}\cdot(\vec{p}-\vec{a})=0$</p>


※$\vec{n}$ を直線の<strong>法線ベクトル</strong>という。




※法線ベクトルについて次のことが成り立つ


<ul>
	<li>点 $\mathrm{A}(x_1,y_1)$ を通り，$\vec{n}=(a,b)$ が法線ベクトルである直線の方程式は $a(x-x_1)+b(y-y_1)=0$</li>
	<li>直線 $ax+by+c=0$ において，$\vec{n}=(a,b)$ はその法線ベクトルである</li>
</ul>


&nbsp;




## 円のベクトル方程式




$\overrightarrow{OA}=\vec{a}$，$\overrightarrow{OB}=\vec{b}$，$\overrightarrow{OC}=\vec{c}$，$\overrightarrow{OP}=\vec{p}$ とし，$\mathrm{P}$ は円周上の任意の点とする。




<strong>中心と半径</strong>




中心 $\mathrm{C}$，半径 $r$ の円のベクトル方程式


<p style="padding-left: 30px;">$|\vec{p}-\vec{c}|=r$</p>
<p style="padding-left: 30px;">$(\vec{p}-\vec{c})\cdot(\vec{p}-\vec{c})=r^2$</p>


<strong>直径</strong>




線分 $\mathrm{AB}$ を直径とする円のベクトル方程式


<p style="padding-left: 30px;">$(\vec{p}-\vec{a})\cdot(\vec{p}-\vec{b})=0$</p>


&nbsp;




## 平面上の点の存在範囲




$\overrightarrow{OA}=\vec{a}$，$\overrightarrow{OB}=\vec{b}$，$\overrightarrow{OP}=\vec{p}$ とし，$\vec{a}$，$\vec{b}$ が1次独立で $\vec{p}=s\vec{a}+t\vec{b}$ ( $s$，$t$ は実数の変数) とする。


<ul>
	<li>$s+t=1$ $\Leftrightarrow$ 直線 $\mathrm{AB}$</li>
	<li>$s+t=1$，$s\geqq0$，$t\geqq0$ $\Leftrightarrow$ 線分 $\mathrm{AB}$</li>
	<li>$s+t\leqq1$，$s\geqq0$，$t\geqq0$ $\Leftrightarrow$ $\triangle \mathrm{OAB}$ の周および内部</li>
	<li>$0 \leqq s \leqq 1$，$0 \leqq t \leqq 1$ $\Leftrightarrow$ 平行四辺形 $\mathrm{OACB}$ の周および内部</li>
</ul>
