#!/usr/bin/env python

import rospy
from control.msg import drive_param
from control.msg import pid_input

kp = 3
kd = 0.05
servo_offset = 18.5
prev_error = 0.0 
vel_input = 30

pub = rospy.Publisher('control/drive_parameters', drive_param, queue_size=1)

def control(data):
	global prev_error
	global vel_input
	global kp
	global kd

	## Your code goes here
	# 1. Scale the error
	# 2. Apply the PID equation on error
	# 3. Make sure the error is within bounds
 	

	## END

	msg = drive_param();
	msg.velocity = data.pid_vel
	error=data.pid_error
	angle_p=error*kp
	angle_d=kd*(error-prev_error)
	angle=angle_p+angle_d	
	prev_error=error
	msg.angle = angle
	pub.publish(msg)


if __name__ == '__main__':
	global kp
	global kd
	global vel_input
	print("Listening to error for PID")
	kp = 3
	kd = 0.05
	vel_input = 30

	#kp = input("Enter Kp Value: ")
	#kd = input("Enter Kd Value: ")
	#vel_input = input("Enter Velocity: ")
	rospy.init_node('pid_controller', anonymous=True)
	rospy.Subscriber("control/error", pid_input, control)
	rospy.spin()
