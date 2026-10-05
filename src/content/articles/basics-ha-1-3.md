---
title: "【定義・定理・公式】高校数学基本事項 - 数学A - 順列，組合せ"
status: "published"
published_at: "2018-09-23 18:08:16"
path: "/basics-of-high-school-math/basics-ha-1-3/"
---

## 円順列，数珠順列，重複順列




【定義】




<strong>円順列</strong>：ものを円形に並べる順列


<p style="padding-left: 30px;">※異なる $n$ 個の円順列の総数は $\displaystyle \frac{{}_n \mathrm{ P }_n}{n}=(n-1)!$</p>


<strong>数珠順列</strong>：ものを円形に並べ，回転または裏返して一致するものは同じものと見る順列


<p style="padding-left: 30px;">※異なる $n$ 個の数珠順列の総数は $\displaystyle \frac{(n-1)!}{2}$</p>


<strong>$\boldsymbol{n}$ 個から $\boldsymbol{r}$ 個取る重複順列</strong>：異なる $n$ 個のものから，重複を許して $r$ 個を取り出して並べる順列


<p style="padding-left: 30px;">※$\boldsymbol{n}$ 個から $\boldsymbol{r}$ 個取る重複順列の総数は $n^r$</p>







## 組合せ




【定義】




<strong>組合せ</strong>：ものを取り出す順序を無視した組の1つ1つのこと




<strong>$\boldsymbol{n}$ 個から $\boldsymbol{r}$ 個取る組合せ</strong>：異なる $n$ 個のものから異なる $r$ 個を取り出して作る組合せ


<p style="padding-left: 30px;">※ $\boldsymbol{n}$ 個から $\boldsymbol{r}$ 個取る組合せの総数を ${}_n \mathrm{ C }_r$ で表す</p>
<p style="padding-left: 60px;">${}_n \mathrm{ C }_r= \displaystyle \frac{{}_n \mathrm{ P }_r}{r!} = \frac{n(n-1)(n-2)……(n-r+1)}{r(r-1)(r-2)……3 \cdot 2 \cdot 1} = \frac{n!}{r!(n-r)!}$ ( $r \leqq n$ )</p>
<p style="padding-left: 60px;">${}_n \mathrm{ C }_n=1$</p>
<p style="padding-left: 60px;">${}_n \mathrm{ C }_1=n$</p>
<p style="padding-left: 60px;">${}_n \mathrm{ C }_0=1$</p>
<p style="padding-left: 30px;">※ ${}_n \mathrm{ C }_r$ の性質</p>
<p style="padding-left: 60px;">${}_n \mathrm{ C }_r={}_n \mathrm{ C }_{n-r}$ ただし $1 \leqq r \leqq n$</p>
<p style="padding-left: 60px;">${}_n \mathrm{ C }_r={}_{n-1} \mathrm{ C }_{r-1} + {}_{n-1} \mathrm{ C }_r$ ただし $1 \leqq r \leqq n-1$，$n \geqq 2$</p>







## 同じものを含む順列




aが $p$ 個，bが $q$ 個，cが $r$ 個あるとき，それら全部を1列に並べる順列の総数は


<p style="padding-left: 30px;">${}_n \mathrm{ C }_p \times {}_{n-p} \mathrm{ C }_q = \displaystyle \frac{n!}{p!q!r!}$ ただし $p+q+r=n$</p>







## 重複組合せ




【定義】




<strong>$\boldsymbol{n}$ 個から $\boldsymbol{r}$ 個取る重複組合せ</strong>：異なる $n$ 個のものから，重複を許して異なる $r$ 個を取り出して作る組合せ


<p style="padding-left: 30px;">※ $\boldsymbol{n}$ 個から $\boldsymbol{r}$ 個取る重複組合せの総数を ${}_n \mathrm{ H }_r$ で表す</p>
<p style="padding-left: 60px;">${}_n \mathrm{ H }_r = {}_{n+r-1} \mathrm{ C }_r$</p>
