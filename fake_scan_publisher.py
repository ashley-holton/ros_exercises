#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
import random
import math
import numpy as np

pub = rospy.Publisher('fake_scan', LaserScan, queue_size=10)
rospy.init_node('fake_scan_publisher')
rate = rospy.Rate(20)

while not rospy.is_shutdown():
  rand_num = random.random() * 10
  rospy.loginfo(rand_num)
  scan = LaserScan()
  scan.header.stamp = rospy.Time.now()
  scan.header.frame_id = "laser"
  scan.angle_min = (-2.0/3.0)*math.pi
  scan.angle_max = (2.0/3.0)*math.pi
  scan.angle_increment = (1.0/300.0)*math.pi
  scan.range_min = 1.0
  scan.range_max = 10.0
  ranges = np.zeros((int((scan.angle_max-scan.angle_min)/scan.angle_increment + 1,)))
  for i in range(len(ranges)):
    ranges[i] = random.uniform(scan.range_min, scan.range_max)
  scan.ranges = ranges
  pub.publish(scan)
  rate.sleep()

if __name__ == '__main__':
  try:
    fake_scan_publisher()
  except rospy.ROSInterruptException:
    pass
