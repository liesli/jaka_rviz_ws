#! /usr/bin/env python


import rospy
from sensor_msgs.msg  import JointState
import numpy as np

def convert_force_file(traj_str):
    traj = []
    for i in range(len(traj_str)):
        traj_current = traj_str[i][:-1].split('	')
        # print(traj_current)
        for j in range(len(traj_current)):
            traj_current[j]=float(traj_current[j])
        traj.append(traj_current)
    return traj


if __name__ == "__main__":
    traj_file=open('/home/liesli/jaka_ros_ws/src/jaka_jog_panel/src/scripts/traj.txt','r')
    traj=traj_file.readlines()
    traj=convert_force_file(traj)
   
    rospy.init_node("control_joint")
   
    pub = rospy.Publisher("/joint_states",JointState,queue_size=100)

    rate = rospy.Rate(10)
    msg = JointState()
    for i in range(len(traj)):
        traj1=traj[i]
        traj1=np.array(traj1) 
        msg.name=['joint_1','joint_2','joint_3','joint_4','joint_5','joint_6']
        msg.position=[float(traj1[0]),float(traj1[1]),float(traj1[2]),-float(traj1[3]),float(traj1[4]),float(traj1[5])]
        msg.header.stamp = rospy.Time.now()
        pub.publish(msg)
        rate.sleep()
