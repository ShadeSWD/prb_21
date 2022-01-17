cmake_minimum_required(VERSION 3.0.2)
project(square_turtle)

find_package(catkin REQUIRED COMPONENTS
  rospy
  geometry_msgs
  message_generation)

#############
## Install ##
#############

catkin_install_python(PROGRAMS scripts/square_turtle.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)






