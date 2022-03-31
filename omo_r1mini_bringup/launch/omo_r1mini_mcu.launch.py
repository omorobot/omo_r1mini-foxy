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
  omo_r1mini_mcu_parameter = LaunchConfiguration(
    'omo_r1mini_mcu_parameter',
    default=os.path.join(
      get_package_share_directory('omo_r1mini_bringup'),
      'param/omo_r1mini_mcu.yaml'
    )
  )

  return LaunchDescription([
    DeclareLaunchArgument(
      'omo_r1mini_mcu_parameter',
      default_value=omo_r1mini_mcu_parameter
    ),

    Node(
      package='omo_r1mini_bringup',
      executable='omo_r1mini_mcu_node',
      name='omo_r1mini_mcu_node',
      output='screen',
      emulate_tty=True,
      parameters=[omo_r1mini_mcu_parameter],
      namespace='',
    )
  ])
