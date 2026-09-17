---
title: "【インスタント中高数学】第6講 広がり続ける数の果て【数】"
wp_id: 2261
content_type: "post"
status: "publish"
published_at: "2019-05-23 21:54:33"
wp_date: "2019-05-23 21:54:33"
modified_at: "2019-06-15 20:45:57"
legacy_url: "http://mathrao.com/instant-jhmath-provisional-6/"
legacy_path: "/instant-jhmath-provisional-6/"
legacy_slug: "instant-jhmath-provisional-6"
former_slugs: []
parent_wp_id: null
parent_title: null
hierarchy: ["【インスタント中高数学】第6講 広がり続ける数の果て【数】"]
category: ["インスタント中高数学【草稿】"]
tags: []
mathrao_section: "インスタント中高数学"
mathrao_grade: null
mathrao_course: null
source_content_sha256: "605feb5f40896ff15eb7540b23f82f91081a7110953fb64993f2f1e233dfe31d"
---

http://mathrao.com/instant-jhmath-provisional-5/




## 見方が変わる面白さ




少中高の数学って本当によくできていて，ちゃんと通しで見れば数学の世界が少しずつ広がっているのがよく分かる。




しかもそれが理論の書き換えではなくて，補完という形で進むのも面白い。




残念ながらそれに気付ける人はまれなんだけどね。




例えば，小学校ではただの引き算記号だった" $-$ "も，中学校では"マイナス"，高校になれば"向き"に見えるようになるし，指数も最初は"掛けられた個数"だったのに，"冪乗・累乗根"に変わっていく。




数学の発展をなぞっているし，上手く編集しているからでもあるんだけど，ストーリーを感じるんだよね。




だから僕は高校数学まででも十分に楽しめるし，ファンになったんだ。




当然，数学の本質忘れちゃいけないから，教えるときはなるべくフラットに，先入観なく学べるよう気をつけたいけど，どうしても楽しさが溢れちゃうんだよ。




君にもこの楽しさが伝わるといいな。




第6講では中高数学で扱う数の範囲の果てに辿り着くからお楽しみに。




## 複素数


<div class="info-box">


【定義】




(   )内はその数全体の集合




<strong>複素数</strong>( $\mathbb{C}$ )： $a+bi$ ( $a$ ， $b$ は実数)の形で表される数




<strong>虚数単位</strong> $i$ ：2乗すると $-1$ になる2つの数のうちの1つ ( $i^2=-1$ )




<strong>実部</strong>：複素数 $a+bi$ ( $a$ ， $b$ は実数)における $a$




<strong>虚部</strong>：複素数 $a+bi$ ( $a$ ， $b$ は実数)における $b$




<strong>実数</strong>( $\mathbb{R}$ )：有理数と無理数の総称(虚部が $0$ の複素数)




<strong>虚数</strong>：実数でない複素数(虚部が $0$ でない複素数)




<strong>純虚数</strong>：実部が $0$ の複素数




<strong>有理数</strong>( $\mathbb{Q}$ )：分数の形で表せる実数




<strong>無理数</strong>：有理数でない実数(分数の形で表せない実数)




<strong>整数</strong>( $\mathbb{Z}$ )： $0$ とそれに $1$ を足すか引くかしてできる数




<strong>自然数</strong>( $\mathbb{N}$ )：正の整数




<strong>有限小数</strong>：小数第何位かで終わる小数




<strong>無限小数</strong>：小数部分が無限に続く小数




<strong>循環小数</strong>：無限小数のうち，ある位以下では数字の同じ並びが繰り返される小数




<strong>循環節</strong>：循環小数において繰り返される数字の列


<p style="padding-left: 30px;">※循環小数は，循環節の最初と最後の数字の上に・をつけて表す。</p>


<strong>既約分数</strong>：分母と分子が整数で，分母と分子が互いに素である分数


</div>


さっそくだけど，基礎計算を身につけた君に，中高数学の数の世界のすべてをお見せしよう。




上の定義に出てきた数の集合の包含関係を図にすると以下のようになるよ。


<div class="blank-box bb-blue">


<strong>複素数の分類</strong>




<img class="alignnone size-full wp-image-2270" src="http://mathrao.com/images/complexnumber.png" alt="" width="600" height="261" />


</div>


どうかな？




数の世界，思ったより広いでしょ？




上の図でいうと，第5講までは有理数しか扱っていなかったんだ。




そこに，無理数，虚数が加わって，中高数学の数の世界の果て，複素数に辿り着く。




以降，どの数の範囲で考えるかによって大きな違いが出てくるから，1つ1つ確認するようにね。




では，補足が必要な用語だけ解説していくよ。




### 自然数




補足と言えるほどのことではないんだけど，自然数には0を含める考え方もある。




第1講でも書いたけど，定義のしかたはその人の自由だからね。




これは数学の分野によって違うこともあるんだけど，中高数学では正の整数，つまり， $0$ は含まない考え方で統一されているから安心してね。




### 分数・小数




$m$ を整数，$n$ を自然数とすると，分数 $\displaystyle \frac{m}{n}$ は整数，有限小数，循環小数のいずれかで表されるんだ。




整数でない既約分数 $\displaystyle \frac{m}{n}$ について次のことが成り立つよ。


<ul>
	<li>分母 $n$ の素因数が $2$ ， $5$ だけからなる $\Leftrightarrow$ $\displaystyle \frac{m}{n}$ は有限小数で表される</li>
	<li>分母 $n$ の素因数に $2$ ， $5$ 以外のものがある $\Leftrightarrow$ $\displaystyle \frac{m}{n}$ は循環小数で表される</li>
</ul>


### 有理数・無理数




有理数とは分数で表すことができる実数で，無理数は表すことができない実数のことなんだけど，現時点で君が知っている無理数は円周率 $\pi$ だけ。




$3.1415 \cdots $ と無限に続くという話は聞いていると思うけど，これって分数で表すことができないんだ。




小学校で $3.14$ の掛け算を頑張った覚えがあるんじゃないかな？




分数で表せるなら，わざわざ3桁の掛け算をする必要なんてないんだよ。




あと，円周率以外にも無限に続く小数=無限小数は小学校でも扱ったけど，それは上の図の $\frac{1}{3} =0.333 \cdots \cdots$ のような同じ数字が繰り返される小数=循環小数だけだったよね？




