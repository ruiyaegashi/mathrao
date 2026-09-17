---
title: "【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 三角形の成立条件・辺と角の大小関係"
wp_id: 2763
content_type: "page"
status: "publish"
published_at: "2020-04-22 22:53:30"
wp_date: "2020-04-22 22:53:30"
modified_at: "2020-04-22 22:53:30"
legacy_url: "http://mathrao.com/theorems-proof-of-high-school-math/theorems-h1-3-3/"
legacy_path: "/theorems-proof-of-high-school-math/theorems-h1-3-3/"
legacy_slug: "theorems-h1-3-3"
former_slugs: []
parent_wp_id: 2564
parent_title: "【定理・公式・証明】高校数学定理・公式一覧"
hierarchy: ["【定理・公式・証明】高校数学定理・公式一覧", "【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 三角形の成立条件・辺と角の大小関係"]
category: []
tags: []
mathrao_section: "定理・公式・証明"
mathrao_grade: null
mathrao_course: "数学I"
source_content_sha256: "0ee6f418cf73d392e03a505fc34ef86f228ec30cafa6d0ea39168f4445ea9ab3"
---

## 三角形の成立条件


<div class="info-box">三角形 $\mathrm{ ABC }$ があるとき，



$\vert b-c \vert \lt a \lt b+c$ .


</div>


[overrule]説明




右図のような三角形 $\mathrm{ ABC }$ に対して，




「2辺の長さの和は，1辺の長さよりも大きい」ことを利用すると，




$\begin{eqnarray}  \left\{    \begin{array}{l}      a \lt b+c \\     b \lt c+a  \\ c \lt a+b    \end{array}  \right.\end{eqnarray}$




$a$ について式変形を行うと，




$\begin{eqnarray}  \left\{    \begin{array}{ll}      a \lt b+c  &amp; …①  \\     b-c \lt a &amp; …②    \\ c-b \lt a &amp; …③      \end{array}  \right.\end{eqnarray}$




ここで、




$c-b \lt a \Leftrightarrow -a \lt b-c $




であるから，②かつ③は




$-a \lt b-c \lt a$




$\vert b-c \vert \lt a$   …④




①かつ④より，




$\vert b-c \vert \lt a \lt b+c$[/overrule]




## 辺と角の大小関係


<div class="info-box">三角形の辺と角の大小関係については，



「 $A \gt B \Leftrightarrow a \gt b$ 」


</div>
<div class="blank-box bb-green">証明



$\mathrm{ A }$ ， $\mathrm{ B }$ は三角形 $\mathrm{ ABC }$ の内角であり， $0^{ \circ } \lt B \lt A \lt 180^{ \circ }$ とすると，




$A \gt B \Leftrightarrow \cos A \lt \cos B$　…①




次に三角形 $\mathrm{ ABC }$ について，余弦定理を用いて次の式を得る。




$\cos A \lt \cos B \Leftrightarrow \cos B - \cos A \gt 0$




$\displaystyle \Leftrightarrow \frac{c^2 +a^2 -b^2}{2ca} - \frac{b^2 +c^2 -a^2}{2bc} \gt 0$




$\displaystyle \Leftrightarrow \frac{b( c^2 +a^2 -b^2) -a(b^2 +c^2 -a^2)}{2abc} \gt 0$




$\Leftrightarrow (a^2 -b^2)(a+b)-(a-b)c^2 \gt 0$ ( $2abc \gt 0$ より)




$\Leftrightarrow (a-b)(a+b)(a+b)-(a-b)c^2 \gt 0$




$\Leftrightarrow (a-b) \left\{ (a+b)^2 -c^2 \right\} \gt 0$




$\Leftrightarrow a \gt b$  ( $a+b \gt c$ より $(a+b)^2 -c^2 \gt 0$ )  …②




①，②より，




$A \gt B \Leftrightarrow a \gt b$


</div>
