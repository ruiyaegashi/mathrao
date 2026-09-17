---
title: "【インスタント中高数学】第11講 【図形の計量】"
wp_id: 2535
content_type: "post"
status: "draft"
published_at: null
wp_date: "2019-07-10 17:54:40"
modified_at: "2019-07-10 17:54:40"
legacy_url: null
legacy_path: null
legacy_slug: "instant-jhmath-provisional-11"
former_slugs: []
parent_wp_id: null
parent_title: null
hierarchy: ["【インスタント中高数学】第11講 【図形の計量】"]
category: ["インスタント中高数学【草稿】"]
tags: []
mathrao_section: "インスタント中高数学"
mathrao_grade: null
mathrao_course: null
source_content_sha256: "e8d0c246d4acd46295554d058b14ecab01641687d729dd83404a4032888759e4"
---

## 図形の計量の基本事項


<div class="info-box">


【定義】




<strong>座標軸</strong>：各文字の値を示すための数直線




<strong>直交座標</strong> $\boldsymbol{(x,y)}$：平面上に2つの直交する座標軸を定めたとき，平面上の点の位置を表した2つの実数の組




<strong>座標平面</strong>：座標軸の定められた平面




<strong>第1象限</strong>：座標平面において， $x$ 座標， $y$ 座標がともに正の部分




<strong>第2象限</strong>：座標平面において， $x$ 座標が負， $y$ 座標が正の部分




<strong>第3象限</strong>：座標平面において， $x$ 座標， $y$ 座標がともに負の部分




<strong>第4象限</strong>：座標平面において， $x$ 座標が正， $y$ 座標が負の部分


<p style="padding-left: 40px;">※座標軸上の点はどの象限にも属さない。</p>
</div>


前の講では図形の性質から分かる辺の比をメインに学んだけど，この講ではもう1歩踏み込んで，具体的に長さや面積，体積を求める方法を学んでいくよ。




そのために，まずは座標平面を押さえておこう。




ここまでは基本的に扱う文字が1つだったから数直線で十分だったけど，平面図形を扱うには直線ではなく平面で考えなきゃいけないからね。




座標平面は平面上に2つの直交する座標軸を定めたもので，点をその座標軸に対応した値の組(左右，上下)で表す方法なんだ。




座標軸の交点を原点として，右に $3$ ，上に $5$ 移動した点を $(3,5)$ ，左に $3$ ，下に $5$ 移動した点を $(-3,-5)$ というように表すよ。




原点に対して右が正，左が負，というのは数直線と同じだけど，縦軸では上が正，下が負となる点に注意。




一般的には横軸を文字 $x$ に対応させた $x$ 軸，縦軸を同様に $y$ 軸とすることが多いんだけど，取り組む問題によっては扱う文字を軸にすることもあるよ。




次に，この講で一番よく使う図形である三角形の一般的な表記をまとめるよ。


<div class="blank-box bb-blue">


<strong>一般的な三角形の表記</strong>




一般的に，$\triangle \mathrm{ABC}$ において


<p style="padding-left: 30px;">辺 $\mathrm{BC}$ ， $\mathrm{CA}$ ， $\mathrm{AB}$ の長さをそれぞれ $a$ ， $b$ ， $c$</p>
<p style="padding-left: 30px;">$\angle \mathrm{A}$ ， $\angle \mathrm{B}$ ， $\angle \mathrm{C}$ の大きさをそれぞれ $A$ ， $B$ ， $C$</p>


と表す。


</div>


辺 $\mathrm{BC}$ は辺の名称で， $a$ は辺 $\mathrm{AB}$ の大きさ，$\angle \mathrm{A}$ は角の名称で， $A$ は $\angle \mathrm{A}$ の大きさを表すよ。




三角形の向かい合う辺と角の大きさを同じアルファベットで表すというように覚えておこう。




あくまで一番よく使われる表現方法というだけだから，自分がかくときに統一されていれば基本的には問題ないからね。




## 三平方の定理


<div class="info-box">


【定理】<strong>三平方の定理</strong>




直角三角形の直角を挟む2辺の長さを $a$，$b$，斜辺の長さを $c$ とすると，$a^2+b^2=c^2$ となる。




【定理】<strong>三平方の定理の逆</strong>




$\triangle \mathrm{ABC}$ の3辺の長さ $a$，$b$，$c$ の間に，$a^2+b^2=c^2$ の関係が成り立てば，$\angle \mathrm{C} = 90^{ \circ }$ である。


</div>


早速だけど，図形の計量で一番大事で一番よく使う定理「三平方の定理」を学んでいこう。




三平方の定理は君も知っているであろうピタゴラスという人(正確にはピタゴラスがリーダーをしていた団体)が発見した，すべての直角三角形で成り立つ定理なんだ。




高校の最後の最後まで使う定理だから使いこなせるようになろう。




定理の内容はとてもシンプルで， $\angle \mathrm{C} =90^{ \circ }$ の直角三角形では $a^2+b^2-c^2$ が成り立つというもの。




文字が3つの方程式とも考えられるから，直角三角形のうちの2辺の長さが分かれば，残りの1辺の長さも分かるんだ。




例えば，斜辺の長さが $13$ ，横の長さが $5$ の直角三角形の縦の長さは，


<p style="padding-left: 40px;">$a^2+5^2=13^2$</p>
<p style="padding-left: 40px;">$a^2=144$</p>
<p style="padding-left: 40px;">$a=12$ ( $\because 0&lt;a$ )</p>


というように求めることができる。




