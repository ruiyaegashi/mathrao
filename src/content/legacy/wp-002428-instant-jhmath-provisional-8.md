---
title: "【インスタント中高数学】第8講 未知なる解を求めて①【恒等式・方程式・不等式】"
wp_id: 2428
content_type: "post"
status: "publish"
published_at: "2019-06-07 12:04:50"
wp_date: "2019-06-07 12:04:50"
modified_at: "2019-06-15 20:52:08"
legacy_url: "http://mathrao.com/instant-jhmath-provisional-8/"
legacy_path: "/instant-jhmath-provisional-8/"
legacy_slug: "instant-jhmath-provisional-8"
former_slugs: []
parent_wp_id: null
parent_title: null
hierarchy: ["【インスタント中高数学】第8講 未知なる解を求めて①【恒等式・方程式・不等式】"]
category: ["インスタント中高数学【草稿】"]
tags: []
mathrao_section: "インスタント中高数学"
mathrao_grade: null
mathrao_course: null
source_content_sha256: "66ef15102ec8ecc39d2a6dd85606011e420dba3ffea9225d0c4a53d2603fce57"
---

http://mathrao.com/instant-jhmath-provisional-7/




## 数学の醍醐味




君は数学を楽しんでいるかな？




僕にとっては，普通に考えたら答えが出ない，あるいは，ものすごく時間がかかる問題をサッと解くのが1つの醍醐味。




単純に気持ちがいいのもあるけど，思いがけない答えが出たときは興奮するからね。




僕の経験上，数学があまり好きではない人は日常生活と結びついた問題のほうが興味を持ちやすい傾向にある。




実際，日常とかけ離れたこんな高度なことをやってなんの意味があるんだ，って学ぶ意味を見失うのも理解できる。




けど，そこから1歩進んで，現実世界では考えられない色々な事象を数式を使って考えることで，美しい答えや関係性が見えてくることに感動できるようになると，数学はもっともっと面白くなるんだ。




数学の本質，論理的思考力はもちろん大事な要素だけど，有用なだけでモチベーションが保てるほど人というのは単純じゃない。




自分の心が突き動かされる，純粋な好奇心，感動があってこそじゃないかな。




この講では中高数学の代名詞の1つである方程式を扱うよ。




条件から式を立てて解を求める，まさに未知の探求。




## 等式と不等式


<div class="info-box">


【定義】




<strong>等式</strong>：等号を使って数量の関係を表した式




<strong>恒等式</strong>：含まれている各文字にどのような値を代入しても，その両辺の式の値が存在する限り，等号が常に成り立つ等式




$x$ についての<strong>方程式</strong>：$x$ の値によって成り立ったり成り立たなかったりする等式




<strong>不等式</strong>：不等号を使って数量の関係を表した式




<strong>左辺</strong>：等式，不等式において，等号，不等号の左側の式




<strong>右辺</strong>：等式，不等式において，等号，不等号の右側の式




<strong>両辺</strong>：左辺と右辺の総称




<strong>比例式</strong>：2つの比が等しいことを表した式




【定理】<strong>等式の性質</strong>




$A$ ， $B$ を複素数とする。


<ul>
	<li>$A=B$ かつ $B=C$ $\Rightarrow$ $A=C$</li>
	<li>$A=B$ $\Leftrightarrow$ $A+C=B+C$ ， $A-C=B-C$</li>
	<li>$A=B$ $\Leftrightarrow$ $AC=BC$</li>
	<li>$A=B$ かつ $C \neq 0$ $\Leftrightarrow$ $\frac{A}{C} = \frac{B}{C}$</li>
	<li>$A=B$ かつ $C=D$ $\Rightarrow$ $A+C=B+D$<br />
※この操作を左辺同士，右辺同士を加えるという意味で「辺々を加える」ということがある。</li>
	<li>$A=B$ かつ $C=D$ $\Rightarrow$ $A-C=B-D$<br />
※この操作を左辺同士，右辺同士の差をとるという意味で「辺々の差をとる」ということがある。</li>
	<li>$A=B$ かつ $C=D$ $\Rightarrow$ $AC=BD$</li>
	<li>$A=B$ かつ $C=D \neq 0$ $\Rightarrow$ $\frac{A}{C} = \frac{B}{D}$</li>
</ul>


【定理】<strong>比の性質</strong>


<ul>
	<li>もとの比と，その左右に同じ数をかけた比は等しい。</li>
	<li>もとの比と，その左右を $0$ でない同じ数で割った比は等しい。</li>
</ul>


【定理】<strong>比例式の性質</strong>




$a:b=c:d$ $\Leftrightarrow$ $ad=bc$


</div>


まずは等号「 $=$ 」について改めて考えてみよう。




小学校までは，「 $1+1=2$ 」=「 $1+1は2$ 」のように，計算とその結果をつなぐもの，という認識が強かったんじゃないかな？




中高数学では，あくまで左辺と右辺が等しい，ということを表していると考えよう。




天秤が釣り合うのをイメージすると分かりやすいかも。




「 $1+1$ 」と「 $2$ 」は釣り合うから，「 $1+1=2$ 」と書けるし，当然，「 $2=1+1$ 」でもあるよね。




また，等式は天秤なので，バランスが崩れなければ何をしてもいいんだ。




