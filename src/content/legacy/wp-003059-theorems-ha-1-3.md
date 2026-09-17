---
title: "【定理・公式・証明】高校数学定理・公式 – 数学A – 組み合わせ・ ${}_n \\mathrm{ C }_k$ の性質"
wp_id: 3059
content_type: "page"
status: "publish"
published_at: "2020-05-10 19:22:53"
wp_date: "2020-05-10 19:22:53"
modified_at: "2020-05-10 19:22:53"
legacy_url: "http://mathrao.com/theorems-proof-of-high-school-math/theorems-ha-1-3/"
legacy_path: "/theorems-proof-of-high-school-math/theorems-ha-1-3/"
legacy_slug: "theorems-ha-1-3"
former_slugs: []
parent_wp_id: 2564
parent_title: "【定理・公式・証明】高校数学定理・公式一覧"
hierarchy: ["【定理・公式・証明】高校数学定理・公式一覧", "【定理・公式・証明】高校数学定理・公式 – 数学A – 組み合わせ・ ${}_n \\mathrm{ C }_k$ の性質"]
category: []
tags: []
mathrao_section: "定理・公式・証明"
mathrao_grade: null
mathrao_course: "数学A"
source_content_sha256: "d3bf90a496938d763f1a15dd10eecc7e18b419d9c1ed68aaf30848c9362dd229"
---

## 組合せ


<div class="info-box">異なる $n$ 個から $k$ 個を選ぶ組合せの総数は，



$\displaystyle _{n} C_{k} = \frac{_{k} P_{k}}{k!}$ (通り)


</div>


[overrule]説明(組合せは，順列との比を利用する！)




$1,2,3,4,5$ の異なる5つから3つを選ぶ組合せを考える。このとき，重要なのは




①：「 $1,2,3,4,5$ から異なる3つを並べる順列」と




②：「 $1,2,3,4,5$ から異なる3つを選ぶ組合せ」との『比』




を考えることである。




このように，①と②の『比』は $3!:1$ である。




①の順列が $_{5} P_{3}$ あるのに対して，②の組合せを $X$ 通りとすると，右のように $X$ は， $_{5} P_{3}$ を $3!$ で割ればよいことになる。このとき，5個から3個を取る組合せ( $X$ )を $_{5} C_{3}$ と書く。




このように，異なる $n$ 個から $k$ 個を選ぶ組合せは，




$\displaystyle _{n} C_{k} = \frac{_{n} C_{k}}{k!}$ (通り)[/overrule]




&nbsp;




## $_{n} C_{k}$ の性質①( $_{n} C_{k} = _{n} C_{n-k}$


<div class="info-box">$n$ は自然数， $k$ は0以上の整数とする。 $0 \leqq k \leqq n$ において，



(Ⅰ) $\displaystyle _{n} C_{k} = \frac{n!}{k!(n-k)!}$




(Ⅱ) $_{n} C_{k} = _{n} C_{n-k}$


</div>


[overrule]説明




(Ⅰ) $_{5} C_{2}$ を具体的に考えてみると，




$\displaystyle _{5} C_{2} = \frac{5 \cdot 3}{2 \cdot 1} = \frac{5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}{2! \cdot 3 \cdot 2 \cdot 1} = \frac{5!}{2!(5-2)!}$




このように $_{n} C_{k}$ は，




$\displaystyle _{n} C_{k}= \frac{n(n-1) \cdots (n-k+1)}{k \cdot (k-1) \cdots 2 \cdot 1}$




$\displaystyle = \frac{n(n-1) \cdots (n-k+1) \cdots (n-k) \cdots 2 \cdot 1}{k! \cdot (n-k) \cdots 2 \cdot 1}$




$\displaystyle = \frac{n!}{k!(n-k)!}$




となる。




(Ⅱ) $_{5} C_{3}$ と $_{5} C_{2}$ を具体的に考えてみると，




$\displaystyle _{5} C_{3} = \frac{5!}{3!2!} =10$




$\displaystyle _{5} C_{5-3} = _{5} C_{2} = \frac{5!}{2!3!} =10$




このように， $_{n} C_{k}$ は，




$\displaystyle _{n} C_{k} = \frac{n!}{k! \cdot (n-k)!}$




$\displaystyle = \frac{n!}{(n-k)! \cdot k!}$




$= _{n} C_{n-k}$




となる。[/overrule]




&nbsp;




## $_{n} C_{k}$ の性質② ( $k \cdot _{n} C_{k} =n \cdot _{n-1} C_{k-1}$ )


<div class="info-box">$n$ は2以上の整数， $1 \leqq k \leqq n$ において，



$k \cdot _{n} C_{k} =n \cdot _{n-1} C_{k-1}$


</div>


証明




$\displaystyle k \cdot _{n} C_{k} =k \cdot \frac{n!}{k! \cdot (n-k)!}$




$\displaystyle =k \cdot \frac{n \cdot (n-1)!}{k \cdot (k-1)! \cdot (n-k)!}$




$\displaystyle = \frac{n \cdot (n-1)!}{(k-1)!(n-k)!}$




$\displaystyle =n \cdot \frac{(n-1)!}{(k-1)! \cdot \{ (n-1)-(k-1) \}!}$




$n \cdot _{n-1} C_{k-1}$




&nbsp;




## $_{n} C_{k}$ の性質③( $_{n} C_{k} = _{n-1} C_{k-1} + _{n-1} C_{k}$ )


<div class="info-box">$n$ は2以上の整数， $k$ は $1 \leqq k \leqq n-1$ を満たす整数とするとき，



$_{n} C_{k} = _{n-1} C_{k-1} + _{n-1} C_{k}$


</div>
<div class="blank-box bb-green">証明



$\displaystyle _{n-1} C_{k-1} + _{n-1} C_{k} = \frac{(n-1)!}{(k-1)! \{ (n-1)-(k-1) \} !} + \frac{(n-1)!}{k! \{ (n-1) -k \} !}$




$\displaystyle = \frac{(n-1)!}{(k-1)!(n-k)!} + \frac{(n-1)!}{k!(n-k-1)!}$




$\displaystyle = \frac{k(n-1)!}{k(k-1)!(n-k)!} \frac{(n-1)!(n-k)}{k!(n-k)(n-k-1)!}$




$\displaystyle = \frac{k(n-1)!}{k!(n-k)!} + \frac{(n-1)!(n-k)}{k!(n-k)!}$




$\displaystyle = \frac{(n-1)!(k-n-k)}{k!(n-k)!}$




$\displaystyle = \frac{n(n-1)!}{k!(n-k)!}$




$\displaystyle = \frac{n!}{k!(n-k)!}$




$= _{n} C_{k}$


</div>