すべての循環小数は分数に直すことができるから，これらはすべて有理数なんだ。




あとで中高数学では代表的な無理数である累乗根と対数を扱うからチェックしてね。




### 複素数・実数・虚数




おおまかにいうと，今までの数直線に表せる数が実数で，そうでない数が虚数。




まあ，複素数平面という単元では虚数を図示するんだけどね。




とりあえず現時点ではそう考えておいてほしい。




そもそも虚数という考えがどこから出てきたのかというと，答えのない問題に答えを与えるためだったんだ。




それまでは2乗してマイナスになる数がなかったから表すことができないものがあったんだけど，虚数というものを定義することで表せるようになったということ。




数学において，表したいものが表せないときに新たな定義が生まれるというのはよくあることなんだよ。




虚数の表し方は色々あるんだけど，高校数学では $i^2=-1$ を満たす虚数単位 $i$ を使ったものに限定される。




虚数単位 $i$ の具体的な使い方はまた後ほど。




そして，この虚数単位を使って  $a+bi$ ( $a$ ， $b$ は実数)の形で表されるのが複素数。




中高数学で扱う数はすべて複素数だと考えることができるんだ。




ちなみに，上の図のさらに左にも数がある。




中高数学では扱わないんだけど，その数を四元数というんだ。




まさに複素数を拡張したような見た目をしていて，実数 $a$ ， $b$ ， $c$ ， $d$ と，基本的な四元数の単位 $i$ ， $j$ ， $k$ を用いて， $a + bi + cj + dk$ と表される。




気になったら調べてみてね。




### 数の集合




定義と上の図にも示した太字の集合がある。


<ul>
	<li>自然数全体の集合： $\mathbb{N}$ (自然数= Natural Number の頭文字)</li>
	<li>整数全体の集合： $\mathbb{Z}$ (ドイツ語の「数」の複数形= Zahlen の頭文字)</li>
	<li>有理数全体の集合： $\mathbb{Q}$ (イタリア語の「商」= Quoziente の頭文字)</li>
	<li>実数全体の集合： $\mathbb{R}$ (実数= Real Number の頭文字)</li>
	<li>複素数全体の集合： $\mathbb{C}$ (複素数= Complex Number の頭文字)</li>
</ul>


中高数学では使われないんだけど，問題集によっては使われることがあるし，数学において広く使われているから覚えておこう。




使い方としては，「 $x$ を実数とする」=「 $x \in \mathbb{R}$」といった感じ。




あと，上の図から分かる通り，これらの集合の間には $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$ という包含関係が成り立つよ。




## 数直線と絶対値


<div class="info-box">


【定義】




<strong>座標</strong>：数直線上で，点 $\mathrm{P}$ に実数 $a$ が対応しているとき，$a$ を点 $\mathrm{P}$ の座標といい，座標が $a$ である点 $\mathrm{P}$ を $\mathrm{P} (a)$ で表す。


<p style="padding-left: 40px;">※数直線では，1つの実数に1つの点が対応している。</p>


<strong>絶対値</strong> $\boldsymbol{|a|}$ ：原点 $\mathrm{O} (0)$ と点 $\mathrm{P} (a)$ の距離