平面図形では辺の長さは正だから，平方根を考えるときに正のものだけが答えになるという点にも注意が必要だよ。




座標平面においても，横と縦の長さ，つまり，座標が分かれば，原点からの距離が求められるということ。




例えば，原点と，点 $(4,3)$ の距離は，横が $4$ ，縦が $3$ の直角三角形の斜辺の長さと考えられるから，


<p style="padding-left: 40px;">$c^2=4^2+3^2$</p>
<p style="padding-left: 40px;">$c^2=25$</p>
<p style="padding-left: 40px;">$c=5$ ( $\because 0&lt;c$ )</p>


となる。




原点以外の2点間の距離も，その2点を結んだ線分を斜辺とする直角三角形で考えれば求めることができるね。




以下は三平方の定理を活用することで求められるものの例だよ。


<ul>
	<li>正方形の対角線の長さや，三角形の高さ</li>
	<li>弦や接線の長さ</li>
	<li>座標が与えられた2点間の距離</li>
	<li>直方体の対角線の長さや，角錐，円錐の高さ</li>
</ul>


&nbsp;


<div class="blank-box bb-blue">


<strong>有名な直角三角形の3辺の長さの比</strong>


<ul>
	<li>$1:1: \sqrt{2} $：直角二等辺三角形</li>
	<li>$1:2: \sqrt{3} $：$30^{ \circ }$ ， $60^{ \circ }$ ， $90^{ \circ }$ の直角三角形</li>
	<li>$4:( \sqrt{6} + \sqrt{2} ):( \sqrt{6} - \sqrt{2} )$：$15^{ \circ }$ ， $75^{ \circ }$ ， $90^{ \circ }$ の直角三角形</li>
	<li>$3:4:5$</li>
	<li>$5:12:13$</li>
	<li>$7:24:25$</li>
	<li>$8:15:17$</li>
</ul>
</div>


&nbsp;




## 三角比




### 平面図形の三角比


<div class="info-box">


【定義】




$\angle \mathrm{C} =90^{ \circ }$ である直角三角形 $\mathrm{ABC}$ において，$\angle \mathrm{B} = \theta$ ( $0^{ \circ } &lt; \theta &lt; 180^{ \circ }$ )とすると


<ul>
	<li><strong>正弦</strong>(sine サイン)：$\sin \theta = \displaystyle \frac{ \mathrm{AC}}{ \mathrm{AB}}$</li>
	<li><strong>余弦</strong>(cosine コサイン)：$\cos \theta = \displaystyle \frac{ \mathrm{BC}}{ \mathrm{AB}}$</li>
	<li><strong>正接</strong>(tangent タンジェント)：$\tan \theta = \displaystyle \frac{ \mathrm{BC}}{ \mathrm{AC}}$</li>
</ul>
</div>


&nbsp;


<div class="blank-box bb-blue">


<strong>三角比の表</strong>




[wpex more="見る" less="閉じる"]


