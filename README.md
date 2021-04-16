# ROS2 packages for omorobot r1 mini

## Build source

### Clone source

```bash
  cd {$workspace_path}/src/
  git clone https://github.com/PinkWink/omo_r1mini-foxy.git
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

- To bringup robot (in simulation environment)
```bash
  cd {$workspace_path}
  ros2 launch omo_r1mini_gazebo omo_r1mini.launch.py
```

- To conduct SLAM (Try after few seconds from MCU and LiDAR bringup)

```bash
  cd {$workspace_path}
  ros2 launch omo_r1mini_cartographer cartographer.launch.py
  ros2 launch omo_r1mini_cartographer cartographer_rviz.launch.py
```

- To conduct path planning & following (Try after few seconds from MCU and LiDAR bringup)
```bash
  cd {$workspace_path}
  ros2 launch omo_r1mini_navigation2 navigation2.launch.py
  ros2 launch omo_r1mini_navigation2 navigation2_rviz.launch.py
```