---
title: "【インスタント中高数学】第5講 xyzという箱を自由自在に操ろう②【展開と因数分解】"
wp_id: 2202
content_type: "post"
status: "publish"
published_at: "2019-05-13 00:21:06"
wp_date: "2019-05-13 00:21:06"
modified_at: "2019-06-15 20:43:12"
legacy_url: "http://mathrao.com/instant-jhmath-provisional-5/"
legacy_path: "/instant-jhmath-provisional-5/"
legacy_slug: "instant-jhmath-provisional-5"
former_slugs: []
parent_wp_id: null
parent_title: null
hierarchy: ["【インスタント中高数学】第5講 xyzという箱を自由自在に操ろう②【展開と因数分解】"]
category: ["インスタント中高数学【草稿】"]
tags: []
mathrao_section: "インスタント中高数学"
mathrao_grade: null
mathrao_course: null
source_content_sha256: "95753b209d9667df622b69fe041e174f373ee9fd84e3847805cf9cb859e0b856"
---

http://mathrao.com/instant-jhmath-provisional-4/




## 箱庭で練習を




数学は，物事の本質を数式を用いて解明する学問。




もちろん数学に終わりはなく，数学者は未知の世界に挑み続けているんだ。




一方で中高数学というのは終わりのある箱庭のようなものだから，解明されていない謎はない。




そんな中で君は何を学ぶべきなのか？




それは，正しい歩き方。




中高数学は今まで数学者が解明してきた事実を学びやすいように整理したものだから，その中を隅から隅まで自由に歩き回ることができるようになれば，その先にある大学数学の世界，未知の世界も歩けるようになる。




実際に歩くかどうかは君次第だけど，箱庭で覚えたことは絶対に社会でも役に立つよ。




その証拠に，「大人になってから後悔したちゃんと勉強しておけばよかった教科」では常に数学は上位だからね。




第5講は第4講の続きで数学の基礎となる多項式の計算について学んでいくよ。




基礎というのは靴紐を結ぶようなもの。




靴紐を結ぶのに時間がかかっていたら，歩く練習に時間が使えなくなっちゃうよ。




## 指数の拡張と指数法則


<div class="info-box">


【定義】




<strong>冪乗</strong>(べきじょう)( $a^r$)：<strong>底</strong>( $a$ )および<strong>冪指数</strong>( $r$ )と呼ばれる2つの数に対して定まる演算




<strong>冪</strong>(べき)：冪乗の結果




<b>累乗</b>：冪指数が自然数の冪乗




$a \neq 0$ で，$n$ が正の整数のとき


<ul>
	<li>$\boldsymbol{a^0=1}$</li>
	<li>$\boldsymbol{a^{-n}= \displaystyle \frac{1}{a^n}}$</li>
</ul>


【定理】<strong>指数法則</strong>




$a \neq 0$，$b \neq 0$ で，$m$，$n$ が整数のとき


<ul>
	<li>$a^ma^n=a^{m+n}$</li>
	<li>$(a^m)^n=a^{mn}$</li>
	<li>$(ab)^n=a^nb^n$</li>
</ul>
</div>


最初に，指数を1段階拡張するよ。




第4講では，指数は数の掛け合わされた個数を表すとしていたから自然数しか考えていなかったんだけど，そこに $0$ と負の数を加えたのが上の定義。




実は， $a^r$ で表される演算は冪乗といって， $n$ が自然数のときだけ累乗というんだ。




冪乗では $a^r$ の $r$ を冪指数，あるいは，単に指数というよ。




これで指数にすべての整数を使うことができるようになったね。




ただ，指数に $0$ と負の数が加わったことによって，数の掛け合わされた個数だと考えるのが難しくなったんじゃないかな。




「 $2$ 個掛ける」は理解できるけど，「 $0$ 個掛ける」，「 $-2$ 個掛ける」は理解できないからね。




数学ではよくあることで，最初にも注意した通り，比喩だけで覚えてはいけないことの典型的な例。




$0$ 乗ってなんだ？マイナス乗ってなんだ？って最初は混乱すると思うけど，最初の理解の仕方に惑わされず，定義の通り書き換えられるようになろう。




こういったことが数学におけるギャップだと感じてつまずいてしまう場合があるんだけど，そのときは簡単な問題でいいから繰り返し練習して，自分の中に落とし込もう。




指数法則は指数の計算について成り立つ事柄をまとめたものなんだけど，自然数の指数であれば，具体的に考えることで理解できるはず。




