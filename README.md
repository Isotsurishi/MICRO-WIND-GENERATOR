# **Micro Wind Turbine (Hand‑Crank Generator)**  
A compact axial‑gap permanent‑magnet generator optimized for DIY small wind turbines.

This project aims to develop a small wind turbine capable of charging smartphones and 12V devices during emergencies, with the goal of practical use and future commercialization.  
The minimum requirement is that it must generate power even under the “Strong” setting of a household electric fan, allowing individuals to experiment without specialized equipment.

Latest experimental results (Release16 – Web Version):  
[https://isotsurishi.github.io/MICRO-WIND-GENERATOR](https://isotsurishi.github.io/MICRO-WIND-GENERATOR)

---

## **Concept**

- Operates as a vertical‑axis wind turbine on a balcony for slow battery charging  
- Independent of wind direction  
- Easy to start rotating at low wind speeds  
- Portable size for emergency use  
- Can be moved to a safe location during typhoons  
- Convertible to a horizontal‑axis propeller or hand‑crank mode  
- Very low rotational torque—spins even with an electric fan  
- Supports both wind power and hand‑crank operation

---

## **Generator Structure**

- Axial‑gap, single‑phase AC generator  
- 12 coils connected in series  
- Core made from two Ferrite Rod 78 units (4278282509) joined together  
- Magnetic flux leakage significantly reduced by connecting the magnet backs with a steel yoke  
- Magnetic material added between magnets and cores to suppress cogging torque, achieving rotation close to coreless behavior  
  - Originally planned to use a toroidal core divided into 12 segments  
  - Since I could not machine it myself, I arranged ferrite plates (2×10×18 mm) radially and filled the gaps with crushed antenna ferrite rods  
- Ring‑shaped neodymium magnets maintain a constant air gap using repulsive force  
- All materials are easy for individuals to obtain

---

## **Experimental Environment**

- No wind tunnel → household electric fan used  
- Custom propeller sized to match the fan’s airflow  
- Prototype accuracy is low, resulting in uneven air gaps

---

## **Experimental Results (Summary)**  
Detailed data is available in the web version:  
[https://isotsurishi.github.io/MICRO-WIND-GENERATOR](https://isotsurishi.github.io/MICRO-WIND-GENERATOR)

---

## **Findings from Experiments**

- Uneven air gaps reduce performance  
- Magnetic material for cogging suppression is effective (prototype permeability is not uniform)  
- High internal resistance limits output under low loads  
- Fan wind is stable, but propeller diameter is restricted  
- Permeability variation of the cogging‑suppression material is large  
  - φ10 and φ12 magnets stop directly over the core  
  - φ13, φ16, φ19 magnets stop between cores  
  - Filling gaps between ferrite plates with magnetic powder helped, but was insufficient

---

## **Practical Potential**

### **● What is possible at the current size**
- LED lighting  
- Slow charging of small batteries  
- Supplemental charging by hand‑cranking

### **● What is difficult at the current size**
- Normal smartphone charging (5 W)  
- Full charging of 12V batteries

### **● Scalability**
- Cogging‑suppression plates provide near‑coreless light rotation  
- Increasing diameter, pole count, magnet size, and RPM  
  **→ 5–10 W class output is realistically achievable (similar to existing small turbines)**

---

## **Points for Improvement**

- Prototype accuracy  
- Core and cogging‑suppression material: higher‑permeability materials and improved geometry  
- Reduced coil resistance  
- Outdoor evaluation  
- More efficient propeller design  
- Stronger ring magnet for axial positioning  
  - Current ring magnet loses against the attraction of the generator magnets

---

## **About Cogging‑Suppression Materials and Powder Procurement**

Materials I would like to test for reducing cogging torque:

- Toroidal core divided into 12 segments  
- Amorphous metal powder  
- Pure iron powder for laminated cores  
- Permalloy / silicon‑steel powder  

However, machining and procurement are difficult for individuals, creating limitations.

---

## **Release16 – Considerations**

Since I could not machine a toroidal core into 12 segments, I substituted ferrite plates arranged radially, filling the gaps with crushed antenna ferrite rods.  
φ16 and φ19 ferrite magnets were not tested because cogging torque caused them to stop between cores and exceeded the holding force of the ring magnet.  
φ10 performed better than the previously used crushed ferrite rod material.  
Additional tests were conducted with φ12t3 and φ13t4 (t2×2).

Even under the “Weak” fan setting, the rotor began spinning, and under “Strong” wind, a 100V 5W bulb glowed faintly.

Details are available in the latest experimental results (Release16 – Web Version):  
[https://isotsurishi.github.io/MICRO-WIND-GENERATOR](https://isotsurishi.github.io/MICRO-WIND-GENERATOR)

Fan used:  
**KOIZUMI KLF3018E9**

This fan is used as the device to generate consistent airflow.

Air gaps were tested at two positions:  
- Starting rotation under “Weak” wind  
- Starting rotation under “Strong” wind

Fan blade diameter: **300 mm**  
Horizontal‑axis generator propeller diameter: **320 mm**

Household fans produce uneven airflow, but typical “Strong” wind speed is **3–5 m/s**, so this experiment assumes **5 m/s**.

Wind power:  
**Pwind = 1/2 ρ A v³**

Efficiency factors:

1. Maximum theoretical wind turbine efficiency: **59.3% (Betz limit)**  
2. Practical rotor efficiency: **0.3–0.45**  
3. Mechanical + generator losses (including magnetic losses): **0.7–0.9**

Best‑case combined efficiency:

0.593 × 0.45 × 0.9 ≈ **0.24 → about 24%**

6 W × 0.24 ≈ **1.44 W (theoretical maximum output)**

Comparing this with the latest experimental results would be appreciated.

Although the current prototype achieves a low percentage of theoretical maximum efficiency, improvements such as stronger magnets, higher‑permeability cogging‑suppression plates, optimized coil wire diameter and turns, and a more efficient propeller should significantly increase performance.

---

## **Note: About the Test Environment**

Ideally, specifications should be defined first and experiments conducted accordingly.  
However, without access to a wind tunnel, the only device available to generate consistent airflow is a household fan, which limits the testing conditions.

---

## **Request for Support**

I have continued prototyping and testing with limited equipment and budget, but material procurement and funding have become increasingly difficult.

If you find this generator concept interesting and feel you would like to contribute within your ability, I would be very grateful.

Any level of support or collaboration is welcome.  
I am reaching the limits of what I can continue alone, so your help would truly mean a lot.

Please contact me via GitHub Issues.

---

## **About English Translation**

English text is generated using translation tools.  
Accuracy may not be perfect—thank you for your understanding.

---

## **Past Experiments**

Experiments are also posted on Instagram.  
#MicroWindTurbine #MobileWindTurbine #HomeWindTurbine

---


# マイクロ風力発電機（手回し発電機）
DIY向け小型風力発電機に最適化した、コンパクトなアキシャルギャップ型永久磁石発電機です。

非常時にスマホや12V機器を充電できる小型風力発電機として、実用化・商品化に向けて検討を進めています。
個人でも実験できる範囲で、最低でも家庭用扇風機の「強」の風でも発電することを条件としています。

最新の実験結果（Release16・WEB版）  
https://isotsurishi.github.io/MICRO-WIND-GENERATOR

---

## 構想

- 普段はベランダで垂直軸風車として発電し、バッテリーにゆっくり充電
- 風向きに依存しない
- 低風速でも回転しやすい
- 非常時には持ち運べる大きさ
- 台風時は安全な場所へ移動
- 水平軸プロペラや手回しハンドルに交換可能
- 扇風機の風でも回る軽い回転トルク
- 風力・手回しの両対応

---

## 発電機の構造

- アキシャルギャップ型・単相交流発電機
- コイル12個を直列接続
- フェライトコアロッド78（4278282509）を2個繋げたものをコアに使用
- 磁石背面をヨークで接続し、漏れ磁束を大幅に低減
- コギングを抑制する磁性体を磁石とコアの間に追加し、
　コアレスに近い軽い回転トルクを実現
　　予定ではトロイドコアを12分割したものを考えてましたが、
　　私には加工できそうもなかったので、フェライトプレート（2×10×18）を
　　放射状に並べ、隙間にアンテナ用フェライトロッドを金槌で砕いたものを充填
- リング状ネオジム磁石の反発力でギャップを一定に保持
- 材料はすべて個人でも入手が簡単なものとしました

---

## 実験環境

- 風洞設備なし → 家庭用扇風機を使用
- プロペラは扇風機の風が当たるサイズに自作
- 試作品の精度が低く、エアーギャップが均一ではない

---

## 実験結果（概要）

※ 詳細データはWEB版に掲載  
https://isotsurishi.github.io/MICRO-WIND-GENERATOR

---

## 実験から得られた知見

- エアーギャップのばらつきが性能を低下
- コギングを抑制する磁性体は効果あり（試作品の透磁率は均一ではない）
- 内部抵抗が大きく、低負荷で頭打ち
- 扇風機の風は安定しているが、プロペラ径に制限あり
- コギングを抑制する磁性体の透磁率のバラツキが大きく
　　φ10、φ12の磁石では磁石がコアの一直線上で停止し、
　　φ13、φ16、φ19の磁石ではコアとコアの間で停止することより
　　フェライトプレート間の隙間に磁性体の粉を充填したが、効果は不十分

---

## 実用化の可能性

### ● 現状のサイズで可能なこと
- LEDライト
- 小型バッテリーのゆっくり充電
- 手回しで ちょい足し充電

### ● 現状のサイズで難しいこと
- スマホの通常充電（5 W）
- 12Vバッテリーの本格充電

### ● スケールアップの可能性
- コギングを抑制する磁性体の板でコアレスに近い軽さ
- 直径・極数・磁石サイズ・回転数を増やせば  
  **5〜10W級も十分に現実的（既存の小型風車と同等）**

---

## 改善すべき点

- 試作品の精度
- 高透磁率素材でコア・コギングを抑制する磁性体材料の材質、形状の改善
- コイル抵抗の低減
- 屋外での評価
- 効率の良いプロペラに変更
- 磁石の回転軸方向の位置決めをするリング状磁石を強くする
　　現行のものは発電用の磁石の吸引力に負けている
　
---

## コギングを抑制する磁性体の加工や粉末の入手について

コギング低減のため、以下の材料で実験したい：

- トロイドコアを12分割したもの
- アモルファス金属粉末
- 積層用純鉄粉末
- パーマロイ系・ケイ素鋼系粉末

しかし、個人では加工が難しかったり、入手が難しく、制約となっています。

---

## Release16 – 考察

コギングを抑制する磁性体の材料が予定していたトロイドコアを12分割したものではなく、フェライトプレートを放射状に並べ、そのプレート間の隙間にアンテナ用フェライトロッドを金槌で砕いたものを充填したもので代用しました
φ16、φ19（フェライト）はコギングトルクによる磁石の停止位置がコアとコアの間になり、且つ、リング磁石の吸引力より強くなったため検証しませんでしたが、φ10では前回使用したアンテナ用フェライトロッドを金槌で砕いたものよりは良い結果が得られました
検証可能であったφ12t3、φ13t4（t2×2）を追加しました
　扇風機の「弱」の風でも回転し始め、「強」の風で100V5Wの電球がほんのり点灯しました

詳細は最新の実験結果（Release16・WEB版）  
　　　https://isotsurishi.github.io/MICRO-WIND-GENERATOR


使用している扇風機
　KOIZUMI KLF3018E9

一定の風を発生する装置として上記扇風機を使用しています

エアーギャップは「弱」の風で回転し始める位置と「強」の風で回転し始める2種類で検証しました

扇風機の羽根の直径は300㎜、水平軸型発電機のプロペラの直径が320㎜です

また、扇風機の風は均一ではなくムラがありますが、一般的な家庭用扇風機「強」の風速は 3〜5 m/s 程度であるため、本検証では 5 m/s と仮定します。

風の持つ出力
　Pwind＝1/2ρAｖ³　

各効率について

　１，どの構造の風車でも最大59.3％（Betz limit）

　２，実際のロータ効率　0.3～0.45

　３，機械損＋発電機損(磁力を含む)　0.7から0.9

項目1～3より　一番効率が良い時を考えると

　0.593×0.45×0.9≒0.24　　約24％

　6W × 0.24 ≒ 1.44W（理論的な最大出力の目安）

上記内容（ネットで調べました）と最新の実験結果を比較していただけると幸いです

現行の試作品では理論上の最大効率に対する割合は低いものの、強力な磁石、透磁率の高い飽和し難いコギング抑制板、コイル線径、コイル巻き数を調整し、効率の良いプロペラにすれば効率を上げることは十分可能と考えています　

## 補足：検証環境について  
本来であれば、まず仕様を決めて、それに向けて変更・検証を進めるべきですが、現状では風洞実験ができず、一定の風を発生させる装置は家庭用扇風機のみであり、検証基準がこの条件に制約されています。

## お願い  
ここまで、設備や資金が限られた中で試作・検証を続けてきましたが、特に材料の調達や資金面で継続が難しくなってきました。

この発電機の構造や取り組みに興味を持ち、「自分の出来る範囲で関わってみたい」と感じていただける方がいれば、ご連絡いただけると大変ありがたく思います。

無理のない範囲でのご支援・ご協力を歓迎しています。  
私自身もそろそろ継続が難しくなってきたため、お力添えをいただければ本当に助かります。
GitHub Issues にてご連絡ください。

---

## 英語表記について

英語は翻訳ツールを使用しています。  
正確でない可能性がありますがご了承ください。

---

## 過去の実験

Instagram にも掲載しています。  
#マイクロ風力発電機 #モバイル風力発電機 #家庭用風力発電機