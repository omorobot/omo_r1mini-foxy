#!/usr/bin/env python3

# Author: Bishop Pearson

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import ThisLaunchFileDir
from launch_ros.actions import Node


def generate_launch_description():
    usb_port = LaunchConfiguration('usb_port', default='/dev/ttyACM0')

    tb3_param_dir = LaunchConfiguration(
        'tb3_param_dir',
        default=os.path.join(
            get_package_share_directory('omo_r1mini_bringup'),'param/omo_r1mini.yaml'))

    omo_r1mini_description_dir = LaunchConfiguration(
        'omo_r1mini_description_dir',
        default=os.path.join(get_package_share_directory('omo_r1mini_description'), 'launch')))

    # lidar_pkg_dir = LaunchConfiguration(
    #     'lidar_pkg_dir',
    #     default=os.path.join(get_package_share_directory('hls_lfcd_lds_driver'), 'launch'))

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value=use_sim_time,
            description='Use simulation (Gazebo) clock if true'),

        DeclareLaunchArgument(
            'usb_port',
            default_value=usb_port,
            description='Connected USB port with OpenCR'),

        # DeclareLaunchArgument(
        #     'tb3_param_dir',
        #     default_value=tb3_param_dir,
        #     description='Full path to turtlebot3 parameter file to load'),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [omo_r1mini_description_dir, '/omo_r1mini_state_publisher.launch.py']),
            launch_arguments={'use_sim_time': use_sim_time}.items(),
        ),

        # IncludeLaunchDescription(
        #     PythonLaunchDescriptionSource([lidar_pkg_dir, '/hlds_laser.launch.py']),
        #     launch_arguments={'port': '/dev/ttyUSB0', 'frame_id': 'base_scan'}.items(),
        # ),

        # Node(
        #     package='turtlebot3_node',
        #     executable='turtlebot3_ros',
        #     parameters=[tb3_param_dir],
        #     arguments=['-i', usb_port],
        #     output='screen'),
    ])
