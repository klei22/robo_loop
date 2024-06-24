#!/bin/bash

# rostopic pub /cmd_vel geometry_msgs/Twist '{linear: {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.0}}'

# sleep 2

# rostopic pub /cmd_vel geometry_msgs/Twist '{linear: {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}'

# rostopic echo /CoreNode/grey_img 


while [ 1 ]; do 
#rostopic echo -n 1 /CoreNode/grey_img > img.txt

bash awktest.sh

python3 test.py

done
