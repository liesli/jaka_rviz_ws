#include"ros/ros.h"
#include<sensor_msgs/JointState.h>

double data[6]={0, 1.57, -1.57, -1.57, 1.57, 0};
int main(int argc, char*argv[]){
    setlocale(LC_ALL,"");
    ros::init(argc,argv,"joint_state_publisher");
    ros::NodeHandle nh;
    ros::Publisher pub=nh.advertise<sensor_msgs::JointState>("/joint_states",100);
    sensor_msgs::JointState msg;
    msg.position.clear(); 

    for (int i=0;i<6;i++){
        msg.position.push_back(data[i]);
        int j = i+1;
        msg.name.push_back("joint_"+ std::to_string(j));
        msg.header.stamp = ros::Time::now();
    }
    while (ros::ok()){
        pub.publish(msg);
        ros::spinOnce();

    }
   
    
    return 0;




}