# Micro Wind Turbine (Hand‑Crank Generator)

A DIY axial-flux permanent magnet generator optimized for low-speed micro wind turbines.


## Keywords
micro wind generator, axial flux generator, ferrite magnet generator,
hand-crank generator, low-speed generator, DIY wind turbine,
ferrite core, coil winding, magnetic flux, renewable energy experiment

A compact axial-flux permanent magnet generator optimized for DIY small wind turbines.

This project aims to develop a compact wind turbine capable of charging smartphones and 12V devices during emergencies.  
All experiments are conducted using materials and tools that individuals can easily obtain.  
A key design requirement is that the generator must operate even with the airflow from a household electric fan set to “Strong”.

This project is a DIY axial flux permanent magnet generator using ferrite cores.
It is designed for low-torque small wind turbines and includes cogging reduction techniques.
The generator core structure, coil arrangement, and magnetic circuit are optimized for low-speed wind power generation.

Latest experimental results (Release 14 – Web version):  
https://isotsurishi.github.io/MICRO-WIND-GENERATOR

---

## Concept

- Operates as a vertical‑axis wind turbine on a balcony for slow battery charging
- Independent of wind direction
- Easy to start rotating even at low wind speeds
- Portable size for emergency use
- Can be moved to a safe location during typhoons
- Swappable between horizontal‑axis propeller and hand‑crank handle
- Very low rotational torque — spins even with fan airflow
- Usable with a 10:1 hand‑crank gear ratio
- Supports both wind and manual operation

---

## Generator Structure

- Axial‑gap, single‑phase AC generator
- 12 coils connected in series
- Φ10 ferrite rods used as cores
- Magnetic flux leakage significantly reduced by adding a rear‑side yoke
- Cogging‑reduction plate added to achieve near‑coreless rotational smoothness
- Ring‑shaped neodymium magnets maintain a constant air gap via repulsive force
- All materials are individually obtainable (ferrite rods, iron sand, epoxy resin)


---

## Experimental Environment

- No wind tunnel — household electric fan used
- Propeller size adjusted to match the fan’s airflow area
- Prototype accuracy is low; air gap is not perfectly uniform
- Cogging‑reduction plate uses ferrite powder + epoxy, resulting in low permeability

---

## Experimental Results (Summary)

Detailed data is available in Release 14 (Web version):  
https://isotsurishi.github.io/MICRO-WIND-GENERATOR

### ● 720 rpm (Hand‑crank)
Maximum output: **0.25–0.35 W** (Neodymium Φ10)

### ● Electric fan “Strong” (estimated 1300–1500 rpm)
Maximum output: **0.4–0.5 W**

### ● After rectifier + DC‑DC converter
**0.3–0.45 W**

### ● Vertical‑axis type
Under the same conditions: **0.15–0.2 W**  
Vertical‑axis output is about one‑third of the horizontal‑axis type.  
Since it is unsuitable for emergency power generation, details are omitted.

### Experimental Video (Horizontal Axis)
[▶ F18‑60‑H.mp4](./video/F18-60-H.mp4)  
*Click “View raw” on GitHub to play the video.*

### Experimental Video (Vertical Axis)
[▶ F18‑60‑V.mp4](./video/F18-60-V.mp4)  
*Click “View raw” to play.*

※ High‑rpm measurement data (1200 rpm / 1800 rpm) has been newly added in Release14.

---

## Findings from Experiments

- Yoke significantly improves output
- Core does not saturate (voltage proportional to load resistance)
- Air‑gap unevenness reduces performance
- Cogging‑reduction plate is effective, though permeability is insufficient
- High internal resistance limits output under low‑load conditions
- Fan airflow is stable, but propeller diameter is restricted

---

## Practical Potential

### ● What is possible with the current size
- LED lighting
- Slow charging of small batteries
- **1–2 W** with a 10:1 hand‑crank gear ratio (estimated; suitable for small top‑up charging)

### ● What is difficult with the current size
- Standard smartphone charging (5 W)
- Full charging of 12V batteries

### ● Potential for scaling up
- Yoke structure is highly effective
- Cogging‑reduction plate provides near‑coreless smoothness
- Increasing diameter, pole count, magnet size, and rpm could achieve:  
  **5–10 W class output (comparable to existing small wind turbines)**

---

## Points for Improvement

- Improve air‑gap parallelism
- Use higher‑permeability materials for core and cogging‑reduction plate
- Increase pole count
- Reduce coil resistance
- Conduct outdoor testing
- Increase propeller diameter

---

## About Magnetic Powder Materials

To further reduce cogging, the following materials are desired for testing:

