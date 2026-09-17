---
title: "【定理・公式・証明】高校数学定理・公式 – 数学A – フェルマーの小定理"
wp_id: 3165
content_type: "page"
status: "publish"
published_at: "2020-05-28 12:48:49"
wp_date: "2020-05-28 12:48:49"
modified_at: "2020-05-28 12:48:49"
legacy_url: "http://mathrao.com/theorems-proof-of-high-school-math/theorems-ha-3-11/"
legacy_path: "/theorems-proof-of-high-school-math/theorems-ha-3-11/"
legacy_slug: "theorems-ha-3-11"
former_slugs: []
parent_wp_id: 2564
parent_title: "【定理・公式・証明】高校数学定理・公式一覧"
hierarchy: ["【定理・公式・証明】高校数学定理・公式一覧", "【定理・公式・証明】高校数学定理・公式 – 数学A – フェルマーの小定理"]
category: []
tags: []
mathrao_section: "定理・公式・証明"
mathrao_grade: null
mathrao_course: "数学A"
source_content_sha256: "61e7ba1b28799d05706fd7eba889836d4dd72f35e83a522f362da5885db43938"
---

## 【発展】フェルマーの小定理の準備①


<div class="info-box">$a$ と $p$ が互いに素な正の整数であるとき，集合



$\{a,2a,3a, \cdots (p-1)a,pa \}$




の各要素を $p$ で割った余りはすべて異なる。




(つまり，その余りの集合は $\{ 0,1,2,3, \cdots , p-1 \}$ となる)


</div>
<div class="blank-box bb-green">証明 背理法で示す



$p \geqq 2$ とする、




$a,2a,3a, \cdots ,(p-1)a,pa$




の中に， $p$ で割った余りが等しいものが存在すると仮定する。それを




$ka,la(1 \leqq l \lt k \leqq p)$




とすると， $ka-la$ すなわち $(k-l)a$ は， $p$ の倍数である。




一方， $0 \lt k-1 \lt p$ より $k-l$ は $p$ の倍数ではなく，また $a$ と $p$ は互いに素であるから， $a$ は $p$ の倍数ではない。これは， $(k-l)a$ が $p$ の倍数であることに矛盾。




したがって，




$a,2a,3a, \cdots ,(p-1)a,pa$




の中に， $p$ で割った余りが等しいものは存在しない。




整数を $p$ で割った余りは $0,1,2, \cdots ,p-1$ の $p$ 個のうちのいずれかであるから，




$a,2a,3a, \cdots , (p-1)a,pa$




をそれぞれ $p$ で割った余りの集合は，<br />
$\{ 0,1,2,3, \cdots , p-1 \}$




である。




特に， $pa$ を $p$ で割った余りは $0$ なので，<br />
$a,2a,3a, \cdots , (p-1)a$




をそれぞれ $p$ で割った余りの集合は， $\{ 1,2,3, \cdots , p-1 \}$ である。


</div>


&nbsp;




## 【発展】フェルマーの小定理の準備②


<div class="info-box">$p$ は素数， $a$ は正の整数とするとき，



$(a+1)^p \equiv a^p +1( \mathrm{ mod } \ p)$


</div>
<div class="blank-box bb-green">証明



二項定理より，




$(a+1)^p =a^p + {}_{p} C_{1} a^{p-1} \cdot 1+ {}_{p} C_{2} a^{p-2} \cdot 1^2 + cdots + {}_{p} C_{p-1} a \cdot 1^{p-1} +1^p$




であるから，




$\displaystyle ( a + 1 )^p - ( a^p + 1 ) = \sum_{r=1}^{p-1} {}_{p} C_{r} a^{ p - r }$




ここで，




$\displaystyle {}_{p} \mathrm{ C }_{r} = \frac{p!}{r!(p-r)!}$




より，




${}_{p} \mathrm{ C }_{r} r!(p-r)!=p!$