<p style="padding-left: 40px;">$|a|= \left \{ \begin{array}{cl} a &amp; (a \geqq 0 のとき) \\ -a &amp; (a&lt;0 のとき) \end{array} \right.$</p>


2点 $\mathrm{P} (a)$，$\mathrm{Q} (b)$ の<strong>距離</strong>：$|b-a|$


</div>


この講で必要になるから座標と絶対値を定義しなおしたよ。




意味は変わらないけど，実数等を学んで表現が変わっているから要注意。




この座標の考え方は後々拡張されるけど，点の名前と座標をセットで表すのは変わらないからね。




また，絶対値を使うことで，2点間の距離が表せる。




例えば，点 $A(1)$ と点 $B(-2)$ の距離は $|-2-1|=|-3|=3$ というようにね。




あと，実数の大小関係は，数直線上では点の左右の位置関係で表されて，左にあるものが小さく，右にあるものが大きいよ。




## 累乗根


<div class="info-box">


【定義】




$\boldsymbol{a}$ の $\boldsymbol{n}$ <strong>乗根</strong>：$n$ を自然数とするとき，$n$ 乗すると $a$ になる数


<p style="padding-left: 40px;">※$a=0$ のとき，$\sqrt[n]{a}=0$。</p>


$\boldsymbol{ \sqrt[r]{a} }$ ： $r$ 乗すると $a$ になる数(のうちの1つ)




<strong>平方根</strong>：2乗根


<p style="padding-left: 40px;">※$a&gt;0$ のとき，$a$ の平方根は正と負の2つあり，そのうち正の数を $\sqrt{a}$，負の数を$- \sqrt{a}$ で表す。</p>


<strong>開平</strong>：平方根を求めること




<strong>立方根</strong>：3乗根




<strong>開立</strong>(かいりゅう)：立方根を求めること




<strong>累乗根</strong>(冪根)： $n$ 乗根の総称




<strong>有理化</strong>：分母に根号を含まない形に直すこと




【定理】<strong>累乗根の性質</strong>




$a&gt;0$，$b&gt;0$ で， $m$，$n$，$p$ が自然数のとき


<ul>
	<li>$( \sqrt[n]{a} )^n =a$</li>
	<li>$\sqrt[n]{a} \sqrt[n]{b} = \sqrt[n]{ab}$</li>
	<li>$\displaystyle \frac{\sqrt[n]{a}}{\sqrt[n]{b}} = \sqrt[n]{\frac{a}{b}}$</li>
	<li>$( \sqrt[n]{a} )^m = \sqrt[n]{a^m}$</li>
	<li>$\sqrt[m]{\sqrt[n]{a}} = \sqrt[mn]{a}$</li>
	<li>$\sqrt[n]{a^m} = \sqrt[np]{a^{mp}}$</li>
</ul>
<p style="padding-left: 40px;">※ $\sqrt{ \ \ }$ を<strong>根号</strong>といい，「 $\sqrt[n]{a}$ 」を「 $n$ 乗根ルート $a$ 」と読む。」</p>
</div>


この中で一つややこしいのが，累乗根と冪根。




累乗，冪乗は指数が自然数か，固定されないかではっきり区別されていたけど，累乗根，冪根はその区別がなくどちらを使ってもいいんだ。




イン数では累乗，冪乗はしっかり区別し，累乗根，冪根は累乗根で統一するよ。




あと，複素数の累乗根は複素数平面という単元で扱うから，この講では実数の累乗根についてのみ扱うよ。




だから，これ以降，特別なことわりがなければ根号の中身は実数だと考えてね。




### 累乗根と無理数




これまでは何かを累乗することはあったけど，ここではその逆を考えるよ。




例えば，「2乗すると $4$ になる数は $2$ と $-2$ 」=「 $4$ の2乗根は $2$ と $-2$ 」のようにね。




まずは累乗根を考えると無理数が表れるということを実感してもらおう。




$2$ の平方根で正のものは頑張れば $1.41^2=1.9881$ くらいまでは探せるかもしれないけど，これでもぴったり $2$ にはならないよね？




実際，小数点以下の桁を増やし続けても， $1.41421356^2=1.999999993287874$ のように $2$ に近づいて行くだけで $2$ にはならない。




つまり， $2$ の平方根で正のものは $1.41421356 \cdots $ というように循環しない無限小数=無理数なんだ。




じゃあ小学校の円周率のように文字で置いて扱うかというと，累乗根が無理数になる数は無限にあるから文字を置き続けることはできない。




そこで登場するのが根号 $\sqrt{ \ \ }$ 。




$n$ 乗すると $a$ になる数を「 $\sqrt[n]{a}$ 」と表し，「 $n$ 乗根ルート $a$ 」と読むんだ。




特に2乗のときは左上の数字を省いて，「 $\sqrt{a}$ 」と表し，「ルート $a$ 」と読む。




### $a$ の $n$ 乗根は $n$ 個ある




累乗根で混乱しやすいポイントを押さえておくね。




1つ目は，「 $n$ 乗根の個数」について。




$a$ の $n$ 乗根って $\sqrt[n]{a}$ じゃないの？って思いがちだけど，実際には $0$ 以外の数の $n$ 乗根は $n$ 個あるんだ。




しかも，平方根のときは $a$ が正の実数であれば2つの平方根も実数になるけど，立方根以上のときは必ず虚数が表れる。




だから， $\sqrt[n]{a}$ は確かに $n$ 乗すれば $a$ になるんだけど， $a$ の $n$ 乗根はこれだけじゃないということを覚えておいてほしい。




以下が実数 $a$ の $n$ 乗根，平方根，立方根の個数をまとめたものだよ。


<div class="blank-box bb-blue">


$a$ を実数とする。




<strong>$a$ の $n$ 乗根の個数</strong>


<table style="border-collapse: collapse; width: 100%;">
<tbody>
<tr>
<td style="width: 14.2857%; text-align: center;" rowspan="2"> </td>
<td style="width: 14.2857%; text-align: center;" colspan="3">$n$ が奇数</td>
<td style="width: 14.2857%; text-align: center;" colspan="3">$n$ が偶数</td>
</tr>
<tr>
<td style="width: 14.2857%; text-align: center;">実数</td>
<td style="width: 14.2857%; text-align: center;">虚数</td>
<td style="width: 14.2857%; text-align: center;">合計</td>
<td style="width: 14.2857%; text-align: center;">実数</td>
<td style="width: 14.2857%; text-align: center;">虚数</td>
<td style="width: 14.2857%; text-align: center;">合計</td>
</tr>
<tr>
<td style="width: 14.2857%; text-align: center;">$a&gt;0$</td>
<td style="width: 14.2857%; text-align: center;">$1$ ( $\sqrt[n]{a} &gt;0$ )</td>
<td style="width: 14.2857%; text-align: center;">$n-1$</td>
<td style="width: 14.2857%; text-align: center;">$n$</td>
<td style="width: 14.2857%; text-align: center;">$2$ ( $\pm \sqrt[n]{a}$ )</td>
<td style="width: 14.2857%; text-align: center;">$n-2$</td>
<td style="width: 14.2857%; text-align: center;">$n$</td>
</tr>
<tr>
<td style="width: 14.2857%; text-align: center;">$a=0$</td>
<td style="width: 14.2857%; text-align: center;">$1$ ( $0$ )</td>
<td style="width: 14.2857%; text-align: center;">$0$</td>
<td style="width: 14.2857%; text-align: center;">$1$</td>
<td style="width: 14.2857%; text-align: center;">$1$ ( $0$ )</td>
<td style="width: 14.2857%; text-align: center;">$0$</td>
<td style="width: 14.2857%; text-align: center;">$1$</td>
</tr>
<tr>
<td style="width: 14.2857%; text-align: center;">$a&lt;0$</td>
<td style="width: 14.2857%; text-align: center;">$1$ ( $\sqrt[n]{a} &lt;0$ )</td>
<td style="width: 14.2857%; text-align: center;">$n-1$</td>
<td style="width: 14.2857%; text-align: center;">$n$</td>
<td style="width: 14.2857%; text-align: center;">$0$</td>
<td style="width: 14.2857%; text-align: center;">$n$</td>
<td style="width: 14.2857%; text-align: center;">$n$</td>
</tr>
</tbody>
</table>


<strong>$a$ の平方根の個数</strong>


<table style="border-collapse: collapse; width: 100%;">
<tbody>
<tr>
<td style="width: 25%; text-align: center;"> </td>
<td style="width: 25%; text-align: center;">実数</td>
<td style="width: 25%; text-align: center;">虚数</td>
<td style="width: 25%; text-align: center;">合計</td>
</tr>
<tr>
<td style="width: 25%; text-align: center;">$a&gt;0$</td>
<td style="width: 25%; text-align: center;">$2$ ( $\pm \sqrt{a}$ )</td>
<td style="width: 25%; text-align: center;">$0$</td>
<td style="width: 25%; text-align: center;">$2$</td>
</tr>
<tr>
<td style="width: 25%; text-align: center;">$a=0$</td>
<td style="width: 25%; text-align: center;">$1$ ( $0$ )</td>
<td style="width: 25%; text-align: center;">$0$</td>
<td style="width: 25%; text-align: center;">$1$</td>
</tr>
<tr>
<td style="width: 25%; text-align: center;">$a&lt;0$</td>
<td style="width: 25%; text-align: center;">$0$</td>
<td style="width: 25%; text-align: center;">$2$ ( $\pm \sqrt{a} i$ )</td>
<td style="width: 25%; text-align: center;">$2$</td>
</tr>
</tbody>
</table>


<strong>$a$ の立方根の個数</strong>


<table style="border-collapse: collapse; width: 100%;">
<tbody>
<tr>
<td style="width: 25%; text-align: center;"> </td>
<td style="width: 25%; text-align: center;">実数</td>
<td style="width: 25%; text-align: center;">虚数</td>
<td style="width: 25%; text-align: center;">合計</td>
</tr>
<tr>
<td style="width: 25%; text-align: center;">$a&gt;0$</td>
<td style="width: 25%; text-align: center;">$1$ ( $\sqrt{a} &gt;0$ )</td>
<td style="width: 25%; text-align: center;">$2$ ( $\displaystyle \frac{-1 \pm \sqrt{3} i}{2} \sqrt[3]{a}$ )</td>
<td style="width: 25%; text-align: center;">$3$</td>
</tr>
<tr>
<td style="width: 25%; text-align: center;">$a=0$</td>
<td style="width: 25%; text-align: center;">$1$ ( $0$ )</td>
<td style="width: 25%; text-align: center;">$0$</td>
<td style="width: 25%; text-align: center;">$1$</td>
</tr>
<tr>
<td style="width: 25%; text-align: center;">$a&lt;0$</td>
<td style="width: 25%; text-align: center;">$1$ ( $\sqrt{a} &lt;0$ )</td>
<td style="width: 25%; text-align: center;">$2$ ( $\displaystyle \frac{-1 \pm \sqrt{3} i}{2} \sqrt[3]{a}$ )</td>
<td style="width: 25%; text-align: center;">$3$</td>
</tr>
</tbody>
</table>
</div>


$a$ が虚数のときも $n$ 乗根が $n$ 個あることに変わりはないけど，実数になるか，虚数になるかの法則性はより難しくなるから注意が必要だよ。




### 根号と符号




2つ目は「根号と符号」について。




根号を含んだ計算はこのあとに触れるけど，練習を重ねると根号の意味を忘れてしまう場合が多い。




特に，根号には符号の要素が含まれている，ということをね。




例えば， $\sqrt{2}$ は2乗すると $2$ になる「正」の数，という定義。




上でもやったけど，2乗すると $2$ になる実数は2つあるから，そのうち正のものを $\sqrt{2}$ と表し， $- \sqrt{2}$ は $\sqrt{2}$ を $-1$ 倍したもの，ということになる。




結果的には $- \sqrt{2}$ も $2$ の平方根なんだけどね。




この意味をしっかり理解していないとつまずく問題がある。




それが， $\sqrt{(-2)^2}$ 。




2乗して $(-2)^2$ になるものなんだから， $-2$ なんじゃないの？と考えるとアウト。




$\sqrt{○}$ と書いた時点で「正」なんだから， $\sqrt{(-2)^2} = \sqrt{4} =2&gt;0$ となる。




$\sqrt{○}$ は，2乗したら○になる正の数，という考え方を忘れちゃいけないよ。




一方で $\sqrt[3]{(-2)^3}$ は $-2$ になる。




$(-2)^3=-8$ で，3乗したら $-8$ になる実数は $-2$ だけだからね。




これら2つの例からも分かるけど，根号の前についている符号と数の符号は必ずしも一致しないんだ。




上の累乗根の個数の表を見ても分かるけど，根号の前の符号と数の符号が一致するのは正の実数の平方根のみだからね。




### 虚数単位 $i$ の正体




3つ目は「虚数単位 $i$ の正体」について。




最初にも書いた通り， $i$ というのは $i^2=-1$ を満たす数のことなんだけど， $i= \sqrt{-1}$ って考えていいかというと微妙。




なぜなら， $i$ は2乗して $-1$ になる「2数のうちの1つ」という定義になっているから。




ややこしいんだけど，2乗して $-1$ になる数は， $\sqrt{-1}$ と $- \sqrt{-1}$ があるよね？




でも，定義では $+$ なのか $-$ なのかはっきり示されていないんだ。




理由は2つ。




高校数学の範囲では虚数に正負の概念がない(定義されていない)，というのと，式の中に $i$ が出てきたところで $\sqrt{-1}$ と $- \sqrt{-1}$ のどっちなのかを特定できない，ということ。




前者の正負の定義がない，というのはそのままで，虚数の前に $+$ がついていれば正， $-$ がついていれば負，というような定義はされていないんだ。




実数の正負は第3講でも触れた通り，0より大きい数が正，小さい数が負，と定義されているけどね。




後者の特定できないというのは，実際に試してみれば分かるけど， $i$ を $\sqrt{-1}$ か $- \sqrt{-1}$ のどちらに置き換えても正しく計算できてしまうということ。




つまり，どっちで計算してもいいということは， $i$ がどちらを表しているか特定できないということなんだ。




これらの理由が分かった上で， $i= \sqrt{-1}$ と考えるのはありだと思うよ。




ただ，記述試験では書かない方がいいけどね。




できるだけ平方根と， $i^2=-1$ という定義だけで問題が解けるようになろう。




ちなみに， $-1$ の平方根は $\pm i$ だからね。




### 虚数単位 $i$ と符号




最後は上の「根号と符号」，「虚数単位 $i$ の正体」にも関わってくるんだけど，「虚数単位 $i$ と符号」について。




累乗根の性質に $\sqrt[n]{a} \sqrt[n]{b} = \sqrt[n]{ab}$ というものがある。




例えば， $\sqrt{2} \sqrt{3} = \sqrt{2 \cdot 3} = \sqrt{6}$ というような性質なんだけど，定理の段階では中身が正のものに限定してあるんだ。




なぜかというと，そこに $i$ が関わってくるから。




同じような計算で $\sqrt{-2} \sqrt{-3}$ ってどうなるか分かるかな？




$\sqrt{-2} \sqrt{-3} = \sqrt{(-2)(-3)} = \sqrt{6}$ というのは間違い。




これだと完全に見た目に惑わされているんだ。




平方根の定義を思い出してほしい。




$\sqrt{-1} \sqrt{-1} = \sqrt{(-1)(-1)} = \sqrt{1} =1$ と $\sqrt{-1} \sqrt{-1} =-1$ のどちらが正しいかな？




平方根とは，2乗すると中身になる数だったよね？




ということは，同じものを2回掛けたら中身になる，つまり，後者が正しいんだ。




今までのマイナス掛けるマイナスがプラスになる，という実数の計算に引っ張られず，ちゃんと根号の定義に従えばこんな間違いはしないからね。




ただ，間違えやすい計算であることは事実だから，「根号の中身が負のままでは扱いづらいから，計算の最初に $i$ を使った表記に変える」という癖をつけよう。




そうすれば， $\sqrt{-2} \sqrt{-3} = \sqrt{2} i \sqrt{3} i = \sqrt{2 \cdot 3} i^2 =- \sqrt{6}$ と間違えずに計算できるよ。




ここまでで， $( \sqrt{-1} )^2$ と $\sqrt{(-1)^2}$ の違いをはっきり説明できるようになってほしいな。




## 指数の拡張と指数法則


<div class="info-box">


【定義】




$a&gt;0$ で，$m$，$n$ が正の整数，$r$ が正の有理数のとき


<ul>
	<li>$a^{\frac{m}{n}}= \sqrt[n]{a^m} =( \sqrt[n]{a} )^m$ 特に $a^{\frac{1}{n}} = \sqrt[n]{a}$</li>
	<li>$a^{-r} = \displaystyle \frac{1}{a^r}$</li>
</ul>


【定理】<strong>指数法則</strong>




$a&gt;0$，$b&gt;0$ で，$r$，$s$ が実数のとき


<ul>
	<li>$a^ra^s=a^{r+s}$</li>
	<li>$\displaystyle \frac{a^r}{a^s} = a^{r-s}$</li>
	<li>$(a^r)^s=a^{rs}$</li>
	<li>$(ab)^r=a^rb^r$</li>
	<li>$\left( \displaystyle \frac{a}{b} \right)^r = \displaystyle \frac{a^r}{b^r}$</li>
</ul>
</div>


定義にもあるように，累乗根は分数の指数を使って表すんだけど，僕が最初にこの定義を見たときよくできてるなーって感動したよ。




もちろん，この完成形ありきで自然数，整数，有理数と，段階的に拡張されるように編集されてるから当たり前なんだけどね。




上の指数法則の範囲が実数になっているのは，中高数学では無理数の指数については特別触れることはないけど，存在はするという扱いだから。




ちなみに，底が負のときは，平方根であれば $i$ を使うことで対応できるけど，それ以上の累乗根では一般化が難しいから，複素数平面の単元で扱うよ。




## 平方根




ここからは累乗根の中でも一番よく使う平方根に限定して話を進めていくよ。




累乗根は $n$ 乗根で考えるからどうしても話の規模が大きくなりがちだよね。




だから， $n=2$ のときに限定することでより深く理解し，スムーズに計算できるようになろう。




平方根ならではの話もあるからじっくり確認してね。




### 平方根の性質


<div class="info-box">


【定理】<strong>平方根の性質</strong>




$a&gt;0$ のとき， $x^2=a$ ならば $x= \pm \sqrt{a}$




$a&lt;0$ のとき， $x^2=a$ ならば $x= \pm \sqrt{a} i$




正の数の平方根は正，負の2つあり，その絶対値は等しい。




$\sqrt{a^2} =|a|= \left \{ \begin{array}{cl} a &amp; (a \geqq 0 のとき) \\ -a &amp; (a&lt;0 のとき) \end{array} \right.$




$a&gt;0$，$b&gt;0$，$k&gt;0$ のとき，


<p style="padding-left: 30px;">$( \sqrt{a} )^2=(- \sqrt{a} )^2=a$</p>
<p style="padding-left: 30px;">$\sqrt{a} \sqrt{b} = \sqrt{ab}$</p>
<p style="padding-left: 30px;">$\displaystyle{ \frac{ \sqrt{a}}{ \sqrt{b}} = \sqrt{ \frac{a}{b}}}$</p>
<p style="padding-left: 30px;">$\sqrt{k^2a} =k \sqrt{a}$</p>
<p style="padding-left: 30px;">$a&lt;b$ ならば $\sqrt{a} &lt; \sqrt{b}$</p>
</div>


ここまでの定理を平方根に限定して抜き出したんだけど，これを定理の具体化というんだ。




どの項目がどの定義，定理に対応しているか，1つずつ確認してみてね。




### 平方根の近似値




根号ってたしかに便利なんだけど，使い続けているとついつい無理数だという認識が薄れて文字のように扱いがち。




部分的には正しいんだけど，「 $\sqrt{2}$ っていくつくらい？」という質問にも常に答えられるようにしてほしい。




そこで，平方根の近似値の求め方を紹介するね。




部分的には平方根だけでなく，他の累乗根にも使えるよ。




まずは，電卓を使う方法。




って言っても電卓の $\sqrt{}$ キーを使うだけ。




これが一番正確で早い。




次に，その平方根が含まれる範囲を小さくしていく方法。


<div class="blank-box bb-green">


例1)


<p style="padding-left: 40px;">$1^2=1$ ， $2^2=4$ より， $1&lt; \sqrt{2} &lt;2$</p>
<p style="padding-left: 40px;">$1.4^2=1.96$ ， $1.5^2=2.25$ より， $1.4&lt; \sqrt{2} &lt;1.5$</p>
<p style="padding-left: 40px;">$1.41^2=1.9881$ ， $1.42^2=2.0164$ より， $1.41&lt; \sqrt{2} &lt;1.42$</p>
<p style="padding-left: 40px;">…</p>
</div>


こうやってその数を平方数で囲むことで範囲を狭めていくんだ。




これを続けると， $\sqrt{2}$ の両側の数の小数部分が限りなく増えていき，より正確な値に近づいていく。




最後に開平法。




開平法とは平方根を筆算で求める方法なんだ。


<div class="blank-box bb-green">


例2)


