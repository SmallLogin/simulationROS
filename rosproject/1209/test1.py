from trajectory_msgs.msg import MultiDOFJointTrajectory, MultiDOFJointTrajectoryPoint
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Transform, Quaternion
import std_msgs.msg
from geometry_msgs.msg import Point
import tf
import rospy
import math
import time


firefly_command_publisher = rospy.Publisher('/firefly/command/trajectory', MultiDOFJointTrajectory, queue_size=10)

desired_yaw_to_go_degree=-10

desired_x_to_go=2
desired_y_to_go=2.5
desired_z_to_go=2.5

quaternion = tf.transformations.quaternion_from_euler(0, 0, math.radians(desired_yaw_to_go_degree))

traj = MultiDOFJointTrajectory()

header = std_msgs.msg.Header()
header.stamp = rospy.Time()
header.frame_id = 'frame'
traj.joint_names.append('base_link')
traj.header=header

transforms =Transform(translation=Point(desired_x_to_go, desired_y_to_go, desired_z_to_go), rotation=Quaternion(quaternion[0],quaternion[1],quaternion[2],quaternion[3]))

velocities =Twist()
accelerations=Twist()
point = MultiDOFJointTrajectoryPoint([transforms],[velocities],[accelerations],rospy.Time(2))

traj.points.append(point)

time.sleep(1)
firefly_command_publisher.publish(traj)