#!/usr/bin/env python

# UNUTULACAK DUNLER
# YASANILACAK GUNLER

import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64 as F64

global x,xi,y,yi,z,zi,w,flag,button
flag=False
x=0.0
y=0.0
z=0.0
xi=0.0
yi=0.0
zi=0.0

#joystickden gelen veriyi okumaca, arekin kodundan kopya
def callback(data):
	global xi,yi,zi,flag,button,pitch,yaw,roll
	button=data.buttons[4]
	xi=data.axes[1]*0.001
	yi=data.buttons[4]*0.001
	zi=-data.axes[2]*0.001
	pitch=-data.axes[5]
	yaw=data.axes[0]
	roll=-data.axes[4]

if __name__ == "__main__":
	rospy.init_node("KONTROL", anonymous=True)
	pub = rospy.Publisher('/rover_arm_j1_joint_position_controller/command', F64, queue_size = 10)
	pub2 = rospy.Publisher('/rover_arm_j2_joint_position_controller/command', F64, queue_size = 10)	
	pub3 = rospy.Publisher('/rover_arm_j3_joint_position_controller/command', F64, queue_size = 10)	
	pub4 = rospy.Publisher('/rover_arm_j4_joint_position_controller/command', F64, queue_size = 10)	
	pub5 = rospy.Publisher('/rover_arm_j5_joint_position_controller/command', F64, queue_size = 10)	
	pub6 = rospy.Publisher('/rover_arm_j6_joint_position_controller/command', F64, queue_size = 10)	

	rospy.Subscriber("joy", Joy, callback)
	rate = rospy.Rate(2259)
	ilk_aci = 0.0
	while not rospy.is_shutdown():
		x = x + xi
		z = z + zi
		y = y + yi
		pub.publish(y)
		#pub2.publish(x)
		#pub3.publish(z)
		#pub4.publish(z)
		#pub5.publish(x)
		#pub6.publish(x)
		rate.sleep()