例えば，両辺に $1$ を足す「 $1+1=2$ 」→「 $1+1+1=2+1$」とか，両辺を2乗する「 $(1+1)^2=2^2$ 」のように，基本的には両辺に同じ計算をする分にはバランスは崩れないよ。




この性質を利用した，よく使われる操作を2つ覚えておこう。


<div class="blank-box bb-blue">


<strong>移項</strong>




例えば， $2x+3=5$ という等式において両辺から $3$ を引くと， $2x=5-3$ となる。




変形前後を見比べると，左辺にあった $3$ が右辺へ符号を変えて移ったように見えるため，等号をまたいで項を移すという意味で移項という。




<strong>(文字)について解く</strong>




例えば， $\displaystyle \frac{a+b}{2} =c$ という等式において，両辺を2倍し， $b$ を右辺へ移項する。


<p style="padding-left: 40px;">$\displaystyle \frac{a+b}{2} =c$</p>
<p style="padding-left: 40px;">$a+b=2c$</p>
<p style="padding-left: 40px;">$a=2c-b$</p>


このように，元の等式を $a=$ の形に変形することを， $a$ について解くという。




(文字)について解けといわれたら，例のように左辺，または，右辺に指定された(文字)だけがある状態に変形しよう。


</div>


そして，文字を含む等式は，等式を成り立たせる値が限定されているかいないかで方程式と恒等式に分けられる。




同じような文字を含む式だけど，扱い方が全然違うから注意が必要だよ。




あと，等式の中では特殊な比例式というものがある。




等式のほとんどは両辺に演算を含んでいるけど，比例式は両辺が比になっていて，それらが等しいことを表しているんだ。




とはいえ，比例式の性質を使って $a:b=c:d$ を $ad=bc$ と変形すれば，両辺が演算で表された等式になるからね。




ここから恒等式，方程式，不等式について具体的に考えていくけど，特にことわりがなければ $x$ の整式の係数( $a$ ， $b$ ，…)は実数で，最高次数の係数は $0$ でないと考えてね。




## 恒等式


<div class="info-box">


【定理】<strong>恒等式の性質</strong>




$P$，$Q$ が $x$ についての整式であるとき


<p style="padding-left: 30px;">$P=0$ が恒等式 $\Leftrightarrow$ $P$ の各項の係数は全て0</p>
<p style="padding-left: 30px;">$P=Q$ が恒等式 $\Leftrightarrow$ $P$ と $Q$ の次数は等しく，両辺の同じ次数の項の係数はそれぞれ等しい。</p>


$P$，$Q$ が $x$ についての $n$ 次以下の整式であるとき


<p style="padding-left: 30px;">等式 $P=Q$ が $(n+1)$ 個の異なる $x$ の値に対して成り立つ $\Leftrightarrow$ 等式 $P=Q$ は $x$ についての恒等式</p>
</div>


恒等式とは，含まれている各文字にどのような値を代入しても，その両辺の式の値が存在する限り，等号が常に成り立つ等式のこと。




別の言い方をすれば，恒等式の左辺は右辺を，右辺は左辺を変形したものなんだ。




例えば，展開，因数分解の乗法公式 $(a+b)^2=a^2+2ab+b^2$ も，両辺の $a$ ， $b$ に何を代入しても等号が成立するから恒等式だよね。




とはいえ，こういった変形公式だけで恒等式が使われるわけではない。




恒等式では係数に着目すると，とても有用な性質があるんだ。




例えば，


<ul>
	<li>$ax^2+bx+c=0$ が $x$ についての恒等式のとき， $a=b=c=0$</li>
	<li>$ax^2+bx+c=dx^2+ex+f$ が $x$ についての恒等式のとき， $a=d$ かつ $b=e$ かつ $c=f$</li>
	<li>$ax^2+bx+c=0$ を満たす $x$ が3つあるとき， $ax^2+bx+c=0$ は $x$ についての恒等式</li>
</ul>


といった具合にね。




そもそも，恒等式なら文字には何が入ってもいいという前提だから，係数に着目することの方が多いんだよ。




これらの性質を利用して未知の係数を求める方法をまとめておくね。


<div class="blank-box bb-blue">


<strong>未定係数法</strong>




恒等式の未知の係数(未定係数)を求めるには，恒等式の性質を利用した2通りの方法がある。


<ul>
	<li><strong>係数比較法</strong>：両辺の同じ次数の項の係数がそれぞれ等しい。</li>
	<li><strong>数値代入法</strong>：両辺に適当な数字をいくつか代入して，連立方程式などを解く。数値代入法を用いた場合，逆の確認が必要となる。</li>
</ul>
</div>


係数比較法は性質をそのまま利用しているからいいんだけど，数値代入法ではすべての数の中からいくつかピックアップして利用しているから，それだけでは十分だとはいえない。




だから，数値代入法では，「求めた係数であれば恒等式になる」=「逆」の確認が必要になるんだ。




数学では問題 $p$ と解答 $q$ は同値でなければいけないから， $p \Rightarrow q$ だけでなく，逆 $q \Rightarrow p$ も示して， $p$ と $q$ が同値 $p \Leftrightarrow q$ であることを示す，ということを常に意識しよう。




