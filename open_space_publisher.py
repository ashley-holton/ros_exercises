#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
from ros_exercises.msg import OpenSpace
import math
import numpy as np

rospy.init_node("open_space_publisher")
rate = rospy.Rate(20)
pub = rospy.Publisher("open_space", OpenSpace, queue_size=10)

def callback(scan):
  ranges = scan.ranges
  max_val = np.max(ranges)
  max_arg = np.argmax(ranges)
  angle = scan.angle_min + scan.angle_increment*max_arg
  open_space = OpenSpace()
  open_space.angle = angle
  open_space.distance = max_val
  rospy.loginfo(open_space)
  pub.publish(open_space)
  rate.sleep()

def listener():
  rospy.Subscriber("fake_scan", LaserScan, callback)
  rospy.spin()

if __name__ == '__main__':
  listener()