- Nanocrystalline powder
- Amorphous metal powder
- Pure iron powder for laminated cores
- Permalloy / silicon‑steel‑based powders

However, obtaining small quantities of these materials is difficult for individuals.

---

## Release15 – Analysis and Future Verification Plan

Analysis
Only this section has been added or modified in Release15.
Basic condition: Household electric fan set to “Strong”.

Although the airflow from a household electric fan is not uniform and contains fluctuations, the typical wind speed of a “Strong” setting on a household fan is around 3–5 m/s.
Therefore, this analysis assumes a wind speed of 5 m/s.

Wind Power
Pwind = 1/2 ρ A v³

Efficiency Factors
Maximum theoretical efficiency for any wind turbine (Betz limit): 59.3%

Practical rotor efficiency: 0.30–0.45

Mechanical + generator efficiency (including magnetic losses): 0.7–0.9

From items 1–3, the best‑case overall efficiency is:

0.593 × 0.45 × 0.9 ≒ 0.24 (about 24%)

With 6 W of wind power:

6 W × 0.24 ≒ 1.44 W (theoretical maximum output)

| Item | Neodymium φ10×3 | Ferrite φ18×5 |
| --- | --- | --- |
| Output | approx. 0.5 W | approx. 0.35 W |
| RPM | approx. 1200 rpm | approx. 1000 rpm |
| Actual efficiency (based on 6 W wind) | approx. 8.3% | approx. 5.8% |
| Ratio to theoretical max (24%) | 34.7% | 24.3% |
| Magnetic flux density | 0.28–0.35 T | 0.10–0.15 T |

Although the current prototype achieves a relatively small fraction of the theoretical maximum efficiency, improvements such as stronger magnets, a high‑permeability cogging‑suppression plate with higher saturation resistance, optimized coil wire diameter, optimized number of turns, and a more efficient propeller design could significantly increase performance.

Small wind turbines typically achieve 5–15% efficiency, and the present prototype’s 5.8–8.3% falls well within this common range.

1. Cogging‑Suppression Plate
Increasing the thickness to t13 increased the volume, which significantly improved cogging reduction and increased output.

Items to verify

Aim for minimum volume and minimum weight while achieving “almost zero cogging”.
Prototype and test different materials, shapes, and volumes.

In the current prototype, the cogging‑suppression plate is made by crushing a ferrite rod into particles and bonding them with epoxy resin. However, the epoxy creates gaps between the particles and the material becomes non-uniform, which likely prevents the ferrite from exhibiting its original permeability.

Ideally, the cogging‑suppression plate should be made from sintered, continuous ferrite material. A continuous ferrite structure would allow higher magnetic performance, enabling a thinner plate while still achieving strong cogging suppression.


2. Coil Core
Under the condition of “starting rotation with the airflow of a household fan”,
the distance between the magnet and the cogging‑reduction plate varied to reduce cogging.
However, the output of neodymium magnets φ10t3 and φ16t2.5 did not differ significantly.

This suggests that the magnetic flux through the core is nearly saturated (“flux‑limited”) in both cases.

Items to verify

Increase the core diameter to increase the magnetic flux capacity (cross‑sectional area).

If possible, reduce weight by testing:

Cylindrical (hollow) cores

Fan‑shaped coils (sector‑shaped coils)

3. Number of Coil Turns
For the 23 mm core (330 turns, 19.9 Ω) and the 60 mm core (1170 turns, 68.9 Ω),
the resistance and rotational speed differ (rpm not measured, but assumed different due to identical wind speed),
yet the maximum output was nearly the same.

This indicates that increasing the number of turns or core length does not increase output because
the magnetic flux does not reach the entire coil evenly,
and the effective number of turns (the turns actually intersected by magnetic flux) is nearly the same.
(Current is unknown, so back‑EMF cannot be calculated, but wind conditions are identical.)

Items to verify

Reconsider the number of turns and wiring method (currently all coils are in series) based on the target specifications.

4. Ring‑Shaped Magnets
Ring magnets are used to maintain a uniform distance between the generator magnets and the cogging‑reduction plate,
but magnetic flux leakage occurs from the ring magnets.

Items to verify

Connect the coil‑side of the ring magnet with a yoke.

On the opposite side of the coil:

Bring the magnet as close as possible to the rotating shaft (magnetic material) to let the shaft function as a yoke,

or connect it to the generator magnet or its yoke.

This should reduce eddy‑current losses caused by leakage flux.

## Supplement: About the Experimental Environment

Ideally, specifications should be defined first and verification should follow accordingly.
However, without a wind tunnel, the only available airflow source is a household electric fan,
and the evaluation criteria are restricted by this limitation.

