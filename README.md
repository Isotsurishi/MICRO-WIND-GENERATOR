# Micro Wind Turbine (Hand‑Crank Generator)
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

## Request for Support

Any information regarding materials or fabrication methods would be greatly appreciated.  
Please contact via GitHub Issues.

---

## About English Translation

English text is generated using translation tools.  
Accuracy is not guaranteed.

---

## Previous Experiments

Also posted on Instagram.  
#micro_wind_turbine #mobile_wind_generator #home_wind_turbine



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

## ご支援・ご協力のお願い

材料や加工方法を無償にて情報提供いただけると助かります。  
GitHub Issues にてご連絡ください。

---

## 英語表記について

英語は翻訳ツールを使用しています。  
正確でない可能性がありますがご了承ください。

---

## 過去の実験

Instagram にも掲載しています。  
#マイクロ風力発電機 #モバイル風力発電機 #家庭用風力発電機