<p style="padding-left: 40px;">$\sqrt{628.5049}$ の求め方</p>
<ol>
	<li style="list-style-type: none;">
<ol>
	<li>小数点を基準に2桁ずつ区切る。</li>
	<li>一番上の区分の6に注目し，平方した数が6以下になる最大の整数2を立てる。</li>
	<li>左側に2を縦に重ねて書き，下に和の4，6の下に積の4を書く。</li>
	<li>通常の割り算と同様に差の2を書き，28を下ろす。</li>
	<li>$4□ \times □$ が228以下になる最大の整数5を立てる。</li>
	<li>左側の4の右に5を縦に重ねて書き，下に和の50，228の下に積の225を書く。</li>
	<li>差の3を書き，50を下ろす。</li>
	<li>$50□ \times □$ が350以下になる最大の整数0を立てる。</li>
	<li>左側の50の右に0を縦に重ねて書き，下に和の500，350の下に積の0を書く。</li>
	<li>差の350を書き，49を下ろす。</li>
	<li>$500□ \times □$ が35049以下になる最大の整数7を立てる。</li>
	<li>左側の500の右に7を縦に重ねて書き，下に和の5014，35049の下に積の35049を書く。</li>
	<li>差が0となって計算終了。結果，$\sqrt{628.5049}=25.07$</li>