<table style="border-collapse: collapse; width: 100%; height: 1911px;" border="1">
<tbody>
<tr>
<td style="width: 25%; text-align: center;">$\theta$</td>
<td style="width: 25%; text-align: center;">$\sin\theta$</td>
<td style="width: 25%; text-align: center;">$\cos\theta$</td>
<td style="width: 25%; text-align: center;">$\tan\theta$</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$0^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.0000</td>
<td style="width: 25%; height: 21px; text-align: center;">1.0000</td>
<td style="width: 25%; height: 21px; text-align: center;">0.0000</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$1^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.0175</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9998</td>
<td style="width: 25%; height: 21px; text-align: center;">0.0175</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$2^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.0349</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9994</td>
<td style="width: 25%; height: 21px; text-align: center;">0.0349</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$3^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.0523</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9986</td>
<td style="width: 25%; height: 21px; text-align: center;">0.0524</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$4^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.0698</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9976</td>
<td style="width: 25%; height: 21px; text-align: center;">0.0699</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$5^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.0872</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9962</td>
<td style="width: 25%; height: 21px; text-align: center;">0.0875</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$6^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.1045</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9945</td>
<td style="width: 25%; height: 21px; text-align: center;">0.1051</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$7^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.1219</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9925</td>
<td style="width: 25%; height: 21px; text-align: center;">0.1228</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$8^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.1392</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9903</td>
<td style="width: 25%; height: 21px; text-align: center;">0.1405</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$9^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.1564</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9877</td>
<td style="width: 25%; height: 21px; text-align: center;">0.1584</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$10^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.1736</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9848</td>
<td style="width: 25%; height: 21px; text-align: center;">0.1763</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$11^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.1908</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9816</td>
<td style="width: 25%; height: 21px; text-align: center;">0.1944</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$12^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.2079</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9781</td>
<td style="width: 25%; height: 21px; text-align: center;">0.2126</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$13^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.2250</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9744</td>
<td style="width: 25%; height: 21px; text-align: center;">0.2309</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$14^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.2419</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9703</td>
<td style="width: 25%; height: 21px; text-align: center;">0.2493</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$15^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.2588</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9659</td>
<td style="width: 25%; height: 21px; text-align: center;">0.2679</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$16^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.2756</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9613</td>
<td style="width: 25%; height: 21px; text-align: center;">0.2867</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$17^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.2924</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9563</td>
<td style="width: 25%; height: 21px; text-align: center;">0.3057</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$18^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.3090</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9511</td>
<td style="width: 25%; height: 21px; text-align: center;">0.3249</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$19^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.3256</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9455</td>
<td style="width: 25%; height: 21px; text-align: center;">0.3443</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$20^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.3420</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9397</td>
<td style="width: 25%; height: 21px; text-align: center;">0.3640</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$21^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.3584</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9336</td>
<td style="width: 25%; height: 21px; text-align: center;">0.3839</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$22^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.3746</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9272</td>
<td style="width: 25%; height: 21px; text-align: center;">0.4040</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$23^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.3907</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9205</td>
<td style="width: 25%; height: 21px; text-align: center;">0.4245</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$24^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.4067</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9135</td>
<td style="width: 25%; height: 21px; text-align: center;">0.4452</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$25^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.4226</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9063</td>
<td style="width: 25%; height: 21px; text-align: center;">0.4663</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$26^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.4384</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8988</td>
<td style="width: 25%; height: 21px; text-align: center;">0.4877</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$27^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.4540</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8910</td>
<td style="width: 25%; height: 21px; text-align: center;">0.5095</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$28^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.4695</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8829</td>
<td style="width: 25%; height: 21px; text-align: center;">0.5317</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$29^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.4848</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8746</td>
<td style="width: 25%; height: 21px; text-align: center;">0.5543</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$30^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.5000</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8660</td>
<td style="width: 25%; height: 21px; text-align: center;">0.5774</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$31^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.5150</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8572</td>
<td style="width: 25%; height: 21px; text-align: center;">0.6009</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$32^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.5299</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8480</td>
<td style="width: 25%; height: 21px; text-align: center;">0.6249</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$33^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.5446</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8387</td>
<td style="width: 25%; height: 21px; text-align: center;">0.6494</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$34^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.5592</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8290</td>
<td style="width: 25%; height: 21px; text-align: center;">0.6745</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$35^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.5736</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8192</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7002</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$36^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.5878</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8090</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7265</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$37^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.6018</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7986</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7536</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$38^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.6157</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7880</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7813</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$39^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.6293</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7771</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8098</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$40^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.6428</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7660</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8391</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$41^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.6561</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7547</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8693</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$42^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.6691</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7431</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9004</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$43^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.6820</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7314</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9325</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$44^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.6947</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7193</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9657</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$45^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7071</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7071</td>
<td style="width: 25%; height: 21px; text-align: center;">1.0000</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$46^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7193</td>
<td style="width: 25%; height: 21px; text-align: center;">0.6947</td>
<td style="width: 25%; height: 21px; text-align: center;">1.0355</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$47^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7314</td>
<td style="width: 25%; height: 21px; text-align: center;">0.6820</td>
<td style="width: 25%; height: 21px; text-align: center;">1.0724</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$48^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7431</td>
<td style="width: 25%; height: 21px; text-align: center;">0.6691</td>
<td style="width: 25%; height: 21px; text-align: center;">1.1106</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$49^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7547</td>
<td style="width: 25%; height: 21px; text-align: center;">0.6561</td>
<td style="width: 25%; height: 21px; text-align: center;">1.1504</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$50^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7660</td>
<td style="width: 25%; height: 21px; text-align: center;">0.6428</td>
<td style="width: 25%; height: 21px; text-align: center;">1.1918</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$51^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7771</td>
<td style="width: 25%; height: 21px; text-align: center;">0.6293</td>
<td style="width: 25%; height: 21px; text-align: center;">1.2349</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$52^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7880</td>
<td style="width: 25%; height: 21px; text-align: center;">0.6157</td>
<td style="width: 25%; height: 21px; text-align: center;">1.2799</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$53^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.7986</td>
<td style="width: 25%; height: 21px; text-align: center;">0.6018</td>
<td style="width: 25%; height: 21px; text-align: center;">1.3270</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$54^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8090</td>
<td style="width: 25%; height: 21px; text-align: center;">0.5878</td>
<td style="width: 25%; height: 21px; text-align: center;">1.3764</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$55^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8192</td>
<td style="width: 25%; height: 21px; text-align: center;">0.5736</td>
<td style="width: 25%; height: 21px; text-align: center;">1.4281</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$56^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8290</td>
<td style="width: 25%; height: 21px; text-align: center;">0.5592</td>
<td style="width: 25%; height: 21px; text-align: center;">1.4826</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$57^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8287</td>
<td style="width: 25%; height: 21px; text-align: center;">0.5446</td>
<td style="width: 25%; height: 21px; text-align: center;">1.5399</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$58^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8480</td>
<td style="width: 25%; height: 21px; text-align: center;">0.5299</td>
<td style="width: 25%; height: 21px; text-align: center;">1.6003</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$59^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8572</td>
<td style="width: 25%; height: 21px; text-align: center;">0.5150</td>
<td style="width: 25%; height: 21px; text-align: center;">1.6643</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$60^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8860</td>
<td style="width: 25%; height: 21px; text-align: center;">0.5000</td>
<td style="width: 25%; height: 21px; text-align: center;">1.7321</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$61^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8746</td>
<td style="width: 25%; height: 21px; text-align: center;">0.4848</td>
<td style="width: 25%; height: 21px; text-align: center;">1.8040</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$62^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8829</td>
<td style="width: 25%; height: 21px; text-align: center;">0.4695</td>
<td style="width: 25%; height: 21px; text-align: center;">1.8807</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$63^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8910</td>
<td style="width: 25%; height: 21px; text-align: center;">0.4540</td>
<td style="width: 25%; height: 21px; text-align: center;">1.9626</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$64^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.8988</td>
<td style="width: 25%; height: 21px; text-align: center;">0.4384</td>
<td style="width: 25%; height: 21px; text-align: center;">2.0503</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$65^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9063</td>
<td style="width: 25%; height: 21px; text-align: center;">0.4226</td>
<td style="width: 25%; height: 21px; text-align: center;">2.1445</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$66^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9135</td>
<td style="width: 25%; height: 21px; text-align: center;">0.4067</td>
<td style="width: 25%; height: 21px; text-align: center;">2.2460</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$67^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9205</td>
<td style="width: 25%; height: 21px; text-align: center;">0.3907</td>
<td style="width: 25%; height: 21px; text-align: center;">2.3559</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$68^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9272</td>
<td style="width: 25%; height: 21px; text-align: center;">0.3746</td>
<td style="width: 25%; height: 21px; text-align: center;">2.4751</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$69^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9336</td>
<td style="width: 25%; height: 21px; text-align: center;">0.3584</td>
<td style="width: 25%; height: 21px; text-align: center;">2.6051</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$70^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9397</td>
<td style="width: 25%; height: 21px; text-align: center;">0.3420</td>
<td style="width: 25%; height: 21px; text-align: center;">2.7475</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$71^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9455</td>
<td style="width: 25%; height: 21px; text-align: center;">0.3256</td>
<td style="width: 25%; height: 21px; text-align: center;">2.9042</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$72^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9511</td>
<td style="width: 25%; height: 21px; text-align: center;">0.3090</td>
<td style="width: 25%; height: 21px; text-align: center;">3.0777</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$73^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9563</td>
<td style="width: 25%; height: 21px; text-align: center;">0.2924</td>
<td style="width: 25%; height: 21px; text-align: center;">3.2709</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$74^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9613</td>
<td style="width: 25%; height: 21px; text-align: center;">0.2756</td>
<td style="width: 25%; height: 21px; text-align: center;">3.4874</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$75^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9659</td>
<td style="width: 25%; height: 21px; text-align: center;">0.2588</td>
<td style="width: 25%; height: 21px; text-align: center;">3.7321</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$76^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9703</td>
<td style="width: 25%; height: 21px; text-align: center;">0.2419</td>
<td style="width: 25%; height: 21px; text-align: center;">4.0108</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$77^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9744</td>
<td style="width: 25%; height: 21px; text-align: center;">0.2250</td>
<td style="width: 25%; height: 21px; text-align: center;">4.3315</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$78^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9781</td>
<td style="width: 25%; height: 21px; text-align: center;">0.2079</td>
<td style="width: 25%; height: 21px; text-align: center;">4.7046</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$79^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9816</td>
<td style="width: 25%; height: 21px; text-align: center;">0.1908</td>
<td style="width: 25%; height: 21px; text-align: center;">5.1446</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$80^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9848</td>
<td style="width: 25%; height: 21px; text-align: center;">0.1736</td>
<td style="width: 25%; height: 21px; text-align: center;">5.6713</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$81^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9877</td>
<td style="width: 25%; height: 21px; text-align: center;">0.1564</td>
<td style="width: 25%; height: 21px; text-align: center;">6.3138</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$82^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9903</td>
<td style="width: 25%; height: 21px; text-align: center;">0.1392</td>
<td style="width: 25%; height: 21px; text-align: center;">7.1154</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$83^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9925</td>
<td style="width: 25%; height: 21px; text-align: center;">0.1219</td>
<td style="width: 25%; height: 21px; text-align: center;">8.1443</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$84^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9945</td>
<td style="width: 25%; height: 21px; text-align: center;">0.1045</td>
<td style="width: 25%; height: 21px; text-align: center;">9.5144</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$85^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9962</td>
<td style="width: 25%; height: 21px; text-align: center;">0.0872</td>
<td style="width: 25%; height: 21px; text-align: center;">11.4301</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$86^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9976</td>
<td style="width: 25%; height: 21px; text-align: center;">0.0698</td>
<td style="width: 25%; height: 21px; text-align: center;">14.3007</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$87^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9986</td>
<td style="width: 25%; height: 21px; text-align: center;">0.0523</td>
<td style="width: 25%; height: 21px; text-align: center;">19.0811</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$88^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9994</td>
<td style="width: 25%; height: 21px; text-align: center;">0.0349</td>
<td style="width: 25%; height: 21px; text-align: center;">28.6363</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$89^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">0.9998</td>
<td style="width: 25%; height: 21px; text-align: center;">0.0175</td>
<td style="width: 25%; height: 21px; text-align: center;">57.2900</td>
</tr>
<tr style="height: 21px;">
<td style="width: 25%; height: 21px; text-align: center;">$90^{ \circ }$</td>
<td style="width: 25%; height: 21px; text-align: center;">1.0000</td>
<td style="width: 25%; height: 21px; text-align: center;">0.0000</td>
<td style="width: 25%; height: 21px; text-align: center;">なし</td>
</tr>
</tbody>
</table>


