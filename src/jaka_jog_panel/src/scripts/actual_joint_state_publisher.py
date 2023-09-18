#! /usr/bin/env python


import rospy
from sensor_msgs.msg  import JointState
import numpy as np
from socket import *
import json
import time
import re
from pathlib import Path
from math import pi


serverName = '10.5.5.100'  # ip address of robot
cmdPort = 10001 #port address
# clientPort=10000
BUFSIZ = 4045
ADDR = (serverName,cmdPort)
# ADDR2 = (serverName,clientPort)
cmdSocket = socket(AF_INET, SOCK_STREAM)
# clientSocket = socket(AF_INET, SOCK_STREAM)
cmdSocket.connect(ADDR)
# clientSocket.connect(ADDR2)
# if True:
#     rospy.INFO("connect successfuly")

def get_actual_joint():
    testDict='{"cmdName":"get_joint_pos"}'
    cmdSocket.sendall(testDict.encode())
    recvdata = cmdSocket.recv(2048)
    Data = json.loads(recvdata.decode())
    joint_actual_pos=Data['joint_pos']
    joint_actual_pos=np.array(joint_actual_pos)
    return joint_actual_pos

if __name__ == "__main__":
    rospy.init_node("control_joint")
   
    pub = rospy.Publisher("/joint_states",JointState,queue_size=100)

    rate = rospy.Rate(10)
    msg = JointState()
    while not rospy.is_shutdown():
         joint_pos=get_actual_joint()
         joint_pos=joint_pos*pi/180
         msg.name=['joint_1','joint_2','joint_3','joint_4','joint_5','joint_6']
         msg.position=[-joint_pos[0],joint_pos[1],joint_pos[2],-joint_pos[3],joint_pos[4],joint_pos[5]]
         msg.header.stamp = rospy.Time.now()
         pub.publish(msg)
         rate.sleep()