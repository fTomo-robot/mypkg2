#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Tomotaka Fujiwara
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class CurrentCalcNode(Node):
    def __init__(self):
        super().__init__('current_calc_node')

        # パラメータの宣言（名前, デフォルト値）
        self.declare_parameter('shunt_resistance', 0.1)

        # 電圧を購読
        self.sub = self.create_subscription(Float32, 'shunt_voltage', self.cb, 10)
        # 電流を配信
        self.pub = self.create_publisher(Float32, 'calculated_current', 10)

    def cb(self, msg):
        # パラメータの最新値を取得
        shunt_ohm = self.get_parameter('shunt_resistance').get_parameter_value().double_value

        # I = V / R
        current = msg.data / shunt_ohm

        out_msg = Float32()
        out_msg.data = current
        self.pub.publish(out_msg)

        self.get_logger().info(f"抵抗値: {shunt_ohm}Ω | 電圧: {msg.data:.3f}V -> 電流: {current:.3f}A")

def main():
    rclpy.init()
    node = CurrentCalcNode()
    try:
        rclpy.spin(node)
    except Exception:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