[/wpex]


</div>


&nbsp;




### 三角比の拡張


<div class="info-box">


【定義】




座標平面上の原点を中心とした半径 $r$ の円の円周上に点 $\mathrm{P} (x,y)$ をとり，円と $x$ 軸正の向きの交点を点 $\mathrm{A}$，$\angle \mathrm{AOP} = \theta$ ( $0^{ \circ } \leqq \theta &lt; 360^{ \circ }$ )とすると


<ul>
	<li>$\sin \theta = \displaystyle \frac{y}{r}$</li>
	<li>$\cos \theta = \displaystyle \frac{x}{r}$</li>
	<li>$\tan \theta = \displaystyle \frac{y}{x}$ ( $\theta \neq 90^{ \circ } , 270^{ \circ }$ )</li>
</ul>


特に， $r=1$ (単位円)の場合


<ul>
	<li>$\sin \theta =y$</li>
	<li>$\cos \theta =x$</li>
	<li>$\tan \theta = \displaystyle \frac{y}{x}$ ( $\theta \neq 90^{ \circ } , 270^{ \circ }$ )</li>
</ul>


また，定義より


<ul>
	<li>$x=r \cos \theta = \displaystyle \frac{y}{ \tan \theta}$</li>
	<li>$y=r \sin \theta =x \tan \theta$</li>
	<li>$r= \displaystyle \frac{x}{ \cos \theta} = \frac{y}{ \sin \theta}$</li>
