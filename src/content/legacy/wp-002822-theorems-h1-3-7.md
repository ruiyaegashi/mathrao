---
title: "【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – トレミーの定理"
wp_id: 2822
content_type: "page"
status: "publish"
published_at: "2020-04-22 23:12:03"
wp_date: "2020-04-22 23:12:03"
modified_at: "2020-04-22 23:12:03"
legacy_url: "http://mathrao.com/theorems-proof-of-high-school-math/theorems-h1-3-7/"
legacy_path: "/theorems-proof-of-high-school-math/theorems-h1-3-7/"
legacy_slug: "theorems-h1-3-7"
former_slugs: []
parent_wp_id: 2564
parent_title: "【定理・公式・証明】高校数学定理・公式一覧"
hierarchy: ["【定理・公式・証明】高校数学定理・公式一覧", "【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – トレミーの定理"]
category: []
tags: []
mathrao_section: "定理・公式・証明"
mathrao_grade: null
mathrao_course: "数学I"
source_content_sha256: "2ebd28e717f885e0f42c9a822c6c40126a166fee6b194df01640c8888eb74474"
---

## トレミーの定理


<div class="info-box">円に内接する四角形 $\mathrm{ ABCD }$ に関して，



$\mathrm{ AC } \cdot \mathrm{ BD } = \mathrm{ AB } \cdot \mathrm{ CD } + \mathrm{ AD } \cdot \mathrm{ BC }$


</div>
<div class="blank-box bb-green">証明



$\mathrm{ AB } =a$ ， $\mathrm{ BC } =b$ ， $\mathrm{ CD }=c$ ， $\mathrm{ DA } =d$ ，$\mathrm{ AC }=x$ ， $\mathrm{ BD } =y$ とおく。




三角形 $\mathrm{ ABC }$ ， 三角形 $\mathrm{ ACD }$ に余弦定理を用いると，




$x^2=a^2+b^2-2ab \cos B$   …①




$x^2=c^2+d^2-2cd \cos D$   …②




ここで， $D=180^{ \circ } -B$ より，②は次式のようになる。




$x^2=c^2+d^2-2cd \cos (180^{ \circ } -B)$




$=c^2+d^2-2cd(- \cos B)$




$=c^2+d^2+2cd \cos B$   …②’




$① \times cd+ ②' \times ab$ を計算し， $\cos B$ を消去すると，




$(cd+ab)x^2=cd(a^2+b^2)+ab(c^2+d^2)=a^2cd+b^2cd+abc^2+abd^2$




$=ad(ac+bd)+bc(ac+bd)$




$=(ac+bd)(ad+bc)$   …(*)




同様に三角形 $\mathrm{ ABD }$ ，三角形 $\mathrm{ BCD }$ にも余弦定理を用いると，




$(bc+da)y^2=(ab+cd)(ac+bd)$   …(**)




(*)と(**)の左辺同士，右辺同士の積をとると，




$(cd+ab)(bc+da)x^2y^2=(ac+bd)^2(ad+bc)(ab+cd)$




$x^2y^2=(ac+bd)^2$




$xy=ac+bd$




となるので，




$\mathrm{ AC } \cdot \mathrm{ BD } = \mathrm{ AB } \cdot \mathrm{ CD } + \mathrm{ AD } \cdot \mathrm{ BC }$


</div>
