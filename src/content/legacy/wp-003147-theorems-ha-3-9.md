---
title: "【定理・公式・証明】高校数学定理・公式 – 数学A – 合同式"
wp_id: 3147
content_type: "page"
status: "publish"
published_at: "2020-05-26 09:11:56"
wp_date: "2020-05-26 09:11:56"
modified_at: "2020-05-26 09:39:43"
legacy_url: "http://mathrao.com/theorems-proof-of-high-school-math/theorems-ha-3-9/"
legacy_path: "/theorems-proof-of-high-school-math/theorems-ha-3-9/"
legacy_slug: "theorems-ha-3-9"
former_slugs: []
parent_wp_id: 2564
parent_title: "【定理・公式・証明】高校数学定理・公式一覧"
hierarchy: ["【定理・公式・証明】高校数学定理・公式一覧", "【定理・公式・証明】高校数学定理・公式 – 数学A – 合同式"]
category: []
tags: []
mathrao_section: "定理・公式・証明"
mathrao_grade: null
mathrao_course: "数学A"
source_content_sha256: "09ab0a3ec135cf0198f01c8deeda0e1134c947ea9b393eac08917fc21bc4798e"
---

## 合同式


<div class="info-box">$a,b$ は整数， $m$ は正の整数とする。 $a-b$ が $m$ の倍数であるとき， $a \equiv b ( \mathrm{ mod } \ m)$ と表す。このとき，次が成り立つ。



[Ⅰ] $a \equiv a( \mathrm{ mod } \ m)$




[Ⅱ] $a \equiv b ( \mathrm{ mod } \ m) $ ならば， $b \equiv a( \mathrm{ mod } \ m)$




[Ⅲ] $a \equiv b( \mathrm{ mod } \ m)$ ， $b \equiv c( \mathrm{ mod } \ m)$ ならば， $a \equiv c( \mathrm{ mod } \ m)$


</div>
<div class="blank-box bb-green">証明



[Ⅰ] $a-a=0=(m の倍数)$




であるから，




$a \equiv a( \mathrm{ mod } \ m)$




[Ⅱ] $a \equiv b( \mathrm{ mod } \ m)$ より，




$a-b=mk$ ( $k$ は整数)




このとき，




$b-a=m \cdot (-k) =(mの倍数)$




であるから，




$b \equiv a ( \mathrm{ mod } \ m)$




[Ⅲ] $a \equiv b ( \mathrm{ mod } \ m),b \equiv c ( \mathrm{ mod } \ m)$ より，




$\begin{eqnarray} \left \{ \begin{array}{l} a-b=mk \\ b-c=ml \end{array} \right. \end{eqnarray}$ ( $k,l$ は整数)




2式の和をとり，




$a-c=m(k+l)=(m の倍数)$




よって，




$a \equiv c ( \mathrm{ mod } \ m)$


</div>


&nbsp;




## 合同式の性質


<div class="info-box">$a,b,c,d$ は整数， $m$ は正の整数とする。 $a \equiv b( \mathrm{ mod } \ m)$ ， $c \equiv d ( \mathrm{ mod } \ m)$ のとき，



[Ⅰ] $a+c \equiv b+d( \mathrm{ mod } \ m)$




[Ⅱ] $a-c \equiv b-d( \mathrm{ mod } \ m)$




[Ⅲ] $ac \equiv bd ( \mathrm{ mod } \ m)$




[Ⅳ] $a^n \equiv b^n ( \mathrm{ mod } \ m)$ ( $n$ は正の整数)


</div>
<div class="blank-box bb-green">証明



$a \equiv b ( \mathrm{ mod } \ m)$ ， $c \equiv d( \mathrm{ mod } \ m)$ より， $a-b=mk$ ， $c-d=ml$ であるから，




$a=ml+b$ ， $c=ml+d$ ( $k,l$ は整数)




[Ⅰ] $(a-c)-(b-d)=(mk+b+ml+d)-(b+d)=m(k+l)=(m の倍数)$ であるから， $a+c \equiv b+d( \mathrm{ mod } \ m)$ である。




[Ⅱ] $(a-c)-(b-d)= \{ mk+b-(ml+d) \} -(b-d)=m(k-l)= (m の倍数)$ であるから， $a-c \equiv b-d( \mathrm{ mod } \ m)$ である。




[Ⅲ] $ac-bd=(mk+b)(ml+d)-bd=m(mkl+dk+bl)=(m の倍数)$ であるから， $ac \equiv bd( \mathrm{ mod } \ m)$ である。




[Ⅳ] $a^n \equiv b^n ( \mathrm{ mod } \ m)$ ( $n$ は正の整数)




が成り立つことを，数学的帰納法で証明する。




(i) $n=1$ のとき， $a \equiv b( \mathrm{ mod } \ m)$ より，(※)は成立。




(ii) $n=k$ のとき，(※)が成り立つこと，すなわち $a^k \equiv b^k( \mathrm{ mod } \ m)$ を仮定する。




これと $a \equiv b( \mathrm{ mod } \ m$ より，[Ⅲ]から，




$a^k \cdot a \equiv b^k \cdot b( \mathrm{ mod } \ m)$ すなわち $a^{k+1} \equiv b^{k+1}( \mathrm{ mod } \ m)$




したがって， $n=k+1$ のときも(※)は成り立つ。




以上，(i)，(ii)より，すべての正の整数 $n$ において，(※)は成り立つ。


</div>
