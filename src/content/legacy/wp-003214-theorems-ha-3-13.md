---
title: "【定理・公式・証明】高校数学定理・公式 – 数学A –  有限小数・既約分数を小数で表す"
wp_id: 3214
content_type: "page"
status: "publish"
published_at: "2020-06-09 11:30:41"
wp_date: "2020-06-09 11:30:41"
modified_at: "2020-06-09 11:30:41"
legacy_url: "http://mathrao.com/theorems-proof-of-high-school-math/theorems-ha-3-13/"
legacy_path: "/theorems-proof-of-high-school-math/theorems-ha-3-13/"
legacy_slug: "theorems-ha-3-13"
former_slugs: []
parent_wp_id: 2564
parent_title: "【定理・公式・証明】高校数学定理・公式一覧"
hierarchy: ["【定理・公式・証明】高校数学定理・公式一覧", "【定理・公式・証明】高校数学定理・公式 – 数学A –  有限小数・既約分数を小数で表す"]
category: []
tags: []
mathrao_section: "定理・公式・証明"
mathrao_grade: null
mathrao_course: "数学A"
source_content_sha256: "90561c8ea30daf22d49899d1f2ed1caff1165bb10349b122e23afeddabda8acb"
---

## 有限小数


<div class="info-box">$m$ は整数， $n$ は $m$ と互いに素な正の整数とするとき，



既約分数 $\displaystyle \frac{m}{n}$ が有限小数 $\Longleftrightarrow$ $n$ の持つ素因数は $2,5$ のみ


</div>


[overrule]説明




有限小数とは，小数点以下の桁数が有限の少数のことであり，




$\displaystyle 0.23= \frac{23}{100}$ ， $\displaystyle 0.1234= \frac{1234}{10000}$




のように，自然数 $k$ を用いて， $\displaystyle \frac{(整数)}{10^k}$ と表すことのできる数である。




$\displaystyle \frac{1}{2} = \frac{5}{10} =0.5$ ， $\displaystyle \frac{31}{50} = \frac{31}{2 \cdot 5^2} = \frac{62}{10^2} =0.62$




のように，分母の素因数が $2,5$ のみであるような分数は，分母，分子それぞれに適当に $2,5$ をかけることにより必ず $\displaystyle \frac{(整数)}{10^k}$ と表せるから，有限小数で表される。




逆に，既約分数 $\displaystyle \frac{m}{n}$ が有限小数で表されるとき，整数 $l$ を用いて，




$\displaystyle \frac{m}{n} = \frac{l}{10^k}$




と表せる。




これより，




$nl=10^k m$




であり， $n$ と $m$ は互いに素であるから， $10^k$ は $n$ の倍数である。よって，




$n$ のもつ素因数は $2,5$ のみ




である。[/overrule]




&nbsp;




## 既約分数を小数で表す


<div class="info-box">$m$ は整数， $n$ は $m$ と互いに素な正の整数とする。このとき，既約分数 $\displaystyle \frac{m}{n}$ は必ず有限小数または循環小数で表すことができる。</div>


[overrule]説明




小数点以下の桁数が有限でない小数を無限小数といい，そのうち，いくつかの数字の配列が繰り返されるものを循環小数という。例えば循環小数 $0.181818 \cdots$ は $0. \dot{1} \dot{8}$ と表す。一方，数字の配列に周期性がない無限小数を非循環小数という。




既約分数 $\displaystyle \frac{m}{n}$ において，有限小数で説明したとおり， $n$ の素因数が $2,5$ のみであるとき， $\displaystyle \frac{m}{n}$ は有限小数で表される。




$n$ が $2,5$ 以外の素因数をもつとき， $\displaystyle \frac{m}{n}$ は無限小数，特に循環小数で表される。これについて説明する。




$(自然数) \div (自然数)$ の計算において，途中で割り切れないときは，いずれ必ず




$(割る数) \gt (割られる数)$




となる，そしてこれ以降は0を繰り返し補って割り算を続け，同じ余りが再度現れたら，そこからは同じ計算の繰り返しとなる。




例えば， $\displaystyle \frac{31}{27}$ について考察する。 $31 \div 27$ は〈図1〉のような計算であり，4が再度現れたところから同じ計算の繰り返しとなる。これより商の部分も $148$ が繰り返され、 $\displaystyle \frac{31}{27}$ は $1. \dot{1} \dot{4} \dot{8}$ という循環小数で表される。




27で割り切れない数は，27で割った余りが




$1,2,3, \cdots 26$




のいずれかであるから，27と互いに素な正の整数 $m$ について， $\displaystyle \frac{m}{27}$ が無限小数で表されるとき， $m \div 27$ の筆算において，0を補いだしてから 27回以内に必ず同じ余りが再度現れる。ゆえに， $\displaystyle {m}{27}$ は循環小数で表される。




また， $m \lt 0$ であれば， $-m \gt 0$ より， $-m \div 27$ の筆算を行うことで同様に $\displaystyle \frac{m}{27} = - \frac{-m}{27}$ は循環小数で表される。




同様にして， $m$ が $n$ で割り切れないとき， $m$ を $n$ で割った余りは $1,2, \cdots , n-1$ のいずれかであるから， $m \div n$ の筆算において，0を補いだしてから $n$ 回以内に必ず同じ余りが再度現れる。それ以降は〈図1〉のように同じ計算の繰り返しとなるから， $\displaystyle \frac{m}{n}$ は循環小数で表されることが分かる。[/overrule]