それが整数に拡張しても成り立つということを覚えておこう。




あとは，指数に絡んでよく使われる考えが $-1$ の累乗。


<p style="padding-left: 40px;">$(-1)^n= \left \{ \begin{array}{cl} 1 &amp; (nが偶数のとき) \\ -1 &amp; (nが奇数のとき) \end{array} \right.$</p>


$-1$ は偶数回掛ければ $1$ になるから，上のように指数に注目することで符号が決まるんだ。




## 展開


<div class="info-box">


【定義】




<strong>展開</strong>：整式の積を単項式の和に表すこと




【定理】<strong>乗法公式</strong>


<ul>
	<li>和の平方：$(a+b)^2=a^2+2ab+b^2$</li>
	<li>差の平方：$(a-b)^2=a^2-2ab+b^2$</li>
	<li>和と差の積：$(a+b)(a-b)=a^2-b^2$</li>
	<li>$1$ 次式の積(1)：$(x+a)(x+b)=x^2+(a+b)x+ab$</li>
	<li>$1$ 次式の積(2)：$(ax+b)(cx+d)$ $=acx^2+(ad+bc)x+bd$</li>
	<li>和の立方：$(a+b)^3=a^3+3a^2b+3ab^2+b^3$</li>
	<li>差の立方：$(a-b)^3=a^3-3a^2b+3ab^2-b^3$</li>
	<li>立方の和：$(a+b)(a^2-ab+b^2)=a^3+b^3$</li>
	<li>立方の差：$(a-b)(a^2+ab+b^2)=a^3-b^3$</li>
</ul>
</div>


次は，(多項式) $\cdot$ (多項式) について考えていくよ。




展開というのは整式の積を単行式の和に表すことなんだけど，括弧をはずすというニュアンスが強いから，主に多項式が含まれる積のときに使われるんだ。




基本的には，括弧を一つの塊だと考えて文字に置き換えることで，多項式がいくつ掛けられていようが，分配法則を使って展開することができる。




展開した式に同類項がある場合はそれらをまとめよう。


<div class="blank-box bb-green">


例1)




$(x+2)(x-3)$ の場合




$M=x+2$ と置くと，$M(x-3)=xM-3M$ となり，文字をもとに戻して，$x(x+2)-3(x+2)=x^2+2x-3x-6=x^2-x-6$ となる。


</div>


展開の中でもよく使われるものが乗法公式としてまとめられているんだけど，どこまでを公式と考えるかは君次第だから，自分で追加してもいい。




ただ，上に挙げたものは最低限覚えておいてほしいな。




## 二項定理・多項定理


<div class="info-box">


【定義】※詳細は「確率」の講にて。




<strong>階乗( $n!$ )</strong>：$n$ に1ずつ小さくした数を次々と1になるまでかけたもの


<p style="padding-left: 30px;">$n!=n(n-1)(n-2)……3 \cdot 2 \cdot 1$</p>
<p style="padding-left: 30px;">$0!=1$</p>


$\boldsymbol{n}$ <strong>個から</strong> $\boldsymbol{r}$ <strong>個取る組合せの総数：</strong> ${}_n \mathrm{ C }_r$


<p style="padding-left: 40px;">${}_n \mathrm{ C }_r= \frac{n(n-1)(n-2)……(n-r+1)}{r(r-1)(r-2)……3 \cdot 2 \cdot 1} = \frac{n!}{r!(n-r)!}$ ( $r \leqq n$ )</p>
<p style="padding-left: 40px;">${}_n \mathrm{ C }_n=1$</p>
<p style="padding-left: 40px;">${}_n \mathrm{ C }_1=n$</p>
<p style="padding-left: 40px;">${}_n \mathrm{ C }_0=1$</p>


【定理】<strong>二項定理</strong>




$(a+b)^n={}_n \mathrm{ C }_0a^n+{}_n \mathrm{ C }_1a^{n-1}b+{}_n \mathrm{ C }_2a^{n-2}b^2+……+{}_n \mathrm{ C }_ra^{n-r}b^r+……+{}_n \mathrm{ C }_{n-1}ab^{n-1}+{}_n \mathrm{ C }_nb^n$


<p style="padding-left: 30px;">【定義】二項定理の $r+1$ 番目の項 ${}_n \mathrm{ C }_ra^{n-r}b^r$ を $(a+b)^n$ の展開式の<strong>一般項</strong>といい，係数 ${}_n \mathrm{ C }_r$ を<strong>二項係数</strong>という。</p>


