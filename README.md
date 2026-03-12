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

## 磁束をコアに集中させるためにΦ6t3のネオジム磁石で検証

水平軸型　　負荷（LED10個）で16.7V発生

![Φ6t3のネオジム磁石](video/video41)

水平軸型　　負荷有で1.4V、無負荷で16.0V発生

![Φ6t3のネオジム磁石](video/video42)

結果

　　・LED10個を直列に結線：16.7V　　　　　↓

　　・100V5W球を結線：1.4V

　磁束がコアに集中しても発電量が少なければ意味が無い

　そこで、コイル周りは最終の形態で磁石を替え、8kΩ、4kΩ、2kΩ・・・と替え、発生する電圧を測定して、どの組み合わせが良いのか検討する予定です

## ご支援・ご協力のお願い

このプロジェクトは個人で開発・検証を行っています。

恥ずかしながら、資金が不足しています。

材料の調達や加工方法など、情報提供やアドバイスを無償でいただけるととても助かります。

GitHubのIssueなどで、連絡頂けると幸いです。




---

# MICRO-WIND-GENERATOR

A compact axial-gap generator prototype designed for low-wind environments, including airflow from household fans.

---

## Core-Type Axial-Gap Generator

This project may be a bit ambitious for an individual developer, but I am working toward building a practical micro wind generator.  
The generator uses 12 coils and produces single-phase AC.  
I am focusing on reducing cogging torque so that it can generate power even with very weak airflow, such as from a household fan.

Currently, I am searching for suitable magnetic materials for the coil cores and for the plates used to reduce cogging.  
However, there are real limits to what I can obtain or fabricate on my own, and this has become a major challenge in the development process.

🌐 **Prototype webpage:**  
https://isotsurishi.github.io/MICRO-WIND-GENERATOR/

---

## Generator Structure

This prototype is a single-phase AC generator that uses core coils in an axial-gap configuration.

- Ferrite antenna rods are used as the coil cores (exact material unknown)  
- Axial positioning is maintained using the repulsive force of ring-shaped neodymium magnets  
- A magnetic plate is placed between the magnets and coils to help reduce cogging  
- Adjacent magnets are connected with magnetic material to prevent flux leakage from the back side  
- All coils are connected in series to reduce the reverse electromotive force caused by the load  

The ferrite rods used in this prototype have good permeability but tend to saturate easily, which I believe is one of the reasons cogging remains.  
For practical use, I think a system that charges a battery first and then outputs power would be more suitable.

---

## Seeking Magnetic Powder Materials

To better understand how much cogging torque can be reduced, I would like to experiment with **magnetic powders with controlled particle size**, suitable for making custom soft-magnetic composite cores.

Unfortunately, obtaining these materials in small quantities as an individual developer has been very difficult.

I am hoping to test the following types of magnetic powders:

- Nanocrystalline powder (high μr, low loss, high Bs)  
- Amorphous metal powder  
- Pure iron powder (lamination-grade)  
- Other soft-magnetic powders such as permalloy or silicon-steel based materials  

Since I could not obtain the materials I originally wanted to test, I ordered ferrite antenna rods again.  
I am also experimenting to see whether increasing the volume of the cogging-suppression plates will help reduce cogging further.

When measuring the resistance of ferrite rods crushed and mixed with epoxy resin, the resulting material showed 2–7 MΩ depending on the measurement point.

---

## Verification Using Φ6 mm × 3 mm Neodymium Magnets to Concentrate Magnetic Flux into the Core

**Horizontal-axis test results**

- 10 LEDs in series: **16.7 V**  
- 100 V / 5 W incandescent bulb: **1.4 V**  
- No-load voltage: **16.0 V**

Even if the magnetic flux is successfully concentrated into the core, it is meaningless if the overall power generation remains low.

To investigate this further, I plan to keep the coil section in its final configuration and replace only the magnets.  
I will then measure the generated voltage while varying the load resistance (8 kΩ, 4 kΩ, 2 kΩ, …) to determine which combination provides the best performance.

---

## Request for Support and Collaboration

This project is being developed and tested independently.  
To be honest, I am currently short on funds.  
Any information or advice regarding material sourcing or processing methods, provided free of charge, would be extremely helpful.  
If you are willing to share your knowledge, please feel free to contact me through GitHub Issues.

---

## Past Experiments

Past experiments are also posted on Instagram.  
#MicroWindGenerator #WindTurbinePrototype #DIYWindPower

---

## Note

The English text in this README was translated from Japanese and may not be a perfect one-to-one match with the original meaning.
