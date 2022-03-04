# ROS2 packages for omorobot r1 mini

This project is to demonstrate R1mini control and navigation in ROS2-foxy environment.  
한국어 사용자는 다음 **한국어**[문서](README_KR.md)를 참조하십시오.  

## Build source

### Clone source

```bash
  cd {$workspace_path}/src/
  git clone https://github.com/omorobot/omo_r1mini-foxy.git
  git clone https://github.com/PinkWink/YDLidar-SDK.git
  git clone https://github.com/PinkWink/ydlidar_ros2_driver.git
```

### Build LiDAR's SDK

```bash
  cd {$workspace_path}/src/YDLidar-SDK
  cd build
  cmake ..
  make
  sudo make install
```

### Install dependency packages

Following additional packages may be reuqired to be installed.  
- gazebo 
- ros-foxy-gazebo-ros-pkgs
- cartographer-ros  
- nav2_map_server
- pyserial

```bash
sudo apt install -y ros-foxy-gazebo-ros ros-foxy-cartographer-ros ros-foxy-nav2-map-server ros-foxy-gazebo-ros-pkgs

pip install pyserial
```

### Build ROS2 source

- To build

```bash
  cd {$workspace_path}
  colcon build --symlink-install
```

- To enable the built source into ROS2 environment

```bash
  cd {$workspace_path}
  ./install/setup.bash
```

## Play with the robot

- To give authority for driver access to MCU and LiDAR

```bash
cd {$workspace_path}/src/omo_r1mini/omo_r1mini_bringup
sudo sh create_udev_rules.sh
```

- To bringup robot

```bash
cd {$workspace_path}
ros2 launch omo_r1mini_bringup omo_r1mini_bringup.launch.py
```

- To bringup robot (in **simulation environment**)
```bash
cd {$workspace_path}
ros2 launch omo_r1mini_gazebo omo_r1mini.launch.py
```
- To teleoperate the robot using **KEYBOARD**

```bash
cd {$workspace_path}
ros2 run omo_r1mini_teleop teleop_keyboard
```

- To conduct SLAM (Try after few seconds from MCU and LiDAR bringup)

```bash
cd {$workspace_path}
ros2 launch omo_r1mini_cartographer cartographer.launch.py
ros2 launch omo_r1mini_cartographer cartographer_rviz.launch.py
```

- Once mapping is done, you can create map.pgm and map.yaml file by executing

```bash
cd {$HOME}
ros2 run nav2_map_server map_saver_cli -f map
```

- To conduct path planning & following (Try after few seconds from MCU and LiDAR bringup)
```bash
cd {$workspace_path}
ros2 launch omo_r1mini_navigation2 navigation2.launch.py map:=$HOME/map.yaml
ros2 launch omo_r1mini_navigation2 navigation2_rviz.launch.py
```