【定理】<strong>多項定理</strong>




$(a+b+c)^n$ の展開式の一般項は $\displaystyle \frac{n!}{p!q!r!}a^pb^qr^c$




ただし，$p$，$q$，$r$ は整数で，$p \geqq 0$，$q \geqq 0$，$r \geqq 0$，$p+q+r=n$


</div>


乗法公式では2項の多項式の3乗までしかなかったけど，これが4乗，5乗…と増えていったどうなるか考えてみよう。




まず，2項の多項式の3乗=和の立方を公式ではなく，あえて文字で置いて展開してみるよ。


<p style="padding-left: 40px;">$ \color{red}{R} = \color{red}{a} + \color{red}{b} $ ， $ \color{blue}{B} = \color{blue}{a} + \color{blue}{b} $ と置くと，<br />
$(a+b)^3$<br />
$=( \color{red}{a} + \color{red}{b} )( \color{blue}{a} + \color{blue}{b} )( \color{green}{a} + \color{green}{b} )$<br />
$= \color{red}{R} \color{blue}{B} ( \color{green}{a} + \color{green}{b} )$<br />
$= \color{red}{R} \color{blue}{B} \color{green}{a} + \color{red}{R} \color{blue}{B} \color{green}{b}$<br />
$= \color{red}{R} \color{green}{a} ( \color{blue}{a} + \color{blue}{b} )+ \color{red}{R} \color{green}{b} ( \color{blue}{a} + \color{blue}{b} )$<br />
$= \color{red}{R} \color{blue}{a} \color{green}{a} + \color{red}{R} \color{blue}{b} \color{green}{a} + \color{red}{R} \color{blue}{a} \color{green}{b} + \color{red}{R} \color{blue}{b} \color{green}{b} $<br />
$= \color{blue}{a} \color{green}{a} ( \color{red}{a} + \color{red}{b} )+ \color{blue}{b} \color{green}{a} ( \color{red}{a} + \color{red}{b} )+ \color{blue}{a} \color{green}{b} ( \color{red}{a} + \color{red}{b} )+  \color{blue}{b} \color{green}{b} ( \color{red}{a} + \color{red}{b} )$<br />
$= \color{red}{a} \color{blue}{a} \color{green}{a} + \color{red}{b} \color{blue}{a} \color{green}{a} + \color{red}{a} \color{blue}{b} \color{green}{a} + \color{red}{b} \color{blue}{b} \color{green}{a} + \color{red}{a} \color{blue}{a} \color{green}{b} + \color{red}{b} \color{blue}{a} \color{green}{b} + \color{red}{a} \color{blue}{b} \color{green}{b} + \color{red}{b} \color{blue}{b} \color{green}{b}$<br />
$=a^3+3a^2b+3ab^2+b^3$</p>


これをさらにこんなふうにまとめてみる。


<p style="padding-left: 40px;">$a^3= \color{red}{a} \color{blue}{a} \color{green}{a} $<br />
$3a^2b= \color{red}{b} \color{blue}{a} \color{green}{a} + \color{red}{a} \color{blue}{b} \color{green}{a} + \color{red}{a} \color{blue}{a} \color{green}{b} $<br />
$3ab^2= \color{red}{b} \color{blue}{b} \color{green}{a} + \color{red}{b} \color{blue}{a} \color{green}{b} + \color{red}{a} \color{blue}{b} \color{green}{b} $<br />
$b^3= \color{red}{b} \color{blue}{b} \color{green}{b} $</p>


ここまででどんなことに気づけたかな？




同類項をまとめる前の項はすべて赤青緑となっていて，その個数は8個。




つまり，すべての項は3つの括弧からそれぞれ $a$ か $b$ を選んでいて，展開したものはその組合せがすべて網羅されているということ。




これで，乗法公式においてどんな意味があるか分からなかった係数にも意味を見いだせるね。




例えば， $a^2b$ の係数の $3$ は，それぞれの括弧から $a$ か $b$ を取り出したとき， $a$ が2つ， $b$ が1つになるような組合せが $aab$ ， $aba$ ， $baa$ の3通りであるということからきている。




そして，この考え方が $n$ 乗でも成り立つというのを示しているのが二項定理，項が3つの場合は多項定理なんだ。




こういった通り数については確率の講で詳しく考えるから，今は係数の意味だけ覚えておいてほしい。




