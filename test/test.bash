#!/bin/bash

# ワークスペースのディレクトリ指定
dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws

# 1. ビルド
colcon build

# 2. 環境設定の読み込み
source /opt/ros/humble/setup.bash
# GitHub Actions等では .bashrc ではなく install/setup.bash を直接読み込むのが確実です
source install/setup.bash

# 3. ノードの実行（15秒間実行してログを保存）
# ここでは mypkg2 の talker ノード（電圧出力）を実行すると仮定します
timeout 15 ros2 run mypkg2 shunt > /tmp/mypkg.log

# 4. 判定
# ログの中に「送信中の電圧:」という文字列があるか、
# かつ「0.」から始まる電圧値が含まれているかを正規表現でチェックします
cat /tmp/mypkg.log | grep -E "送信中の電圧: 0\.[0-9]+"

# grepの終了ステータス（見つかれば0）をそのままスクリプトの戻り値にする
exit $?
