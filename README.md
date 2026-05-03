# マイクロ風力発電機（手回し発電機）

非常時にスマホや12V機器を充電できる小型風力発電機として、実用化・商品化に向けて検討を進めています。
個人でも実験できる範囲で、家庭用扇風機の「強」の風でも発電することを条件としています。

最新の実験結果（Release12・WEB版）  
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
- コギング抑制板を追加し、コアレスに近い軽さを実現
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

※ 詳細データは Release12（WEB版）に掲載  
https://isotsurishi.github.io/MICRO-WIND-GENERATOR

### ● 720 rpm（手回し）
最大出力：約 **0.3 W**（ネオジムΦ10）

### ● 扇風機「強」相当（推定 1300〜1500 rpm）
最大出力：約 **1 W**

### ● 整流＋DC-DC後の実力値
**0.4〜0.6 W**

### ● 垂直軸型
水平軸の **約1/3** の発電量 → 実用性が低いため省略

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
- 手回し10:1で **2〜3 W**（ちょい足し充電）

### ● 現状のサイズで難しいこと
- スマホの通常充電（5 W）
- 12Vバッテリーの本格充電

### ● スケールアップの可能性
- ヨーク構造が非常に効果的
- コギング抑制板でコアレスに近い軽さ
- 直径・極数・磁石サイズ・回転数を増やせば  
  **5〜10 W級の小型風力発電機も十分に狙える**

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
#マイクロ風力発電機 #モバイル風力発電機 #家庭用風力発電機 #自作発電機

# Micro Wind Generator (Hand-Crank Compatible)

This project aims to develop a compact wind generator capable of charging smartphones and 12V devices during emergencies.
The key requirement is that the generator must operate even with the “strong” setting of a household electric fan, allowing experiments to be performed without special equipment.

Latest experimental results (Release 12):  
https://isotsurishi.github.io/MICRO-WIND-GENERATOR

---

## Concept

- Vertical-axis turbine for daily slow charging
- Independent of wind direction
- Easy to rotate at low wind speeds
- Portable during emergencies
- Can be moved to a safe place during typhoons
- Interchangeable with horizontal-axis blades or a hand-crank
- Very low rotational torque — spins even with a household fan
- Works with a 10:1 hand‑crank gear ratio
- Supports both wind and manual operation

---

## Generator Structure

- Axial‑flux, single‑phase AC generator
- 12 coils connected in series
- Φ10 ferrite rods used as cores
- Magnetic yoke on the back of the magnets to reduce flux leakage
- Cogging‑reduction plate for near‑coreless rotation
- Axial gap maintained by repulsion between ring‑shaped neodymium magnets
- All materials are easy to obtain (ferrite rods, iron sand, epoxy resin)

---

## Experimental Environment

- No wind tunnel — household fan used
- Propeller size matched to the fan
- Prototype has limited precision; air gap is not perfectly uniform
- Cogging‑reduction plate made from crushed ferrite rods + epoxy (low permeability)

---

## Experimental Results (Summary)

Full data is available in Release 12 (Web version).

### ● 720 rpm (hand‑crank)
Max output: **~0.3 W** (NdFeB Φ10)

### ● Household fan “strong” wind (estimated 1300–1500 rpm)
Max output: **~1 W**

### ● After rectifier + DC‑DC converter
Usable output: **0.4–0.6 W**

### ● Vertical‑axis test
Output was roughly **1/3** of the horizontal‑axis version.

---

## Findings

- Yoke is highly effective (clear increase in output)
- Core is not saturated (voltage proportional to load resistance)
- Gap unevenness reduces performance
- Cogging‑reduction plate works, but permeability is insufficient
- Internal resistance is high, limiting power at low loads
- Fan wind is stable, but propeller size is restricted

---

## Practical Possibilities

### ● Feasible at the current size
- LED lighting
- Slow charging of small batteries
- **2–3 W** with a 10:1 hand‑crank (useful for quick top‑up charging)

### ● Difficult at the current size
- Normal smartphone charging (5 W)
- Proper charging of 12V batteries

### ● Potential for scaling up
- Yoke‑based flux‑closing structure is very effective
- Cogging‑reduction plate enables near‑coreless rotation
- Increasing diameter, pole count, magnet size, or rpm could enable  
  **5–10 W class small wind generators**

---

## Areas for Improvement

- Improve air‑gap parallelism
- Use higher‑permeability materials for cores and cogging‑reduction plate
- Increase pole count
- Reduce coil resistance
- Outdoor testing
- Larger propeller

---

## About Magnetic Powders

To further reduce cogging, I would like to experiment with:

- Nanocrystalline powder
- Amorphous metal powder
- Pure iron powder for lamination
- Permalloy / silicon‑steel powders

However, obtaining small quantities as an individual is difficult.

---

## Request for Support

I would greatly appreciate any information you can provide about materials or processing methods, free of charge.
Please contact me via GitHub Issues.

---

## About the English Version

I rely on translation tools, so the English text may not be perfect.  
Thank you for your understanding.

---

## Past Experiments

Past experiments are also posted on Instagram.  
#MicroWindGenerator #MobileWindGenerator #DIYGenerator