ここで，二項定理の係数を視覚的に分かりやすく表現したパスカルの三角形というものを紹介するね。


<div class="blank-box bb-blue">


<strong>パスカルの三角形</strong>


<p style="padding-left: 30px;">$\begin{array}{cccccccccccc} (a+b)^1 &amp; &amp; &amp; &amp; &amp; 1 &amp; &amp; 1 &amp; &amp; &amp; &amp; \\ (a+b)^2 &amp; &amp; &amp; &amp; 1 &amp; &amp; 2 &amp; &amp; 1 &amp; &amp; &amp; \\ (a+b)^3 &amp; &amp; &amp; 1 &amp; &amp; 3 &amp; &amp; 3 &amp; &amp; 1 &amp; &amp; \\ (a+b)^4 &amp; &amp; 1 &amp; &amp; 4 &amp; &amp; 6 &amp; &amp; 4 &amp; &amp; 1 &amp; \\ (a+b)^5 &amp; 1 &amp; &amp; 5 &amp; &amp; 10 &amp; &amp; 10 &amp; &amp; 5 &amp; &amp; 1 \\ \end{array}$</p>


$(a+b)^n$ を展開した各項の係数だけを取り出して順に並べると，上の図のような三角形(パスカルの三角形)になる。


<ul>
	<li>各行の両端の数字は1である。</li>
	<li>2行目以降の両端以外の数は，その左上の数と右上の数の和に等しい。</li>
	<li>各行の数は中央に関して左右対称である。</li>
</ul>
</div>


これを使えば，二項定理を使わなくても係数を求めることができるし，二項定理のように1つの項に着目するわけじゃないから，展開後のすべての係数が一気に分かるね。




この数の並びに敏感になるのも後々大事になってくるよ。




## 因数分解


<div class="info-box">


【定義】




<strong>因数</strong>：整式を複数の整式の積に表したときの1つ1つの整式




<strong>素数</strong>： $1$ より大きい自然数で，正の約数が $1$ とその数自身のみであるもの




<strong>合成数</strong>： $2$ 以上の自然数で，素数でない数




<strong>素因数</strong>：素数である因数




<strong>素因数分解</strong>：自然数を素因数だけの積に表すこと


<p style="padding-left: 40px;">素因数分解の一意性：1つの合成数の素因数分解は積の順序を考えなければ1通りであること</p>


<strong>互いに素</strong>：2つの整数の最大公約数が1であること




<strong>因数分解</strong>：整式を $1$ 次以上の整式の積に表すこと




<strong>共通因数</strong>：整式のすべての項に共通な因数




<strong>共通因数でくくる</strong>：整式に共通因数があるとき，分配法則を用いて $AB+AC=A(B+C)$ の形に因数分解すること




【定理】<strong>因数分解公式</strong>


<ul>
	<li>和の平方：$a^2+2ab+b^2=(a+b)^2$</li>
	<li>差の平方：$a^2-2ab+b^2=(a-b)^2$</li>
	<li>平方の差：$a^2-b^2=(a+b)(a-b)$</li>
	<li>$2$ 次 $3$ 項式(1)：$x^2+(a+b)x+ab=(x+a)(x+b)$</li>
	<li>$2$ 次 $3$ 項式(2)：$acx^2+(ad+bc)x+bd=(ax+b)(cx+d)$</li>
	<li>和の立方：$a^3+3a^2b+3ab^2+b^3=(a+b)^3$</li>
	<li>差の立方：$a^3-3a^2b+3ab^2-b^3=(a-b)^3$</li>
	<li>立方の和：$a^3+b^3=(a+b)(a^2-ab+b^2)$</li>
	<li>立方の差：$a^3-b^3=(a-b)(a^2+ab+b^2)$</li>
</ul>
</div>


用語の確認をしたいんだけど，いきなり残念なお知らせ。




因数というのは整式を複数の整式の積に表したときの1つ1つの整式のことなんだけど，実は，因数は無限にあるんだ。




つまり，整式を因数分解の計算結果も無限にあるということ。




にもかかわらず，学校で扱う問題は「因数分解せよ」としか書かれていない。




中高数学の闇でもあるんだけど，因数分解をするときは空気を読まなきゃいけないんだ。




数学においては問題文に書かれていることがすべてだから，憶測で条件を追加したり排除したりすることは絶対にあってはならない，はずなんだけどね。




それも踏まえた上で，まずは素因数分解について。




