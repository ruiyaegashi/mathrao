---
title: "【インスタント中高数学】第9講 未知なる解を求めて②【恒等式・方程式・不等式】"
wp_id: 2392
content_type: "post"
status: "publish"
published_at: "2019-06-15 20:35:33"
wp_date: "2019-06-15 20:35:33"
modified_at: "2019-07-03 14:10:09"
legacy_url: "http://mathrao.com/instant-jhmath-provisional-9/"
legacy_path: "/instant-jhmath-provisional-9/"
legacy_slug: "instant-jhmath-provisional-9"
former_slugs: []
parent_wp_id: null
parent_title: null
hierarchy: ["【インスタント中高数学】第9講 未知なる解を求めて②【恒等式・方程式・不等式】"]
category: ["インスタント中高数学【草稿】"]
tags: []
mathrao_section: "インスタント中高数学"
mathrao_grade: null
mathrao_course: null
source_content_sha256: "2a7beab1123802d77d61a7a2ca5dcb4134f78ec14c45d34df8193b169ea47b83"
---

http://mathrao.com/instant-jhmath-provisional-8/




## 意味のない改行はない




数学というのは論理の積み重ね。




だから，論理自体はもちろん，そのつなぎ目である行間にも必ず意味があるんだ。




それが定義なのか定理なのか，しっかり見極めた上で進まないと本当に理解しているとはいえないよ。




だんだん内容が難しくなってきて大変かもしれないけど，このルールだけは絶対に変わらない。




自分では説明できない謎の論理や行間があったら絶対に解決して，人に説明できるくらいになってから前に進む，くらいのつもりでいよう。




第9講は不等式。




等式より自由度が高い分，考えなきゃいけないことの量は方程式の比じゃないから気合を入れて臨もう。




数学において自分の感覚を数学的な正しさにすり合わせるのはとても大事。




こうかな，って思っていたことが違っていたとき，それにどう向き合い，自分の中にどう落とし込むか。




不等式はそんな葛藤の連続になるはずだよ。




## 不等式


<div class="info-box">


【定理】<strong>不等式の性質</strong>




$A$ ， $B$ ， $C$ ， $D$ を実数とする。


<ul>
	<li>$A&lt;B$ かつ $B&lt;C$ $\Rightarrow$ $A&lt;C$</li>
	<li>$A&lt;B$ かつ $B&lt;C$ $\Leftrightarrow$ $A&lt;B&lt;C$</li>
	<li>$A&lt;B$ $\Leftrightarrow$ $A+C&lt;B+C$ かつ $A-C&lt;B-C$</li>
	<li>$A&lt;B$ かつ $C&gt;0$ $\Rightarrow$ $AC&lt;BC$ かつ $\frac{A}{C} &lt; \frac{B}{C}$</li>
	<li>$A&lt;B$ かつ $C&lt;0$ $\Rightarrow$ $AC&gt;BC$ かつ $\frac{A}{C} &gt; \frac{B}{C}$</li>
	<li>$0&lt;A&lt;B$ かつ $r$ は正の実数 $\Rightarrow$ $A^r&lt;B^r$</li>
	<li>$0&lt;A&lt;B$ かつ $r$ は負の実数 $\Rightarrow$ $A^r&gt;B^r$</li>
	<li>$A&lt;B&lt;0$ かつ $n$ は偶数 $\Rightarrow$ $A^n&gt;B^n$</li>
	<li>$A&lt;B&lt;0$ かつ $n$ は奇数 $\Rightarrow$ $A^n&lt;B^n$</li>
	<li>$A&lt;B&lt;0$ $\Rightarrow$ $\frac{1}{A} &gt; \frac{1}{B}$</li>
	<li>$A&lt;0&lt;B$ $\Rightarrow$ $\frac{1}{A} &lt; \frac{1}{B}$</li>
	<li>$A&lt;0&lt;B$ かつ $|A|&lt;|B|$ $\Rightarrow$ $A^2&lt;B^2$</li>
	<li>$A&lt;0&lt;B$ かつ $|A|&gt;|B|$ $\Rightarrow$ $A^2&gt;B^2$</li>
	<li>$A&lt;B$ かつ $C&lt;D$ $\Rightarrow$ $A+C&lt;B+D$ かつ $A-D&lt;B-C$</li>
	<li>$0&lt;A&lt;B$ かつ $0&lt;C&lt;D$ $\Rightarrow$ $AC&lt;BD$ かつ $\frac{A}{D} &lt; \frac{B}{C}$</li>
	<li>$A&lt;B&lt;0$ かつ $C&lt;D&lt;0$ $\Rightarrow$ $AC&gt;BD$ かつ $\frac{A}{D} &gt; \frac{B}{C}$</li>
	<li>$0&lt;A&lt;B$ かつ $C&lt;D&lt;0$ $\Rightarrow$ $AD&lt;BC$ かつ $\frac{A}{C} &lt; \frac{B}{D}$</li>