## $n$ 次方程式


<div class="info-box">


【定義】




$x$ についての $\boldsymbol{n}$ <strong>次方程式</strong>：$x$ の次数が $n$ の方程式




<strong>高次方程式</strong>：3次以上の方程式




$x$ についての方程式の<strong>解</strong>：方程式を成り立たせる $x$ の値




<strong>実数解</strong>：実数の解




<strong>虚数解</strong>：虚数の解




$\boldsymbol{n}$ <strong>重解</strong>：方程式が $(x- \alpha)^nQ(x)=0$，$Q(\alpha) \neq 0$ の形になるときの解 $\alpha$




<strong>重解</strong>：$n$ 重解の総称




方程式を<strong>解く</strong>：方程式の解を求めること




【定理】<strong>数や式についての性質</strong>




一般に，数や式について，


<p style="padding-left: 30px;">$AB=0$ $\Leftrightarrow$ $A=0$ または $B=0$</p>


【定理】<strong>方程式の解の性質</strong>




実数を係数とする $n$ 次方程式が虚数解 $\alpha$ をもつならば，$\alpha$ と共役な複素数 $\overline{\alpha}$ も解である。




$n$ 重解を解が $n$ 個と数えるとき，$n$ 次方程式は，複素数の範囲に必ず $n$ 個の解をもつ。


</div>


方程式というのは代入する値によって成り立ったり成り立たなかったりする等式のことで，その種類や作り方，使われ方はたくさんある。




ここではその中でも $(x$ の $n$ 次式 $)=0$ の形で表される $n$ 次方程式に限定して，その解を求める方法を考えていくよ。




ちなみに， $n$ 次方程式には，必ず $n$ 個の解があって，2次以上の方程式では虚数解が出てくる場合がある。




3次方程式までは以下の方法で虚数解まで求めることができるけど，4次以上の虚数解は複素数平面の単元で扱うからね。




### 1次方程式の解き方




$n$ 次方程式を解く基本になるのが1次方程式。




1次方程式は $ax+b=0$ のような形をしていて，この式を $x$ について解いた $x=- \frac{b}{a}$ がその解になる。




2次以上の方程式でもこの考え方を使うからしっかり覚えておこう。




### 2次以上の方程式の解き方




2次以上の方程式の解き方はいくつかある。




方程式には，どの方法でも解くことができるものもあれば，現実的にどれか1つの方法でしか解けないものもあるから，すべての方法を習得しよう。




#### 因数分解による解法




この解法では数や式についての性質を利用するよ。




それが，「 $AB=0$ ならば $A=0$ または $B=0$ 」。




掛け算をして $0$ になるということは，その掛けた数の中に少なくとも1つは $0$ があるよね，ということ。




当然，数が3つ以上になっても，「 $ABC=0$ ならば $A=0$ または $B=0$ または $C=0$」のように成り立つよ。




方程式を因数分解できれば，この性質を使って解を求めることができるんだ。




第5講で学んだ因数分解を最大限活用しよう。


<div class="blank-box bb-green">


例1)


<p style="padding-left: 40px;">$x^2-x-2=0$</p>
<p style="padding-left: 40px;">$(x+1)(x-2)=0$</p>
<p style="padding-left: 40px;">$x+1=0$ または $x-2=0$</p>
<p style="padding-left: 40px;">$x=-1$ または $x=2$ ：解</p>
</div>
<div class="blank-box bb-blue">


<strong>因数分解による解法</strong>




一般に，




$ax^2+bx+c=a(x- \alpha )(x- \beta )=0$




$x= \alpha , \beta$ ：解




$ax^3+bx^2+cx+d=a(x- \alpha )(x- \beta )(x-\gamma )=0$




$x= \alpha , \beta , \gamma$ ：解




…


</div>


また，この解法の逆を考えることで，方程式を作ることができるよ。


<div class="blank-box bb-blue">


<strong>2数を解とする2次方程式</strong>




2数 $\alpha$ ， $\beta$ を解とする2次方程式の1つは


<p style="padding-left: 40px;">$(x- \alpha)(x- \beta)=0$ すなわち $x^2-(\alpha + \beta)x+ \alpha \beta =0$</p>


<strong>3数を解とする3次方程式</strong>




3数 $\alpha$ ， $\beta$ ， $\gamma$ を解とする3次方程式の1つは


<p style="padding-left: 40px;">$(x- \alpha )(x- \beta )(x- \gamma )=0$ すなわち $x^3-( \alpha + \beta + \gamma )x^2+( \alpha \beta + \beta \gamma + \gamma \alpha )x- \alpha \beta \gamma =0$</p>


※同様に， $n$ 数を解とする $n$ 次方程式も作ることができる。




<strong>和・積が与えられた2数を解にもつ2次方程式</strong>




和が $p$，積が $q$ である2数は 2次方程式 $x^2-px+q=0$ の2解である。


</div>


#### 累乗根を利用した解法




この方法では累乗根の定義を利用するよ。


<div class="blank-box bb-green">


例2)


<p style="padding-left: 40px;">$x^2=4$</p>
<p style="padding-left: 40px;">$x= \pm 2$ ：解</p>
<p style="padding-left: 40px;">※「2乗すると $4$ になる数→ $4$ の平方根→ $\pm 2$ 」と，定義的に解いた。</p>
</div>
<div class="blank-box bb-green">


