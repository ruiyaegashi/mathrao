---
title: "【定義・定理・公式】高校数学基本事項 - 数学B - 空間のベクトルの成分，内積"
wp_id: 1023
content_type: "page"
status: "publish"
published_at: "2018-10-15 01:16:49"
wp_date: "2018-10-15 01:16:49"
modified_at: "2018-10-15 17:04:16"
legacy_url: "http://mathrao.com/basics-of-high-school-math/basics-hb-2-2/"
legacy_path: "/basics-of-high-school-math/basics-hb-2-2/"
legacy_slug: "basics-hb-2-2"
former_slugs: []
parent_wp_id: 448
parent_title: "【定義・定理・公式】高校数学基本事項一覧"
hierarchy: ["【定義・定理・公式】高校数学基本事項一覧", "【定義・定理・公式】高校数学基本事項 - 数学B - 空間のベクトルの成分，内積"]
category: []
tags: []
mathrao_section: "高校数学"
mathrao_grade: null
mathrao_course: "数学B"
source_content_sha256: "b29d49c42aaefbac5c1fbae4bd2e494c07b48e2192d973f2fb6b0dfb4052fa35"
---

## 空間ベクトルの成分




【定義】




<strong>平面上の基本ベクトル</strong>：$\vec{e_1}=(1,0,0)$，$\vec{e_2}=(0,1,0)$，$\vec{e_3}=(0,0,1)$




<strong>基本ベクトル表示・成分表示</strong>




座標空間の原点を $\mathrm{O}$ とし，ベクトル $\vec{a}$ に対して $\vec{a}=\overrightarrow{OA}$ となる点 $\mathrm{A}$ をとり，$\mathrm{A}$ の座標を $(a_1,a_2,a_3)$ とするとき


<p style="padding-left: 30px;"><strong>基本ベクトル表示</strong>：$\vec{a}=a_1\vec{e_1}+a_2\vec{e_2}+a_3\vec{e_3}$</p>
<p style="padding-left: 30px;"><strong>成分表示</strong>：$\vec{a}=(a_1,a_2,a_3)$</p>


$a_1$ を $x$ 成分，$a_2$ を $y$ 成分，$a_3$ を $z$ 成分という。




&nbsp;




## 成分表示の相等・大きさ・演算




<strong>相等</strong>




$\vec{a}=(a_1,a_2,a_3)$，$\vec{b}=(b_1,b_2,b_3)$ について


<p style="padding-left: 30px;">$\vec{a}=\vec{b}$ $\Leftrightarrow$ $a_1=b_1$ かつ $a_2=b_2$ かつ $a_3=b_3$</p>
<p style="padding-left: 30px;">特に $\vec{a}=\vec{0}$ $\Leftrightarrow$ $a_1=a_2=a_3=0$</p>


<strong>大きさ</strong>




$\vec{a}=(a_1,a_2,a_3)$ に対して


<p style="padding-left: 30px;">$|\vec{a}|=\sqrt{a_1^2+a_2^2+a_3^2}$</p>


<strong>演算</strong>




$k$，$l$ を実数とするとき


<ul>
	<li>$(a_1,a_2,a_3)+(b_1,b_2,b_3)=(a_1+b_1,a_2+b_2,a_3+b_3)$</li>
	<li>$(a_1,a_2,a_3)-(b_1,b_2,b_3)=(a_1-b_1,a_2-b_2,a_3-b_3)$</li>
	<li>$k(a_1,a_2,a_3)=(ka_1,ka_2,ka_3)$</li>
	<li>$k(a_1,a_2,a_3)+l(b_1,b_2,b_3)=(ka_1+lb_1,ka_2+lb_2,ka_3+lb_3)$</li>
</ul>


&nbsp;




## 点の座標とベクトルの成分




2点 $\mathrm{A}(a_1,a_2,a_3)$，$\mathrm{B}(b_1,b_2,b_3)$ について


<p style="padding-left: 30px;">$\overrightarrow{AB}=(b_1-a_1,b_2-a_2,b_3-a_3)$</p>
<p style="padding-left: 30px;">$\left|\overrightarrow{AB}\right|=\sqrt{(b_1-a_1)^2+(b_2-a_2)^2+(b_3-a_3)^2}$</p>