## Request

I have continued prototyping and testing with limited equipment and budget,
but material procurement and financial constraints are making it difficult to continue.

If anyone is interested in the structure or concept of this generator and
would like to be involved within their own reasonable capacity,
I would be sincerely grateful for your support.

I welcome any support or cooperation within your comfortable capacity.
As it is becoming increasingly difficult for me to continue this project alone, any assistance you can offer would be truly appreciated.
Please feel free to contact me via GitHub Issues.

---

## About English Translation
English text is generated using translation tools.
Accuracy is not guaranteed.

---

## Past Experiments
Also posted on Instagram.
#micro_wind_turbine #mobile_wind_generator #home_wind_turbine

---

# マイクロ風力発電機（手回し発電機）
DIY向け小型風力発電機に最適化した、コンパクトなアキシャルフラックス型永久磁石発電機です。

非常時にスマホや12V機器を充電できる小型風力発電機として、実用化・商品化に向けて検討を進めています。
個人でも実験できる範囲で、家庭用扇風機の「強」の風でも発電することを条件としています。

最新の実験結果（Release14・WEB版）  
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
- ギヤ比10:1の手回しでも使用可能
- 風力・手回しの両対応

---

## 発電機の構造

- アキシャルギャップ型・単相交流発電機
- コイル12個を直列接続
- Φ10フェライトロッドをコアに使用
- 磁石背面をヨークで接続し、漏れ磁束を大幅に低減
- コギング抑制板を追加し、コアレスに近い軽い回転トルクを実現
- リング状ネオジム磁石の反発力でギャップを一定に保持
- 材料はすべて個人入手可能（フェライトロッド・砂鉄・エポキシ樹脂）

---

## 実験環境

- 風洞設備なし → 家庭用扇風機を使用
- プロペラは扇風機の風が当たるサイズに調整
- 試作品の精度が低く、ギャップが完全に均一ではない
- コギング抑制板はフェライト粉末＋エポキシで透磁率が低い

---

## 実験結果（概要）

※ 詳細データは Release14（WEB版）に掲載  
https://isotsurishi.github.io/MICRO-WIND-GENERATOR

### ● 720 rpm（手回し）
最大出力：約 **0.25～0.35 W**（ネオジムΦ10）

### ● 扇風機「強」相当（推定 1300〜1500 rpm）
最大出力：約 **0.4～0.5 W**

### ● 整流＋DC-DC後の実力値
**0.3〜0.45 W**

### ● 垂直軸型
同条件で **0.15〜0.2 W**  
垂直軸は水平軸の約1/3の出力で、  
今回の目的（非常時の発電）には不向きなため詳細は省略

### 実験動画（水平軸）
[▶ F18-60-H.mp4 を再生](./video/F18-60-H.mp4)  
※ GitHub の仕様により動画は直接再生できません。  
　リンク先のページで **「View raw」** を押すと再生できます。

### 実験動画（垂直軸）
[▶ F18-60-V.mp4 を再生](./video/F18-60-V.mp4)  
※ 同様に、**「View raw」** を押すと再生できます。

※1200 rpm / 1800 rpm の高回転域データも Release14 にて追加しました。

---

## 実験から得られた知見

- ヨークの効果は大きい（出力が明確に向上）
- コアは飽和していない（電圧が抵抗に比例）
- ギャップのばらつきが性能を低下
- コギング抑制板は効果あり（ただし透磁率不足）
- 内部抵抗が大きく、低負荷で頭打ち
- 扇風機の風は安定しているが、プロペラ径に制限あり

---

## 実用化の可能性

### ● 現状のサイズで可能なこと
- LEDライト
- 小型バッテリーのゆっくり充電
- 手回し10:1で **1〜2 W 程度（推定値・ちょい足し充電）**

### ● 現状のサイズで難しいこと
- スマホの通常充電（5 W）
- 12Vバッテリーの本格充電

### ● スケールアップの可能性
- ヨーク構造が非常に効果的
- コギング抑制板でコアレスに近い軽さ
- 直径・極数・磁石サイズ・回転数を増やせば  
  **5〜10W級も十分に現実的（既存の小型風車と同等）**

---

## 改善すべき点

- ギャップの平行度を改善
- 高透磁率素材でコア・コギング抑制板を改善
- 多極化
- コイル抵抗の低減
- 屋外での評価
- プロペラの大型化

---

## 磁性粉末の入手について

コギング低減のため、以下の材料で実験したい：

- ナノ結晶材粉末
- アモルファス金属粉末
- 積層用純鉄粉末
- パーマロイ系・ケイ素鋼系粉末