例3)


<p style="padding-left: 40px;">$x^2-2x-1=0$ *</p>
<p style="padding-left: 40px;">$x^2-2x+1-2=0$ *</p>
<p style="padding-left: 40px;">$(x-1)^2-2=0$ *</p>
<p style="padding-left: 40px;">$(x-1)^2=2$</p>
<p style="padding-left: 40px;">$x-1= \pm \sqrt{2}$</p>
<p style="padding-left: 40px;">$x=1 \pm \sqrt{2}$ ：解</p>
<p style="padding-left: 40px;">※ $x$ を含んだ $( \ )^2$ を作り出し，同様に定義的に変形したあと，余分な $-1$ を移項して解いた。</p>
<p style="padding-left: 40px;">※ *のついた行の操作を<strong>平方完成</strong>という。</p>
</div>


ちなみに，3次方程式では $( \ )^3$ を作り出す<strong>立体完成</strong>をすることで途中までは変形できるけど，立方根は3つあるから複素数平面を理解するまでは解を求めることができないんだ。




ただ，立方完成をした状態から，公式を使って因数分解に持ち込むことはできるよ。


<div class="blank-box bb-green">


例4)


<p style="padding-left: 40px;">$x^3+3x^2+3x-7=0$</p>
<p style="padding-left: 40px;">$x^3+3x^2+3x+1-8=0$</p>
<p style="padding-left: 40px;">$(x+1)^3-2^3=0$</p>
<p style="padding-left: 40px;">$\left\{ (x+1)-2 \right\} \left\{ (x+1)^2+(x+1) \cdot 2+2^2 \right\} =0$</p>
<p style="padding-left: 40px;">$(x-1)(x^2+4x+7)=0$</p>
<p style="padding-left: 40px;">$x-1=0$ または $x^2+4x+7=0$</p>
<p style="padding-left: 40px;">$x=1, -2 \pm \sqrt{3} i$</p>
</div>


とはいえ，この場合実数解 $x=1$ を持つから，因数定理を使って最初から因数分解できてほしい問題ではあるかな。




ちなみに，最後から2行目の $x^2+4x+7=0$ は，例3のように累乗根を利用するか，次の解の公式で解くことができるよ。




#### 解の公式による解法


<div class="info-box">


【定理】<strong>2次方程式の解の公式</strong>




2次方程式 $ax^2+bx+c=0$ の解は


<p style="padding-left: 30px;">$x= \displaystyle{\frac{-b \pm \sqrt{b^2-4ac}}{2a}}$</p>


特に $b=2b'$ のとき


<p style="padding-left: 30px;">$x= \displaystyle{\frac{-b' \pm \sqrt{b'^2-ac}}{a}}$</p>
</div>


これが2次方程式を問答無用に解くことができる公式。




問題では頻繁に出てくるし， $x$ の係数が偶数のときの公式は約分を省けるからぜひ覚えておこう。




以下がその証明。


<div class="blank-box bb-blue">


<strong>2次方程式の解の公式の証明</strong>


<p style="padding-left: 40px;">$ax^2+bx+c=0$</p>
<p style="padding-left: 40px;">$a(x^2+ \frac{b}{a} x)+c=0$</p>
<p style="padding-left: 40px;">$a(x^2+ \frac{b}{a} x+ \frac{b^2}{4a^2} - \frac{b^2}{4a^2} )+c=0$</p>
<p style="padding-left: 40px;">$a \left\{ (x+ \frac{b}{2a} )^2 - \frac{b^2}{4a^2} \right\} +c=0$</p>
<p style="padding-left: 40px;">$a(x+ \frac{b}{2a} )^2 - \frac{b^2}{4a} +c=0$</p>
<p style="padding-left: 40px;">$a(x+ \frac{b}{2a} )^2 = \frac{b^2}{4a} -c$</p>
<p style="padding-left: 40px;">$a(x+ \frac{b}{2a} )^2 = \frac{b^2-4ac}{4a}$</p>
<p style="padding-left: 40px;">$(x+ \frac{b}{2a} )^2 = \frac{b^2-4ac}{4a^2}$</p>
<p style="padding-left: 40px;">$x+ \frac{b}{2a} = \pm \frac{ \sqrt{b^2-4ac}}{2a}$</p>
<p style="padding-left: 40px;">$x=- \frac{b}{2a} \pm \frac{ \sqrt{b^2-4ac}}{2a}$</p>
<p style="padding-left: 40px;">$x=\frac{-b \pm \sqrt{b^2-4ac}}{2a}$</p>


特に， $b=2b'$ のとき，


<p style="padding-left: 40px;">$x=\frac{-2b' \pm \sqrt{(2b')^2-4ac}}{2a}$</p>
<p style="padding-left: 40px;">$x=\frac{-2b' \pm \sqrt{4b'^2-4ac}}{2a}$</p>
<p style="padding-left: 40px;">$x=\frac{-2b' \pm 2 \sqrt{b'^2-ac}}{2a}$</p>
<p style="padding-left: 40px;">$x=\frac{-b' \pm \sqrt{b'^2-ac}}{a}$</p>
</div>


