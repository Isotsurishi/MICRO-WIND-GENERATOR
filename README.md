# マイクロ風力発電機

家庭用扇風機のような弱い風でも発電できる、小型風力（手回し）発電機の試作と実験記録です

## コア付きアキシャルギャップ型発電機

個人開発としてはちょっと無謀な挑戦かもしれませんが、実用的なマイクロ発電機の実現を目指して検証を進めています。本発電機は12個のコイルを用いた単相交流発電機で、弱い風でも発電できるようコギングトルクの低減に重点を置いています

現在は、コイルのコア材やコギング抑制用磁性体プレートに適した材料を探索していますが、個人で入手できる材料には限界があり、大きな開発課題となっています

試作品のWebページ:  
https://isotsurishi.github.io/MICRO-WIND-GENERATOR/

## 発電機の構造

本試作品は、アキシャルギャップ型のコア付きコイルを用いた単相交流発電機です

- コアにはアンテナ用フェライトロッド（材質の詳細は不明）を使用
- アキシャル方向の位置決めにリング状ネオジム磁石の反発力を利用
- コギング抑制のため、磁石とコイルの間に磁性体の板を配置
- 磁石背面からの漏れ磁束を防ぐため、隣接する磁石を磁性体で連結
- 負荷による逆起電力の影響を抑えるため、全コイルを直列接続

今回使用したフェライトロッドは透磁率は高いものの磁気飽和しやすく、コギングが残る一因になっていると考えています。実用化を考えると、一度バッテリーに充電してから出力する方式が適していると考えています

## 磁性体粉末の入手について

コギングトルクをどこまで低減できるか検証するため、粒径の揃った磁性体粉末を用いたソフト磁性複合材の実験を行いたいと考えていますが、個人で少量を入手することが非常に難しく、開発の大きな制約となっています

試してみたい粉末材料:
- ナノ結晶材粉末（高透磁率・低損失・高飽和磁束密度）
- アモルファス金属粉末
- 積層用純鉄粉末
- パーマロイ系・ケイ素鋼系などの軟磁性粉末

希望する材料が入手できなかったため、代替としてアンテナ用フェライトロッドを再度通販で購入、コギング抑制板の容積を増やすことでコギングがさらに低減できるかどうかを検証しています

フェライトロッドを砕いてエポキシ樹脂で固めた材料の抵抗を測定したところ、測定位置によってばらつきはあるものの、概ね2～7MΩ程度の高抵抗となっていました。

## 磁石部の最新5種類による、負荷抵抗と出力電圧の関係検証

これまでに作成した磁石部のうち、最新の5種類をそれぞれ組み替え、負荷抵抗と出力電圧の関係を検証しました

回転数は360 r.p.m.、720 r.p.m.を目安として測定しています（時計の秒針を見ながら手で回転させているため、回転数には多少の誤差があります）

使用した負荷抵抗:
10 kΩ、6.8 kΩ、4.7 kΩ、2.1 kΩ、1 kΩ、470 Ω、270 Ω、200 Ω

プロペラ:
全て同じものを使用

詳細な測定結果はWebページに掲載しています

## 実用化の可能性と展望

Release 9 の実測値を見ると、弱い風でも少しずつ発電が始まることが確認できました

まだ USB などを直接動かせるほどの出力ではありませんが、小さなバッテリーにいったん蓄電して使う方式なら、実用に近づく可能性があります

コギングをもう少し減らせれば、さらに低い風速でも回り始めるはずです

材料や磁気回路を工夫することで、電圧もまだ伸びる余地があります

小型で弱風でも動く発電機は市販品にほとんど無いため、ゆっくりでも改良を続ければ、役に立つものになると思っています

## ご支援・ご協力のお願い

この検証は私一人で行っており、恥ずかしい話ですが資金に余裕がありません

材料の調達方法や加工方法など、情報提供やアドバイスを無償でいただけると大変助かります。GitHubのIssueなどでご連絡いただけると幸いです

