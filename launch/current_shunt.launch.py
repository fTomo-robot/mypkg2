#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Tomotaka Fujiwara
# SPDX-License-Identifier: BSD-3-Clause

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='mypkg2', executable='shunt', name='shunt_node'),
        Node(
            package='mypkg2',
            executable='current',
            name='current_node',
            parameters=[{'shunt_resistance': 0.05}] # ここで値を指定
        ),
    ])
