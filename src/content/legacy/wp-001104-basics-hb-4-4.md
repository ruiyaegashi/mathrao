---
title: "【定義・定理・公式】高校数学基本事項 - 数学B - 統計的な推測"
wp_id: 1104
content_type: "page"
status: "publish"
published_at: "2018-10-21 02:34:06"
wp_date: "2018-10-21 02:34:06"
modified_at: "2018-10-21 02:34:06"
legacy_url: "http://mathrao.com/basics-of-high-school-math/basics-hb-4-4/"
legacy_path: "/basics-of-high-school-math/basics-hb-4-4/"
legacy_slug: "basics-hb-4-4"
former_slugs: []
parent_wp_id: 448
parent_title: "【定義・定理・公式】高校数学基本事項一覧"
hierarchy: ["【定義・定理・公式】高校数学基本事項一覧", "【定義・定理・公式】高校数学基本事項 - 数学B - 統計的な推測"]
category: []
tags: []
mathrao_section: "高校数学"
mathrao_grade: null
mathrao_course: "数学B"
source_content_sha256: "45bda35abef16a9a039d562751953af5ccf7ccce3a17a303de977c7f52cd9771"
---

## 母集団と標本




【定義】




<strong>全数調査</strong>：対象全体からデータを集めて調べる統計的な調査




<strong>標本調査</strong>：対象全体から一部を抜き出して調べる統計的な調査




<strong>母集団</strong>：標本調査の対象全体




<strong>個体</strong>：母集団に属する個々の対象




<strong>母集団の大きさ</strong>：個体の総数




<strong>標本</strong>：調査のために母集団から抜き出された個体の集合




<strong>標本の大きさ</strong>：標本に属する個体の総数




<strong>抽出</strong>：母集団から標本を抜き出すこと




<strong>無作為抽出</strong>：母集団の各個体を等しい確率で抽出する方法


<p style="padding-left: 30px;">※無作為抽出では，乱数さいや乱数表などが使われる。</p>


<strong>復元抽出</strong>：毎回元に戻しながら個体を1個ずつ抽出すること




<strong>非復元抽出</strong>：個体をもとに戻さないで抽出すること




<strong>無作為標本</strong>：無作為抽出によって選ばれた標本




<strong>統計的な調査対象の特性</strong>：身長，時間，不良品などの特定の性質




<strong>変量</strong>：ある特性を表す数量




<strong>母集団分布</strong>：母集団における変量 $x$ の分布




<strong>母平均( $m$ )</strong>：母集団における変量 $x$ の平均




<strong>母標準偏差( $\sigma$ )</strong>：母集団における変量 $x$ の標準偏差


<p style="padding-left: 30px;">※大きさ1の無作為標本について，変量 $x$ の値を確率変数と見たときの期待値，標準偏差は，母平均 $m$，母標準偏差 $\sigma$ と一致する。</p>


&nbsp;




## 標本平均と標本比率




【定義】




<strong>標本平均( $\overline{X}$ )</strong>




母集団から大きさ $n$ の無作為標本を抽出し，それらの変量 $x$ の値を $X_1,X_2,\cdots\cdots,X_n$ とするとき


<p style="padding-left: 30px;">$\overline{X}=\displaystyle\frac{X_1+X_2+\cdots\cdots+X_n}{n}$</p>


<strong>標本平均の期待値( $E(\overline{X})$ )・標準偏差( $\sigma(\overline{X})$ )・分布</strong>




母平均 $m$，母標準偏差 $\sigma$ の母集団から大きさ $n$ の無作為標本を抽出するときの標本平均を $\overline{X}$ とすると


<p style="padding-left: 30px;">$E(\overline{X})=m$</p>
<p style="padding-left: 30px;">$\sigma(\overline{X})=\displaystyle\frac{\sigma}{\sqrt{n}}$</p>


また，$\overline{X}$ は $n$ が大きとき，近似的に正規分布 $N(m,\frac{\sigma^2}{n})$ に従う。




すなわち，確率変数 $Z=\frac{\overline{X}-m}{\frac{\sigma}{\sqrt{n}}}$ は近似的に標準正規分布 $N(0,1)$ に従う。




<strong>母比率</strong>：母集団の中である特性をもつものの割合




<strong>標本比率</strong>：抽出された標本の中である特性を持つものの割合


<p style="padding-left: 30px;">※ある特性の母比率 $p$ の母集団から抽出された大きさ $n$ の無作為標本について，標本比率 $R$ は $n$ が大きいとき，近似的に正規分布 $N(p,\frac{pq}{n})$ に従うとみなすことができる。</p>


&nbsp;




## 大数の法則




【法則】




母平均 $m$ の母集団から大きさ $n$ の無作為標本を抽出するとき，$n$ が大きくなるに従ってその標本平均 $\overline{X}$ は母平均 $m$ に近づく。




&nbsp;




## 母平均の推定




正規分布表によると $P(|Z|\leqq1.96)=0.95$ であるから


<p style="padding-left: 30px;">$P\left(|\overline{X}-m|\leqq1.96\cdot\displaystyle\frac{\sigma}{\sqrt{n}}\right)=0.95$</p>


このことから，標本の大きさ $n$ が大きいとき，母平均 $m$ に対する


<p style="padding-left: 30px;">信頼度95%の信頼区間は $\left[\overline{X}-1.96\cdot\displaystyle\frac{\sigma}{\sqrt{n}},\overline{X}+1.96\cdot\frac{\sigma}{\sqrt{n}}\right]$</p>


母平均 $m$ に対して信頼度95%の信頼区間を求めることを，「母平均 $m$ を信頼度95%で推定する」ということがある。




&nbsp;




## 母比率の推定




正規分布表によると $P(|Z|\leqq1.96)=0.95$ であるから


<p style="padding-left: 30px;">$P\left(|R-p|\leqq1.96\sqrt{\displaystyle\frac{p(1-p)}{n}}\right)=0.95$</p>


このことから，標本の大きさ $n$ が大きいとき，大数の法則により $R$ は $p$ に近いとみなしてよいから，母比率 $p$ に対する


<p style="padding-left: 30px;">信頼度95%の信頼区間は $\left[R-1.96\sqrt{\displaystyle\frac{R(1-R)}{n}},R+1.96\sqrt{\displaystyle\frac{R(1-R)}{n}}\right]$</p>
