---
title: "【定義・定理・公式】高校数学基本事項 - 数学B - 【補足】偏差値の求め方"
wp_id: 1112
content_type: "page"
status: "publish"
published_at: "2018-10-22 12:51:14"
wp_date: "2018-10-22 12:51:14"
modified_at: "2018-10-22 12:51:14"
legacy_url: "http://mathrao.com/basics-of-high-school-math/basics-hb-4-5/"
legacy_path: "/basics-of-high-school-math/basics-hb-4-5/"
legacy_slug: "basics-hb-4-5"
former_slugs: []
parent_wp_id: 448
parent_title: "【定義・定理・公式】高校数学基本事項一覧"
hierarchy: ["【定義・定理・公式】高校数学基本事項一覧", "【定義・定理・公式】高校数学基本事項 - 数学B - 【補足】偏差値の求め方"]
category: []
tags: []
mathrao_section: "高校数学"
mathrao_grade: null
mathrao_course: "数学B"
source_content_sha256: "7e9a6c69b9a8dcd330d82bc07b7a57f9117bb7e34ebef9be20377f22a3d240f3"
---

## 確率変数の変換1




期待値 $m=E(X)$，標準偏差 $\sigma=\sigma(X)$ である確率変数 $X$ を $Y=\displaystyle\frac{X-m}{\sigma}$ すなわち $Y=\displaystyle\frac{1}{\sigma}X-\frac{m}{\sigma}$ で変換する。


<p style="padding-left: 30px;">期待値：$\displaystyle{E(Y)=E\left(\frac{1}{\sigma}X-\frac{m}{\sigma}\right)=\frac{1}{\sigma}E(X)-\frac{m}{\sigma}=\frac{1}{\sigma}\cdot m-\frac{m}{\sigma}=0}$</p>
<p style="padding-left: 30px;">標準偏差：$\displaystyle{\sigma(Y)=\sqrt{V(Y)}=\sqrt{V\left(\frac{1}{\sigma}X-\frac{m}{\sigma}\right)}=\sqrt{\left(\frac{1}{\sigma}\right)^2V(X)}=\left|\frac{1}{\sigma}\right|\sqrt{V(X)}=\frac{1}{\sigma}\cdot\sigma=1}$</p>


&nbsp;




## 確率変数の変換2




期待値 $m=E(X)$，標準偏差 $\sigma=\sigma(X)$ である確率変数 $X$ を期待値 $50$，標準偏差 $10$ の確率変数 $Z$ に変換する。


<p style="padding-left: 30px;">$Z=aX+b$ とおくと</p>
<p style="padding-left: 60px;">$E(Z)=aE(X)+b=am+b$</p>
<p style="padding-left: 60px;">$\sigma(Z)=|a|\sigma(X)=a\sigma$</p>
<p style="padding-left: 30px;">$am+b=50$，$a\sigma=10$ より $a=\displaystyle\frac{10}{\sigma}$，$b=-\displaystyle\frac{10}{\sigma}m+50$ であるから</p>
<p style="padding-left: 60px;">$Z=\displaystyle\frac{10(X-m)}{\sigma}+50$</p>


&nbsp;




## 偏差値




【定義】




<strong>偏差値</strong>




テストなどの得点を，平均点 $50$，標準偏差 $10$ の変量で表したもの，すなわち


<p style="padding-left: 30px;">$Z=\displaystyle\frac{10(X-m)}{\sigma}+50$</p>


で変換した値を偏差値という。




&nbsp;




## 偏差値の特徴




平均点や標準偏差が異なるテストでも偏差値を比較することができる。そして，得点分布が正規分布になる場合，偏差値と得点上位から何%にあるかの対応が下表のようになり，仮に，100人が受験した試験におけるA君の偏差値が60ならば，A君は上位から約16人の集団に入ることが分かる。


<table style="border-collapse: collapse; width: 100%; height: 63px;" border="1">
<tbody>
<tr style="height: 63px;">
<td style="width: 100%; height: 63px;">$\begin{array}{c|ccccccccccccccccccccc} 偏差値 &amp; 75 &amp; … &amp; 70 &amp; … &amp; 65 &amp; … &amp; 60 &amp; … &amp; 55 &amp; … &amp; 50 &amp; … &amp; 45 &amp; … &amp; 40 &amp; … &amp; 35 &amp; … &amp; 30 &amp; … &amp; 25 \\ \hline ％ &amp; 0.7 &amp; &amp; 2.3 &amp; &amp; 6.7 &amp; &amp; 15.9 &amp; &amp; 30.9 &amp; &amp; 50.0 &amp; &amp; 69.1 &amp; &amp; 84.1 &amp; &amp; 93.3 &amp; &amp; 97.7 &amp; &amp; 99.3 \end{array}$</td>
</tr>
</tbody>
</table>


&nbsp;
