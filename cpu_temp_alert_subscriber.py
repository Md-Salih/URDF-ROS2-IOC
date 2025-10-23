#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

def callback(temp):
    if temp.data > 60.0:
        rospy.logwarn("⚠ CPU Overheating: %.2f °C", temp.data)
    else:
        rospy.loginfo("CPU Normal: %.2f °C", temp.data)

def listener():
    rospy.init_node('cpu_temp_listener', anonymous=True)
    rospy.Subscriber("cpu_temperature", Float32, callback)
    rospy.spin()

if _name_ == "_main_":
    listener()
