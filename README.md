# マイクロ風力発電機

家庭用扇風機の風でも発電できる、小型風力（手回し）発電機の試作と実験記録  

---

## コア有りアキシャルギャップ型

個人開発としては少し挑戦的かもしれませんが、実用的なマイクロ発電機の実現を目指して研究を進めています。  
この発電機は 12 個のコイルを使用した単相交流発電機で、家庭用扇風機のような弱い風でも発電できるよう、コギングトルクの低減に取り組んでいます。

現在は、コイルのコア材やコギング抑制用の磁性体プレートに適した材料を探していますが、個人で入手できる材料には限界があり、開発の大きな課題となっています。

🌐 [試作品のWebページを見る](https://isotsurishi.github.io/MICRO-WIND-GENERATOR/)

---

## 発電機の構造

本試作品はアキシャルギャップ型のコアコイルを用いた単相交流発電機です。

- コアにはアンテナ用フェライトロッド（材質の詳細は不明）を使用  
- アキシャル方向の位置決めにリング状ネオジム磁石の反発を利用  
- コギング抑制のため、磁石とコイルの間に磁性体板を配置  
- 磁石背面からの漏れ磁束を防ぐため、隣接磁石を磁性体で連結  
- 負荷による逆起電力を抑えるため、全コイルを直列接続  

今回使用したフェライトロッドは透磁率は良いものの磁気飽和しやすく、コギングが残る原因になったと考えています。  
実用化する場合は、一度バッテリーに充電してから出力する方式が適していると判断しています。

---

## 磁性体粉末の入手について

現在、コギングトルクをどこまで低減できるか検証するために、**粒径の揃った磁性体粉末**を用いた実験を行いたいと考えています。  
しかし、個人で少量入手することが非常に難しく、プロジェクトの進行に大きな制約となっています。

実験してみたい粉末材料は次の通りです。

- ナノ結晶材粉末（高透磁率・低損失・高飽和磁束密度）  
- アモルファス金属粉末  
- 積層用純鉄粉末  
- パーマロイ系、ケイ素鋼系などの軟磁性粉末  

実験してみたかった材料の入手がかなわなかったので、再度、アンテナ用のフェライトロッドを通販で発注
コギング抑制板の容積を増やしてコギングが更に減るか実験



フェライトロッドを砕いてエポキシ樹脂で固めた材料の抵抗を測定すると測定位置にもよりますが、２～７MΩの導体となっていました


## 磁束がコアに集まりやすくするために

コアに使う磁石よりより大きい面積のフェライトの棒を再度探したのですが見つからなかったので、磁石の面積の小さいのネオジム磁石（Φ6t3）にて検証を予定しています

現行の試作品より太いコアの材料が見つからないと強い磁石による検証はできそうもないです

プロペラも私が作ったものではなく、効率の良いものを使ってみたいです

ホームページにも記載しましたが、材料の調達が叶わないと次の検証はできません

残念ではありますが、暫くは何か良い方法が有るか検討します

![Φ6t3のネオジム磁石、磁石から磁束が漏れない板（砂鉄+エポキシ樹脂）、フェライトロッド](img/Φ6-t3.JPG)

### 🔍 磁石の変更に伴い垂直軸型プロペラも変更

![垂直軸型プロペラ](img/suihei.JPG)

### 🔍 磁石の変更に伴い水平軸型プロペラも変更

![水平軸型プロペラ](img/suityoku.JPG)



## ご支援・ご協力のお願い

このプロジェクトは個人で開発・検証を行っています。

恥ずかしながら、資金が不足しています。

材料の調達や加工方法など、情報提供やアドバイスを無償でいただけるととても助かります。

GitHubのIssueなどで、連絡頂けると幸いです。


---

# MICRO-WIND-GENERATOR

A compact axial‑gap generator prototype designed for low‑wind environments, including airflow from household fans.

### Prototype Overview: Core‑Type Axial‑Gap Generator

This project may be a bit ambitious for an individual developer, but I’m working toward building a practical micro wind generator.  
The generator uses 12 coils and produces single‑phase AC.  
I’m focusing on reducing cogging torque so that it can generate power even with very weak airflow, such as from a household fan.

Right now, I’m searching for suitable magnetic materials for the coil cores and for the plates used to reduce cogging.  
However, there are real limits to what I can obtain or fabricate on my own, and this has become a challenge as I try to move the project forward.

🌐 [See the prototype webpage](https://isotsurishi.github.io/MICRO-WIND-GENERATOR/)

---

## Generator Structure

This prototype is a single‑phase AC generator that uses core coils in an axial‑gap configuration.

- Ferrite antenna rods are used as the coil cores (exact material unknown)  
- Axial positioning is maintained using the repulsive force of ring‑shaped neodymium magnets  
- A magnetic plate is placed between the magnets and coils to help reduce cogging  
- Adjacent magnets are connected with magnetic material to prevent flux leakage from the back side  
- All coils are connected in series to reduce the reverse electromotive force caused by the load  

The ferrite rods used in this prototype have good permeability but tend to saturate easily, which I believe is one of the reasons cogging remains.  
For practical use, I think a system that charges a battery first and then outputs power would be more suitable.

---

## Seeking Magnetic Powder Materials

To better understand how much cogging torque can be reduced, I would like to experiment with **magnetic powders with controlled particle size**, suitable for making custom soft‑magnetic composite cores.

Unfortunately, obtaining these materials in small quantities as an individual developer has been very difficult.

I’m hoping to test the following types of magnetic powders:

- Nanocrystalline powder (high μr, low loss, high Bs)  
- Amorphous metal powder  
- Pure iron powder (lamination‑grade)  
- Other soft‑magnetic powders such as permalloy or silicon‑steel based materials  

Since I couldn’t obtain the materials I originally wanted to test, I ordered ferrite antenna rods again.  
I’m also experimenting to see whether increasing the volume of the cogging‑suppression plates will help reduce cogging further.

---

## Improving Magnetic Flux Concentration in the Core

I searched again for ferrite rods with a larger cross‑sectional area than the magnets, but I couldn’t find any.  
So, I plan to run tests using neodymium magnets with a smaller cross‑sectional area (Φ6×t3).

Based on the results from version 6.0, it seems that if the device doesn’t require much power, it might be able to run even with the airflow from a household fan.  
I would like to continue testing, but I’m currently unable to obtain the core materials or the cogging‑reduction plates.

I also want to try using a more efficient propeller instead of the one I made myself.

As mentioned on my website, without the necessary materials, I can’t move on to the next round of testing.  
It’s disappointing, but for now I’ll take some time to think about whether there’s a good workaround.

### 🔍 Magnet Comparison: Neodymium vs Ferrite

### 🔍 Vertical‑Axis Propeller Updated with Magnet Change

### 🔍 Horizontal‑Axis Propeller Updated with Magnet Change

---

## Request for Support and Collaboration

This project is being developed and tested independently.  
To be honest, I am currently short on funds.  
Any information or advice regarding material sourcing or processing methods, provided free of charge, would be extremely helpful.  
If you are willing to share your knowledge, please feel free to contact me through GitHub Issues.

---

---

過去の実験の様子は Instagram にも掲載しています。  
#モバイル風力発電機 #風力発電機プロトタイプ #家庭用風力発電機


You can also find past experiments on Instagram:  
#MicroWindGenerator #WindTurbinePrototype #DIYWindPower

注意：英文は翻訳機にて翻訳したもので、日本語の文章と全く同じではない可能性が有ります

Note: The English text above was translated using a translation tool and may not exactly match the original Japanese.