3次方程式にも解の公式はあるんだけど，かなり長いから暗記するのは難しいだろうね。




ちなみに，解の公式を使うことで，すべての2次式を因数分解することができる。




上にあるように，2次方程式 $ax^2+bx+c=0$ の2解を $\alpha$ ， $\beta$ とすると，


<p style="padding-left: 40px;">$ax^2+bx+c=a(x- \alpha )(x- \beta )$</p>


と因数分解できるから，この2解と解の公式を対応させれば，


<p style="padding-left: 40px;">$ax^2+bx+c=a \left( x- \displaystyle{\frac{-b+ \sqrt{b^2-4ac}}{2a}} \right) \left( x- \displaystyle{\frac{-b- \sqrt{b^2-4ac}}{2a}} \right)$</p>


となる。




本当は因数分解の講で扱いたかったんだけど，解の公式を理解してからじゃないと意味がないからね。




## 方程式の解に関する性質




### 解と係数の関係


<div class="info-box">


【定理】<strong>2次方程式の解と係数の関係</strong>




2次方程式 $ax^2+bx+c=0$ の2つの解を $\alpha$，$\beta$ とすると


<p style="padding-left: 30px;">$\alpha + \beta =- \displaystyle \frac{b}{a}$</p>
<p style="padding-left: 30px;">$\alpha \beta = \displaystyle \frac{c}{a}$</p>


【定理】<strong>3次方程式の解と係数の関係</strong>




3次方程式 $ax^3+bx^2+cx+d=0$ の3つの解を $\alpha$，$\beta$，$\gamma$ とすると


<p style="padding-left: 30px;">$\alpha + \beta + \gamma =- \displaystyle \frac{b}{a}$</p>
<p style="padding-left: 30px;">$\alpha \beta + \beta \gamma + \gamma \alpha = \displaystyle \frac{c}{a}$</p>
<p style="padding-left: 30px;">$\alpha \beta \gamma =- \displaystyle \frac{d}{a}$</p>
</div>


因数分解による解法と方程式の作り方から，以下のような恒等式が成り立つ。




$\alpha$ ， $\beta$ ， $\gamma$ を解とすると，


<p style="padding-left: 40px;">$ax^2+bx+c$<br />
$=a(x- \alpha )(x- \beta )$<br />
$=ax^2-a(\alpha + \beta)x+a \alpha \beta$</p>
<p style="padding-left: 40px;">$ax^3+bx^2+cx+d$<br />
$=a(x- \alpha )(x- \beta )(x-\gamma )$<br />
$=ax^3-a( \alpha + \beta + \gamma )x^2+a( \alpha \beta + \beta \gamma + \gamma \alpha )x-a \alpha \beta \gamma$</p>


恒等式の性質を利用してそれぞれの1行目と3行目の係数を比較することで，解と係数の関係を導けるんだ。




当然，4次方程式以上でも同様の関係は成り立つけど，次数が増えるほど左辺が煩雑になっていくから要注意。




この解と係数の関係から分かるのは，方程式の解というのは2次，3次方程式でも有理数，無理数，虚数といろいろな形があるにもかかわらず，解の和や積は必ず実数で表されるということ。




方程式の係数さえ分かっていれば，具体的な解を求めなくても左辺のような和や積を扱えるんだ。




解を求めろという問題ではなく解を利用するような問題では，わざわざ解を求めてから進めるのではなく，左辺のような形のまま扱うことで解答を簡略化することもできるよ。




### 2次方程式の解の種類の判別




2次方程式 $ax^2+bx+c=0$ の解は $x=\frac{-b \pm \sqrt{b^2-4ac}}{2a}$ だから， $\sqrt{ \ }$ の中身を調べることで解の種類を判別することができるんだ。




$\sqrt{ \ }$ の中身が正なら $\pm \sqrt{ \ }$ となるから実数解が2つ，中身が $0$ なら $\pm 0$ になって， $\sqrt{ \ }$ の部分が消えるから実数解が1つ，中身が負なら $\pm \sqrt{ \ } i$ となって虚数解が2つになる。




この $\sqrt{ \ }$ の中身 $\boldsymbol{D=b^2-4ac}$ を<strong>判別式</strong>というよ。


<table style="border-collapse: collapse; width: 100%; height: 231px;" border="1">
<tbody>
<tr style="height: 20px;">
<td style="width: 25%; text-align: center; height: 20px;">$D$ の符号</td>
<td style="width: 25%; text-align: center; height: 20px;">$D&gt;0$</td>
<td style="width: 25%; text-align: center; height: 20px;">$D=0$</td>
<td style="width: 25.1222%; text-align: center; height: 20px;">$D&lt;0$</td>
</tr>
<tr style="height: 71px;">
<td style="width: 25%; text-align: center; height: 150px;" rowspan="2">実数解</td>
<td style="width: 25%; text-align: center; height: 71px;">


異なる2つの実数解<br />
$x= \displaystyle{\frac{-b \pm \sqrt{b^2-4ac}}{2a}}$


</td>
<td style="width: 25%; text-align: center; height: 71px;">


重解<br />
$x=- \displaystyle \frac{b}{2a}$


