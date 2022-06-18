# R1mini 공식 ROS2 패키지

## 소스 빌드하기

### 소스 받아오기

workspace_path 는 ros2의 작업공간입니다(workspace) 
```bash
  cd {$workspace_path}/src/
  git clone https://github.com/omorobot/omo_r1mini-foxy.git
  git clone https://github.com/PinkWink/YDLidar-SDK.git
  git clone https://github.com/PinkWink/ydlidar_ros2_driver.git
```

### YD-라이다 SDK 패키지 빌드

```bash
  cd {$workspace_path}/src/YDLidar-SDK
  cd build
  cmake ..
  make
  sudo make install
```
### 추가 패키지 설치하기

다음 패키지들이 필요할 수 있습니다.  
- gazebo 
- ros-foxy-gazebo-ros-pkgs
- cartographer-ros  
- nav2_map_server
- nav2_bringup
- pyserial : 파이썬에서 serial을 import하기 위함

```bash
sudo apt install -y ros-foxy-gazebo-ros\
 ros-foxy-cartographer-ros\
 ros-foxy-nav2-map-server\
 ros-foxy-gazebo-ros-pkgs\
 ros-foxy-nav2-bringup

pip install pyserial
```

### ROS2 소스코드 빌드하기

- 터미널에서 다음과 같이 입력합니다.

```bash
cd {$workspace_path}
colcon build --symlink-install
```

- 빌드한 소스를 bash에 등록하기 위해 다음을 입력합니다.

```bash
cd {$workspace_path}
source install/setup.bash
```

## R1mini 로봇 조작하기

- YD-라이다의 USB포트 경로를 /dev/ttyLiDAR 로 변경하기 위해 다음을 수행합니다.

```bash
cd {$workspace_path}/src/omo_r1mini/omo_r1mini_bringup
sudo sh create_udev_rules.sh
```

- R1mini 브링업

```bash
  cd {$workspace_path}
  ros2 launch omo_r1mini_bringup omo_r1mini_bringup.launch.py
```

- 시뮬레이션 환경에서 로봇을 브링업 하는 방법은 다음과 같습니다.
```bash
  cd {$workspace_path}
  ros2 launch omo_r1mini_gazebo omo_r1mini.launch.py
```

- 키보드를 사용하여 조작하기 위해 키보드 Teleop 노드를 실행합니다.

```bash
  cd {$workspace_path}
  ros2 run omo_r1mini_teleop teleop_keyboard
```

- SLAM을 실행하기위해 다음을 입력합니다. (MCU 와 LiDAR 가 정상적으로 동작할때까지 기다린 후 실행합니다)

```bash
  cd {$workspace_path}
  ros2 launch omo_r1mini_cartographer cartographer.launch.py
  ros2 launch omo_r1mini_cartographer cartographer_rviz.launch.py
```
- SLAM 매핑이 완료되면 다음 명령으로 map.pgm과 map.yaml 파일을 만들 수 있습니다.

```bash
cd {$HOME}
ros2 run nav2_map_server map_saver_cli -f map
```

- 경로 계획(Path planning)과 추종(following)을 위해 다음을 실행합니다. (키보드 Teleop 노드는 중지합니다)
```bash
  cd {$workspace_path}
  ros2 launch omo_r1mini_navigation2 navigation2.launch.py map:=$HOME/map.yaml
  ros2 launch omo_r1mini_navigation2 navigation2_rviz.launch.py
```