</ol>
</li>
</ol>
<p style="padding-left: 40px;">$\begin{array}{rrrr||r|r|r|r} &amp; &amp; &amp; &amp; 2 &amp; 5. &amp; 0 &amp; 7 \\ \hline 2 &amp; &amp; &amp; &amp; 6 &amp; 28. &amp; 50 &amp; 49 \\ 2 &amp; &amp; &amp; &amp; 4 &amp; &amp; &amp; \\ \hline 4 &amp; 5 &amp; &amp; &amp; 2 &amp; 28 &amp; &amp; \\ &amp; 5 &amp; &amp; &amp; 2 &amp; 25 &amp; &amp; \\ \hline 5 &amp; 0 &amp; 0 &amp; &amp; &amp; 3 &amp; 50 &amp; \\ &amp; &amp; 0 &amp; &amp; &amp; &amp; 0 &amp; \\ \hline 5 &amp; 0 &amp; 0 &amp; 7 &amp; &amp; 3 &amp; 50 &amp; 49 \\ &amp; &amp; &amp; 7 &amp; &amp; 3 &amp; 50 &amp; 49 \\ \hline 5 &amp; 0 &amp; 1 &amp; 4 &amp; &amp; &amp; &amp; 0 \\ \end{array}$</p>
</div>


### 平方根の近似値の一覧