②より， ${}_{p} \mathrm{ C }_{r} r!(p-r)!$ は $p$ の倍数であり， $p$ は素数であるから， $r=1,2,3, \cdots ,p-1$ において， $r! , (p-r)!$ は $p$ の倍数ではない。これと $p$ が整数であることより，




${}_{p} \mathrm{ C }_{r}$ は $p$ の倍数　( $r=1,2, \cdots , p-1$ ) である。




よって， $\displaystyle \sum_{k=1}^{p-1} {}_{p} \mathrm{ C }_{r} a^{p-r}$ は $p$ の倍数であるから，①より，




$(a+1)^p -(a^p +1) =(p の倍数)$




したがって，




$(a+1)^p \equiv a^p +1 ( \mathrm{ mod } \ p)$


</div>


&nbsp;




## 【発展】フェルマーの小定理


<div class="info-box">$p$ は素数， $a$ は正の整数とするとき，



$a^p \equiv a \ ( \mathrm{ mod } \ p)$




(特に $a$ が $p$ の倍数でないとき， $a^{p-1} \equiv 1 \ ( \mathrm{ mod } \ p)$ )


</div>
<div class="blank-box bb-green">証明①



$a^p \equiv 1 \ ( \mathrm{ mod } \ p)$




が成り立つことを， $a$ に関する数学的帰納法で証明する。




(i) $a=1$ のとき




$1^p \equiv 1 \ ( \mathrm{ mod } \ p)$ より，(＊)は成り立つ。




(ii) $a=k(k \geqq 1)$ のとき




(＊)が成り立つこと，すなわち $k^p \equiv k \ (\mathrm{ mod } \ p)$ を仮定する。




フェルマーの小定理準備②より，




$(k+1)^p \equiv k^p +1 \ ( \mathrm{ mod } \ p)$




であり、帰納法の仮定より $k^p +1 \equiv k+1 \ ( \mathrm{ mod } \ p)$ であるから，




$(k+1)^p \equiv k+1 \ ( \mathrm{ mod } \ p)$




よって， $a=k+1$ のときも (＊)は成り立つ。




以上，(i)，(ii)より，任意の正の整数 $a$ において(＊)は成り立つ。




また，(＊)より




$a^p -a \equiv 0 \ ( \mathrm{ mod } \ p)$




$a(a^{p-1} -1) \equiv 0 \ ( \mathrm{ mod } \ p)$




であるから， $a$ が $p$ の倍数でないとき， $a^{p-1} -1$ は $p$ の倍数である。したがって，




$a^{p-1} \equiv 1 \ ( \mathrm{ mod } \ p)$


</div>
<div class="blank-box bb-green">証明②



$a$ は $p$ の倍数でないとする。集合 $A$ を，




$A= \{a,2a,3a, \cdots , (p-1)a \}$




とする。このとき，フェルマーの小定理の準備①より，集合 $A$ 要素それぞれを $p$ で割った余りの集合は， $B= \{ 1,2,3, \cdots , p-1 \}$ と一致する。




したがって，




$(集合Aのすべての要素の積) \equiv (集合Bのすべての要素の積)( \mathrm{ mod } \ p)$




であるから，




$a \times 2a \times 3a \times \cdots \times (p-1)a \equiv 1 \times 2 \times 3 \times \cdots \times (p-1)( \mathrm{ mod } \ p)$




$a^{p-1} \cdot (p-1)! \equiv (p-1)!( \mathrm{ mod } \ p)$




$(a^{p-1} -1) \cdot (p-1)! \equiv 0 \ ( \mathrm{ mod } \ p)$




$p$ は素数であるから， $(p-1)!$ と $p$ は互いに素であり，




$a^{p-1} -1 \equiv 0 \ ( \mathrm{ mod } \ p)$




$a^{p-1} \equiv 1 \ ( \mathrm{ mod } \ p)$




これと $a \equiv a \ ( \mathrm{ mod } \ p)$ より，




$a^{p-1} \cdot a \equiv 1 \cdot a \ ( \mathrm{ mod } \ p)$ すなわち $a^p \equiv a \ ( \mathrm{ mod } \ p)$


</div>
