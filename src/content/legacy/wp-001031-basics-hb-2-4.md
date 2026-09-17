---
title: "【定義・定理・公式】高校数学基本事項 - 数学B - 座標空間の図形，ベクトル方程式"
wp_id: 1031
content_type: "page"
status: "publish"
published_at: "2018-10-15 02:25:39"
wp_date: "2018-10-15 02:25:39"
modified_at: "2018-10-15 17:04:01"
legacy_url: "http://mathrao.com/basics-of-high-school-math/basics-hb-2-4/"
legacy_path: "/basics-of-high-school-math/basics-hb-2-4/"
legacy_slug: "basics-hb-2-4"
former_slugs: []
parent_wp_id: 448
parent_title: "【定義・定理・公式】高校数学基本事項一覧"
hierarchy: ["【定義・定理・公式】高校数学基本事項一覧", "【定義・定理・公式】高校数学基本事項 - 数学B - 座標空間の図形，ベクトル方程式"]
category: []
tags: []
mathrao_section: "高校数学"
mathrao_grade: null
mathrao_course: "数学B"
source_content_sha256: "acf76172a7064d39064b4bec834ca9fc59f0be224d56e0918b5db78ef28284ca"
---

## 平面の方程式




点 $\mathrm{A}(x_1,y_1,z_1)$ を通り，$\vec{0}$ でないベクトル $\vec{n}=(a,b,c)$ に垂直な平面の方程式


<p style="padding-left: 30px;">$a(x-x_1)+b(y-y_1)+c(z-z_1)=0$：標準形</p>


また，標準形を展開して整理すると


<p style="padding-left: 30px;">$ax+by+cz+d=0$ ( $(a,b,c)\neq(0,0,0)$ )：一般形</p>


一般に，$\vec{n}=(a,b,c)$ は平面 $ax+by+cz+d=0$ の法線ベクトルである。




&nbsp;




## 点と平面の距離




【定理】




<strong>点と平面の距離</strong>




点 $\mathrm{A}(x_1,y_1,z_1)$ と平面 $\alpha$：$ax+by+cz+d=0$ の距離は


<p style="padding-left: 30px;">$\displaystyle\frac{|ax_1+by_1+cz_1+d|}{\sqrt{a^2+b^2+c^2}}$</p>


&nbsp;




## 平面のベクトル方程式




平面上の任意の点 $\mathrm{P}(\vec{p})$，$s$，$t$，$u$ を実数とする。




<strong>3定点</strong>




一直線上にない3点 $\mathrm{A}(\vec{a})$，$\mathrm{B}(\vec{b})$，$\mathrm{C}(\vec{c})$ の定める平面のベクトル方程式は


<p style="padding-left: 30px;">$\vec{p}=s\vec{a}+t\vec{b}+u\vec{c}$ ( $s+t+u=1$ )</p>
<p style="padding-left: 30px;">$\vec{p}=s\vec{a}+t\vec{b}+(1-s-t)\vec{c}$</p>


<strong>1定点と垂直</strong>




点 $\mathrm{A}(\vec{a})$ を通り，$\vec{0}$ でないベクトル $\vec{n}$ に垂直な平面 $\alpha$ のベクトル方程式


<p style="padding-left: 30px;">$\vec{n}\cdot(\vec{p}-\vec{a})=0$</p>


&nbsp;




## 空間における直線の方程式




$\mathrm{A}(x_1,y_1,z_1)$，$\mathrm{B}(x_2,y_2,z_2)$ を定点，$\mathrm{P}(x,y,z)$ を直線上の点とし，$t$ を実数の変数とする。




<strong>1定点と方向ベクトル</strong>




点 $\mathrm{A}$ を通り，$\vec{d}=(l,m,n)$ に平行な直線の方程式


<p style="padding-left: 30px;">$\left \{ \begin{array}{l}x=x_1+lt\\y=y_1+mt\\z-z_1+nt\end{array} \right.$</p>
<p style="padding-left: 30px;">$\displaystyle\frac{x-x_1}{l}=\frac{y-y_1}{m}=\frac{z-z_1}{n}$ ( $lmn\neq0$ )</p>


<strong>2定点</strong>




異なる2点 $\mathrm{A}$，$\mathrm{B}$ を通る直線の方程式


<p style="padding-left: 30px;">$\left \{ \begin{array}{l}x=(1-t)x_1+tx_2\\y=(1-t)y_1+ty_2\\z=(1-t)z_1+tz_2\end{array} \right.$</p>
<p style="padding-left: 30px;">$\displaystyle\frac{x-x_1}{x_2-x_1}=\frac{y-y_1}{y_2-y_1}=\frac{z-z_1}{z_2-z_1}$ ( $x_2\neq x_1$，$y_2\neq y_1$，$z_2\neq z_1$ )</p>


&nbsp;




## 空間における直線のベクトル方程式




$s$，$t$ は実数の変数とし，直線上の任意の点を $\mathrm{P}(\vec{p})$ とする。




<strong>1定点と方向ベクトル</strong>




点 $\mathrm{A}(\vec{a})$ を通り，$\vec{0}$ でないベクトル $\vec{d}$ に平行な直線のベクトル方程式


<p style="padding-left: 30px;">$\vec{p}=\vec{a}+t\vec{d}$</p>


<strong>2定点</strong>




異なる2点 $\mathrm{A}(\vec{a})$，$\mathrm{B}(\vec{b})$ を通る直線のベクトル方程式


<p style="padding-left: 30px;">$\vec{p}=(1-t)\vec{a}+t\vec{b}$</p>
<p style="padding-left: 30px;">$\vec{p}=s\vec{a}+t\vec{b}$ ( $s+t=1$ )</p>


&nbsp;




## 球面の方程式




空間において，定点 $\mathrm{C}$ からの距離が一定の値 $r$ であるような点の全体を，$\mathrm{C}$ を中心とする半径 $r$ の<strong>球面</strong>(または単に<strong>球</strong>)という。




点 $(a,b,c)$ を中心とする半径 $r$ の球面の方程式は


<p style="padding-left: 30px;">$(x-a)^2+(y-b)^2+(z-c)^2=r^2$：標準形</p>


特に，中心が原点の場合


<p style="padding-left: 30px;">$x^2+y^2+z^2=r^2$</p>


また，標準形を展開して整理すると


<p style="padding-left: 30px;">$x^2+y^2+z^2+Ax+By+Cz+D=0$：一般形</p>


&nbsp;




## 球面のベクトル方程式




球面上の任意の点を $\mathrm{P}(\vec{p})$ とする。




<strong>中心と半径</strong>




中心が $\mathrm{C}(\vec{c})$，半径 $r$ の球面のベクトル方程式


<p style="padding-left: 30px;">$|\vec{p}-\vec{c}|=r$</p>
<p style="padding-left: 30px;">$(\vec{p}-\vec{c})\cdot(\vec{p}-\vec{c})=r^2$</p>


<strong>直径</strong>




$\mathrm{A}(\vec{a})$，$\mathrm{B}(\vec{b})$ とし，線分 $\mathrm{AB}$ を直径とする球面のベクトル方程式


<p style="padding-left: 30px;">$(\vec{p}-\vec{a})\cdot(\vec{p}-\vec{b})=0$</p>
