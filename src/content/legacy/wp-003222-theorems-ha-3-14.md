---
title: "【定理・公式・証明】高校数学定理・公式 – 数学A – 一次不定方程式 $ax+by=1$"
wp_id: 3222
content_type: "page"
status: "publish"
published_at: "2020-06-09 16:57:01"
wp_date: "2020-06-09 16:57:01"
modified_at: "2020-06-09 16:57:01"
legacy_url: "http://mathrao.com/theorems-proof-of-high-school-math/theorems-ha-3-14/"
legacy_path: "/theorems-proof-of-high-school-math/theorems-ha-3-14/"
legacy_slug: "theorems-ha-3-14"
former_slugs: []
parent_wp_id: 2564
parent_title: "【定理・公式・証明】高校数学定理・公式一覧"
hierarchy: ["【定理・公式・証明】高校数学定理・公式一覧", "【定理・公式・証明】高校数学定理・公式 – 数学A – 一次不定方程式 $ax+by=1$"]
category: []
tags: []
mathrao_section: "定理・公式・証明"
mathrao_grade: null
mathrao_course: "数学A"
source_content_sha256: "02df7e6d9d3d69426aad79aca7960951c1d9f5a8dc91543aa36db7ece5099a87"
---

## 【発展】一次不定方程式 $ax+by=1$ の解


<div class="info-box">$a$ と $b$ が互いに素な整数であるとき， $ax+by=1$ を満たす整数の組 $(x,y)$ は，無数に存在する。</div>


[overrule]説明




まず，$a,b$ を自然数とし，方程式 $ax+by=0$ …① の解が少なくとも1つは存在することを示す。




$b=1$ のとき，①は $\displaystyle x= \frac{1-y}{a}$ となる。例えば， $y=a+1$ とすると




$\displaystyle x= \frac{1-(a+1)}{a} =-1$ であるから， $(x,y)=(-1,a+1)$ は①の解であり，①の解は少なくとも1つは存在する。




$b \geqq 2$ のとき， $a$ と $b$ がお互いに素であることから，フェルマーの小定理の準備①において示したことより，




$a,2a,3a, \cdots ,ba$




を$b$ で割った余りはすべて異なる。$ba$ を $b$ で割った余りは0であるから， $x_{1} a$ を $b$ で割った余りが1となるような整数 $x_{1} (1 \leqq x_{1} \leqq b-1$ が必ず存在し，整数 $q$ を用いて，




$x_{1} a=bq+1$




と表せる。ここで，整数 $y_{1}$ を用いて $q=-y_{1}$ とおくと，②は




$x_{1} a=b(-y_{1} ) +1$




$ax_{1} +by_{1} =1$




したがって， $(x,y)=(x_{1} ,y_{1})$ は，方程式 $ax+by=1$ の解の1つである。




また， $a,b$ が負の整数である場合も，方程式 $ax+by=1$ の解 $(x,y)$ は必ず存在する。例えば， $a=3,y=5$ として， $3x+5y=1$ の整数解 $(x_{1} ,y_{1})$ が見つかったとする。このとき， $3x_{1} +5y_{1}=1$ より， $3x_{1} -5(-y_{1} )=1$ であるから，




$(x,y)=(x_{1} -y{1} )$ は $3x-5y=1$ の解である。




次に，方程式 $ax+by=1$ の解は無限に存在することについて説明する。




例えば， $b \gt 0,a \lt 0$ とすると，直線 $ax+by=1$ すなわち $\displaystyle y= - \frac{a}{b} x + \frac{1}{b}$ (傾き $\displaystyle - \frac{a}{b} \gt 0$ )は上図のようになる。この直線上の点において， $x$ 座標が $b$ だけ増えると， $y$ 座標が $-a( \gt 0)$ 増えるから， $(x_{1} +b,y_{1} -a)$ もまた直線上の点である。




これを図のように繰り返すと， $(x,y)=(x_{1} +kb,y_{1} -ka)$ ( $k$ は整数)はすべて直線 $ax+by=1$ 上の点であり， $a(x_{1} +kb)+b(y_{1} -ka) =1$ をみたす。




よって，方程式 $ax+by=1$ の解は無限に存在する。[/overrule]
