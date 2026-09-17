---
title: "【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 四角形の面積と対角線"
wp_id: 2807
content_type: "page"
status: "publish"
published_at: "2020-04-22 23:03:30"
wp_date: "2020-04-22 23:03:30"
modified_at: "2020-04-22 23:03:30"
legacy_url: "http://mathrao.com/theorems-proof-of-high-school-math/theorems-h1-3-6/"
legacy_path: "/theorems-proof-of-high-school-math/theorems-h1-3-6/"
legacy_slug: "theorems-h1-3-6"
former_slugs: []
parent_wp_id: 2564
parent_title: "【定理・公式・証明】高校数学定理・公式一覧"
hierarchy: ["【定理・公式・証明】高校数学定理・公式一覧", "【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – 四角形の面積と対角線"]
category: []
tags: []
mathrao_section: "定理・公式・証明"
mathrao_grade: null
mathrao_course: "数学I"
source_content_sha256: "04f2795a178afc2cb8919491371f905436d16509b62f431d9718cea084ec0456"
---

## 四角形の面積(対角線の積)


<div class="info-box">右のような凸四角形 $\mathrm{ ABCD }$ の対角線の交点を $\mathrm{ E }$ ，$\angle \mathrm{ AED } = \alpha$ とする。四角形の面積を $S$ とするとき，



$\displaystyle S= \frac{1}{2} \mathrm{ AC } \cdot \mathrm{ BD } \cdot \sin \alpha$


</div>
<div class="blank-box bb-green">証明



右図の凸四角形 $\mathrm{ ABCD }$ について， $\angle \mathrm{ AED } = \alpha$ より， $\angle \mathrm{ AEB } =180^{ \circ } - \alpha$ ， $\angle \mathrm{ BEC } = \alpha$ ， $\angle \mathrm{ CED } =180^{ \circ } - \alpha$ 。




ここで四角形 $\mathrm{ ABCD }$ の面積を $\triangle \mathrm{ AEB }$ ， <span style="display: inline !important; float: none; background-color: #ffffff; color: #333333; cursor: text; font-family: '游ゴシック体','Yu Gothic','Hiragino Kaku Gothic Pro','Meiryo',sans-serif; font-size: 16px; font-style: normal; font-variant: normal; font-weight: 400; letter-spacing: normal; orphans: 2; overflow-wrap: break-word; text-align: left; text-decoration: none; text-indent: 0px; text-transform: none; -webkit-text-stroke-width: 0px; white-space: normal; word-spacing: 0px;">$\triangle \mathrm{ BEC }$ ， $\triangle \mathrm{ CED }$ ， $\triangle \mathrm{ DEA }$ の4つに分割して $S$ を求める。</span>




$S= \triangle \mathrm{ AEB } + \triangle \mathrm{ BEC } + \triangle \mathrm{ CED } + \triangle \mathrm{ DEA }$




$= \displaystyle \frac{1}{2} \cdot \mathrm{ AE } \cdot \mathrm{ BE } \cdot \sin (180^{ \circ } - \alpha ) + \frac{1}{2} \cdot \mathrm{ BE } \cdot \mathrm{ CE } \cdot \sin \alpha$




$\displaystyle +\frac{1}{2} \cdot \mathrm{ CE } \cdot \mathrm{ DE } \cdot \sin (180^{ \circ } - \alpha )+ \frac{1}{2} \cdot \mathrm{ DE } \cdot \mathrm{ AE } \cdot \sin \alpha$




$\sin (180^{ \circ } - \alpha ) = \sin \alpha$ であるから，




$\displaystyle S= \frac{1}{2} \cdot \mathrm{ AE } \cdot \mathrm{ BE } \cdot \sin \alpha + \frac{1}{2} \cdot \mathrm{ BE } \cdot \mathrm{ CE } \cdot \sin \alpha+ \frac{1}{2} \cdot \mathrm{ CE } \cdot \mathrm{ DE } \cdot \sin \alpha + \frac{1}{2} \cdot \mathrm{ DE } \cdot \mathrm{ AE } \cdot \sin \alpha$




$\displaystyle =\frac{1}{2} \cdot ( \mathrm{ AE } + \mathrm{ CE } ) \cdot \mathrm{ BE } \cdot \sin \alpha + \frac{1}{2} \cdot ( \mathrm{ AE } + \mathrm{ CE } ) \cdot \mathrm{ DE } \cdot \sin \alpha$




$\displaystyle = \frac{1}{2} \cdot \mathrm{ AC } \cdot \mathrm{ BE } \cdot \sin \alpha + \frac{1}{2} \cdot \mathrm{ AC } \cdot \mathrm{ DE } \cdot \sin \alpha$




$\displaystyle = \frac{1}{2} \cdot \mathrm{ AC } \cdot ( \mathrm{ BE } \cdot  \mathrm{ DE } ) \cdot \sin \alpha$




$\displaystyle = \frac{1}{2} \cdot \mathrm{ AC } \cdot \mathrm{ BD } \cdot \sin \alpha$


</div>