すべてを覚える必要はないけど， $\sqrt{2}$ ， $\sqrt{3}$ ， $\sqrt{5}$ くらいは覚えておこうね。


<ul>
	<li>$\sqrt{2} =1.41421356……$<br />
ひとよひとよにひとみごろ(ひと夜ひと夜に人見ごろ)</li>
	<li>$\sqrt{3} =1.7320508……$<br />
ひとなみにおごれや(人並みにおごれや)</li>
	<li>$\sqrt{5} =2.23606797……$<br />
ふじさんろくおうむなく(富士山麓オウム鳴く)</li>
	<li>$\sqrt{6} =2.4494897……$<br />
によよくよく(似よよくよく) ※最後の「く」は四捨五入</li>
	<li>$\sqrt{7} =2.6457513……$<br />
(な)にむしいない(菜に虫いない)</li>
	<li>$\sqrt{8} =2.8284271……$<br />
にやにやよぶな(ニヤニヤ呼ぶな)</li>
	<li>$\sqrt{10} =3.1622776……$<br />
(ひとまるは)みついろにならぶ(一丸は3色2並ぶ)</li>
</ul>


### 2重根号


<div class="info-box">


【定理】<strong>2重根号</strong>




$a&gt;0$，$b&gt;0$ のとき，


<p style="padding-left: 40px;">$\sqrt{(a+b)+2 \sqrt{ab}} = \sqrt{a} + \sqrt{b}$</p>


$a&gt;b&gt;0$ のとき，


<p style="padding-left: 40px;">$\sqrt{(a+b)-2 \sqrt{ab}} = \sqrt{a}- \sqrt{b}$</p>
</div>


2重根号とは，根号の中に根号が入っている状態のこと。




当然，2重根号があれば3重根号もあるし，平方根に限らないんだけど，上の定理のように変形する方法はどれも同じ。




平方根であれば，中身を何かの2乗の形に，$n$ 乗根であれば $n$ 乗の形に因数分解するんだ。




上の例でいうと，




$a&gt;0$，$b&gt;0$ のとき，


<p style="padding-left: 40px;">$\sqrt{(a+b)+2 \sqrt{ab}}$</p>
<p style="padding-left: 40px;">$= \sqrt{ ( \sqrt{a} )^2 +2 \sqrt{a} \sqrt{b} +( \sqrt{b} )^2 }$</p>
<p style="padding-left: 40px;">$= \sqrt{( \sqrt{a} + \sqrt{b} )^2}$</p>
<p style="padding-left: 40px;">$= \sqrt{a} + \sqrt{b}$</p>


現段階では，$n$ 乗の形に変形できないものは2重根号をはずすことはできないと考えよう。




あと，平方根の2重根号で気をつけなければいけないのが定理の2つ目。




$\sqrt{( \sqrt{a} - \sqrt{b} )^2}$ と因数分解するところまでは同じなんだけど，この段階で $\sqrt{a} - \sqrt{b}$ が正になるようにしなければいけない。




なぜなら， $\sqrt{}$ は正って定義されているからね。




因数分解的には $( \sqrt{a} - \sqrt{b} )^2$ でも $( \sqrt{b} - \sqrt{a} )^2$ でもいいんだけど，根号がはずれたあとに負にならない方を選ぼう。




まあ，定理のような変形であれば，常に $a$ と $b$ を大きい順に書く癖をつければ大丈夫だけどね。




## 対数


<div class="info-box">


【定義】




<strong>対数</strong>：$a&gt;0$，$a \neq 1$ とするとき，任意の正の数 $M$ に対して，$a^p=M$ となる実数 $p$ がただ1つ定まる。この $p$ の値を $\boldsymbol{\log_{a} M}$ (ログ $a$ 底の $M$ と読む)で表し，$a$ を<strong>底</strong>とする $M$ の<strong>対数</strong>という。また，$M$ をこの対数の<strong>真数</strong>という。なお，$a^p&gt;0$ であるから，<strong>真数</strong> $\boldsymbol{M}$ <strong>は正の数</strong>でなければならない。




$a&gt;0$，$a \neq 1$，$M&gt;0$ のとき


<p style="padding-left: 40px;">$a^p=M$ $\Leftrightarrow$ $p= \log_{a} M$</p>
<p style="padding-left: 40px;">$\log_{a} a^p =p$</p>
<p style="padding-left: 40px;">$a^{ \log_{a} M }=M$</p>


