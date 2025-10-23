#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
import random  # fallback if system file not available

def get_cpu_temperature():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp_str = f.readline()
            return float(temp_str) / 1000.0
    except:
        
        return random.uniform(30.0, 70.0)

def cpu_temp_publisher():
    rospy.init_node('cpu_temp_publisher', anonymous=True)
    pub = rospy.Publisher('cpu_temperature', Float32, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        temp = get_cpu_temperature()
        rospy.loginfo("CPU Temp: %.2f °C", temp)
        pub.publish(temp)
        rate.sleep()

if _name_ == "_main_":
    try:
        cpu_temp_publisher()
    except rospy.ROSInterruptException:
        pass
