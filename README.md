## Overview (Search-Optimized Description)

This repository contains a DIY Axial Flux Generator designed specifically for low RPM operation.
It is a Single Phase Axial Flux Ferrite Magnet Generator intended for small wind turbines and
hand‑crank power generation. The generator uses ferrite magnetic materials, cogging reduction
plates, and an optimized air‑gap structure to achieve extremely low starting torque.

This axial flux ferrite magnet generator is designed as a low‑RPM single‑phase AC generator for DIY wind turbine and hand‑crank applications.

Key features:
- Axial Flux Generator (Ferrite Magnet Type)
- Single Phase AC Generator with 12 coils in series
- Low RPM operation suitable for weak wind or hand‑crank use
- DIY small wind turbine and emergency power applications
- Cogging reduction plate for improved startup performance


# Micro Wind Turbine (Hand‑Crank Generator)
A compact axial‑gap permanent‑magnet generator optimized for DIY small wind turbines.

This project aims to develop a small wind turbine capable of charging smartphones and 12V devices during emergencies, with future practical use and commercialization in mind.
The minimum requirement is that the generator must produce power even under the “Strong” setting of a household electric fan, allowing anyone to experiment without specialized equipment.

Latest experimental results (Release16 – Web Version)  
https://isotsurishi.github.io/MICRO-WIND-GENERATOR

---

## Concept

- Operates as a vertical‑axis wind turbine on a balcony for slow battery charging
- Independent of wind direction
- Easy to start rotating at low wind speeds
- Portable size for emergency use
- Can be moved to a safe location during typhoons
- Convertible to a horizontal‑axis propeller or hand‑crank mode
- Very low rotational torque—spins even with an electric fan
- Supports both wind power and hand‑crank operation

---

## Generator Structure

- Axial‑gap, single‑phase AC generator
- 12 coils connected in series
- Core made by connecting two Ferrite Core Rod 78 units (4278282509)
- Magnetic flux leakage significantly reduced by connecting the magnet backs with a steel yoke
- Magnetic material added between magnets and cores to suppress cogging torque, achieving rotation close to coreless behavior
- A toroidal core divided into 12 segments was originally planned, but machining was not feasible
- Instead, ferrite plates (2×10×18 mm) were arranged radially, and gaps were filled with crushed antenna ferrite rods
- Ring‑shaped neodymium magnets maintain a constant air gap using repulsive force
- All materials are easy for individuals to obtain

---

## Experimental Environment

- No wind tunnel → household electric fan (KOIZUMI KLF3018E9) used
- Custom propeller sized to match the fan’s airflow
- Prototype accuracy is low, resulting in uneven air gaps

---

## Experimental Results (Summary)

Detailed data is available in the web version:  
https://isotsurishi.github.io/MICRO-WIND-GENERATOR

---

## Findings from Experiments

- The magnetic plate used to suppress cogging torque is effective
- Internal resistance is high, limiting output under low loads
- Permeability variation of the cogging‑suppression material is large  
  - φ10 and φ12 magnets stop directly over the core  
  - φ13, φ16, φ19 magnets stop between cores  
  - Filling gaps between ferrite plates with magnetic powder helped, but was insufficient
- Release18 confirmed that removing the cogging‑suppression plate reduces output by **1.6–1.8×** and worsens weak‑wind startup performance

---

## Practical Potential

### ● What is possible at the current size
- LED lighting
- Slow charging of small batteries
- Supplemental charging by hand‑cranking

### ● What is difficult at the current size
- Normal smartphone charging (5 W)
- Full charging of 12V batteries

### ● Scalability
Increasing diameter, pole count, magnet size, and RPM could make **5–10 W output realistically achievable**, comparable to existing small wind turbines.

---

## Points for Improvement

- Prototype accuracy
- Higher‑permeability materials and improved geometry for core and cogging‑suppression plate
- Reduced coil resistance
- Outdoor evaluation
- More efficient propeller design
- Stronger ring magnet for axial positioning (current one loses against generator magnet attraction)