素因数分解とは自然数を素因数だけの積に表すこと。




例えば， $6=2 \cdot 3$ ， $12=2^2 \cdot 3$ ， $100=2^2 \cdot 5^2$ 。




同じ素因数が複数含まれている場合は累乗を使って表そう。




ちなみに，素因数分解は計算結果が一つに定まるから安心してね。




次に因数分解について。




因数分解は展開と逆の操作で，整式を1次以上の整式の積に表すこと。




因数分解公式を見れば分かるけど，すべて乗法公式をひっくり返したものになっているよね。




因数分解は展開のように作業的に計算をするのではなく，何を展開したらこの形になるのかということを見抜かなきゃいけない。




つまり，与えられた式がどのパターンに当てはまるかを瞬時に見極めなきゃいけないということ。




ほとんどは特殊な形をしているから見分けやすいんだけど，2次3項式は3つの係数を見て推測するから，かなりの練習が必要だよ。




あと，整式のすべての項に共通な因数のことを共通因数というんだけど，共通因数でくくることも因数分解に含まれているからね。




ちなみに，因数分解の計算結果は展開することで検算ができるから見直しを怠らないように。




そして，最初にも言った通り，因数は無限にあるから因数分解の答えは一つに定まらないんだけど，なんとなくのルールはある。


<ul>
	<li>整数の因数は自然数のみ</li>
	<li>括弧内に分数がない状態にする</li>
	<li>括弧内の整式に共通因数がない状態にする</li>
	<li>なるべく，1次の整式にまで因数分解する</li>
</ul>


これらはほぼ共通のルールなんだけど，正直先生のさじ加減。




授業で先生が言っている通りにしないと，思いがけない減点につながるから要注意だよ。




## 分数式の計算


<div class="info-box">


【定義】




<strong>分数式</strong>： $A$ ， $B$ が整式のとき， $ \displaystyle \frac{A}{B} $ ( $B \neq 0$ ) の形の式




<strong>既約分数式</strong>：これ以上約分できない分数式




<strong>繁分数式</strong>：分母や分子に分数式を含む分数式




<strong>部分分数分解</strong>：1つの分数式を，それ以上簡単にできない2つ以上の分数式の和として表すこと


</div>


さあ，整式の計算も終盤だから最後まで気を引き締めていこう。




分数の分母や分子に整式が含まれる式を分数式，これ以上約分できない分数式を既約分数式，分母や分子に分数式を含む分数式を繁分数式という。




と，新しい用語はあるものの，計算は従来通り，分母と分子に同じものを掛けても値は変わらないという分数の基本性質を使うことになる。




新しい要素としては，分母と分子を因数分解したときに同じ因数があった場合，整式の約分ができるくらい。




分数が苦手でなくても整式になった途端混乱してしまったら，その都度似たような数だけの仮の分数を作って，やっていいこと，いけないことを確認するようにしよう。




こうやって具体化して確認するというのは，色々なことを一貫して理解するためにとても有効だよ。




あと，中高では分母が0であってはいけない，ということにより敏感にならないといけない。




整式を扱うと，今まで見えていたものが見えづらくなることもあるから要注意だよ。


<div class="blank-box bb-blue">


<strong>分数式の計算</strong>




$A$ ， $B$ ， $C$ ， $D$ を整式とする。




(すべての式において，分母は $0$ でないとする。)




<strong>基本性質</strong>


<ul>
	<li>$\displaystyle \frac{A}{B} = \frac{AC}{BC}$ (ただし $C \neq 0$ )</li>
</ul>


<strong>四則計算</strong>


<ul>
	<li>加法：$\displaystyle \frac{A}{C} + \frac{B}{C} = \frac{A+B}{C}$</li>
	<li>減法：$\displaystyle \frac{A}{C} - \frac{B}{C} = \frac{A-B}{C}$</li>
	<li>乗法：$\displaystyle \frac{A}{B} \times \frac{C}{D} = \frac{AC}{BD}$</li>
	<li>除法：$\displaystyle \frac{A}{B} \div \frac{C}{D} = \frac{A}{B} \times \frac{D}{C} = \frac{AD}{BC}$</li>
</ul>


<strong>繁分数式の計算</strong>


<ul>
	<li>$\frac{A}{B} =A \div B$ を利用して，分子を分母で割る，または，$\frac{A}{B} = \frac{A \times C}{B \times C}$ を利用して，分母や分子の分数式を整式にする。</li>
</ul>