</ul>
</div>


&nbsp;


<div class="info-box">


【定義】




<strong>三角方程式</strong>：未知の角の三角比を含む方程式




三角方程式を<strong>解く</strong>：方程式を満たす角を求めること




【定理】<strong>三角比の範囲</strong>




$0^{ \circ } \leqq \theta &lt; 360^{ \circ }$ のとき


<ul>
	<li>$-1 \leqq \sin \theta \leqq 1$</li>
	<li>$-1 \leqq \cos \theta \leqq 1$</li>
	<li>$\tan \theta$ はすべての実数値をとる</li>
</ul>


【定理】<strong>三角比の相互関係</strong>




$0^{ \circ } \leqq \theta &lt; 360^{ \circ }$ のとき( $\tan \theta$ では $\theta \neq 90^{ \circ } , 270^{ \circ }$ )


<ul>
	<li>$\tan \theta = \displaystyle \frac{ \sin \theta}{ \cos \theta}$</li>
	<li>$\sin^2 \theta + \cos^2 \theta =1$</li>
	<li>$1+ \tan \theta = \displaystyle \frac{1}{ \cos^2 \theta}$</li>
</ul>
</div>


&nbsp;


<div class="blank-box bb-blue">


<strong>三角比の符号</strong>


<table style="border-collapse: collapse; width: 100%; height: 80px;" border="1">
<tbody>
<tr style="height: 20px;">
<td style="width: 16.6667%; height: 20px; text-align: center;">$\theta$</td>
<td style="width: 16.6667%; height: 20px; text-align: center;">第1象限</td>
<td style="width: 16.6667%; height: 20px; text-align: center;">第2象限</td>
<td style="width: 16.6667%; height: 20px; text-align: center;">第3象限</td>
<td style="width: 16.6667%; height: 20px; text-align: center;">第4象限</td>
</tr>
<tr style="height: 20px;">
<td style="width: 16.6667%; height: 20px; text-align: center;">$\sin \theta$</td>
<td style="width: 16.6667%; height: 20px; text-align: center;">$+$</td>
<td style="width: 16.6667%; height: 20px; text-align: center;">$+$</td>
<td style="width: 16.6667%; height: 20px; text-align: center;">$-$</td>
<td style="width: 16.6667%; height: 20px; text-align: center;">$-$</td>
</tr>
<tr style="height: 20px;">
<td style="width: 16.6667%; height: 20px; text-align: center;">$\cos \theta$</td>
<td style="width: 16.6667%; height: 20px; text-align: center;">$+$</td>
<td style="width: 16.6667%; height: 20px; text-align: center;">$-$</td>
<td style="width: 16.6667%; height: 20px; text-align: center;">$-$</td>
<td style="width: 16.6667%; height: 20px; text-align: center;">$+$</td>
</tr>
<tr style="height: 20px;">
<td style="width: 16.6667%; height: 20px; text-align: center;">$\tan \theta$</td>
<td style="width: 16.6667%; height: 20px; text-align: center;">$+$</td>
<td style="width: 16.6667%; height: 20px; text-align: center;">$-$</td>
<td style="width: 16.6667%; height: 20px; text-align: center;">$+$</td>
<td style="width: 16.6667%; height: 20px; text-align: center;">$-$</td>
</tr>
</tbody>
</table>
</div>


&nbsp;


<div class="blank-box bb-blue">


<strong>有名角の三角比</strong>


