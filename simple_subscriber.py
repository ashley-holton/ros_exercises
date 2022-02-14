#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
import math

pub = rospy.Publisher("random_float_log", Float32)

def callback(data):
  log = math.log(data.data)
  pub.publish(Float32(log))

def listener():
  rospy.init_node("simple_subscriber")
  rospy.Subscriber("my_random_float", Float32, callback)
  rospy.spin()

if __name__ == '__main__':
  listener()