<strong>部分分数分解</strong>


<ul>
	<li>例)　$\displaystyle \frac{2x-1}{x(x-1)} = \frac{1}{x} + \frac{1}{x-1}$</li>
	<li>例)　$\displaystyle \frac{1}{(n+1)(n+2)} = \frac{1}{n+1} - \frac{1}{n+2}$</li>
</ul>
</div>


## 整式の除法


<div class="info-box">


【定義】




<strong>剰余</strong>：除法における余り




【定理】<strong>除法の基本公式</strong>




同じ1つの文字についての2つの整式 $A$，$B$ ( $B \neq 0$ )において，$A$ を $B$ で割ったときの商を $Q$，剰余を $R$ とすると


<p style="padding-left: 30px;">$A=BQ+R$</p>


ただし，$R$ は0か，$B$ より次数の低い整式。


</div>


整式の除法は分数式にするだけでなく，剰余を求める除法と同じ考え方で式変形することができるんだ。


<div class="blank-box bb-green">


<strong>整式の除法</strong>




例2)　$(x^3-10x+2) \div (x+2)$ の商と剰余を求める。


<p style="padding-left: 40px;">$ \begin{array}{ccccc} &amp; x^2 &amp; -2x &amp; -6 &amp; \\ \hline x+2 &amp; ) \ x^3 &amp; &amp; -10x &amp; +2 \\ &amp; x^3 &amp; +2x^2 &amp; &amp; \\ \hline &amp; &amp; -2x^2 &amp; -10x &amp; \\ &amp; &amp; -2x^2 &amp; -4x &amp; \\ \hline &amp; &amp; &amp; -6x &amp; +2 \\ &amp; &amp; &amp; -6x &amp; -12 \\ \hline &amp; &amp; &amp; &amp; 14 \end{array} $</p>
<p style="padding-left: 40px;">商は $x^2-2x-6$ ，剰余は $14$</p>
</div>


整式 $A$ を整式 $B$ で割るときには，次のことに注意しよう。


<ul>
	<li>$A$ も $B$ も降べきの順に整理してから割り算を行う。</li>
	<li>剰余の次数が割る式 $B$ の次数より低くなるか，あまりが0になるまで計算を続ける。</li>
</ul>


整式を1次式で割るときには，組立除法という特殊な筆算を使うと圧倒的に速くできるから練習してみよう。


<div class="blank-box bb-green">


<strong>組立除法</strong>




組立除法は整式 $P(x)$ を1次式 $x-k$ で割ったときの商 $Q(x)$，剰余 $R$ を求める簡便法である。




$P(x)=ax^3+bx^2+cx+d$ を $x-k$ で割るとき


<p style="padding-left: 30px;">$\begin{array}{ccccc} a &amp; b &amp; c &amp; d &amp; | \underline{k} \\ &amp; ak &amp; mk &amp; nk &amp; \\ \hline a &amp; m &amp; n &amp; R &amp; \\ \end{array}$</p>


として，商 $Q(x)=ax^2+mx+n$ と $R$ を求める。




例3)




$(x^3-10x+2) \div (x+2)$ の商と剰余を求める。


<p style="padding-left: 30px;">$\begin{array}{ccccc} 1 &amp; 0 &amp; -10 &amp; 2 &amp; | \underline{-2} \\ &amp; -2 &amp; 4 &amp; 12 &amp; \\ \hline 1 &amp; -2 &amp; -6 &amp; 14 &amp; \\ \end{array}$</p>
<ol>
	<li>1行目に割られる式の係数 $1$，$0$，$-10$，$2$ と割る式 $x+2=x-(-2)$ の $-2$ を書く。</li>
	<li>3行目の一番左に，1行目の一番左の $1$ を下ろす。</li>
	<li>下ろした $1$ と右上の $-2$ の積 $-2$ を2行目の2列目に書く。</li>
	<li>1，2行目の2列目を縦に足し，和 $0+(-2)=-2$ を3行目の2列目に書く。</li>
	<li>同様に，今書いた $-2$ と右上の $-2$ の積 $4$ を2行目の3列目に書く。</li>
	<li>1，2行目の3列目を縦に足し，和 $-10+4=-6$ を3行目の3列目に書く。</li>
	<li>同様に，今書いた $-6$ と右上の $-2$ の積 $12$ を2行目の4列目に書く。</li>
	<li>1，2行目の4列目を縦に足し，和 $2+12=14$ を3行目の4列目に書く。</li>
	<li>結果，商が $x^2-2x-6$，剰余が $14$ となる。</li>
