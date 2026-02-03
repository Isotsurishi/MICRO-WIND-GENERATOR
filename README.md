マイクロ風力（手回し）発電機の試作と実験記録
<br>
実用可能な、低風速でも発電可能な構造を目指す
<br><br>
<strong>Core‑Type Axial‑Gap Generator Project<strong>
<br>
I might be taking on something a bit ambitious, but I’m exploring the idea of creating a practical micro‑generator as an individual developer.
<br>
This generator uses 12 coils and produces single‑phase AC.
<br>
I’m working on reducing cogging torque so it can generate power even with very weak airflow, like from a household fan.
<br>
Right now I’m searching for suitable magnetic materials for the coil cores and for the plates that help reduce cogging.
<br>
However, there are real limits to what I can obtain or do on my own, and that’s becoming a challenge as I try to move this project forward.
<br>
<br>
🌐 [試作品のWebページを見る See the prototype webpage](https://isotsurishi.github.io/MICRO-WIND-GENERATOR/)
<br><br>
発電機の構造はアキシャルギャップ型のコアコイルを使った単相交流発電機です
<br>
　１、コアにはアンテナ用フェライトロッドを使用しました
<br>
　２、アキシャル側の位置決めにリング状のネオジム磁石の反発を利用しました
<br>
　３、コギングを抑制するために磁性体の板を磁石とコイルの間に配置しました
<br>
　４、磁石のコイルと反対側の面から漏れる磁気を防ぐために隣接する磁石を磁性体で繋げました
<br>
　５、負荷に応じて発生する逆起電力を小さくするためにコイルは全て直列に結線しました
<br><br>
今回の実験で使用したフェライトロッドの特製は不明ですが、透磁性は良いが磁気飽和しやすいためにコギングが残ったと考えています
<br>
実用化するには発電した電気を一度バッテリーに充電した後、出力するのが良いと考えています
<br>
<br>
この試作品に至るまで
<br>
　コアの材料
<br>
　　SS400の丸棒
<br>
　　　　↓
<br>
　　純鉄の丸棒
<br>
　　　　↓
<br>
　　砂鉄　+　エポキシ樹脂
<br>
　　　　↓
<br>
　　アンテナ用フェライトロッド
<br>
　　　　↓
<br>
　コギング抑制板の材料
<br>
　　SPCC
<br>
　　　　↓
<br>
　　砂鉄　+　エポキシ樹脂
<br>
　　アンテナ用フェライトロッドを金槌で粉砕　+　エポキシ樹脂
<br>
<br>
これまでの実験結果を考えると、コギングの材質は不導体、高等磁性、軟磁性体、磁気飽和し難い、振動等で壊れない強度を兼ね備えた材料が良いと思います
<br>
<br>
その他の部品
<br>
　　1㎜のプラバンを購入、加工して作成（時間がかかる、精度が悪い）
<br>
　　　　↓
<br>
　　図面を引いて工場に依頼（時間がかかる、精度は良い、高額）
<br>
　　　　↓
<br>
　　３Dプリンターを購入（時間は早い、強度がそれほど強くない、精度もそれほど良くない）
<br>
<br>
軸受、パイプの価格、加工のしやすさからΦ８のパイプとしましたが強度は有りません、あくまで試作用です
<br>
<br>
このように実用化を目指してきたのですが、個人では材料の調達、加工非常に難しいという問題に直面しました
<br><br>
実験してみたい材料は
<br>
　ナノ結晶材　μr：10,000～100,000　　飽和磁束密度　Bs：1.2T　　損失：低い
<br>
　アモルファス金属　μr：10,000～100,000　　飽和磁束密度　Bs：1.5～1.6T　　損失：低い
<br>
　純鉄（積層）　μr：5,000～10,000　　飽和磁束密度　Bs：2.1T　　損失：低い
<br>
　その他、パーマロイ、ケイ素鋼等、色んな材料で実験してみたいのですが現状叶いません
<br><br>
残念ではありますが、今までの実験結果をもとに何か良い方法が無いか考えている状態です