#!/usr/bin/env python
import math

import rospy
from geometry_msgs.msg import Twist


def velocity(vel, lin_x=0, lin_y=0, lin_z=0, ang_x=0, ang_y=0, ang_z=0):
    vel.linear.x = lin_x
    vel.linear.y = lin_y
    vel.linear.z = lin_z

    vel.angular.x = ang_x
    vel.angular.y = ang_y
    vel.angular.z = ang_z

    return vel


def square_turtle(linear_vel, angular_vel):
    rospy.init_node('turtle_square', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(0.5)
    vel = Twist()

    while True:
        pub.publish(velocity(vel, lin_x=linear_vel))
        rate.sleep()
        pub.publish(velocity(vel, ang_z=angular_vel))
        rate.sleep()


if __name__ == '__main__':
    try:
        square_turtle(3.0, math.pi/2)
    except rospy.ROSInterruptException:
        pass
    