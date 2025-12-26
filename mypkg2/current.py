import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32  # 電圧や電流は小数になるためFloat32を使用

# 設定値
SHUNT_OHMS = 0.1  # 使用するシャント抵抗の値をΩで指定

rclpy.init()
node = Node("current_calc_node")

# 計算結果を配信するためのパブリッシャー
pub = node.create_publisher(Float32, "current_out", 10)

def cb(msg):
    # msg.data にはシャント抵抗の両端電圧(V)が入っていると想定
    voltage = msg.data
    
    # オームの法則 I = V / R
    current = voltage / SHUNT_OHMS
    
    # 結果を表示
    node.get_logger().info(f"Voltage: {voltage:.3f}V -> Current: {current:.3f}A")
    
    # 計算結果を送信
    out_msg = Float32()
    out_msg.data = current
    pub.publish(out_msg)

def main():
    # 電圧トピック "shunt_voltage" を購読
    sub = node.create_subscription(Float32, "shunt_voltage", cb, 10)
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
