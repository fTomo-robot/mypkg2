#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Tomotaka Fujiwara
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():

   shunt = launch_ros.actions.Node(
      package='mypkg2',      #パッケージの名前を指定
      executable='shunt',  #実行するファイルの指定
      )
   current = launch_ros.actions.Node(
      package='mypkg2',
      executable='current',
      output='screen'        #ログを端末に出すための設定
      )

   return launch.LaunchDescription([shunt, current])
