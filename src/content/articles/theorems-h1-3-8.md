---
title: "【定理・公式・証明】高校数学定理・公式 – 数学Ⅰ – ヘロンの公式"
status: "published"
published_at: "2020-04-22 23:14:44"
path: "/theorems-proof-of-high-school-math/theorems-h1-2-1/theorems-h1-3-8/"
---

## ヘロンの公式


<div class="info-box">三角形 $\mathrm{ ABC }$ の面積を $S$ とすると， $\displaystyle s= \frac{a+b+c}{2}$



として，




$S= \sqrt{s(s-a)(s-b)(s-c)}$


</div>
<div class="blank-box bb-green">証明



三角形 $\mathrm{ ABC }$ に対して，余弦定理を用いると




$\displaystyle c^2=a^2+b^2-2ab \cos C \Leftrightarrow \cos C = \frac{a^2+b^2-c^2}{2ab}$




$\displaystyle s= \frac{a+b+c}{2}$ すなわち $a+b+c=2s$ とし，三角形 $\mathrm{ ABC }$ の面積を $S$ とすると，




$\displaystyle S= \frac{1}{2} ab \sin C = \frac{1}{2} ab \sqrt{1- \cos ^2 C} = \frac{1}{2} \sqrt{a^2b^2-a^2b^2 \left( \frac{a^2+b^2-c^2}{2ab} \right) ^2}$




$\displaystyle = \frac{1}{4} \sqrt{4a^2b^2-(a^2+b^2-c^2)^2}$




$\displaystyle =\frac{1}{4} \sqrt{ \left\{ 2ab-(a^2+b^2-c^2) \right\} \left\{2ab+(a^2+b^2-c^2) \right\}}$




$\displaystyle =\frac{1}{4} \sqrt{ \left\{ c^2-(a^2-2ab+b^2) \right\} \left\{ (a^2+2ab+b^2)-c^2 \right\}}$




$\displaystyle =\frac{1}{4} \sqrt{ \left\{ c^2- (a-b)^2 \right\} \left\{ (a+b)^2 -c^2 \right\}}$




$\displaystyle =\frac{1}{4} \sqrt{(c+a-b)(c-a+b)(a+b+c)(a+b-c)}$




$\displaystyle =\frac{1}{4} \sqrt{(a+b+c-2b)(a+b+c-2a)(a+b+c)(a+b+c-2c)}$




$\displaystyle =\frac{1}{4} \sqrt{(2s-2b)(2s-2a) \cdot 2s \cdot (2s-2c)}$




$= \sqrt{s(s-a)(s-b)(s-c)}$


</div>