</td>
<td style="width: 25.1222%; text-align: center; height: 150px;" rowspan="2">異なる2つの虚数解<br />
$x= \displaystyle{\frac{-b \pm \sqrt{b^2-4ac}}{2a}}$<br />
※2つの虚数解は互いに共役な複素数</td>
</tr>
<tr style="height: 79px;">
<td style="width: 50%; text-align: center; height: 79px;" colspan="2">


実数解をもつ( $D \geqq 0$ )


</td>
</tr>
<tr style="height: 20px;">
<td style="width: 25%; text-align: center; height: 20px;">実数解の個数</td>
<td style="width: 25%; text-align: center; height: 20px;">2個</td>
<td style="width: 25%; text-align: center; height: 20px;">1個</td>
<td style="width: 25.1222%; text-align: center; height: 20px;">0個</td>
</tr>
<tr style="height: 41px;">
<td style="width: 25%; text-align: center; height: 41px;">虚数解の個数</td>
<td style="width: 25%; text-align: center; height: 41px;">0個</td>
<td style="width: 25%; text-align: center; height: 41px;">0個</td>
<td style="width: 25.1222%; text-align: center; height: 41px;">2個</td>
</tr>
</tbody>
</table>


解そのものではなく，どのような解を持つかを知りたいだけならこの判別式を使うだけで十分だね。




### 2次方程式の実数解の存在範囲




解と係数の関係と判別式を使うことで，2次方程式の実数解の存在範囲，つまり，実数解が原点を基準として数直線上のどこにあるかを考えることができる。




これも，解そのものではなく，解がどこにあるかということに着目したものだね。


<div class="blank-box bb-blue">


<strong>2次方程式の実数解の存在範囲</strong>




2次方程式 $ax^2+bx+c=0$ の2つの実数解を $\alpha$，$\beta$，判別式を $D=b^2-4ac$ とする。


<ul>
	<li>2解のうち少なくとも一方が正 $\Leftrightarrow$ $\alpha &gt;0$ または $\beta &gt;0$ $\Leftrightarrow$ $\alpha + \beta &gt;0$</li>
	<li>2解のうち少なくとも一方が負 $\Leftrightarrow$ $\alpha &lt;0$ または $\beta &lt;0$ $\Leftrightarrow$ $\alpha + \beta &lt;0$</li>
	<li>2解が同符号 $\Leftrightarrow$ $\alpha \beta &gt;0$</li>
	<li>2解が異符号 $\Leftrightarrow$ $\alpha \beta &lt;0$</li>
	<li>2解がともに正 $\Leftrightarrow$ $\alpha &gt;0$ かつ $\beta &gt;0$ $\Leftrightarrow$ $D \geqq 0$ かつ $\alpha + \beta &gt;0$ かつ $\alpha \beta &gt;0$</li>
	<li>2解がともに負 $\Leftrightarrow$ $\alpha &lt;0$ かつ $\beta &lt;0$ $\Leftrightarrow$ $D \geqq 0$ かつ $\alpha + \beta &lt;0$ かつ $\alpha \beta &lt;0$</li>
	<li>2解が異符号 $\Rightarrow$ $D&gt;0$</li>
	<li>$\alpha \beta &lt;0$ $\Rightarrow$ $D&gt;0$</li>
</ul>


特に， $a&gt;0$ のとき，


<ul>
	<li>2解のうち少なくとも一方が正 $\Leftrightarrow$ $\alpha &gt;0$ または $\beta &gt;0$ $\Leftrightarrow$ $b&lt;0$</li>
	<li>2解のうち少なくとも一方が負 $\Leftrightarrow$ $\alpha &lt;0$ または $\beta &lt;0$ $\Leftrightarrow$ $b&gt;0$</li>
	<li>2解が同符号 $\Leftrightarrow$ $c&gt;0$</li>
	<li>2解が異符号 $\Leftrightarrow$ $c&lt;0$</li>
	<li>2解がともに正 $\Leftrightarrow$ $\alpha &gt;0$ かつ $\beta &gt;0$ $\Leftrightarrow$ $D \geqq 0$ かつ $b&lt;0$ かつ $c&gt;0$</li>
	<li>2解がともに負 $\Leftrightarrow$ $\alpha &lt;0$ かつ $\beta &lt;0$ $\Leftrightarrow$ $D \geqq 0$ かつ $b&gt;0$ かつ $c&lt;0$</li>
	<li>2解が異符号 $\Rightarrow$ $D&gt;0$</li>
	<li>$c&lt;0$ $\Rightarrow$ $D&gt;0$</li>
</ul>
</div>


## $m$ 元 $n$ 次方程式と連立方程式


<div class="info-box">


【定義】




<strong>$m$ 元 $n$ 次方程式</strong>： $m$ 種類の文字を含む $n$ 次方程式




<strong>$m$ 元 $n$ 次方程式の解</strong>：方程式を成り立たせる値の組




<strong>不定方程式</strong>：解が無数にある方程式




<strong>整数解</strong>：整数の解




<strong>連立方程式</strong>：複数の方程式を組み合わせたもの




<strong>連立方程式の解</strong>(共通解)：すべての方程式を同時に成り立たせる値の組




【定理】<strong>互いに素である整数の性質</strong>




