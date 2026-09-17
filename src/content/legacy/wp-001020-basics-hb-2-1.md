---
title: "【定義・定理・公式】高校数学基本事項 - 数学B - 空間の座標，空間のベクトル"
wp_id: 1020
content_type: "page"
status: "publish"
published_at: "2018-10-15 00:41:41"
wp_date: "2018-10-15 00:41:41"
modified_at: "2018-10-21 02:40:08"
legacy_url: "http://mathrao.com/basics-of-high-school-math/basics-hb-2-1/"
legacy_path: "/basics-of-high-school-math/basics-hb-2-1/"
legacy_slug: "basics-hb-2-1"
former_slugs: []
parent_wp_id: 448
parent_title: "【定義・定理・公式】高校数学基本事項一覧"
hierarchy: ["【定義・定理・公式】高校数学基本事項一覧", "【定義・定理・公式】高校数学基本事項 - 数学B - 空間の座標，空間のベクトル"]
category: []
tags: []
mathrao_section: "高校数学"
mathrao_grade: null
mathrao_course: "数学B"
source_content_sha256: "3fe64f300ed68c59a68515a00e30c40544796a0c85e46b6b9910e0cae2db6481"
---

## 空間の点の座標




【定義】




<strong>座標軸</strong>




空間に点 $\mathrm{O}$ をとり，$\mathrm{O}$ で互いに直交する3本の数直線をそれぞれ $\boldsymbol{x}$ <strong>軸</strong>，$\boldsymbol{y}$ <strong>軸</strong>，$\boldsymbol{z}$ <strong>軸</strong> といい，まとめて<strong>座標軸</strong>という。また，点 $\mathrm{O}$ を<strong>原点</strong>という。




<strong>座標平面</strong>




$x$ 軸と $y$ 軸で定める平面を $\boldsymbol{xy}$ <strong>平面</strong>といい，同様の $\boldsymbol{yz}$ <strong>平面</strong>，$\boldsymbol{zx}$ <strong>平面</strong> をまとめて<strong>座標平面</strong>という。




<strong>座標</strong>




空間の点 $\mathrm{P}$ に対して，$\mathrm{P}$ を通り各座標軸に垂直な平面が $x$ 軸，$y$ 軸， $z$ 軸と交わる点をそれぞれ点 $\mathrm{A}$，$\mathrm{B}$，$\mathrm{C}$ とする。$\mathrm{A}$，$\mathrm{B}$，$\mathrm{C}$ の各座標軸上での座標がそれぞれ $a$，$b$，$c$ のとき，3つの実数の組 $(a,b,c)$ を点 $\mathrm{P}$ の<strong>座標</strong>といい，$a$，$b$，$c$ をそれぞれ点 $\mathrm{P}$ の$\boldsymbol{x}$ <strong>座標</strong>，$\boldsymbol{y}$ <strong>座標</strong>，$\boldsymbol{z}$ <strong>座標</strong>という。この点 $\mathrm{P}$ を $\mathrm{P}(a,b,c)$ と書くことがある。




<strong>座標空間</strong>




座標の定められた空間を<strong>座標空間</strong>という。




&nbsp;




## 2点間の距離




2点 $\mathrm{A}(a_1,a_2,a_3)$，$\mathrm{B}(b_1,b_2,b_3)$ について，$\mathrm{A}$，$\mathrm{B}$ 間の距離は


<p style="padding-left: 30px;">$\mathrm{AB}=\sqrt{(b_1-a_1)^2+(b_2-a_2)^2+(b_3-a_3)^2}$</p>


特に，原点 $\mathrm{O}$ と点 $\mathrm{A}(a_1,a_2,a_3)$ の距離は


<p style="padding-left: 30px;">$\mathrm{OA}=\sqrt{a_1^2+a_2^2+a_3^2}$</p>


&nbsp;




## 空間ベクトルの演算




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




## 空間ベクトルの平行条件




$\vec{a}\neq\vec{0}$，$\vec{b}\neq\vec{0}$ のとき


<p style="padding-left: 30px;">$\vec{a}/\!/\vec{b}$ $\Leftrightarrow$ $\vec{b}=k\vec{a}$ となる実数 $k$ が存在する</p>


&nbsp;




## 空間ベクトルの分解




1次独立な3つのベクトル $\vec{a}$，$\vec{b}$，$\vec{c}$ に対して，任意のベクトル $\vec{p}$ は実数 $s$，$t$，$u$ を用いて次の形にただ1通りに表される。


<p style="padding-left: 30px;">$\vec{p}=s\vec{a}+t\vec{b}+u\vec{c}$</p>


このことから，$s$，$s'$，$t$，$t'$，$u$，$u'$ を実数として次の性質が成り立つ。


<p style="padding-left: 30px;">$s\vec{a}+t\vec{b}+u\vec{c}=s'\vec{a}+t'\vec{b}+u'\vec{c}$ $\Leftrightarrow$ $s=s'$ かつ $t=t'$ かつ $u=u'$</p>
<p style="padding-left: 30px;">特に $s\vec{a}+t\vec{b}+u\vec{c}=\vec{0}$ $\Leftrightarrow$ $s=t=u=0$</p>