</ul>
</div>


等式と同じように，まずは不等号「 $&lt;,&gt;, \leqq , \geqq$」について考えていこう。




小学校までは $2&lt;3$ のように2つの数の大小を比べた結果を表す記号として使ってきたけど，中高数学では使われ方が増えるからあとで紹介するね。




不等式を等式と同じように天秤で考えると，天秤が左辺か右辺のどちらかに傾いている状態で，それを表しているのが不等号の向き。




この不等号の向きが操作によって変わったり変わらなかったりするから，等式のように両辺に何をしてもいいわけじゃないんだ。




無条件で不等号の向きが変わらない操作は，


<ul>
	<li>すべての辺に同じ数を加える</li>
	<li>すべての辺から同じ数を引く</li>
	<li>複数の不等式の辺々を足す</li>
</ul>


これだけ。




乗法，除法，冪乗，複数の不等式の辺々の演算は，数の正負や絶対値によって不等号の向きが変わることがあるからね。




とはいえ，上にある不等式の性質を丸暗記するのではなく，その操作をすると両辺の大小関係がどう変わるかを具体的な数でシミュレーションして徐々に身につけていこう。




ちなみに，使う回数をどうこういうのはあまり好きじゃないけど，「両辺に同じ負の数を掛けたり，割ったりすると，不等号の向きが変わる」というのは頻出かな。




あと，3つ以上の数を比べるときは，不等式の性質の2つ目「 $A&lt;B$ かつ $B&lt;C$ $\Leftrightarrow$ $A&lt;B&lt;C$ 」を使うことで複数の不等式に分けることができるよ。




## 不等式の主な使われ方




もちろん，不等号の定義さえ守ればどのような使い方をするのも自由だけど，中高数学で多い使われ方を紹介しておくね。




### 数の大小関係を表す




小学校のときに習った使い方と同じで，2つ以上の数の大小関係を，$2&lt;3$ というように表すよ。




### 文字のとり得る値の範囲を表す




ある文字が特定の値ではなく，特定の範囲の値をとるとき，どこからどこまでの値をとるかを表すのに不等号を使うんだ。




例えば， $x$ が $2$ 以上 $3$ 未満の値をとることを $2 \leqq x&lt;3$ と表す。




もちろん， $2$ と $x$ ， $x$ と $3$ の大小関係を表していると考えることもできるけどね。




あとは，不等式の性質を使って $2&lt;x&lt;3$ $\Leftrightarrow$ $2&lt;x$ かつ $x&lt;3$ というように分けて考えることもできるよ。




### $n$ 次不等式




方程式と同じように解くことができる，文字を含んだ不等式。




詳しい解き方にはあとで触れるけど，具体的な数を比べるわけではないから慎重に扱わなきゃいけないよ。




## 共通範囲と合わせた範囲




不等式の問題や場合分けを必要とするような問題では，「共通範囲」と「合わせた範囲」という考え方をすることがあるんだ。




それぞれの意味をしっかり理解して，どちらの範囲を求めるべきか正しく判断できるようになろう。




まずは第2講の復習から。


<div class="info-box">


【定義】




2つの条件 $p$，$q$ について，


<p style="padding-left: 30px;">$p$ <strong>かつ</strong> $q$：$p$ と $q$ のどちらも満たす条件</p>
<p style="padding-left: 30px;">$p$ <strong>または</strong> $q$：$p$ と $q$ の少なくとも一方を満たす条件</p>
</div>


これらの定義を確認した上で，「共通範囲」と「合わせた範囲」について再確認すると，


<p style="padding-left: 30px;">$p$ と $q$ の共通範囲：「$p$ かつ $q$」を満たす範囲</p>
<p style="padding-left: 30px;">$p$ と $q$ の合わせた範囲：「$p$ または $q$」を満たす範囲</p>


となり，不等式を数直線で考えると，


<p style="padding-left: 30px;">$p$ と $q$ の共通範囲：2つの範囲が重なっている部分</p>
<p style="padding-left: 30px;">$p$ と $q$ の合わせた範囲：2つの範囲の少なくとも一方に含まれている部分</p>


になる。




両方を満たすべきか，少なくとも一方を満たすべきか，見極められるようになろう。




## $n$ 次不等式


<div class="info-box">


【定義】




$x$ についての $\boldsymbol{n}$ <strong>次不等式</strong>： $x$ の次数が $n$ の不等式




$x$ についての不等式の<strong>解</strong>：不等式を満たす $x$ の値，または，値のとり得る範囲




不等式を<strong>解く</strong>：不等式の解を求めること




<strong>連立不等式</strong>：複数の不等式を組み合わせたもの




連立不等式の<strong>解</strong>：すべての不等式を同時に満たす値，または，値のとり得る範囲




連立不等式を<strong>解く</strong>：連立不等式の解を求めること




【定理】<strong>数や式についての性質</strong>




