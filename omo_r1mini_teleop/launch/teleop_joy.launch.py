#!/usr/bin/env python3

# Author: Kyuhyong You

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import TextSubstitution
from launch_ros.actions import Node


def generate_launch_description():
  teleop_joy_parameter = LaunchConfiguration(
    'teleop_joy_parameter',
    default=os.path.join(
      get_package_share_directory('omo_r1mini_teleop'),
      'param/teleop_joy.yaml'
    )
  )
  joy_config = LaunchConfiguration('joy_config')
  joy_dev = LaunchConfiguration('joy_dev')

  return LaunchDescription([
    #DeclareLaunchArgument(
    #  'teleop_joy_parameter',
    #  default_value=teleop_joy_parameter
    #),
    Node(
      package='omo_r1mini_teleop',
      executable='teleop_joy',
      name='teleop_joy',
      output='screen',
      emulate_tty=True,
      parameters=[{'max_fwd_m_s':0.24}],
      namespace='/',
    ),
    DeclareLaunchArgument(
      'joy_config', 
      default_value='xbox'
    ),
    DeclareLaunchArgument(
      'joy_dev', 
      default_value='/dev/input/js0'
    ),
    DeclareLaunchArgument(
      'config_filepath', 
      default_value=[
        TextSubstitution(text=os.path.join(
          get_package_share_directory(
            'teleop_twist_joy'), 
            'config', '')),
          joy_config, TextSubstitution(text='.config.yaml')
      ]
    ),
    Node(
      package='joy', 
      executable='joy_node', 
      name='joy_node',
      parameters=[{
        'dev': joy_dev,
        'deadzone': 0.3,
        'autorepeat_rate': 20.0,
      }]
    )
  ])