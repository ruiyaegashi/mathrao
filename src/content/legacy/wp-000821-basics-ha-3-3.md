---
title: "【定義・定理・公式】高校数学基本事項 - 数学A - 互除法と整数の性質の活用"
wp_id: 821
content_type: "page"
status: "publish"
published_at: "2018-09-24 03:40:29"
wp_date: "2018-09-24 03:40:29"
modified_at: "2019-05-27 17:22:31"
legacy_url: "http://mathrao.com/basics-of-high-school-math/basics-ha-3-3/"
legacy_path: "/basics-of-high-school-math/basics-ha-3-3/"
legacy_slug: "basics-ha-3-3"
former_slugs: []
parent_wp_id: 448
parent_title: "【定義・定理・公式】高校数学基本事項一覧"
hierarchy: ["【定義・定理・公式】高校数学基本事項一覧", "【定義・定理・公式】高校数学基本事項 - 数学A - 互除法と整数の性質の活用"]
category: []
tags: []
mathrao_section: "高校数学"
mathrao_grade: null
mathrao_course: "数学A"
source_content_sha256: "fb6d48148bb9e94c22f1d7c188dc0473e8eec287ae63c750774436efac01a96c"
---

## ユークリッドの互除法




### 割り算と最大公約数




自然数 $a$，$b$ について，$a$ を $b$ で割ったときの余りを $r$ とすると，$a$ と $b$ の最大公約数は，$b$ と $r$ の最大公約数に等しい。




### ユークリッドの互除法




整数 $a$，$b$ の最大公約数を求めるには，次の手順を繰り返せば良い。この方法をユークリッドの互除法，または，単に互除法という。


<ol>
	<li>$a$ を $b$ で割ったときの余りを $r$ とする。</li>
	<li>$r=0$ ならば，$b$ が $a$ と $b$ の最大公約数である。<br />
$r&gt;0$ ならば，$a$ を $b$ で，$b$ を $r$ でおきかえて，1に戻る。</li>
</ol>


この手順を繰り返すと，余り $r$ が小さくなり，$r$ が0になって必ず終了する。




&nbsp;




## 1次不定方程式




【定理】




<strong>互いに素である整数の性質</strong>




2つの整数 $a$，$b$ が互いに素であるとき，整数 $c$ について $ax+by=c$ を満たす整数 $x$，$y$ が存在する。




【定義】




$a$，$b$，$c$ は整数の定数で，$a \neq 0$，$b \neq 0$ とする。$x$，$y$ の1次方程式 $ax+by=c$ を成り立たせる整数 $x$，$y$ の組を，この方程式の<strong>整数解</strong>という。この方程式の整数解を求めることを，<strong>1次不定方程式</strong>を解くという。


<p style="padding-left: 30px;">※2つの整数 $a$，$b$ が互いに素であるとき，方程式 $ax+by=c$ の整数解の1つを $x=p$，$y=q$ とすると，全ての整数解は $x=bk+p$，$y=-ak+q$ ( $k$ は整数) と表される。</p>


&nbsp;




## 分数と小数




【定義】




<strong>有限小数</strong>：小数第何位かで終わる小数




<strong>無限小数</strong>：小数部分が無限に続く小数




<strong>循環小数</strong>：無限小数のうち，ある位以下では数字の同じ並びが繰り返される小数




<strong>既約分数</strong>：分母と分子が整数で，分母と分子が互いに素である分数


<p style="padding-left: 30px;">※ $m$ を整数，$n$ を自然数とすると，分数 $\frac{m}{n}$ は整数，有限小数，循環小数のいずれかで表される。</p>
<p style="padding-left: 30px;">※整数でない既約分数 $\frac{m}{n}$ について次のことが成り立つ。</p>
<p style="padding-left: 60px;">分母 $n$ の素因数は2，5だけからなる $\Leftrightarrow$ $\frac{m}{n}$ は有限小数で表される</p>
<p style="padding-left: 60px;">分母 $n$ の素因数に2，5以外のものがある $\Leftrightarrow$ $\frac{m}{n}$ は循環小数で表される</p>


&nbsp;




## $n$ 進法




【定義】




<strong>底</strong>：位取りの基礎となる数




$\boldsymbol{n}$ <strong>進法</strong>：底を $n$ として数を表す記数法( $n$ は2以上の整数)




$\boldsymbol{n}$ <strong>進数</strong>：$n$ 進法で表された数


<p style="padding-left: 30px;">※$n$ 進数では，その数の右下に${}_{(n)}$ と書く。(10進数は省略する)</p>
<p style="padding-left: 30px;">※$n$ 進数の各位の数字は0以上 $n-1$ 以下の整数。</p>


&nbsp;




## $n$ 進法の位




……，$n^3$ の位，$n^2$ の位，$n^1$ の位，$n^0$，$\frac{1}{n^1}$ の位，$\frac{1}{n^2}$ の位，$\frac{1}{n^3}$ の位，……




&nbsp;




## 2進法の四則計算




2進法の四則計算では，次の計算が基本となる。


<ul>
	<li>足し算：$0+0=0$，$0+1=1$，$1+0=1$，$1+1=10$</li>
	<li>引き算：$0-0=0$，$1-0=1$，$1-1=0$，$10-1=1$</li>
	<li>掛け算：$0 \times 0=0$，$0 \times 1=0$，$1 \times 0=0$，$1 \times 1=1$</li>
</ul>


2進法の割り算は，10進法の割り算と同様に，掛け算と引き算を組み合わせて行う。




&nbsp;




&nbsp;