2つの整数 $a$，$b$ が互いに素であるとき，整数 $c$ について $ax+by=c$ を満たす整数 $x$，$y$ が存在する。




【定理】<strong>1次不定方程式の解</strong>




2つの整数 $a$，$b$ が互いに素であるとき，方程式 $ax+by=c$ の整数解の1つを $x=p$，$y=q$ とすると，全ての整数解は $x=bk+p$，$y=-ak+q$ ( $k$ は整数) と表される。


</div>


### 不定方程式




基本的に，文字が1種類の方程式，つまり1元 $n$ 次方程式の解は $n$ 個だけど，文字が2種類以上の方程式，つまり， $m$ 元 $n$ 次方程式になると解が無数に存在するようになるんだ。




例えば，2元1次方程式 $x+y=1$ の解は，$(x,y)=(1,0),(0,1),( \frac{1}{2} , \frac{1}{2} ),(-\frac{2}{3} , \frac{5}{3} ) \cdots$ のようにね。




このように解が無数にある方程式を不定方程式といって，上のように具体的な解を考えることもあれば，すべての解を表すことができる一般解を用いることもあるよ。


<div class="blank-box bb-green">


例5)




$x+y=1$ の一般解を求めよ。


<p style="padding-left: 40px;">$x$ の解の1つを実数 $k$ でおくと，</p>
<p style="padding-left: 40px;">$k+y=1$</p>
<p style="padding-left: 40px;">$y=-k+1$</p>
<p style="padding-left: 40px;">したがって求める一般解は $(x,y)=(k,-k+1)$ ( $k$ は実数)</p>
</div>


$(x,y)=(k,-k+1)$ の $k$ には，実数であれば何を代入しても解になるんだ。




また，1次不定方程式では解を整数に絞ることがある。


<div class="blank-box bb-green">


例6)




$2x+3y=23$ ー① の整数解を求めよ。


<p style="padding-left: 40px;">整数解の1つは $(x,y)=(4,5)$ であるから，</p>
<p style="padding-left: 40px;">$2 \cdot 4+3 \cdot 5=23$ ー②</p>
<p style="padding-left: 40px;">①と②の辺々の差をとると，</p>
<p style="padding-left: 40px;">$2(x-4)+3(y-5)=0$</p>
<p style="padding-left: 40px;">$2(x-4)=-3(y-5)$ ー③</p>
<p style="padding-left: 40px;">$2$ と $3$ は互いに素だから， $x-4$ は $3$ を因数にもつ，つまり， $3$ の倍数であり，これを整数 $k$ を用いて $3k$ とおくと，</p>
<p style="padding-left: 40px;">$x-4=3k$</p>
<p style="padding-left: 40px;">$x=3k+4$</p>
<p style="padding-left: 40px;">これを③に代入して，</p>
<p style="padding-left: 40px;">$2 \cdot 3k=-3(y-5)$</p>
<p style="padding-left: 40px;">$2k=-y+5$</p>
<p style="padding-left: 40px;">$y=-2k+5$</p>
<p style="padding-left: 40px;">したがって，求める整数解は $(x,y)=(3k+4,-2k+5)$ ( $k$ は整数)</p>
</div>


例6も例5と同じように，整数であれば $k$ に何を代入しても解になるよ。




ちなみに，例6の解答の中で互いに素の性質を使っているんだけど，1次不定方程式 $ax+by=c$ の係数 $a$ ， $b$ が互いに素でない場合， $c$ が $a$ と $b$ の最大公約数を約数に持たないと整数解を求めることができない点には注意が必要だよ。




### 連立方程式




$m$ 元 $n$ 次方程式は方程式が1つであれば解は無数にあるけど，複数の方程式の共通解であれば有限に決まるんだ。




例えば，2つの2元1次方程式 $x+y=1$ ， $x-y=-3$ はそれぞれが無数に解をもつけど，共通解は $(x,y)=(-1,2)$ の1つだけ。




こうやって複数の方程式を組み合わせたものを，連立方程式といって，波括弧を使って以下のように表すよ。


