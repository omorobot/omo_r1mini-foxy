#!/bin/bash

echo ""
echo "This script copies OMO R1 udev rules to /etc/udev/rules.d/"
echo ""

echo "Motor Driver (USB Serial from RS232) : /dev/ttyTHS1 to /dev/ttyMCU :"
if [ -f "/etc/udev/rules.d/98-omo-r1-mini-mcu" ]; then
    echo "98-omo-r1-mini-mcu file already exist."
else 
    echo 'KERNEL=="ttyTHS1", MODE:="0666", GROUP:="dialout", SYMLINK+="ttyMCU"' > /etc/udev/rules.d/98-omo-r1-mini-mcu.rules
    
    echo '98-omo-r1-mini-mcu created'
fi

echo ""
echo "YD LiDAR (USB Serial) : /dev/ttyUSBx to /dev/ttyLiDAR :"
if [ -f "/etc/udev/rules.d/97-omo-r1-mini-lidar.rules" ]; then
    echo "97-omo-r1-mini-lidar.rules file already exist."
else 
    echo 'KERNEL=="ttyUSB*", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60", MODE:="0666", GROUP:="dialout",  SYMLINK+="ttyLiDAR"' >/etc/udev/rules.d/97-omo-r1-mini-lidar.rules
    
    echo '97-omo-r1-mini-lidar.rules created'
fi

# if [ -f "/etc/udev/rules.d/ydlidar-V2.rules" ]; then
#     echo "ydlidar-V2.rules file already exist."
# else 
#     echo 'KERNEL=="ttyACM*", ATTRS{idVendor}=="0483", ATTRS{idProduct}=="5740", MODE:="0666", GROUP:="dialout",  SYMLINK+="ttyLiDAR"' >/etc/udev/rules.d/ydlidar-V2.rules
    
#     echo 'ydlidar-V2.rules created'
# fi

# if [ -f "/etc/udev/rules.d/ydlidar-2303.rules" ]; then
#     echo "ydlidar-2303.rules file already exist."
# else 
#     echo 'KERNEL=="ttyUSB*", ATTRS{idVendor}=="067b", ATTRS{idProduct}=="2303", MODE:="0666", GROUP:="dialout",  SYMLINK+="ttyLiDAR"' >/etc/udev/rules.d/ydlidar-2303.rules
    
#     echo 'ydlidar-2303.rules created'
# fi

echo ""
echo "Reload rules"
echo ""
sudo udevadm control --reload-rules
sudo udevadm trigger