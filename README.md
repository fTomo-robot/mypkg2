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
## shunt
  - 以下のコマンドからシャント抵抗にかかる電圧を疑似的に生成できます。
```
$ ros2 run mypkg2 shunt
```

## current
  - 以下のコマンドからシャント抵抗の計算のみを独立して実行できます。
```
$ ros2 run mypkg2 current
```

### シャント抵抗設定
  - current ノードはシャント抵抗の値をパラメータとして保持しています。使用する抵抗に合わせて値を変更してください。
	- パラメータ名: `shunt_resistance`
	- デフォルト値: `0.1 [Ω] `
  - 設定方法: Launchファイル内の parameters 項目を書き換えることで、任意の抵抗値を適用できます。

```
parameters=[{'shunt_resistance': 0.01}]
```

## launchfile
  - コマンドを実行すると、電圧の生成（シミュレータ）と電流の計算が連動して動作します。
  - [shunt-1]: 電圧シミュレータノードからの出力です。5秒ごとにランダムな電圧（0〜0.5V）を生成し、トピック `/shunt_voltage` に送信します。
  - [current-2]: 電流計算ノードからの出力です。トピック経由で受信した電圧値に対し、設定したシャント抵抗値を適用して電流値を算出します。

```
$ ros2 launch mypkg2 current_shunt.launch.py

[shunt-1] [INFO] [1766993698.643026729] [voltage_sim_node]: 送信中の電圧: 0.391 V
[current-2] [INFO] [1766993698.643362847] [current_calc_node]: Voltage: 0.391V -> Current: 3.907A
[shunt-1] [INFO] [1766993703.643141788] [voltage_sim_node]: 送信中の電圧: 0.062 V
[current-2] [INFO] [1766993703.644429569] [current_calc_node]: Voltage: 0.062V -> Current: 0.620A
```

# ライセンス・コピーライト
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2025 Tomotaka Fujiwara
