#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
import math
import numpy as np

rospy.init_node("open_space_publisher")
rate = rospy.Rate(20)
pub = rospy.Publisher("open_space/distance", Float32, queue_size=10)
pub2 = rospy.Publisher("open_space/angle", Float32, queue_size=10)

def callback(scan):
  ranges = scan.ranges
  max_val = np.max(ranges)
  max_arg = np.argmax(ranges)
  angle = scan.angle_min + scan.angle_increment*max_arg
  pub.publish(Float32(max_val))
  pub2.publish(Float32(angle))
  rate.sleep()

def listener():
  rospy.Subscriber("fake_scan", LaserScan, callback)
  rospy.spin()

if __name__ == '__main__':
  listener()
