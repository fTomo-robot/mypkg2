# current_shunt.launch.py
![test](https://github.com/fTomo-robot/mypkg2/actions/workflows/test.yml/badge.svg)  
電流監視パッケージ  
- シャント抵抗の電圧を読み取り、電流に変換するパッケージ

# テスト環境
- Ubuntu-22.04
- python-version: [3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13] をGitHub Actions のテストにて動作確認済み

# ノードの機能説明
## current
  - 受信した電圧値と、あらかじめ設定しておいたシャント抵抗の抵抗値から電流値を計算するノード
  - プログラム名:current.py
  - `/shunt_voltage` トピックを読む
  - シャント抵抗の抵抗値をもとに`I=V/R`によって電流値を計算
  - サブスクライブ (Input):`/shunt_voltage` ([std_msgs/msg/Float32]): 入力電圧値 [V]
  - パブリッシュ (Output):`/calculated_current` ([std_msgs/msg/Float32]): 計算後の電流値 [A]

## shunt
  - シャント抵抗にかかる電圧を疑似的に生成するノード
  - プログラム名:shunt.py
  - 5秒ごとに0.0V~0.5Vの範囲でランダムに電圧値を生成する
  - パブリッシュ (Output):`/shunt_voltage` ([std_msgs/msg/Float32]): 疑似電圧値 [V]

# トピックの仕様説明
## `/shunt_voltage`
  - 型:`std_msgs/Float32`
  - 単位:`V`
  - 内容:シャント抵抗両端の電位差（模擬値）

## `/calculated_current`
  - 型:`std_msgs/Float32`
  - 単位:`A`
  - 内容:算出された回路の電流値

# 使用方法

# ライセンス・コピーライト
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2025 Tomotaka Fujiwara