<strong>常用対数</strong>：底が10の対数




<strong>小数首位</strong>：$0&lt;M&lt;1$ である小数 $M$ の初めて $0$ でない数字が現れる位




【定理】<strong>対数の性質</strong>




$a&gt;0$，$b&gt;0$，$c&gt;0$，$a \neq 1$，$b \neq 1$，$c \neq 1$，$M&gt;0$，$N&gt;0$，$k$ は実数のとき


<ul>
	<li>$\log_{a} a=1$</li>
	<li>$\log_{a} 1=0$</li>
	<li>$\log_{a} \frac{1}{a} =-1$</li>
	<li>$\log_{a} MN= \log_{a} M + \log_{a} N$</li>
	<li>$\log_{a} \displaystyle \frac{M}{N} = \log_{a} M - \log_{a} N$　特に　$\log_{a} \displaystyle \frac{1}{N} =- \log_{a} N$</li>
	<li>$\log_{a} M^k=k \log_{a} M$　特に　$\log_{a} \sqrt[n]{M} = \displaystyle \frac{1}{n} \log_{a} M$</li>
	<li><strong>底の変換公式</strong>：$\log_{a} b = \displaystyle \frac{ \log_{c} b }{ \log_{c} a }$　特に　$\log_{a} b = \displaystyle \frac{1}{ \log_{b} a }$</li>
</ul>


【定理】<strong>桁数・小数首位と常用対数</strong>


<p style="padding-left: 30px;">自然対数 $N$ が $n$ 桁 $\Leftrightarrow$ $10^{n-1} \leqq N&lt;10^n$ $\Leftrightarrow$ $n-1 \leqq \log_{10} N&lt;n$</p>
<p style="padding-left: 30px;">小数首位が小数第 $n$ 位 $\Leftrightarrow$ $\frac{1}{10^n} \leqq M&lt; \frac{1}{10^{n-1}}$ $\Leftrightarrow$ $-n \leqq \log_{10} M&lt;-n+1$</p>
</div>


$2$ の累乗は，$2^1=1$ ， $2^2=4$ ， $2^3=8$ ，…というように続いていくよね？




じゃあ， $2$ を何乗したら $3$ になるのかな？というのを考えたのが対数。




この場合， $2$ を $\log_{2} 3$ 乗したものが $3$ ，つまり， $2^{ \log_{2} 3 }=3$ ということ。




対数は $\log_{2} 8=3$ のように有理数で表せることもあるけど， $\log_{2} 3$ のように無理数のものもあるんだ。




対数にも多くの性質があるから，それを使った計算ができるようになることも大事なんだけど， $\log_{a} M$ は $a$ を $M$ にするような指数，という定義を忘れないでね。




### 対数と桁数




対数を使うと，今までできなかった桁数の計算ができるようになる。




例えば，今までは $2^{100}$ が何桁になるか分からなかったけど，底が $10$ である常用対数を使うことで， $2^{100}$ が $10$ の何乗なのか求めることができ，そこから桁数が分かるんだ。




常用対数は無理数も含めて値がすでに求められていて，例えば $\log_{10} 2=0.3010$ (概数)だから，それを使うと以下のように計算できる。


<p style="padding-left: 40px;">$\log_{10} 2^{100}=100 \log_{10} 2=100 \cdot 0.3010=30.1$</p>
<p style="padding-left: 40px;">$\Leftrightarrow 2^{100}=10^{30.1}$</p>


$10^{30.1}$ は $10^{30}&lt;10^{30.1}&lt;10^{31}$ だから， $1,000,000,000,000,000,000,000,000,000,000$ より大きく， $10,000,000,000,000,000,000,000,000,000,000$ より小さい。




つまり，$2^{100}$ は31桁の数になる，ということ。




同じようにして， $2^{-100}$ の小数第何位に初めて0でない数が現れるかも計算することもできるよ。




### 対数と身近な単位




例えば常用対数の場合，




$\log_{10} 10=$1 ， $\log_{10} 100=2$ ， $\log_{10} 1000=3$ ， $\log_{10} 10000=4$ ，…




というように，真数が10，100，1000と，隣同士の差がどんどん大きくなっているのに対して，値は1，2，3と1ずつ増えていっている。




つまり，対数の値は桁数を表しているとも考えられるから，値の範囲が大きいものを表すのに適していてるといえる。




例えば，地震の規模を表すマグニチュードや，星の明るさを表す等級とかね。




これらは地球規模，宇宙規模の指標だから，小さいものお大きいものの差が大きく，その数値を直接表すと比較ができないんだ。




## 複素数


<div class="info-box">


$a$，$b$，$c$，$d$ を実数とする。




【定義】




<strong>共役な複素数</strong>：複素数 $a+bi$ に対する複素数 $a-bi$


<p style="padding-left: 30px;">※ $a+bi$ と $a-bi$ は互いに共役な複素数である。</p>
<p style="padding-left: 30px;">※複素数 $\alpha$ に対して，共役な複素数を $\overline{\alpha}$ と表す。</p>


【定理】<strong>複素数の相等</strong>




$a+bi=c+di$ $\Leftrightarrow$ $a=c$ かつ $b=d$




特に $a+bi=0$ $\Leftrightarrow$ $a=b=0$




【定理】<strong>共役な複素数の性質</strong>




$\alpha$，$\beta$ を複素数とすると


<ul>
	<li>$\overline{\alpha + \beta} = \overline{\alpha} + \overline{\beta}$</li>
	<li>$\overline{\alpha-\beta} = \overline{\alpha}-\overline{\beta}$</li>
	<li>$\overline{\alpha \beta} = \overline{\alpha} \cdot \overline{\beta}$</li>
	<li>$\displaystyle \overline{\left( \frac{\alpha}{\beta} \right)} = \frac{\overline{\alpha}}{\overline{\beta}}$</li>
	<li>$\overline{\alpha ^n} =( \overline{\alpha} )^n$ ($n$ は自然数)</li>
	<li>$k$ が実数のとき $\overline{k} =k$，$\overline{k \alpha} =k \overline{\alpha}$</li>
</ul>


【定理】$\boldsymbol{n}$ <strong>次方程式の解</strong>




実数係数の $n$ 次方程式が虚数解 $\alpha$ をもつならば，共役な複素数 $\overline{\alpha}$ も解である。


