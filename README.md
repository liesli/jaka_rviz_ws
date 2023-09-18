# jaka_rviz_ws
this project is a rviz simulation environment with jaka robot. With socket communication， the position and orientation of robot in real world will mapped to simulation. Its suitable for first learner to practice.
usuage:
cd jaka_ros_ws
source ./devel/setup.bash
roslaunch jaka_rviz jaka_zu18_rviz_control.launch
//start a new terminal
roslaunch jaka_jog_panel jaka_joint_state_publisher // for publish jaka joint angle
//start a new terminal
roslaunch jaka_jog_panel jaka_joint_state_subscriber // for subscribe real jaka joint angle into rviz model