&nbsp;




## 空間ベクトルの内積の定義




【定義】




<strong>内積</strong>( $\vec{a}\cdot\vec{b}$ )：$\vec{0}$ でない2つのベクトル $\vec{a}$，$\vec{b}$ のなす角を $\theta$ ( $0^{ \circ }\leqq\theta\leqq180^{ \circ }$ )としたとき


<p style="padding-left: 30px;">$\vec{a}\cdot\vec{b}=|\vec{a}||\vec{b}|\cos\theta$</p>


内積は実数であり，$\vec{a}=\vec{0}$ または $\vec{b}=\vec{0}$ のときは $\vec{a}\cdot\vec{b}=0$




また，$\vec{a}=(a_1,a_2,a_3)$，$\vec{b}=(b_1,b_2,b_3)$ のとき


<p style="padding-left: 30px;">$\vec{a}\cdot\vec{b}=a_1b_1+a_2b_2+a_3b_3$</p>


であり，なす角 $\theta$ ( $0^{ \circ }\leqq\theta\leqq180^{ \circ }$ )に着目すると


<p style="padding-left: 30px;">$\cos\theta=\displaystyle\frac{\vec{a}\cdot\vec{b}}{|\vec{a}||\vec{b}|}=\frac{a_1b_1+a_2b_2+a_3b_3}{\sqrt{a_1^2+a_2^2+a_3^2}\sqrt{b_1^2+b_2^2+b_3^2}}$</p>


&nbsp;




## 内積と平行・垂直条件




$\vec{a}\neq\vec{0}$，$\vec{b}\neq\vec{0}$，$\vec{a}=(a_1,a_2,a_3)$，$\vec{b}=(b_1,b_2,b_3)$ とする


<ul>
	<li>平行条件：$\vec{a}/\!/\vec{b}$ $\Leftrightarrow$ $\vec{a}\cdot\vec{b}=\pm|\vec{a}||\vec{b}|$ $\Leftrightarrow$ $\frac{a_1}{b_1}=\frac{a_2}{b_2}=\frac{a_3}{b_3}$<br />
(ただし，分母が $0$ のとき分子も $0$ )</li>
	<li>垂直条件：$\vec{a}\perp\vec{b}$ $\Leftrightarrow$ $\vec{a}\cdot\vec{b}=0$ $\Leftrightarrow$ $a_1b_1+a_2b_2+a_3b_3=0$</li>
</ul>


&nbsp;




## 内積の性質




【法則】




<strong>内積の演算法則</strong>




$k$，$p$，$q$，$r$，$s$ を実数とする


<ul>
	<li>$\vec{a}\cdot\vec{b}=\vec{b}\cdot\vec{a}$</li>
	<li>$(\vec{a}+\vec{b})\cdot\vec{c}=\vec{a}\cdot\vec{c}+\vec{b}\cdot\vec{c}$</li>
	<li>$\vec{a}\cdot(\vec{b}+\vec{c})=\vec{a}\cdot\vec{b}+\vec{a}\cdot\vec{c}$</li>
	<li>$(k\vec{a})\cdot\vec{b}=\vec{a}\cdot(k\vec{b})=k(\vec{a}\cdot\vec{b})=k\vec{a}\cdot\vec{b}$</li>
	<li>$(p\vec{a}+q\vec{b})\cdot(r\vec{c}+s\vec{d})=pr\vec{a}\cdot\vec{c}+ps\vec{a}\cdot\vec{d}+qr\vec{b}\cdot\vec{c}+qs\vec{b}\cdot\vec{d}$</li>
</ul>


<strong>ベクトルの大きさと内積</strong>


<ul>
	<li>$\vec{a}\cdot\vec{a}=|\vec{a}|^2$</li>
	<li>$|\vec{a}|=\sqrt{\vec{a}\cdot\vec{a}}$</li>
	<li>$-|\vec{a}||\vec{b}|\leqq\vec{a}\cdot\vec{b}\leqq|\vec{a}||\vec{b}|$</li>
</ul>