<table style="border-collapse: collapse; width: 104.285%;">
<tbody>
<tr>
<td style="width: 10%; text-align: center;">$\theta$</td>
<td style="width: 10%; text-align: center;">$0^{ \circ }$</td>
<td style="width: 10%; text-align: center;">$30^{ \circ }$</td>
<td style="width: 10%; text-align: center;">$45^{ \circ }$</td>
<td style="width: 10%; text-align: center;">$60^{ \circ }$</td>
<td style="width: 10%; text-align: center;">$90^{ \circ }$</td>
<td style="width: 10%; text-align: center;">$120^{ \circ }$</td>
<td style="width: 10%; text-align: center;">$135^{ \circ }$</td>
<td style="width: 10%; text-align: center;">$150^{ \circ }$</td>
<td style="width: 5%; text-align: center;">$180^{ \circ }$</td>
<td style="width: 2.5%; text-align: center;">$210^{ \circ }$</td>
<td style="width: 1.25%; text-align: center;">$225^{ \circ }$</td>
<td style="width: 0.625%; text-align: center;">$240^{ \circ }$</td>
<td style="width: 0.3125%; text-align: center;">$270^{ \circ }$</td>
<td style="width: 0.15625%; text-align: center;">$300^{ \circ }$</td>
<td style="width: 0.078125%; text-align: center;">$315^{ \circ }$</td>
<td style="width: 0.078125%; text-align: center;">$330^{ \circ }$</td>
</tr>
<tr>
<td style="width: 10%; text-align: center;">$\sin \theta$</td>
<td style="width: 10%; text-align: center;">$0$</td>
<td style="width: 10%; text-align: center;">$\displaystyle \frac{1}{2}$</td>
<td style="width: 10%; text-align: center;">$\displaystyle \frac{1}{\sqrt{2}}$</td>
<td style="width: 10%; text-align: center;">$\displaystyle \frac{\sqrt{3}}{2}$</td>
<td style="width: 10%; text-align: center;">$1$</td>
<td style="width: 10%; text-align: center;">$\displaystyle \frac{\sqrt{3}}{2}$</td>
<td style="width: 10%; text-align: center;">$\displaystyle \frac{1}{\sqrt{2}}$</td>
<td style="width: 10%; text-align: center;">$\displaystyle \frac{1}{2}$</td>
<td style="width: 5%; text-align: center;">$0$</td>
<td style="width: 2.5%; text-align: center;">$\displaystyle - \frac{1}{2}$</td>
<td style="width: 1.25%; text-align: center;">$\displaystyle - \frac{1}{\sqrt{2}}$</td>
<td style="width: 0.625%; text-align: center;">$\displaystyle - \frac{\sqrt{3}}{2}$</td>
<td style="width: 0.3125%; text-align: center;">$-1$</td>
<td style="width: 0.15625%; text-align: center;">$\displaystyle - \frac{\sqrt{3}}{2}$</td>
<td style="width: 0.078125%; text-align: center;">$\displaystyle - \frac{1}{\sqrt{2}}$</td>
<td style="width: 0.078125%; text-align: center;">$\displaystyle - \frac{1}{2}$</td>
</tr>
<tr>
<td style="width: 10%; text-align: center;">$\cos \theta$</td>
<td style="width: 10%; text-align: center;">$1$</td>
<td style="width: 10%; text-align: center;">$\displaystyle \frac{\sqrt{3}}{2}$</td>
<td style="width: 10%; text-align: center;">$\displaystyle \frac{1}{\sqrt{2}}$</td>
<td style="width: 10%; text-align: center;">$\displaystyle \frac{1}{2}$</td>
<td style="width: 10%; text-align: center;">$0$</td>
<td style="width: 10%; text-align: center;">$\displaystyle - \frac{1}{2}$</td>
<td style="width: 10%; text-align: center;">$\displaystyle - \frac{1}{\sqrt{2}}$</td>
<td style="width: 10%; text-align: center;">$\displaystyle - \frac{\sqrt{3}}{2}$</td>
<td style="width: 5%; text-align: center;">$-1$</td>
<td style="width: 2.5%; text-align: center;">$\displaystyle - \frac{\sqrt{3}}{2}$</td>
<td style="width: 1.25%; text-align: center;">$\displaystyle - \frac{1}{\sqrt{2}}$</td>
<td style="width: 0.625%; text-align: center;">$\displaystyle - \frac{1}{2}$</td>
<td style="width: 0.3125%; text-align: center;">$0$</td>
<td style="width: 0.15625%; text-align: center;">$\displaystyle \frac{1}{2}$</td>
<td style="width: 0.078125%; text-align: center;">$\displaystyle \frac{1}{\sqrt{2}}$</td>
<td style="width: 0.078125%; text-align: center;">$\displaystyle \frac{\sqrt{3}}{2}$</td>
</tr>
<tr>
<td style="width: 10%; text-align: center;">$\tan \theta$</td>
<td style="width: 10%; text-align: center;">$0$</td>
<td style="width: 10%; text-align: center;">$\displaystyle \frac{1}{\sqrt{3}}$</td>
<td style="width: 10%; text-align: center;">$1$</td>
<td style="width: 10%; text-align: center;">$\sqrt{3}$</td>
<td style="width: 10%; text-align: center;">／</td>
<td style="width: 10%; text-align: center;">$- \sqrt{3}$</td>
<td style="width: 10%; text-align: center;">$-1$</td>
<td style="width: 10%; text-align: center;">$\displaystyle - \frac{1}{\sqrt{3}}$</td>
<td style="width: 5%; text-align: center;">$0$</td>
<td style="width: 2.5%; text-align: center;">$\displaystyle \frac{1}{\sqrt{3}}$</td>
<td style="width: 1.25%; text-align: center;">$1$</td>
<td style="width: 0.625%; text-align: center;">$\sqrt{3}$</td>
<td style="width: 0.3125%; text-align: center;">／</td>
<td style="width: 0.15625%; text-align: center;">$- \sqrt{3}$</td>
<td style="width: 0.078125%; text-align: center;">$-1$</td>
<td style="width: 0.078125%; text-align: center;">$\displaystyle - \frac{1}{\sqrt{3}}$</td>
</tr>
</tbody>
</table>
</div>


&nbsp;


<div class="blank-box bb-blue">


<strong>三角比の角の変換</strong>