</ol>


※ $(8x^3-2x^2-7x+6) \div (4x-3)$ のように割る式の1次の項の係数が1でない場合，$(8x^3-2x^2-7x+6) \div (x- \frac{3}{4}) \div 4$ と変形し，$(8x^3-2x^2-7x+6) \div (x- \frac{3}{4})$ を先に行い，最後に $Q(x) \div 4$ を行うことができる。ただし，剰余は最初に求めたものである。


<p style="padding-left: 30px;">$\begin{array}{rcl} 8x^3-2x^2-7x+6 &amp; = &amp; (4x-3)Q(x)+R \\ &amp; = &amp; (x- \frac{3}{4}) \cdot 4Q(x)+R \\ \end{array}$</p>
</div>


## 剰余の定理・因数定理


<div class="info-box">


【定理】<strong>剰余の定理</strong>




整式 $P(x)$ を1次式 $x-k$ で割ったときの剰余は $P(k)$




※整式 $P(x)$ を1次式 $ax+b$ で割ったときの剰余は $P(- \frac{b}{a})$




【定理】<strong>因数定理</strong>




1次式 $x-k$ が整式 $P(x)$ の因数である $\Leftrightarrow$ $P(k)=0$




※1次式 $ax+b$ が整式 $P(x)$ の因数である $\Leftrightarrow$ $P(- \frac{b}{a})=0$


</div>


整式を扱うとき，どの文字に着目した整式であるかをはっきりさせ，扱いやすくするために， $x$ の整式を $P(x)$，$Q(x)$ のように表すことがあるんだ。




さらに，整式の文字に値を代入したことを表現したいとき， $P(x)$ の $x$ に数 $k$ を代入した値を $P(k)$ と表せる。




例えば，これらを使って除法の基本公式を表すと，


<p style="padding-left: 40px;">整式 $P(x)$ を整式 $A$ で割ったときの商を $Q(x)$，剰余を $R(x)$ とすると， $P(x)=A Q(x)+R(x)$ が成り立つ。</p>


となる。




剰余の定理と因数定理はこの除法の基本公式から導かれた定理。




これらの定理は，整式の除法の剰余を求めたり，因数を探す，あるいは，因数であることを確かめるときに使えるから，因数分解でも有効だよ。




証明はとても簡単。


<div class="blank-box bb-blue">


<strong>剰余の定理の証明</strong>




整式 $P(x)$ を1次式 $x-k$ で割ったときの商を $Q(x)$ ，剰余を $R$ とすると，除法の基本公式より，


<p style="padding-left: 40px;">$P(x)=(x-k)Q(x)+R$</p>


と表せるので， $x$ に $k$ を代入すると， $P(k)=R$ となる。




<strong>因数定理の証明</strong>




1次式 $x-k$ が整式 $P(x)$ の因数であるとき，整式 $P(x)$ を $x-k$ で割ったときの商を $Q(x)$ とすると， $P(x)=(x-k)Q(x)$ と表せるので， $x$ に $k$ を代入して， $P(k)=0$ が得られる。




逆に， $P(k)=0$ のとき，剰余の定理より，整式 $P(x)$ を $x-k$ で割ったときの剰余が $0$ になる。




よって，$P(x)=(x-k)Q(x)$ となる。


</div>


## 対称式と交代式


<div class="info-box">


【定義】




$a$ と $b$ の<strong>対称式</strong>：$a$，$b$ に関する式で，文字 $a$ と $b$ を入れ替えても，元の式と同じ式になるもの




$a$，$b$，$c$ の<strong>対称式</strong>：$a$，$b$，$c$ に関する式で，どの2つの文字を入れ替えても，元の式と同じ式になるもの




$a$，$b$ の対称式の<strong>基本対称式</strong>：$a+b$，$ab$




$a$，$b$，$c$ の対称式の<strong>基本対称式</strong>：$a+b+c$，$ab+bc+ca$，$abc$




$a$ と $b$ の<strong>交代式</strong>：$a$，$b$ に関する式で，文字 $a$ と $b$ を入れ替えると，元の式と符号だけが変わる(元の式の $(-1)$ 倍になる)もの




$a$，$b$，$c$ の<strong>交代式</strong>：$a$，$b$，$c$ に関する式で，どの2つの文字を入れ替えても，元の式と符号だけが変わるもの




【定理】




