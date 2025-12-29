#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Tomotaka Fujiwara
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws

# 1. ビルド
colcon build

# 2. 環境設定の読み込み
source /opt/ros/humble/setup.bash
source install/setup.bash

# 3. ノードの実行
# timeoutで終了すると戻り値が124になるため、|| true でスクリプトの中断を防ぎます
# また、標準エラー(2)を標準出力(1)にまとめてログに記録します
timeout 15 ros2 run mypkg2 shunt > /tmp/mypkg.log 2>&1 || true

# 4. 判定
# ログを確認用に出力（Actionsのコンソールで見れるようにする）
echo "--- Captured Log ---"
cat /tmp/mypkg.log
echo "--------------------"

# grep で検索。-q は「見つかったかどうか」だけを確認するオプション
if grep -qE "送信中の電圧: 0\.[0-9]+" /tmp/mypkg.log; then
    echo "TEST PASSED"
    exit 0
else
    echo "TEST FAILED: Target string not found in log"
    exit 1
fi