<table style="border-collapse: collapse; width: 100%;">
<tbody>
<tr>
<td style="width: 20%; text-align: center;"> </td>
<td style="width: 20%; text-align: center;">$90^{ \circ } - \theta$</td>
<td style="width: 20%; text-align: center;">$90^{ \circ } + \theta$</td>
<td style="width: 20%; text-align: center;">$180^{ \circ } - \theta$</td>
<td style="width: 20%; text-align: center;">$180^{ \circ } + \theta$</td>
</tr>
<tr>
<td style="width: 20%; text-align: center;">$\sin$</td>
<td style="width: 20%; text-align: center;">$\cos \theta$</td>
<td style="width: 20%; text-align: center;">$\cos \theta$</td>
<td style="width: 20%; text-align: center;">$\sin \theta$</td>
<td style="width: 20%; text-align: center;">$- \sin \theta$</td>
</tr>
<tr>
<td style="width: 20%; text-align: center;">$\cos$</td>
<td style="width: 20%; text-align: center;">$\sin \theta$</td>
<td style="width: 20%; text-align: center;">$- \sin \theta$</td>
<td style="width: 20%; text-align: center;">$- \cos \theta$</td>
<td style="width: 20%; text-align: center;">$- \cos \theta$</td>
</tr>
<tr>
<td style="width: 20%; text-align: center;">$\tan$</td>
<td style="width: 20%; text-align: center;">$\displaystyle \frac{1}{\tan \theta}$</td>
<td style="width: 20%; text-align: center;">$- \displaystyle \frac{1}{\tan \theta}$</td>
<td style="width: 20%; text-align: center;">$- \tan \theta$</td>
<td style="width: 20%; text-align: center;">$\tan \theta$</td>
</tr>
</tbody>
</table>
</div>


&nbsp;




### 正弦定理・余弦定理


<div class="info-box">


【定理】<strong>正弦定理</strong>




$\triangle \mathrm{ABC}$ の外接円の半径を $R$ とすると


<ul>
	<li>$\displaystyle \frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} =2R$</li>
	<li>$a=2R \sin A$，$b=2R \sin B$，$c=2R \sin C$</li>
	<li>$a: \sin A=b: \sin B=c: \sin C$</li>
	<li>$a:b:c= \sin A: \sin B: \sin C$</li>
</ul>


【定理】<strong>余弦定理</strong>




$\triangle \mathrm{ABC}$ について


<ul>
	<li>$a^2=b^2+c^2-2bc \cos A$</li>
	<li>$b^2=c^2+a^2-2ca \cos B$</li>
	<li>$c^2=a^2+b^2-2ab \cos C$</li>
</ul>


余弦について解くと


<ul>
	<li>$\cos A= \displaystyle \frac{b^2+c^2-a^2}{2bc}$</li>
	<li>$\cos B= \displaystyle \frac{c^2+a^2-b^2}{2ca}$</li>
	<li>$\cos C= \displaystyle \frac{a^2+b^2-c^2}{2ab}$</li>
</ul>


【定理】<strong>三角形の辺と角の大小関係</strong>




$\triangle \mathrm{ABC}$ について


<ul>
	<li>$\angle \mathrm{A}$ が鋭角( $A&lt;90^{ \circ }$ ) $\Leftrightarrow$ $a^2&lt;b^2+c^2$</li>
	<li>$\angle \mathrm{A}$ が直角( $A=90^{ \circ }$ ) $\Leftrightarrow$ $a^2=b^2+c^2$</li>
	<li>$\angle \mathrm{A}$ が鈍角( $A&gt;90^{ \circ }$ ) $\Leftrightarrow$ $a^2&gt;b^2+c^2$</li>
</ul>
</div>


## 平面図形の計量




### 多角形の計量


<div class="info-box">


【定理】<strong>中線定理</strong>




$\triangle \mathrm{ABC}$ の辺 $\mathrm{BC}$ の中点を $\mathrm{M}$ とすると


<p style="padding-left: 40px;">$\mathrm{AB}^2 + \mathrm{AC}^2 =2( \mathrm{AM}^2 + \mathrm{BM}^2 )$</p>


【定理】<strong>三角形の面積公式</strong>




$\triangle \mathrm{ABC}$ において，点 $\mathrm{A}$ から辺 $\mathrm{BC}$ に下ろした垂線の足を $\mathrm{H}$ ， $\mathrm{AH} =h$ ， 内接円の半径を $r$ ， $\angle \mathrm{A}$ ， $\angle \mathrm{B}$ ， $\angle \mathrm{C}$ の大きさをそれぞれ $A$ ， $B$ ， $C$ ， $\triangle \mathrm{ABC} =S$ とする。




<strong>基本公式</strong>


<p style="padding-left: 40px;">$S= \displaystyle \frac{1}{2} ah$</p>


<strong>2辺とその間の角を用いた公式</strong>


<p style="padding-left: 40px;">$S= \displaystyle \frac{1}{2} bc \sin A= \frac{1}{2} ca \sin B= \frac{1}{2} ab \sin C$</p>


<strong>ヘロンの公式</strong>


<p style="padding-left: 40px;">$s= \displaystyle \frac{a+b+c}{2}$ とすると $S= \sqrt{s(s-a)(s-b)(s-c)}$</p>


<strong>内接円の半径を用いた公式</strong>


<p style="padding-left: 40px;">$S= \displaystyle \frac{1}{2} r(a+b+c)$</p>
<p style="padding-left: 80px;">※この公式とヘロンの公式から以下の等式が得られる。</p>
<p style="padding-left: 80px;">$S=sr$</p>
<p style="padding-left: 80px;">$r= \sqrt{ \displaystyle \frac{(s-a)(s-b)(s-c)}{s}}$</p>


【定理】<strong>四角形の面積公式</strong>




四角形 $\mathrm{ABCD}$ において， $\mathrm{AB} =a$ ， $\mathrm{BC} =b$ ， $\mathrm{CD} =c$ ， $\mathrm{DA} =d$ ，四角形 $\mathrm{ABCD}$ の面積を $S$ とする。