<p style="padding-left: 40px;">$\left \{ \begin{array}{l} x+y=1 \\ x-y=-3 \end{array} \right.$</p>


また，解は


<p style="padding-left: 40px;">$\left \{ \begin{array}{l} x=-1 \\ y=2 \end{array} \right.$ または $(x,y)=(-1,2)$</p>


と表す。




もちろん，「2式を連立して～」という文言でも大丈夫。




ちなみに，同じ方程式を連立しても，解は無数に存在するからね。




### 連立方程式の解き方




連立方程式は2つの方程式から解を求めるから，解き方も $n$ 次方程式とは異なるよ。




基本的には等式の性質を利用するか代入をして， $m$ 元 $n$ 次方程式を1元方程式に落とし込むんだ。




有名な方法を2つ紹介しておくね。


<div class="blank-box bb-blue">


<strong>連立方程式の解法</strong>




<strong>加減法</strong>：特定の文字の係数の絶対値をそろえ，2式の辺々を加減することによってその文字を消去し，1元方程式に落とし込む解く方法。




<strong>代入法</strong>：一方の式を変形し，他方の式に代入することによって文字を消去し，1元方程式に落とし込む解く方法。


</div>
<div class="blank-box bb-green">


例7)




$\left \{ \begin{array}{ll} x+y=1 &amp; -① \\ x-y=-3 &amp; -② \end{array} \right.$




【加減法】




①と②の辺々を加えると，


<p style="padding-left: 40px;">$2x=-2$</p>
<p style="padding-left: 40px;">$x=-1$</p>


これを①に代入して，


<p style="padding-left: 40px;">$-1+y=1$</p>
<p style="padding-left: 40px;">$y=2$</p>


したがって，求める解は $(x,y)=(-1,2)$




【代入法】




①を $x$ について解くと，


<p style="padding-left: 40px;">$x=-y+1$</p>


これを②に代入すると，


<p style="padding-left: 40px;">$(-y+1)-y=-3$</p>
<p style="padding-left: 40px;">$-2y+1=-3$</p>
<p style="padding-left: 40px;">$y=2$</p>


これを①に代入すると，


<p style="padding-left: 40px;">$x+2=1$</p>
<p style="padding-left: 40px;">$x=-1$</p>


したがって，求める解は $(x,y)=(-1,2)$


</div>


### 方程式 $A=B=C$




また，連立方程式に見えなくても，連立方程式の考え方で解ける方程式がある。




それが， $A=B=C$ の形の方程式。




この場合，等式の性質を使って，


<p style="padding-left: 30px;">$\left\{ \begin{array}{l} A=B \\ A=C \end{array} \right.$ または $\left\{ \begin{array}{l} A=B \\ B=C \end{array} \right.$ または $\left\{ \begin{array}{l} A=C \\ B=C \end{array} \right.$</p>


という連立方程式を作って解くんだ。




## 方程式の検算




方程式の解というのは方程式を成り立たせる値だから，求めた解を方程式に代入することが検算になるんだ。




考え方のミスというのはその場では確かめようがないんだけど，計算ミスは見つけられるから，数学においてはミスをしないだけでなく，ミスを発見する練習も積み重ねないといけない。




ほんの一部の問題を除いて検算は存在するからね。




## 等式の証明




最後は等式の証明について。




左辺と右辺が等しいことを証明する方法はいろいろあるけど，基本的な3つの方法を紹介するね。


<div class="blank-box bb-blue">


<strong>等式</strong> $\boldsymbol{A=B}$ <strong>を証明する方法</strong>


<ul>
	<li>$A→B$：$A$ か $B$ の一方を変形して他方を導く。複雑な式の方を変形するのが原則。</li>
	<li>$A→C$，$B→C$：$A$，$B$ をそれぞれ変形して同じ式を導く。</li>
	<li>$A-B→0$：$A-B$ を計算して0になることを示す。</li>
</ul>
</div>
<div class="blank-box bb-green">


例8)




$(a^2+b^2)(c^2+d^2)=(ac+bd)^2+(ad-bc)^2$ を示せ。




【 $A→B$ 】


<p style="padding-left: 40px;">$($ 左辺 $)$</p>
<p style="padding-left: 40px;">$=a^2c^2+a^2d^2+b^2c^2+b^2d^2$</p>
<p style="padding-left: 40px;">$=a^2c^2+2ac \cdot bd+b^2d^2+a^2d^2-2ad \cdot bc+b^2c^2$</p>
<p style="padding-left: 40px;">$=(ac+bd)^2+(ad-bc)^2$</p>
<p style="padding-left: 40px;">$=($ 右辺 $)$</p>


【 $A→C$，$B→C$ 】


<p style="padding-left: 40px;">$($ 左辺 $)$</p>
<p style="padding-left: 40px;">$=a^2c^2+a^2d^2+b^2c^2+b^2d^2$</p>
<p style="padding-left: 40px;">$($ 右辺 $)$</p>
<p style="padding-left: 40px;">$=a^2c^2+2abcd+b^2d^2+a^2d^2-2abcd+b^2c^2$</p>
<p style="padding-left: 40px;">$=a^2c^2+a^2d^2+b^2c^2+b^2d^2$</p>


よって，$($ 左辺 $)=($ 右辺 $)$




【 $A-B→0$ 】


<p style="padding-left: 40px;">$($ 左辺 $)-($ 右辺 $)$</p>
<p style="padding-left: 40px;">$=(a^2c^2+a^2d^2+b^2c^2+b^2d^2)-(a^2c^2+2abcd+b^2d^2+a^2d^2-2abcd+b^2c^2)$</p>
<p style="padding-left: 40px;">$=a^2c^2+a^2d^2+b^2c^2+b^2d^2-a^2c^2-2abcd-b^2d^2-a^2d^2+2abcd-b^2c^2$</p>
<p style="padding-left: 40px;">$=0$</p>


よって，$($ 左辺 $)=($ 右辺 $)$


</div>


## 第8講のまとめ




等号「 $=$ 」のイメージは変えられたかな？




恒等式も方程式も等式の証明も，等式の性質を十分に理解していないと身につけるのは難しい。




腑に落ちないところは何度でも読み返して，必要なら調べて，納得してから次の不等式に進んでほしい。




等式も不等式も，両辺の数の関係を表していることに違いはないんだけど，扱い方は大きく異なるからね。




http://mathrao.com/instant-jhmath-provisional-7/




http://mathrao.com/instant-jhmath-provisional-9/