全ての対象式は基本対象式で表すことができる。




例)


<p style="padding-left: 30px;">$a^2+b^2=(a+b)^2-2ab$</p>
<p style="padding-left: 30px;">$a^3+b^3=(a+b)^3-3ab(a+b)$</p>
<p style="padding-left: 30px;">$a^2+b^2+c^2=(a+b+c)^2-2(ab+bc+ca)$</p>


【定理】




$a$，$b$，$c$ の対称式が $a+b$，$b+c$，$c+a$ のうち1つを因数にもてば，他の2つも因数にもつ。


<p style="padding-left: 30px;">※$a$，$b$，$c$ の対称式がこの3つを必ず因数にもつわけではない。</p>


例)


<p style="padding-left: 30px;">$a(b+c)^2+b(c+a)^2+c(a+b)^2-4abc=(a+b)(b+c)(c+a)$</p>


【定理】




$a$，$b$ の交代式は，必ず $a-b$ を因数にもつ。




例)


<p style="padding-left: 30px;">$a^2-b^2=(a+b)(a-b)$</p>
<p style="padding-left: 30px;">$a^3-b^3=(a-b)(a^2+ab+b^2)$</p>


$a$，$b$，$c$ の交代式は，必ず $(a-b)(b-c)(c-a)$ を因数にもつ。




例)


<p style="padding-left: 30px;">$a(b^2-c^2)+b(c^2-a^2)+c(a^2-b^2)=(a-b)(b-c)(c-a)$</p>
</div>


対称式と交代式は整式の中でも特徴のある式で，とても面白い性質があるんだ。




上に挙げた定理はどれも実用性のあるものだから，因数分解はもちろん，イン数でも最後の方に出てくる単元まで忘れずにね。




## 因数分解の手順




当然だけど，問題に出されたものであればすべて因数分解できる。




ただ，それができたりできなかったりするのは感覚に頼ってしまっている場合が多いんだ。




因数分解は展開と違って予測がしにくい分，しっかりと選択肢を持ち，手順に沿って，確実に解かなきゃいけない。




この講で学んだことをフル動員して因数分解の手順をまとめたから確認してね。


<div class="blank-box bb-blue">


<strong>因数分解の手順</strong>


<ol>
	<li><strong>共通因数でくくる</strong><br />
すべての項に共通な因数があればくくり出す。<br />
共通因数でくくっていない状態でも因数分解を進められるから見落としがち。</li>
	<li><strong>公式の適用・たすき掛け</strong><br />
公式や二項定理の逆を適用する，または，たすき掛けを行う。</li>
	<li><strong>文字置き</strong><br />
明らかに同じ形がある，または，作れそうであれば整式を部分的に因数分解し，他の文字に置き換える。その後，公式を適用する，または，たすき掛けを行い，最後に置き換えた文字を元に戻す。</li>
	<li><strong>因数定理<br />
</strong>因数定理を用いて因数を探す。代入する値は，定数項の約数に絞る。</li>
	<li><strong>複2次式</strong><br />
次数が2の倍数のみ(複2次式)の場合，(文字の $2$ 乗)を文字で置くか，平方の差を作り，和と差の積を適用する。</li>
	<li><strong>対称式・交代式</strong><br />
対称式，交代式の場合は，性質を利用して因数を探す。</li>
	<li><strong>展開</strong><br />
与式が最初から部分的に因数分解されている場合は最初に文字置きを検討し，できない場合は整式が煩雑になりすぎないよう注意して展開し，手順の最初に戻る。</li>
	<li><strong>最低次数の文字に着目して降べきの順に整理する</strong><br />
1～7に当てはまらず，2元以上や項数が多い場合はこの方針をとる。整理した後，着目した文字の係数や定数項を部分的に因数分解し，文字を含んだ状態で因数分解公式の適用・たすき掛けを行う。</li>
	<li><strong>これ以上因数分解できる部分がないか確認する</strong><br />
因数分解は問題によって計算結果の範囲が指定されている場合があり，そこに到達していない場合は誤答になるので，条件をしっかり確認して途中で終わらないようにする。</li>
</ol>
</div>


## 第5講のまとめ




さあ，これで準備は整った。




第6講からは数がどんどん拡張していくよ。




ここまでで身につけたものを多用するから，もし分からなくなったら戻って確認してね。




http://mathrao.com/instant-jhmath-provisional-4/




http://mathrao.com/instant-jhmath-provisional-6/
