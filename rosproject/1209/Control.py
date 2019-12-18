#!/usr/bin/env python


# Waypoint publisher for RotorS
# Reference: https://github.com/ethz-asl/rotors_simulator/issues/510
# 

import rospy
import sys
import tf
import numpy as np

from trajectory_msgs.msg import MultiDOFJointTrajectory, MultiDOFJointTrajectoryPoint
from geometry_msgs.msg import Twist 
from geometry_msgs.msg import Transform

def publish_waypoint(x,y,z,yaw):
	"""
	Publish a waypoint to 
	"""

	command_publisher = rospy.Publisher('/firefly/command/trajectory', MultiDOFJointTrajectory, queue_size = 10)

	# create trajectory msg
	traj = MultiDOFJointTrajectory()
	traj.header.stamp = rospy.Time.now()
	traj.header.frame_id = 'frame'
	traj.joint_names.append('base_link')


	# create start point for trajectory
	transforms = Transform()
	velocities = Twist()
	accel = Twist()
	point = MultiDOFJointTrajectoryPoint([transforms],[velocities],[accel],rospy.Time(1))
	traj.points.append(point)

	# create end point for trajectory
	# transforms = Transform()
	transforms.translation.x = x
	transforms.translation.y = y
	transforms.translation.z = z 

	quat = tf.transformations.quaternion_from_euler(0, 0, yaw*np.pi/180.0, axes = 'rzyx')

	transforms.rotation.x = quat[0]
	# transforms.rotation.x = 0
	transforms.rotation.y = quat[3]
	transforms.rotation.z = quat[2]
	transforms.rotation.w = quat[1]

	print("quat[0]:",transforms.rotation.x)
	print("quat[1]:",transforms.rotation.y)
	print("quat[2]:",transforms.rotation.z)
	print("quat[3]:",transforms.rotation.w)

	velocities = Twist()
	accel = Twist()
	point = MultiDOFJointTrajectoryPoint([transforms],[velocities],[accel],rospy.Time(2))
	traj.points.append(point)

	rospy.sleep(1)
	command_publisher.publish(traj)


if __name__ == '__main__':
	try:
		rospy.init_node("riseq_rotors_waypoint_publisher", anonymous = True)
		print "666666"
		x_des=float(0)
		y_des=float(0)
		z_des=float(2)
		yaw_des=float(181.878668538703422)
		publish_waypoint(x_des, y_des, z_des, yaw_des)

		rospy.loginfo(" >> Published waypoint: x: {}, y: {}, z: {}, yaw: {}".format(x_des, y_des, z_des, yaw_des))
        # get command line params
		# x_des = float(sys.argv[1])
		# y_des = float(sys.argv[2])
		# z_des = float(sys.argv[3])
		# yaw_des = float(sys.argv[4])
		
		#rospy.spinOnce()

	except rospy.ROSInterruptException:
		print("ROS Terminated")
		pass