</div>


共役な複素数について詳しくは方程式や複素数平面の講で解説するけど，複素数の大事な基本事項だから押さえておこう。




まず，虚数単位 $i$ の定義は「2乗すると $-1$ になる2つの数のうちの1つ」で，虚数単位の符号は特定できないから，1つの式の中では $i= \sqrt{-1}$ か $i=- \sqrt{-1}$ のどちらで考えてもよかったよね。




そういった事情もあって，複素数では虚部の絶対値が等しい2つの数を同時に扱うということがよくある。




だから，複素数 $\alpha$ に対して，虚部の符号が逆の複素数を共役な複素数 $\overline{ \alpha }$ としたんだ。




複素数とその共役な複素数を同時に扱う，というのは方程式の講で実感してもらいたいから，ここでは共役な複素数の性質をそれぞれ理解し，使えるようになるところまでで留めておこう。




次に複素数の相当だけど，これは実数の相当の拡張になっている。




実数の相当は，実部が等しければよかったけど，複素数では実部と虚部の両方が等しくないといけない。




逆に，複素数が等しければ，実部と虚部がそれぞれ等しいということがいえる。




複素数は和の形で表されるから，実部と虚部をいじることで，見た目は違うけど等しい複素数が存在しそうに感じるけど，そんなことはないということをしっかり覚えておこう。




以下，複素数の計算をまとめてみたよ。


<div class="blank-box bb-blue">


<strong>複素数の計算</strong>




$a$，$b$ を実数，$\alpha$，$\beta$ を複素数とする。




<strong>複素数の四則演算</strong>


<ul>
	<li>$i^2=-1$ とするほかは，文字 $i$ の式と考えて行う。</li>
</ul>


<strong>共役な複素数</strong>


<ul>
	<li>共役な複素数の和と積はともに実数である。</li>
	<li>$(a+bi)+(a-bi)=2a$</li>
	<li>$(a+bi)(a-bi)=a^2-(bi)^2=a^2+b^2$</li>
</ul>


<strong>複素数の積</strong>


<ul>
	<li>$\alpha \beta =0$ $\Rightarrow$ $\alpha =0$ または $\beta =0$</li>
</ul>


<strong>負の数の平方根</strong>


<ul>
	<li>$a&gt;0$ のとき $\sqrt{-a} = \sqrt{a} i$</li>
	<li>負の数 $-a$ の平方根は $\pm \sqrt{-a} = \pm \sqrt{a} i$</li>
</ul>
</div>


この中でも共役な複素数の和と積が実数になるというのは不思議だよね。




## <strong>数の範囲と四則演算</strong>


<div class="info-box">


【定義】




<strong>閉じている</strong>：その集合の要素を用いた演算の結果がもとの集合に属すること


</div>


具体的な数で計算するときにはいいけど，文字で置くときには十分注意する必要があるのが数の範囲。




例えば，自然数と自然数の和はすべて自然数になるけど，差は自然数でない数になることがあるよね。




これを，自然数は和について閉じているけど，差については閉じていない，というんだ。




前提を有理数，実数，複素数にすれば四則演算について閉じているから注意する必要はないけど，閉じていない演算を含む数を扱うときには気をつけてね。




それぞれの集合に対して，四則演算について閉じているかどうかまとめると以下のようになる。


<div class="blank-box bb-blue">


閉じている：○　閉じていない：×


<table style="border-collapse: collapse; width: 100%;">
<tbody>
<tr>
<td style="width: 20%; text-align: center;"> </td>
<td style="width: 20%; text-align: center;">和</td>
<td style="width: 20%; text-align: center;">差</td>
<td style="width: 20%; text-align: center;">積</td>
<td style="width: 20%; text-align: center;">商</td>
</tr>
<tr>
<td style="width: 20%; text-align: center;">自然数</td>
<td style="width: 20%; text-align: center;">○</td>
<td style="width: 20%; text-align: center;">×</td>
<td style="width: 20%; text-align: center;">○</td>
<td style="width: 20%; text-align: center;">×</td>
</tr>
<tr>
<td style="width: 20%; text-align: center;">整数</td>
<td style="width: 20%; text-align: center;">○</td>
<td style="width: 20%; text-align: center;">○</td>
<td style="width: 20%; text-align: center;">○</td>
<td style="width: 20%; text-align: center;">×</td>
</tr>
<tr>
<td style="width: 20%; text-align: center;">有理数</td>
<td style="width: 20%; text-align: center;">○</td>
<td style="width: 20%; text-align: center;">○</td>
<td style="width: 20%; text-align: center;">○</td>
<td style="width: 20%; text-align: center;">○</td>
</tr>
<tr>
<td style="width: 20%; text-align: center;">無理数</td>
<td style="width: 20%; text-align: center;">×</td>
<td style="width: 20%; text-align: center;">×</td>
<td style="width: 20%; text-align: center;">×</td>
<td style="width: 20%; text-align: center;">×</td>
</tr>
<tr>
<td style="width: 20%; text-align: center;">実数</td>
<td style="width: 20%; text-align: center;">○</td>
<td style="width: 20%; text-align: center;">○</td>
<td style="width: 20%; text-align: center;">○</td>
<td style="width: 20%; text-align: center;">○</td>
</tr>
<tr>
<td style="width: 20%; text-align: center;">虚数</td>
<td style="width: 20%; text-align: center;">×</td>
<td style="width: 20%; text-align: center;">×</td>
<td style="width: 20%; text-align: center;">×</td>
<td style="width: 20%; text-align: center;">×</td>
</tr>
<tr>
<td style="width: 20%; text-align: center;">複素数</td>
<td style="width: 20%; text-align: center;">○</td>
<td style="width: 20%; text-align: center;">○</td>
<td style="width: 20%; text-align: center;">○</td>
<td style="width: 20%; text-align: center;">○</td>
</tr>
</tbody>
</table>


※除法では，0で割ることは考えないものとする。


</div>


## 第6講のまとめ




中高数学で扱う数の果て，理解してもらえたかな？




今まで表せなかった数が次々と表せるようになると，できることがどんどん増えていく。




これは数学の楽しさの1つだよね。




第7講は整数について深掘りしていくよ。




http://mathrao.com/instant-jhmath-provisional-5/




http://mathrao.com/instant-jhmath-provisional-7/