---

## Cogging‑Suppression Material and Powder Procurement

Materials desired for future testing:

- Toroidal core divided into 12 segments
- Amorphous metal powder
- Pure iron powder for laminated cores
- Permalloy / silicon‑steel powder

However, machining and procurement are difficult for individuals, creating limitations.

---

## Considerations

The effectiveness of the cogging‑suppression plate has been confirmed.

By optimizing the core material, plate geometry, coil winding count, magnet selection, and propeller efficiency,
the target generator performance may be achievable.

I believe that single‑phase AC generators can sometimes be more advantageous than three‑phase AC generators in compact designs. Single‑phase generators allow the output coils to be connected entirely in series to increase voltage more easily, require fewer diodes for AC‑to‑DC conversion, and can use iron‑core coils that enable longer coil lengths. For these reasons, single‑phase AC generators may offer practical benefits over three‑phase generators in small‑scale applications.

In the current prototype, the “magnetic plate that suppresses cogging” works well with φ12 magnets, as verified in Release16. However, even with φ12 magnets, if the air gap is smaller than 5 mm, the magnet stops between the coils just like φ16 and φ19 magnets. If the air gap is larger than 5 mm, the magnet stops directly above the coil, similar to φ10 magnets.

I believe this happens because the “magnetic plate that suppresses cogging” is made from two different materials: a ferrite plate and crushed antenna ferrite rods. As a result, the magnetic flux does not flow smoothly.

If the “magnetic plate that suppresses cogging” can be made from a single material and its shape adjusted to suppress cogging, then φ10, φ16, and φ19 magnets may also become usable. In addition, it may allow the air gap of φ12 magnets to be reduced.

By improving the “magnetic plate that suppresses cogging,” I believe it will be possible to reduce the air gap for φ12 magnets and increase the power generation.

Details:  
https://isotsurishi.github.io/MICRO-WIND-GENERATOR

---

## Reference Information

The household fan above was used as the airflow source.

Air gaps were tested at two positions:  
- Starting rotation under “Weak” wind  
- Starting rotation under “Strong” wind  

Fan blade diameter: 300 mm  
Horizontal‑axis propeller diameter: 320 mm  

Household fan airflow is uneven, but typical “Strong” wind speed is 3–5 m/s,
so 5 m/s was assumed for calculations.

Wind power:  
Pwind = 1/2 ρ A v³

Efficiency factors:

1. Betz limit: 59.3%
2. Practical rotor efficiency: 0.3–0.45
3. Mechanical + generator losses: 0.7–0.9

Best‑case combined efficiency:  
0.593 × 0.45 × 0.9 ≈ 0.24 → about 24%

Theoretical maximum output:  
6 W × 0.24 ≈ **1.44 W**

Current prototype achieves a low percentage of this,
but improvements in magnets, materials, coil design, and propeller efficiency could significantly increase performance.

---

## Notes on Test Environment

Ideally, specifications should be defined first,
but without a wind tunnel, a household fan is the only available airflow source,
limiting test conditions.

---

## Request for Support

I have continued prototyping and testing with limited equipment and budget,
but material procurement and funding have become increasingly difficult.

If you find this generator concept interesting and would like to contribute within your ability,
your support would be greatly appreciated.

Any level of collaboration is welcome.
I am reaching the limits of what I can continue alone, so your help would truly mean a lot.

Please contact me via GitHub Issues.

---

## About English Translation

English text is generated using translation tools.
Accuracy may not be perfect—thank you for your understanding.

---

## Past Experiments

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
- フェライトコアロッド78（4278282509）を2本接続してコアにしました
- 磁石背面をヨークで接続し、漏れ磁束を大幅に低減
- コギングを抑制する磁性体を磁石とコアの間に追加し、コアレスに近い軽い回転トルクを実現
　予定ではトロイドコアを12分割したものを考えてましたが、私には加工できそうもなかったので、フェライトプレート（2×10×18）を放射状に並べ、隙間にアンテ用フェライトロッドを金槌で砕いたものを充填
- リング状ネオジム磁石の反発力でギャップを一定に保持
- 材料はすべて個人でも入手が簡単なものとしました

