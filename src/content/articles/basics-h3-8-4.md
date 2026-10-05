---
title: "【定義・定理・公式】高校数学基本事項 - 数学Ⅲ - 種々の量の計算"
status: "published"
published_at: "2018-10-25 14:40:38"
path: "/basics-of-high-school-math/basics-h3-8-4/"
---

## 速度と道のり




<strong>直線運動</strong>




数直線状を運動する点 $\mathrm{P}$ の速度 $v$ を時刻 $t$ の関数と見て $v=f(t)$ とする。また $t=a$ のときの $\mathrm{P}$ の座標を $k$ とする。


<ul>
	<li>$t=b$ における $\mathrm{P}$ の座標 $x$ は $x=k+\displaystyle\int_{a}^{b}f(t)dt$</li>
	<li>$t=a$ から $t=b$ までの $\mathrm{P}$ の位置の変化量 $s$ は $s=\displaystyle\int_{a}^{b}f(t)dt$</li>
	<li>$t=a$ から $t=b$ までの $\mathrm{P}$ の道のり $l$ は $l=\displaystyle\int_{a}^{b}|f(t)|dt$</li>
</ul>


<strong>平面運動</strong>




点 $\mathrm{P}$ が平面上の曲線 $y=f(t)$，$y=g(t)$ ( $t$ は時刻)上を動くとき$t=\alpha$ から $t=\beta$ までの間に点 $\mathrm{P}$ が移動した道のり $l$ は


<ul>
	<li>$\displaystyle{l=\int_{\alpha}^{\beta}|\vec{v}|dt=\int_{\alpha}^{\beta}\sqrt{\left(\frac{dx}{dt}\right)^2+\left(\frac{dy}{dt}\right)^2}dt}$</li>
</ul>







## 曲線の長さ




<strong>媒介変数</strong>




曲線 $x=f(t)$，$y=g(t)$ ( $\alpha\leqq x\leqq\beta$ )の長さ $L$ は


<ul>
	<li>$\displaystyle{L=\int_{\alpha}^{\beta}\sqrt{\left(\frac{dx}{dt}\right)^2+\left(\frac{dy}{dt}\right)^2}dt=\int_{\alpha}^{\beta}\sqrt{\{f'(t)\}^2+\{g'(t)\}^2}dt}$</li>
</ul>


<strong>直交座標</strong>


<ul>
	<li>$\displaystyle{L=\int_{a}^{b}\sqrt{1+\left(\frac{dy}{dx}\right)^2}dx=\int_{a}^{b}\sqrt{1+\{f'(x)\}^2}dx}$</li>
</ul>
