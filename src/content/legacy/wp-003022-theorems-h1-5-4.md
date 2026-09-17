---
title: "【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 平均・分散・共分散・標準偏差における変量の変換"
wp_id: 3022
content_type: "page"
status: "publish"
published_at: "2020-05-03 21:53:33"
wp_date: "2020-05-03 21:53:33"
modified_at: "2020-05-03 21:53:33"
legacy_url: "http://mathrao.com/theorems-proof-of-high-school-math/theorems-h1-5-4/"
legacy_path: "/theorems-proof-of-high-school-math/theorems-h1-5-4/"
legacy_slug: "theorems-h1-5-4"
former_slugs: []
parent_wp_id: 2564
parent_title: "【定理・公式・証明】高校数学定理・公式一覧"
hierarchy: ["【定理・公式・証明】高校数学定理・公式一覧", "【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 平均・分散・共分散・標準偏差における変量の変換"]
category: []
tags: []
mathrao_section: "定理・公式・証明"
mathrao_grade: null
mathrao_course: "数学I"
source_content_sha256: "424cf78400435bcce29739c36a78547021716d3f85394d7fb38a106b93bbff2e"
---

## 平均における変量の変換


<div class="info-box">$n$ 個の値からなるデータ $x_{1} , x_{2} , \cdots  , x_{n}$ の平均値を $\overline{x}$ とする。



$u_{i} = ax_{i} +b$ $(i=1,2, \cdots ,n)$ としたとき，$u_{i}$ の平均値 $\overline{u}$ は，




$\overline{u}= a \overline{x} +b$


</div>
<div class="blank-box bb-green">証明



$x$ の平均値 $\overline{x}$ は，




$\overline{x} = \frac{1}{n} (x_{1} + x_{2} + \cdots + x_{n})$




このとき， $u_{i}$ の平均値 $\overline{u}$ は，




$\overline{u} = \frac{1}{n} (u_{1} + u_{2} + \cdots + u_{n})$




$= \frac{1}{n} \{ (ax_{1} +b) + (ax_{2} +b) + \cdots + (ax_{n} +b) \}$




$= \frac{1}{n} \{ a (x_{1} + x_{2} + \cdots + x_{n} ) +nb \}$




$= a \cdot \frac{1}{n} (x_{1} + x_{2} + \cdots + x_{n} ) +b$




$=a \overline{x} +b$


</div>


&nbsp;




## 分散・標準偏差における変量の変換


<div class="info-box">$n$ 個の値からなるデータ $x_{1} , x_{2} , \cdots , x_{n}$ の平均値を $\overline{x}$  ， 分散 $s_{x}^2$ ，標準偏差を $s_{x}$ とする。 $u_{i} = ax_{i} +b$ $(i=1,2, \cdots ,n)$ としたとき， $u_{i}$ の分散を $s_{1}^2$ ，標準偏差を $s_{u}$ とすると，



[Ⅰ] $s_{u}^2 = a^2 s_{x}^2$




[Ⅱ] $s_{u} = \vert a \vert s_{x}$


</div>
<div class="blank-box bb-green">証明



$x$ の平均値 $\overline{x}$ ，分散 $s_{x}^2$ は，




$\begin{eqnarray} \left\{ \begin{array}{l} \displaystyle \overline{x} = \frac{1}{n} (x_{1} + x_{2} + x_{n} ) \\ \displaystyle s_{x}^2= \frac{1}{n} \{ (x_{1} - \overline{x} )^2 + (x_{2} - \overline{x} )^2 + \cdots + (x_{n} - \overline{x} ) ^2 \} \ ( \gt 0 ) \end{array} \right. \end{eqnarray}$




$u_{i} =ax_{i} +b$ のとき， $\overline{u} =a \overline{x} +b$ 。このとき，$u$ の分散 $u_{x}^2$ は，




$u_{1} - \overline{u} =ax_{1} +b-(a \overline{x} +b) = a(x_{1} - \overline{x}$




$u_{2} - \overline{u} =ax_{2} +b-(a \overline{x} +b) = a(x_{2} - \overline{x}$




$\vdots$




$u_{n} - \overline{u} =ax_{n} +b-(a \overline{x} +b) = a(x_{n} - \overline{x}$




より，




[Ⅰ] $\displaystyle s_{u}^2 = \frac{1}{n} \{ (u_{1} - \overline{u} )^2 + (u_{2} - \overline{u} )^2 + \cdots + ( u_{n} - \overline{u} )^2 \}$




$\displaystyle = \frac{1}{n} \{ a^2 (x_{1} - \overline{x} )^2 + a^2 (x_{2} - \overline{x} )^2 + \cdots + a^2 (x_{n} - \overline{x} )^2 \} $




$\displaystyle =a^2 \cdot \frac{1}{n} \{ ( x_{1} - \overline{x} )^2 + (x_{2} - \overline{x} )^2 + \cdots +(x_{n} - \overline{x} )^2 \} = a^2 \cdot s_{x} ^2$




したがって，




[Ⅱ] $s_{u} = \sqrt{a^2 \cdot s_{x}^2} = \vert a \vert s_{x}$


</div>


&nbsp;




## 共分散における変量の変換


<div class="info-box">2つの変量 $x$ ， $y$ からなるデータとして， $n$ 個の値の組 $(x_{1} , y_{1} ) , (x_{2} , u_{2} ) , \cdots (x_{n} , y_{n} )$ がある。 $i=1,2, \cdots , n$ として， $x_{i}$ ， $y_{i}$ の平均値を $\overline{x}$ ， $\overline{y}$ ， $x_{i}$ ， $y_{i}$ の共分散を $s_{xy}$ とおく。このとき， $u_{i}=ax_{i} +b$ ， $v_{i} =cy_{i} +d$ としたとき， $u_{i}$ ， $v_{i}$ の共分散を $s_{uv}$ とおくと，



$s_{uv} =acs_{xy}$


</div>
<div class="blank-box bb-green">証明



$x_{i}$ , $y_{i}$ の共分散 $s_{xy}$ は，




$\displaystyle s_{xy} = {1}{n} \{ (x_{1} - \overline{x} )(y_{1} - \overline{y} ) + \cdots + (x_{n} - \overline{x} )( y_{n} - \overline{y} ) \}$




このとき， $u_{i}$ ， $v_{i}$ の共分散 $s_{uv}$ は，




$\displaystyle s_{uv} = \frac{1}{n} \{ (u_{1} - \overline{u} )(v_{1} - \overline{v} )+( u_{2} - \overline{u} )( v_{2} - \overline{v} ) + \cdots + u_{n} - \overline{u} )( v_{n} - \overline{v} ) \}$




$\displaystyle = \frac{1}{n} ( \{ ax_{1} +b- (a \overline{x} +b) \} \{ cy_{1} +d-(c \overline{y} +d) \} + \cdots + \{ ax_{n} +b-(a \overline{x} + b) \} \{ cy_{n} +d-(c \overline{y} +d) \} )$




$\displaystyle = \frac{1}{n} \{ a (x_{1} -\overline{x} ) \cdot c( y_{1} - \overline{y} ) + \cdots +a (x_{n} - \overline{x} ) \cdot c ( y_{n} - \overline{y} ) \}$




$\displaystyle =a \cdot c \cdot \frac{1}{n} \{ x_{1} - \overline{x} )(y_{1} - \overline{y} )+ \cdots + ( x_{n} - \overline{x} )( y_{n} - \overline{y} ) \}$




$=acs_{xy}$


</div>
