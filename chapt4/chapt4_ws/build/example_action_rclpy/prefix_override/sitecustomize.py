import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/aurora/d2lros2/chapt4/chapt4_ws/install/example_action_rclpy'
