---
title: "【定義・定理・公式】高校数学基本事項 - 数学Ⅲ - 定積分で表された関数"
status: "published"
published_at: "2018-10-25 13:39:27"
path: "/basics-of-high-school-math/basics-h3-7-6/"
---

## 定積分と和の極限(区分求積法)




関数 $f(x)$ が閉区間 $[a,b]$ で連続であるとき，この区間を $n$ 等分して両端と分点を順に $a=x_0,x_1,x_2,\cdots\cdots$，$x_n=b$ とし，$\frac{b-a}{n}=\Delta x$ とすると，




$x_k=a+k\Delta x$ で


<p style="padding-left: 30px;">$\displaystyle{\int_{a}^{b}f(x)dx=\lim_{n\to\infty}\sum_{k=0}^{n-1}f(x_k)\Delta x=\lim_{n\to\infty}\sum_{k=1}^{n}f(x_k)\Delta x}$</p>


特に，$a=0$，$b=1$ とすると，$\Delta x=\frac{1}{n}$，$x_k=\frac{k}{n}$ となり


<p style="padding-left: 30px;">$\displaystyle{\int_{0}^{1}f(x)dx=\lim_{n\to\infty}\frac{1}{n}\sum_{k=0}^{n-1}f(\frac{k}{n})=\lim_{n\to\infty}\frac{1}{n}\sum_{k=1}^{n}f(\frac{k}{n})}$</p>


が成り立つ。









## 定積分と不等式




区間 $[a,b]$ で $f(x)\geqq 0$ ならば


<p style="padding-left: 30px;">$\displaystyle\int_{a}^{b}f(x)dx\geqq 0$</p>


等号は，常に $f(x)=0$ であるときに限り成り立つ。




区間 $[a,b]$ で $f(x)\geqq g(x)$ ならば


<p style="padding-left: 30px;">$\displaystyle{\int_{a}^{b}f(x)dx\geqq\int_{a}^{b}g(x)dx}$</p>


等号は，常に $f(x)=g(x)$ であるときに限り成り立つ。