しかし、個人では少量入手が難しく、制約となっています。

---

## Release15 – 考察と今後の検証方針

Release15 では、この部分のみ追加・変更しています。  
基本条件：家庭用扇風機「強」の風

使用している扇風機
　KOIZUMI KLF3018E9

一定の風を発生する装置として上記扇風機の「強」の風として、扇風機の風のみで自然に回転を始めることを前提とします

扇風機の羽根の直径は300㎜ですが、水平軸型発電機のプロペラの直径が320㎜なので、320㎜とします

また、扇風機の風は均一ではなくムラがありますが、一般的な家庭用扇風機「強」の風速は 3〜5 m/s 程度であるため、本検証では 5 m/s と仮定します。

風の持つ出力
　Pwind＝1/2ρAｖ³　

各効率について

　１，どの構造の風車でも最大59.3％(Betz limit）

　２，実際のロータ効率　0.3～0.45

　３，機械損＋発電機損(磁力を含む)　0.7から0.9

項目1～3より　一番効率が良い時を考えると

　0.593×0.45×0.9≒0.24　　約24％

　6W × 0.24 ≒ 1.44W（理論的な最大出力の目安）

φ10t3のネオジム磁石、φ18ｔ5のフェライト磁石での実験結果より

| 項目 | φ10×3 ネオジム磁石 | φ18×5 フェライト磁石 |
| --- | --- | --- |
| 出力 | 約 0.5 W | 約 0.35 W |
| 回転数 | 約 1200 rpm | 約 1000 rpm |
| 実際の効率（6W基準） | 約 8.3％ | 約 5.8％ |
| 理論最大効率24％に対する割合 | 34.7％ | 24.3％ |
| 磁束密度の目安 | 0.28〜0.35 T | 0.10〜0.15 T |

現行の試作品では理論最大効率に対する割合は低いものの、強力な磁石、透磁率の高い飽和し難いコギング抑制板、コイル線径、コイル巻き数を調整し、効率の良いプロペラにすれば効率を上げることは十分可能と考えています　

なお、小型風車では 5〜15％ 程度の効率が一般的とされており、本試作機の 5.8〜8.3％ はその範囲内にあります。

1. コギング抑制板  
厚みを t13 に変更して容積を増やしたところ、コギングの抑制効果が大きくなり、発電量も増加した。

検証したい内容  
　コギングがほぼ無くなる最小容積・最小重量を目指し、  
　材質・形状・容積を変更して試作・検証する。

現在の試作品では、フェライトロッドを砕いた粒子をエポキシ樹脂で固めて
コギング抑制板を作成しているが、
エポキシ樹脂によって粒子間に空隙が生じ、材質も均一ではないため、
フェライト本来の透磁率を十分に発揮できていない可能性がある。

理想的には、焼結された連続フェライト材 を用いて抑制板を製作することで、
より薄い板でも高いコギング抑制効果が得られると考えています。

2. コイルのコア  
「扇風機の風で回り始める」という条件下では、コギングを小さくするために  
磁石とコギング抑制板の距離に差は生じたが、  
ネオジム磁石 φ10t3 と φ16t2.5 の発電量は大きく変わらなかった。
このことから、どちらもコアを通る磁束量が「ほぼ頭打ち（飽和）」になっていると考えられる。

検証したい内容  
- コアを太くして、磁束が通れる量（断面積）を増やす  
- 可能であれば軽量化のため、円筒状のコアやファンシェイプコイル（扇形に近い形状）を検討する

3. コイルの巻き数  
コア23mm（330巻・19.9Ω）とコア60mm（1170巻・68.9Ω）では、  
抵抗値や回転数は異なる（回転数は測定していないが、風速が同じため異なると推測）ものの、最高出力はほぼ同じだった。
巻き数やコア長さを増やしても出力が増えないことから、磁束がコイル全体に均等に行き渡らず、 磁束が通っている巻き数（有効巻き数）がほぼ同じと考えられる。  
（電流値が不明のため逆起電力は不明だが、扇風機の風条件は同じ）

検証したい内容  
　仕様に合わせて、巻き数・結線方法（現状は全て直列）を再検討する。

4. リング状磁石  
コイルを挟んだ発電用磁石とコギング抑制板の距離を均一に保つために配置しているが、 リング状磁石から磁束が漏れている。

検証したい内容  
- リング状磁石のコイル側をヨークで接続する  
- コイルと反対側は、回転軸（磁性体）に接触、またはできるだけ近づけて回転軸にヨークとしての機能を持たせる  
- もしくは発電用磁石またはそのヨークに接続する  
これにより、漏れ磁束によって発生する渦電流損失を抑制する。

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