## 過去の実験

過去の実験内容はInstagramにも掲載しています
#マイクロ風力発電機　#モバイル風力発電機　#家庭用風力発電機　#自作発電機　

---

# MICRO-WIND-GENERATOR
A compact axial-gap generator prototype designed for low-wind environments, including airflow from household fans.

## Axial-Gap Generator with Ferrite-Core Coils

This project is an ambitious undertaking for a solo developer, but I am steadily working toward a practical micro wind generator. The prototype uses 12 coils and produces single-phase AC, with a major focus on minimizing cogging torque so that power can be generated even under very weak airflow and low rotational speeds.

I am currently exploring suitable magnetic materials for both the coil cores and the cogging-suppression plates. However, the range of materials that can be sourced in small quantities by an individual is limited, which has become a significant challenge in the development process.

Prototype webpage:  
https://isotsurishi.github.io/MICRO-WIND-GENERATOR/

## Generator Structure

This prototype is a single-phase AC generator using ferrite-core coils arranged in an axial-gap configuration.

- Ferrite antenna rods are used as the coil cores (exact material unknown)
- Axial positioning is maintained using magnetic repulsion between ring-shaped neodymium magnets
- A magnetic plate is placed between the magnets and coils to help reduce cogging torque
- Adjacent magnets are linked with magnetic material to suppress flux leakage from the back side
- All coils are connected in series to reduce the reverse electromotive force under load

The ferrite rods used here offer high permeability but saturate relatively easily, which likely contributes to the remaining cogging torque. For practical applications, a system that charges a battery first and then outputs power is expected to be more suitable.

## Seeking Magnetic Powder Materials

To further investigate how much cogging torque can be reduced, I would like to experiment with soft-magnetic composite materials made from powders with controlled particle size.

Unfortunately, obtaining such powders in small quantities as an individual developer has proven extremely difficult.

Materials I would like to test include:

- Nanocrystalline powder (high permeability, low loss, high saturation flux density)
- Amorphous metal powder
- Pure iron powder for laminated structures
- Other soft-magnetic powders such as permalloy-based or silicon-steel-based materials

Since I was unable to obtain these materials, I purchased additional ferrite antenna rods and am currently testing whether increasing the volume of the cogging-suppression plates can further reduce cogging.

When measuring the resistance of ferrite rods that were crushed and mixed with epoxy resin, the resulting composite showed 2–7 MΩ, depending on the measurement location.

## Relationship Between Load Resistance and Output Voltage
Using the five latest magnet-assembly designs

I tested the five most recent magnet assemblies by swapping them into the generator and measuring how the output voltage varied with different load resistances.

Measurements were taken at approximately 360 r.p.m. and 720 r.p.m.  
(The rotor was turned by hand while watching a clock’s second hand, so some error is expected.)

### Load Resistors Used
10 kΩ, 6.8 kΩ, 4.7 kΩ, 2.1 kΩ, 1 kΩ, 470 Ω, 270 Ω, 200 Ω

### Propeller
The same propeller was used for all tests.

### Detailed Results
Please refer to the data tables and graphs on the project webpage.

## Practical Potential and Future Prospects

Based on the measurements from Release 9, the generator begins producing power even under weak airflow.
The output is not yet strong enough to power USB devices directly, but storing the energy in a small battery first could make practical use possible.

If cogging torque can be reduced further, the generator should start rotating at even lower wind speeds.
There is still room for improvement in voltage output through better materials and magnetic design.

Compact generators that work in very low wind are rare on the market,
so steady improvements may eventually lead to something genuinely useful.

## Request for Support and Collaboration

This project is being developed independently, and my resources are limited. Any information or advice regarding material sourcing or processing methods would be greatly appreciated.

If you are willing to share your knowledge, please feel free to contact me through GitHub Issues.

## Past Experiments

Past experiments are also posted on Instagram.  
#マイクロ風力発電機 #モバイル風力発電機 #家庭用風力発電機 #自作発電機