一般に，数や式について，


<ul>
	<li>$AB&gt;0$ $\Leftrightarrow$「 $A&gt;0$ かつ $B&gt;0$ 」または「 $A&lt;0$ かつ $B&lt;0$ 」</li>
	<li>$AB \geqq 0$ $\Leftrightarrow$「 $A \geqq 0$ かつ $B \geqq 0$ 」または「 $A \leqq 0$ かつ $B \leqq 0$ 」</li>
	<li>$AB&lt;0$ $\Leftrightarrow$ 「 $A&gt;0$ かつ $B&lt;0$ 」または「 $A&lt;0$ かつ $B&gt;0$ 」</li>
	<li>$AB \leqq 0$ $\Leftrightarrow$ 「 $A \geqq 0$ かつ $B \leqq 0$ 」または「 $A \leqq 0$ かつ $B \geqq 0$ 」</li>
</ul>
</div>


$n$ 次不等式は方程式と同じように解くことができるんだけど，その解の形は様々。




パターン暗記にならないように，しっかりと不等式の意味を理解して解くようにしよう。




あと，連立方程式と同じように不等式も連立することができて，その解はすべての不等式の共通解になるんだ。




特に，不等式の解が範囲の場合はその共通範囲をとるよ。




### 1次不等式の解法




$n$ 次不等式を解く基本になるのが1次不等式。




1次不等式は $ax+b$ (不等号) $0$ のような形をしていて，この式を $x$ について解いた $x$ (不等号) $- \frac{b}{a}$ がその解になるよ。




ただ，方程式と違って $a$ の正負によって不等号の向きが変わる点は要注意。




「両辺に同じ負の数を掛けたり，割ったりすると，不等号の向きが変わる」を忘れないようにね。


<table style="border-collapse: collapse; width: 100%;">
<tbody>
<tr>
<td style="width: 33.3333%; text-align: center;"> </td>
<td style="width: 33.3333%; text-align: center;">$a&gt;0$ のとき</td>
<td style="width: 33.3333%; text-align: center;">$a&lt;0$ のとき</td>
</tr>
<tr>
<td style="width: 33.3333%; text-align: center;">$ax+b&lt;0$</td>
<td style="width: 33.3333%; text-align: center;">$x&lt;- \frac{b}{a}$</td>
<td style="width: 33.3333%; text-align: center;">$x&gt;- \frac{b}{a}$</td>
</tr>
<tr>
<td style="width: 33.3333%; text-align: center;">$ax+b \leqq 0$</td>
<td style="width: 33.3333%; text-align: center;">$x \leqq - \frac{b}{a}$</td>
<td style="width: 33.3333%; text-align: center;">$x \geqq - \frac{b}{a}$</td>
</tr>
<tr>
<td style="width: 33.3333%; text-align: center;">$ax+b&gt;0$</td>
<td style="width: 33.3333%; text-align: center;">$x&gt;- \frac{b}{a}$</td>
<td style="width: 33.3333%; text-align: center;">$x&lt;- \frac{b}{a}$</td>
</tr>
<tr>
<td style="width: 33.3333%; text-align: center;">$ax+b \geqq 0$</td>
<td style="width: 33.3333%; text-align: center;">$x \geqq - \frac{b}{a}$</td>
<td style="width: 33.3333%; text-align: center;">$x \leqq - \frac{b}{a}$</td>
</tr>
</tbody>
</table>


<span style="font-size: 16px;">2次以上の不等式でもこの考え方を使うからしっかり覚えておこう。</span>




### 2次以上の不等式の解き方




2次以上の方程式の解き方はいくつかあるけど，ここでは2つだけ紹介するね。




これ以外の方法は関数の講で紹介するよ。




#### 因数分解による解法




この解法では数や式についての性質を利用するよ。




一般に，2つの数の積の符号は，


<ul>
	<li>(正) $\times$ (正) $=$ (正)</li>
	<li>(正) $\times$ (負) $=$ (負)</li>
	<li>(負) $\times$ (負) $=$ (正)</li>
</ul>


つまり，


<ul>
	<li>2つの数は同符号 $\Leftrightarrow$ 2つの数の積が正</li>
	<li>2つの数は異符号 $\Leftrightarrow$ 2つの数の積が負</li>
</ul>


となるよね。




当然，数が3つ以上になっても，


<ul>
	<li>(正) $\times$ (正) $\times$ (正) $=$ (正)</li>
	<li>(正) $\times$ (正) $\times$ (負) $=$ (負)</li>
	<li>(正) $\times$ (負) $\times$ (負) $=$ (正)</li>
	<li>(負) $\times$ (負) $\times$ (負) $=$ (負)</li>
</ul>


というような関係が成り立つ。




不等式が因数分解できれば，この性質を使って解を求めることができるんだ。




第5講で学んだ因数分解を最大限活用しよう。


<div class="blank-box bb-green">例1)