---

## 実験環境

- 風洞設備なし → 家庭用扇風機（KOIZUMI KLF3018E9）を使用
- プロペラは扇風機の風が当たるサイズに自作
- 試作品の精度が低く、エアーギャップが均一ではない

---

## 実験結果（概要）

※ 詳細データはWEB版に掲載  
https://isotsurishi.github.io/MICRO-WIND-GENERATOR

---

## 実験から得られた知見

- 「コギングを抑制する磁性体の板」の効果は十分ある
- 内部抵抗が大きく、低負荷で頭打ち
- コギングを抑制する磁性体の透磁率のバラツキが大きくφ10、φ12の磁石では磁石がコアの一直線上で停止し、φ13、φ16、φ19の磁石ではコアとコアの間で停止する
　ことよりフェライトプレート間の隙間に磁性体の粉を充填したが、効果は不十分
- Release18 の比較実験では、コギング抑制プレートの有無で発電量が 1.6〜1.8倍変化、弱風での回転開始性にも大きく影響することが確認できました。
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
- 直径・極数・磁石サイズ・回転数を増やせば  
  **5〜10W級も十分に現実的（既存の小型風車と同等）**

---

## 改善すべき点

- 試作品の精度
- 高透磁率素材でコア・コギングを抑制する磁性体材料の材質、形状の改善
- コイル抵抗の低減
- 屋外での評価
- 効率の良いプロペラに変更
- 磁石の回転軸方向の位置決めをするリング状磁石を強くする（現行のものは発電用の磁石の吸引力に負けている）
　
---

## コギングを抑制する磁性体の加工や粉末の入手について

コギング低減のため、以下の材料で実験したい：

- トロイドコアを12分割したもの
- アモルファス金属粉末
- 積層用純鉄粉末
- パーマロイ系・ケイ素鋼系粉末

しかし、個人では加工が難しかったり、入手が難しく、制約となっています。

---

## 考察
「コギングを抑制する磁性体の板」の効果が十分あることが確認できました

必要な電圧などに合わせたコア、「コギングを抑制する磁性体の板」の材質や形状、他に、コイルの巻き数、磁石、プロペラを調整できれば、目的とする発電機も視野に入ってくると考えています

単相交流発電機のほうが3相交流発電機より電圧を上げやすく（コイルをすべて直流に結線）、交流を直流に変換するダイオードの数も少なく、コイルにコアが有るコイルを使うことでコイル長を長くできるので、小型発電機においては、単相交流発電機のほうが3相交流発電機より有利な場合もあると考えています

現行の試作品で使用している「コギングを抑制する磁性体の板」ではφ12の磁石と相性が良いとRelease16で検証しましたが、φ12の磁石でもエアーギャップを5㎜より小さくするとφ16、φ19の磁石同様、磁石はコイルとコイルの間で停止し、5㎜より大きくするとφ10の磁石同様、磁石はコイルの一直線上に停止します
これは「コギングを抑制する磁性体の板」が「フェライトプレート」と「アンテナ用フェライトロッドを砕いたもの」の二種類の材料からできており、磁束の流れが滑らかではないからだと考えています
「コギングを抑制する磁性体の板」を一つの材料で、形状を調整することでコギングの抑制ができれば、φ10、φ16、φ19の磁石も使用可能となり、且つ、φ12の磁石のエアーギャップを小さくできると考えています
「コギングを抑制する磁性体の板」を改良すればφ12の磁石での、エアーギャップを小さくするだけで発電量の増加を望めると考えています

詳細は最新の実験結果  
　　　https://isotsurishi.github.io/MICRO-WIND-GENERATOR


## 参考


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