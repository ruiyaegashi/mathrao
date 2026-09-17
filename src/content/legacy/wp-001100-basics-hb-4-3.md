---
title: "【定義・定理・公式】高校数学基本事項 - 数学B - 正規分布"
wp_id: 1100
content_type: "page"
status: "publish"
published_at: "2018-10-21 00:18:13"
wp_date: "2018-10-21 00:18:13"
modified_at: "2018-10-21 00:18:13"
legacy_url: "http://mathrao.com/basics-of-high-school-math/basics-hb-4-3/"
legacy_path: "/basics-of-high-school-math/basics-hb-4-3/"
legacy_slug: "basics-hb-4-3"
former_slugs: []
parent_wp_id: 448
parent_title: "【定義・定理・公式】高校数学基本事項一覧"
hierarchy: ["【定義・定理・公式】高校数学基本事項一覧", "【定義・定理・公式】高校数学基本事項 - 数学B - 正規分布"]
category: []
tags: []
mathrao_section: "高校数学"
mathrao_grade: null
mathrao_course: "数学B"
source_content_sha256: "4055743cdba374de069f24d14054f4f6cdd4282184e340029e5f91321e62ad78"
---

## 連続型確率変数




【定義】




<strong>連続型確率変数</strong>：連続した値を取る確率変数




<strong>離散型確率変数</strong>：とびとびの値をとる確率変数




<strong>分布曲線</strong>：連続型確率変数 $X$ に対応させた曲線




<strong>確率密度関数</strong>：分布曲線 $y=f(x)$ における $f(x)$




<strong>連続型確率変数の期待値・分散・標準偏差</strong>




連続型確率変数 $X$ のとる値の範囲が $\alpha\leqq X\leqq\beta$ で，その確率密度関数が $f(x)$ であるとき，$X$ の期待値 $m=E(X)$，分散 $V(X)$，標準偏差 $\sigma(X)$ を次の式で定める。


<ul>
	<li>$m=E(X)=\int_{\alpha}^{\beta}xf(x)dx$</li>
	<li>$V(X)=\int_{\alpha}^{\beta}(x-m)^2f(x)dx$</li>
	<li>$\sigma(X)=\sqrt{V(X)}=\sqrt{\int_{\alpha}^{\beta}(x-m)^2f(x)dx}$</li>
</ul>


【定理】




<strong>確率密度関数の性質</strong>




確率密度関数 $f(x)$ について


<ul>
	<li>常に $f(x)\geqq0$</li>
	<li>$P(a\leqq X\leqq b)=\int_{a}^{b}f(x)dx$</li>
	<li>$X$ のとる値の範囲が $\alpha\leqq X\leqq\beta$ のとき $\int_{\alpha}^{\beta}f(x)dx=1$</li>
</ul>


&nbsp;




## 正規分布




【定義】




<strong>正規分布曲線・正規分布</strong>




$m$ が実数，$\sigma$ が正の実数，$e$ が自然対数の底のときの曲線


<p style="padding-left: 30px;">$y=f(x)=\displaystyle\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x-m)^2}{2\sigma^2}}$</p>


を<strong>正規分布曲線</strong>といい，連続型確率変数 $X$ の確率密度関数が正規分布曲線の関数 $f(x)$ のとき，$X$ の確率分布を<strong>正規分布</strong>という。




このとき，$X$ は<strong>正規分布</strong> $\boldsymbol{N(m,\sigma^2)}$ に従うといい，期待値 $E(X)$ と標準偏差 $\sigma(X)$ は


<p style="padding-left: 30px;">$E(X)=m$</p>
<p style="padding-left: 30px;">$\sigma(X)=\sigma$</p>


<strong>標準正規分布</strong>




正規分布 $N(0,1)$ を<strong>標準正規分布</strong>という。




確率変数 $X$ が正規分布 $N(m,\sigma^2)$ に従うとき，$Z=\frac{X-m}{\sigma}$ とおくと，確率変数 $Z$ は標準正規分布 $N(0,1)$ に従う。




標準正規分布 $N(0,1)$ に従う確率変数 $Z$ の確率密度関数 $f(z) は


<p style="padding-left: 30px;">$f(z)=\displaystyle\frac{1}{\sqrt{2\pi}}e^{-\frac{z^2}{2}}$</p>


また，一般に確率 $P(0\leqq Z\leqq u)$ を $P(0\leqq Z\leqq u)=p(u)$ と表す。




<strong>標準化</strong>：正規分布を標準正規分布に直すこと




【定理】




<strong>正規分布に従う確率変数の分布曲線の性質</strong>




確率変数 $X$ が正規分布 $N(m,\sigma^2)$ に従うとき，$X$ の分布曲線 $y=f(x)$ は次のような性質をもつ。


<ul>
	<li>直線 $x=m$ に関して対称であり，$y$ は $x=m$ で最大値を取る。</li>
	<li>$x$ 軸を漸近線とし，$x$ 軸と分布曲線の間の面積は1である。</li>
	<li>標準偏差 $\sigma$ が大きくなると曲線の山は低くなって横に広がる。</li>
	<li>標準偏差 $\sigma$ が小さくなると曲線の山は高くなって直線 $x=m$ の周りに集まる。</li>
</ul>


&nbsp;




## 二項分布と正規分布




$q=1-p$ とする


<ul>
	<li>二項分布 $B(n,p)$ に従う確率変数 $X$ は，$n$ が大きいとき，近似的に正規分布 $N(np,npq)$ に従う。</li>
	<li>二項分布 $B(n,p)$ に従う確率変数 $X$ に対し，$Z=\frac{X-np}{\sqrt{npq}}$ は，$n$ が大きいとき，近似的に標準正規分布 $N(0,1)$ に従う。</li>
</ul>