<p style="padding-left: 40px;">$x^2-x-2&gt;0$</p>
<p style="padding-left: 40px;">$(x-2)(x+1)&gt;0$</p>


よって，


<p style="padding-left: 40px;">$\left \{ \begin{array}{l} x-2&lt;0 \\ x+1&lt;0 \end{array} \right.$ または $\left \{ \begin{array}{l} x-2&gt;0 \\ x+1&gt;0 \end{array} \right.$</p>
<p style="padding-left: 40px;">$\left \{ \begin{array}{l} x&lt;2 \\ x&lt;-1 \end{array} \right.$ または $\left \{ \begin{array}{l} x&gt;2 \\ x&gt;-1 \end{array} \right.$</p>
<p style="padding-left: 40px;">$x&lt;-1$ または $2&lt;x$</p>
</div>


例1の


<p style="padding-left: 40px;">$\left \{ \begin{array}{l} x-2&lt;0 \\ x+1&lt;0 \end{array} \right.$</p>


は連立不等式だから，それぞれの不等式を解いて，


<p style="padding-left: 40px;">$\left \{ \begin{array}{l} x&lt;2 \\ x&lt;-1 \end{array} \right.$</p>


となり，その共通範囲 $x&lt;-1$ が解になるんだ。




2つの連立不等式を「または」で考えているから，解は合わせた範囲の $x&lt;-1$ または $2&lt;x$ になるよ。


<div class="blank-box bb-green">


例2)


<p style="padding-left: 40px;">$x^3+6x^2+11x+6 \leqq 0$</p>
<p style="padding-left: 40px;">$(x+1)(x+2)(x+3) \leqq 0$</p>


$x$ は実数なので $x+1&lt;x+2&lt;x+3$ であるから，


<p style="padding-left: 40px;">$\left \{ \begin{array}{l} x+1 \leqq 0 \\ x+2 \leqq 0 \\ x+3 \leqq 0 \end{array} \right.$ または $\left \{ \begin{array}{l} x+1 \leqq 0 \\ x+2 \geqq 0 \\ x+3 \geqq 0 \end{array} \right.$</p>
<p style="padding-left: 40px;">$\left \{ \begin{array}{l} x \leqq -1 \\ x \leqq -2 \\ x \leqq -3 \end{array} \right.$ または $\left \{ \begin{array}{l} x \leqq -1 \\ x \geqq -2 \\ x \geqq -3 \end{array} \right.$</p>
<p style="padding-left: 40px;">$x \leqq -3$ または $-2 \leqq x \leqq -1$</p>
</div>


例2では単純に組み合わせで考えると，


<p style="padding-left: 40px;">$\left \{ \begin{array}{l} x+1 \geqq 0 \\ x+2 \leqq 0 \\ x+3 \geqq 0 \end{array} \right.$ ， $\left \{ \begin{array}{l} x+1 \geqq 0 \\ x+2 \geqq 0 \\ x+3 \leqq 0 \end{array} \right.$</p>


も有り得そうなんだけど， $x+1&lt;x+2&lt;x+3$ という大小関係が成り立っているから，数直線で考えればこの不等式において $0$ がくるのは $x+1&lt;x+2&lt;x+3 \leqq 0$ か $x+1 \leqq 0 \leqq x+2&lt;x+3$ しかないということが分かる。




だから，上の2つの可能性はあり得ないから省いているんだよ。




実際に計算してみても，


<p style="padding-left: 40px;">$\left \{ \begin{array}{l} x+1 \geqq 0 \\ x+2 \leqq 0 \\ x+3 \geqq 0 \end{array} \right.$ $\Leftrightarrow$ $\left \{ \begin{array}{l} x \geqq -1 \\ x \leqq -2 \\ x \geqq -3 \end{array} \right.$ $\Leftrightarrow$ 解なし</p>
<p style="padding-left: 40px;">$\left \{ \begin{array}{l} x+1 \geqq 0 \\ x+2 \geqq 0 \\ x+3 \leqq 0 \end{array} \right.$ $\Leftrightarrow$ $\left \{ \begin{array}{l} x \geqq -1 \\ x \geqq -2 \\ x \leqq -3 \end{array} \right.$ $\Leftrightarrow$ 解なし</p>


となるしね。


<div class="blank-box bb-blue">


<strong>因数分解による解法</strong>




$a$ ， $b$ ， $c$ ， $\alpha$ ， $\beta$ ， $\gamma$ は実数で $a \neq 0$ ， $\alpha &lt; \beta &lt; \gamma$ とする。




$ax^2+bx+c=a(x- \alpha )(x- \beta )$




$ax^3+bx^2+cx+d=a(x- \alpha )(x- \beta )(x-\gamma )$




のとき，


<table style="border-collapse: collapse; width: 100%;">
<tbody>
<tr>
<td style="width: 33.3333%; text-align: center;"> </td>
<td style="width: 33.3333%; text-align: center;">$a&gt;0$</td>
<td style="width: 33.3333%; text-align: center;">$a&lt;0$</td>
</tr>
<tr>
<td style="width: 33.3333%; text-align: center;">$ax^2+bx+c &gt;0$</td>
<td style="width: 33.3333%; text-align: center;">$x&lt; \alpha$ ， $\beta &lt;x$</td>
<td style="width: 33.3333%; text-align: center;">$\alpha &lt;x&lt; \beta$</td>
</tr>
<tr>
<td style="width: 33.3333%; text-align: center;">$ax^2+bx+c \geqq 0$</td>
<td style="width: 33.3333%; text-align: center;">$x \leqq \alpha$ ， $\beta \leqq x$</td>
<td style="width: 33.3333%; text-align: center;">$\alpha \leqq x \leqq \beta$</td>
</tr>
<tr>
<td style="width: 33.3333%; text-align: center;">$ax^2+bx+c &lt;0$</td>
<td style="width: 33.3333%; text-align: center;">$\alpha &lt;x&lt; \beta$</td>
<td style="width: 33.3333%; text-align: center;">$x&lt; \alpha$ ， $\beta &lt;x$</td>
</tr>
<tr>
<td style="width: 33.3333%; text-align: center;">$ax^2+bx+c \leqq 0$</td>
<td style="width: 33.3333%; text-align: center;">$\alpha \leqq x \leqq \beta$</td>
<td style="width: 33.3333%; text-align: center;">$x \leqq \alpha$ ， $\beta \leqq x$</td>
</tr>
<tr>
<td style="width: 33.3333%; text-align: center;">$ax^3+bx^2+cx+d &gt;0$</td>
<td style="width: 33.3333%; text-align: center;">$\alpha &lt;x&lt; \beta$ ， $\gamma &lt;x$</td>
<td style="width: 33.3333%; text-align: center;">$x&lt; \alpha$ ， $\beta &lt;x&lt; \gamma$</td>
</tr>
<tr>
<td style="width: 33.3333%; text-align: center;">$ax^3+bx^2+cx+d \geqq 0$</td>
<td style="width: 33.3333%; text-align: center;">$\alpha \leqq x \leqq \beta$ ， $\gamma &lt;x$</td>
<td style="width: 33.3333%; text-align: center;">$x \leqq \alpha$ ， $\beta \leqq x \leqq \gamma$</td>
</tr>
<tr>
<td style="width: 33.3333%; text-align: center;">$ax^3+bx^2+cx+d &lt;0$</td>
<td style="width: 33.3333%; text-align: center;">$x&lt; \alpha$ ， $\beta &lt;x&lt; \gamma$</td>
<td style="width: 33.3333%; text-align: center;">$\alpha &lt;x&lt; \beta$ ， $\gamma &lt;x$</td>
</tr>
<tr>
<td style="width: 33.3333%; text-align: center;">$ax^3+bx^2+cx+d \leqq 0$</td>
<td style="width: 33.3333%; text-align: center;">$x \leqq \alpha$ ， $\beta \leqq x \leqq \gamma$</td>
<td style="width: 33.3333%; text-align: center;">$\alpha \leqq x \leqq \beta$ ， $\gamma &lt;x$</td>
</tr>
</tbody>
</table>
</div>


4次以上でも上記のように因数分解できるのであれば，一般化することができるし，方程式と同じように，この解法の逆を考えることで不等式を作ることもできるよ。




#### 平方を利用した解法




この方法では「 $x$ が実数 $\Leftrightarrow$ $x^2 \geqq 0$ 」という性質を利用するよ。


<div class="blank-box bb-green">


例3)


<p style="padding-left: 40px;">$x^2+3&gt;0$</p>


$x^2 \geqq 0$ であるから $x^2+3 \geqq 3$ となり，この不等式は常に成り立つ。




したがって，$x$ はすべての実数。


</div>


また，平方完成をすることで， $n$ 次式部分を平方数と定数だけにすることができるんだ。


<div class="blank-box bb-green">


例4)


<p style="padding-left: 40px;">$x^2+2x+2 \leqq 0$</p>
<p style="padding-left: 40px;">$(x+1)^2+1 \leqq 0$</p>


$(x+1)^2 \geqq 0$ であるから $(x+1)^2+1 \geqq 1$ となり，この不等式は常に成り立たない。




したがって，解なし。


</div>


平方完成をすることで常に符号が決まっている部分を作ることができるから， $n$ 次不等式が $n$ 個の因数に因数分解できない場合にも有効だよ。


<div class="blank-box bb-green">


例5)


<p style="padding-left: 40px;">$x^3-3x^2+x+5 \geqq 0$</p>
<p style="padding-left: 40px;">$(x+1)(x^2-4x+5) \geqq 0$</p>


$x^2-4x+5=(x-2)^2+1&gt;0$ であるから，


<p style="padding-left: 40px;">$x+1 \geqq 0$</p>
<p style="padding-left: 40px;">$x \geqq -1$</p>
</div>


例5のように因数の符号が固定されている場合，因数ごとの符号の組合せが限定されるんだ。




$x^2-4x+5=(x-2)^2+1&gt;0$ であることを確認せずに進めると，


<p style="padding-left: 40px;">$\left \{ \begin{array}{l} x+1 \geqq 0 \\ x^2-4x+5 \geqq 0 \end{array} \right.$ または $\left \{ \begin{array}{l} x+1 \leqq 0 \\ x^2-4x+5 \leqq 0 \end{array} \right.$</p>


の2つの組合せを考えるけど，2つめの組合せはあり得ないから省けるということだね。




## 絶対値を含む方程式，不等式


<div class="info-box">


【定理】<strong>絶対値の性質</strong>


<ul>
	<li>$|a|=|-a|$</li>
	<li>$|a| \geqq a$</li>
	<li>$|a| \geqq -a$</li>
	<li>$|a|^2=a^2$</li>
	<li>$|ab|=|a||b|$</li>
	<li>$b \neq 0$ のとき $| \frac{a}{b} |= \frac{|a|}{|b|}$</li>
</ul>
</div>


第6講で触れた絶対値について復習しよう。




絶対値 $\boldsymbol{|a|}$ とは，原点 $\mathrm{O} (0)$ と点 $\mathrm{P} (a)$ の距離だったね。




そして，その値は，


<p style="padding-left: 40px;">$|a|= \left \{ \begin{array}{cl} a &amp; (a \geqq 0 のとき) \\ -a &amp; (a&lt;0 のとき) \end{array} \right.$</p>


方程式，不等式に絶対値が含まれる場合，この定義に従って解く必要があるよ。


<div class="blank-box bb-blue">


<strong>絶対値を含む方程式，不等式</strong>




$a&gt;0$ のとき


<ul>
	<li>方程式 $|x|=a$ を満たす $x$ の値は $x= \pm a$</li>
	<li>不等式 $|x|&lt;a$ を満たす $x$ の値の範囲は $-a&lt;x&lt;a$</li>
	<li>不等式 $|x| \leqq a$ を満たす $x$ の値の範囲は $-a \leqq x \leqq a$</li>
	<li>不等式 $|x| &gt;a$ を満たす $x$ の値の範囲は $x&lt;-a$，$a&lt;x$</li>
	<li>不等式 $|x| \geqq a$ を満たす $x$ の値の範囲は $x \leqq -a$，$a \leqq x$</li>
</ul>
</div>


1つずつ，定義を踏まえて数直線で考えていこう。




方程式 $|x|=a$


<p style="padding-left: 40px;">$\Leftrightarrow$ 原点 $\mathrm{O} (0)$ と点 $\mathrm{P} (x)$ の距離が $a$</p>
<p style="padding-left: 40px;">$\Leftrightarrow$ 原点 $\mathrm{O} (0)$ からの距離が $a$ の点の座標は $x= \pm a$</p>


不等式 $|x|&lt;a$ ※ $|x| \leqq a$ も同様


<p style="padding-left: 40px;">$\Leftrightarrow$ 原点 $\mathrm{O} (0)$ と点 $\mathrm{P} (x)$ の距離が $a$ より短い</p>
<p style="padding-left: 40px;">$\Leftrightarrow$ 原点 $\mathrm{O} (0)$ からの距離が $a$ より短い点の座標の範囲は $-a&lt;x&lt;a$</p>


不等式 $|x|&gt;a$ ※ $|x| \geqq a$ も同様


<p style="padding-left: 40px;">$\Leftrightarrow$ 原点 $\mathrm{O} (0)$ と点 $\mathrm{P} (x)$ の距離が $a$ より長い</p>
<p style="padding-left: 40px;">$\Leftrightarrow$ 原点 $\mathrm{O} (0)$ からの距離が $a$ より長い点の座標の範囲は $x&lt;-a$，$a&lt;x$</p>


「 $|x|=a$ 」と「 $x= \pm a$ 」の間にこういった論理があるということを無視して暗記してはいけないよ。




ここで，絶対値を含む不等式を使って，混同しやすい「共通範囲」と「合わせた範囲」に着目して問題を解いてみるよ。


<div class="blank-box bb-green">


例6)




不等式 $|2x-4|&lt;x+1$ を解け。




(ⅰ) $2x-4&lt;0$ すなわち $\color{red}{x&lt;2}$ のとき


<p style="padding-left: 30px;">$|2x-4|=-(2x-4)$ より</p>
<p style="padding-left: 60px;">$\begin{array}{rcl} -(2x-4) &amp; &lt; &amp; x+1 \\ \color{red}{1} &amp; \color{red}{&lt;} &amp; \color{red}{x} \end{array}$</p>
<p style="padding-left: 30px;">よって $\color{red}{1&lt;x&lt;2}$</p>


(ⅱ) $2x-4 \geqq 0$ すなわち $\color{blue}{2 \leqq x}$ のとき


<p style="padding-left: 30px;">$|2x-4|=2x-4$ より</p>
<p style="padding-left: 60px;">$\begin{array}{rcl} 2x-4 &amp; &lt; &amp; x+1 \\ \color{blue}{x} &amp; \color{blue}{&lt;} &amp; \color{blue}{5} \end{array}$</p>
<p style="padding-left: 30px;">よって $\color{blue}{2 \leqq x&lt;5}$</p>


(ⅰ)，(ⅱ) より $\color{green}{1&lt;x&lt;5}$


</div>


まず，$\color{red}{x&lt;2}$ と $\color{blue}{2 \leqq x}$ は，絶対値の定義に従って実数 $x$ の範囲を2つに分けた「場合分けの条件」だよね。




場合分けは問題の条件をいくつかの場合に分けて解答を進める解法だから，例えば，場合(ⅰ)を考えるときは $\color{red}{x&lt;2}$ 以外の範囲は存在しないものとして考えるんだ。




つまり，場合(ⅰ)では与式から $\color{red}{1&lt;x}$ が導かれたんだけど， $\color{red}{x&lt;2}$ の範囲内でしか考えないから， $\color{red}{x&lt;2}$ と $\color{red}{1&lt;x}$ の共通範囲をとって，解は $\color{red}{1&lt;x&lt;2}$ になるということ。




同様に，場合(ⅱ)の解は，$\color{blue}{2 \leqq x}$ と $\color{blue}{x&lt;5}$ の共通範囲をとって $\color{blue}{2 \leqq x&lt;5}$ になる。




最後に，場合(ⅰ)と(ⅱ)で導かれた解は場合分けされているけどどちらも与式の解だから，$\color{red}{1&lt;x&lt;2}$ と $\color{blue}{2 \leqq x&lt;5}$ の合わせた範囲である $\color{green}{1&lt;x&lt;5}$ が与式の解になるんだ。




この例6の解答を連立方程式を使って表すと次のようになるよ。


<div class="blank-box bb-green">


例6')




不等式 $|2x-4|&lt;x+1$ を解け。




$|2x-4|&lt;x+1$




$\Leftrightarrow$ $\left \{ \begin{array}{l} x はすべての実数 \\ |2x-4|&lt;x+1 \end{array} \right.$




$\Leftrightarrow$ $\left \{ \begin{array}{l} 2x-4&lt;0 \\ |2x-4|&lt;x+1 \end{array} \right.$ または $\left \{ \begin{array}{l} 2x-4 \geqq 0 \\ |2x-4|&lt;x+1 \end{array} \right.$




$\Leftrightarrow$ $\left \{ \begin{array}{l} x&lt;2 \\ -(2x-4)&lt;x+1 \end{array} \right.$ または $\left \{ \begin{array}{l} x \geqq 2 \\ 2x-4&lt;x+1 \end{array} \right.$




$\Leftrightarrow$ $\left \{ \begin{array}{l} x&lt;2 \\ 1&lt;x \end{array} \right.$ または $\left \{ \begin{array}{l} x \geqq 2 \\ x&lt;5 \end{array} \right.$




$\Leftrightarrow$ $1&lt;x&lt;2$ または $2 \leqq x&lt;5$




$\Leftrightarrow$ $1&lt;x&lt;5$


</div>


普通，不等式を解くときに「 $x$ はすべての実数」という条件との連立と考えることはないけど，場合分けのときはこの「 $x$ はすべての実数」が2つ以上の範囲に分けられることになる。




だから，あえて連立させることで「 $x$ はすべての実数」$\Leftrightarrow$「 $2x-4&lt;0$ または $2x-4 \geqq 0$」ということを強調してみたんだ。




場合分けは考える範囲を分割することで限定された範囲で考えられるという，数学の問題を解く上でとても重要な手法。




最初は例を見て真似をしつつ，なぜ場合分けするのかを考え，使いこなせるようになろう。




## 相加平均と相乗平均の関係


<div class="info-box">


【定義】




実数 $a$，$b$ について




<strong>相加平均</strong>：$\displaystyle \frac{a+b}{2}$




<strong>相乗平均</strong>：$\sqrt{ab}$




【定理】<strong>相加平均と相乗平均の関係</strong>




$a&gt;0$，$b&gt;0$ のとき


<p style="padding-left: 30px;">$\displaystyle \frac{a+b}{2} \geqq \sqrt{ab}$ ( $a=b$ のとき等号成立)</p>
</div>


ここで，不等式を含む定理「相加平均と相乗平均の関係」を紹介するね。




相加平均(算術平均)というのは小学校でも習ったいわゆる平均のことなんだけど，相乗平均(幾何平均)はなじみがないんじゃないかな？




定義は上の通り2数を掛けてルートをとるだけなんだけど，あえて意味を考えるのであれば， $a$ ， $b$ の相乗平均は，辺の長さが $a$ ， $b$ の長方形と同じ面積の正方形の1辺の長さと考えることができるよ。




とはいえ，中高数学で相乗平均が出てくるのはこの定理だけなんだけどね。




相加平均と相乗平均の関係の証明は非常に簡単。


<div class="blank-box bb-blue">


<strong>相加平均と相乗平均の関係の証明</strong>




$a&gt;0$，$b&gt;0$ のとき，


<p style="padding-left: 40px;">$( \sqrt{a} - \sqrt{b} )^2 \geqq 0$</p>
<p style="padding-left: 40px;">$a-2 \sqrt{ab} +b \geqq 0$</p>
<p style="padding-left: 40px;">$\frac{a+b}{2} \geqq \sqrt{ab}$</p>


$a=b$ のとき等号成立


</div>


この定理は，次の不等式の証明や，整式の最小値を求めるようなときに使われるよ。




## 不等式の証明




最後は不等式の証明。




等式の証明と同じで方法はいろいろあるけど，基本的な3つの方法を紹介するね。


<div class="blank-box bb-blue">


<strong>不等式 $A&gt;B$ を証明する方法</strong>


<ul>
	<li>$A-B&gt;0$ を示す。</li>
	<li>$A&gt;0$ ， $B&gt;0$ のとき， $A^2-B^2&gt;0$ を示す。<br />
$A \geqq 0$ ， $B \geqq 0$ のとき， $A^2-B^2 \geqq 0$ を示す。</li>
	<li>相加平均と相乗平均の関係を使って示す。</li>
</ul>
</div>


両辺が具体的な値をとるわけではないから，基本的には「示す不等式を変形して，それが $0$ より大きい，あるいは， $0$ 以上であることを示す」方向にもっていくか，「相加平均と相乗平均の関係」を使うんだ。




もちろんそれ以外でも示せればなんでもいいんだけどね。




ちなみに，相加平均と相乗平均の関係の証明では2つ目の方法を使ったよ。




不等式の証明でよく使われる性質を抜粋したのが以下。


<div class="blank-box bb-blue">


<strong>不等式の性質の抜粋</strong>


<ul>
	<li>任意の2つの実数 $a$，$b$ については，$a&gt;b$，$a=b$，$a&lt;b$ のうちどれか1つの関係だけが成り立つ。</li>
	<li>$a&gt;b$ $\Leftrightarrow$ $a-b&gt;0$</li>
	<li>$a&lt;b$ $\Leftrightarrow$ $a-b&lt;0$</li>
	<li>$a^2 \geqq 0$ ( $a=0$ のとき等号成立)</li>
	<li>$a^2+b^2 \geqq 0$ ( $a=b=0$ のとき等号成立)</li>
	<li>$a&gt;0$，$b&gt;0$ のとき $a^2&gt;b^2$ $\Leftrightarrow$ $a&gt;b$</li>
	<li>$a&gt;0$，$b&gt;0$ のとき $a^2 \geqq b^2$ $\Leftrightarrow$ $a \geqq b$</li>
</ul>
</div>
<div class="blank-box bb-green">


例7)




$2(a^2+b^2) \geqq 3ab$ を示せ。また，等号成立条件を求めよ。


<p style="padding-left: 40px;">$(左辺)-(右辺)$</p>
<p style="padding-left: 40px;">$=2(a^2+b^2)-3ab$</p>
<p style="padding-left: 40px;">$=2a^2-3ab+2b^2$</p>
<p style="padding-left: 40px;">$=2(a- \frac{3}{4} b)^2 - \frac{9}{8} b^2 +2b^2$</p>
<p style="padding-left: 40px;">$=2(a- \frac{3}{4} b)^2 + \frac{7}{8} b^2$</p>
<p style="padding-left: 40px;">$\geqq 0$</p>


したがって， $(左辺) \geqq (右辺)$ となり与式は示された。




また， $(a- \frac{3}{4} b)^2=0$ かつ $\frac{7}{8} b^2=0$ ，つまり， $a=b=0$ のとき等号成立。


</div>


等式，不等式の証明で気をつけなければいけないのが，示したい式を最初から書いてはいけない，ということ。




何が示せれば与式が示されたことになるかをよく考え，それを示せたあとに与式が示されたと述べるようにしようね。




## 第9講のまとめ




不等式は乗り越えられたかな？




これまでの講で1番頭を使ったんじゃないかと思うよ。




この講で計算は一段落して，第10講からは図形を扱うよ。




ここまではあえて図形の考え方を使ってこなかったけど，図形の後半の講でそこまでに学んだことががっちり結びつく瞬間が来るからお楽しみに。




http://mathrao.com/instant-jhmath-provisional-8/




http://mathrao.com/instant-jhmath-provisional-10/
