#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Tomotaka Fujiwara
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

rclpy.init()
node = Node("voltage_sim_node")
# トピック名 "shunt_voltage" でパブリッシャを作成
pub = node.create_publisher(Float32, "shunt_voltage", 10)

def cb():
    msg = Float32()
    
    # 0.0 から 0.5 の範囲でランダムな浮動小数点数を生成
    voltage = random.uniform(0.0, 0.5)
    
    msg.data = voltage
    pub.publish(msg)
    
    # ログに表示（確認用）
    node.get_logger().info(f"送信中の電圧: {voltage:.3f} V")

def main():
    # 5.0秒ごとに cb 関数を呼び出す
    node.create_timer(5.0, cb)
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