<strong>基本公式</strong>




四角形 $\mathrm{ABCD}$ が長方形のとき


<p style="padding-left: 40px;">$S=ab=bc=cd=da$</p>


四角形 $\mathrm{ABCD}$ が平行四辺形のとき，辺 $\mathrm{AB}$ と辺 $\mathrm{CD}$ ，辺 $\mathrm{BC}$ と辺 $\mathrm{DA}$ の距離をそれぞれ $h$ ， $h'$ とすると


<p style="padding-left: 40px;">$S=ah=ch=bh'=dh'$</p>


四角形 $\mathrm{ABCD}$ が $\mathrm{AB} /\!/ \mathrm{CD}$ の台形のとき，辺 $\mathrm{AB}$ と辺 $\mathrm{CD}$ の距離を $h$ とすると


<p style="padding-left: 40px;">$S= \displaystyle \frac{1}{2} h(a+c)$</p>


<strong>ブラーマグプタの公式</strong>




四角形 $\mathrm{ABCD}$ が円に内接するとき， $s= \displaystyle \frac{a+b+c+d}{2}$ とすると


<p style="padding-left: 40px;">$S= \sqrt{(s-a)(s-b)(s-c)(s-d)}$</p>
<p style="padding-left: 40px;">※ $d=0$ のとき，ヘロンの公式と一致する。</p>


<strong>ブレートシュナイダーの公式</strong>




$\angle \mathrm{A}$ ， $\angle \mathrm{C}$ の大きさをそれぞれ $A$ ， $C$ ， $s= \displaystyle \frac{a+b+c+d}{2}$ とすると


<p style="padding-left: 40px;">$S= \sqrt{(s-a)(s-b)(s-c)(s-d)-abcd \cos ^2 \displaystyle \frac{A+C}{2}}$</p>
<p style="padding-left: 40px;">※ $A+C=180^{ \circ }$ のとき，四角形 $\mathrm{ABCD}$ は円に内接し，ブラーマグプタの公式と一致する。</p>


【定理】<strong>平行線と面積</strong>




線分 $\mathrm{BC}$ を共有し，線分 $\mathrm{BC}$ に対して同じ側に $\mathrm{A}$ ， $\mathrm{A'}$ をもつ2つの三角形 $\triangle \mathrm{ABC}$ ， $\triangle \mathrm{A'BC}$ について


<p style="padding-left: 40px;">$\mathrm{AA'} /\!/ \mathrm{BC}$ $\Leftrightarrow$ $\triangle \mathrm{ABC} = \triangle \mathrm{A'BC}$</p>
</div>


### 円と扇形の計量


<div class="info-box">


【定義】




<strong>円周率</strong>：円周の直径に対する割合，$\pi$


<p style="padding-left: 40px;">※円の半径を $r$ ，円周を $l$ とすると $\pi = \displaystyle \frac{l}{2r}$</p>


【定理】<strong>円の周長・面積</strong>




円の半径を $r$，円周の長さを $l$，面積を $S$ とすると，


<p style="padding-left: 30px;">$l=2 \pi r$</p>
<p style="padding-left: 30px;">$S= \pi r^2$</p>


【定理】<strong>扇形の弧長・面積</strong>




扇形の半径を $r$ ，中心角を $\theta$ ，弧の長さを $l$ ，面積を $S$ とすると，


<p style="padding-left: 30px;">$l=2 \pi r \times \displaystyle \frac{\theta}{360}$</p>
<p style="padding-left: 30px;">$S= \pi r^2 \times \displaystyle \frac{\theta}{360}$</p>
</div>


## 空間図形の計量


<div class="info-box">


【定義】




<strong>表面積</strong>：立体の表面全体の面積




<strong>底面積</strong>：立体の1つの底面の面積




<strong>側面積</strong>：立体の側面全体の面積




【定理】<strong>柱体の表面積・体積</strong>




柱体の底面積を $S_1$ ，側面積を $S_2$ ，表面積を $S$ ，高さを $h$ ，体積を $V$ とすると


<ul>
	<li>$S=S_1+2S_2$</li>
	<li>$V=Sh$</li>
</ul>


【定理】<strong>錐体の表面積・体積</strong>




錐体の底面積を $S_1$ ，側面積を $S_2$ ，表面積を $S$ ，高さを $h$ ，体積を $V$ とすると


<ul>
	<li>$S=S_1+S_2$</li>
	<li>$V= \displaystyle \frac{1}{3} Sh$</li>
</ul>


【定理】<strong>球の表面積・体積</strong>




球の半径を $r$，表面積を $S$，体積を $V$ とすると，


<ul>
	<li>$S=4 \pi r^2$</li>
	<li>$V= \displaystyle \frac{4}{3} \pi r^3$</li>
</ul>
</div>


&nbsp;




空間図形から適当な平面を取り出して三角比を適用する。また，円柱，円錐，角柱，角錐では，底面積と高さと体積の関係なども利用する。




## 相似な図形の計量


<div class="info-box">


【定義】




<strong>相似比</strong>：相似な立体における対応する線分の長さの比。




【定理】<strong>相似な図形の面積比・表面積比・体積比</strong>




2つの図形・立体の相似比が $m:n$ のとき，


<ul>
	<li>相似な図形の面積比：$m^2:n^2$</li>
	<li>相似な立体の表面積比：$m^2:n^2$</li>
	<li>相似な立体の体積比：$m^3:n^3$</li>
</ul>
</div>


&nbsp;
