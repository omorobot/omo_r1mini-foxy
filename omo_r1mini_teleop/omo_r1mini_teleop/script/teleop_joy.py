#!/usr/bin/env python
#
# Copyright (c) 2011, Willow Garage, Inc.
# All rights reserved.
#
# Software License Agreement (BSD License 2.0)
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of {copyright_holder} nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

# Author: Kyuhyong You

from tokenize import Double
import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from rclpy.logging import get_logger

from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from rclpy.qos import QoSProfile


OMO_R1MINI_MAX_LIN_VEL = 0.50
OMO_R1MINI_MAX_ANG_VEL = 5.70

LIN_VEL_STEP_SIZE = 0.01
ANG_VEL_STEP_SIZE = 0.1

class TeleopJoyNode(Node):

    def __init__(self):
        super().__init__('teleop_joy')
        self.timer_inc = 0
        self.auto_mode = False
        self.headlight_on = False
        self.mode_button_last = 0
        self.colorIdx = 0
        self.colors = [ [255, 0, 0], [255,50, 0], [255,255,0], [0,255,0], 
            [0,0,255], [0,5,255], [100,0,255], [255,255,255] ]
        # Get parameter values
        print('__________Params_______________')
        #print(self.get_parameter('max_fwd_m_s'))
        self.max_fwd_vel = 0.2#self.get_parameter('/max_fwd_m_s').get_parameter_value().double_value #OMO_R1mini_MAX_LIN_VEL = 1.20
        self.max_rev_vel = 0.2#self.get_parameter('/max_rev_m_s').get_parameter_value().double_value 
        self.max_ang_vel = 2.0#self.get_parameter('/max_deg_s').get_parameter_value().double_value 
        print('Param max fwd: %s m/s, max rev: -%s m/s, max ang: %s dev/s'%
            (self.max_fwd_vel,
            self.max_rev_vel,
            self.max_ang_vel)
        )
        self.qos = QoSProfile(depth=10)
        self.pub_twist = self.create_publisher(Twist, 'cmd_vel', self.qos)
        self.sub = self.create_subscription(Joy, 'joy', self.cb_joy, 10)
        self.timer = self.create_timer(0.1, self.cb_timer)
        self.twist = Twist()

    def cb_joy(self, joymsg):
        if joymsg.buttons[2] == 1 and self.mode_button_last == 0:
            if self.auto_mode == False:
                self.auto_mode = True
                self.get_logger().info("AUTO MODE ON")
            else:
                self.auto_mode = False
                self.get_logger().info("AUTO MODE OFF")
        self.mode_button_last = joymsg.buttons[2]

        if joymsg.axes[1] > 0.0:
            self.twist.linear.x = joymsg.axes[1] * self.max_fwd_vel
        elif joymsg.axes[1] < 0.0:
            self.twist.linear.x = joymsg.axes[1] * self.max_rev_vel
        else:
            self.twist.linear.x = 0.0
        if joymsg.buttons[0] == 1:
            if self.headlight_on == False:
                self.headlight_on = True
                #self.set_headlight_onOff(True)
            else:
                self.headlight_on = False
                #self.set_headlight_onOff(False)

        if joymsg.buttons[3] == 1:
            #self.get_logger().info("Color Set: %s, %s, %s", self.colors[self.colorIdx][0], self.colors[self.colorIdx][1],self.colors[self.colorIdx][2])
            #self.set_ledColor(self.colors[self.colorIdx][0], self.colors[self.colorIdx][1],self.colors[self.colorIdx][2])
            self.colorIdx += 1
            if self.colorIdx == len(self.colors):
                self.colorIdx = 0

        self.twist.linear.y = 0.0; 
        self.twist.linear.z = 0.0
        self.twist.angular.x = 0.0; 
        self.twist.angular.y = 0.0; 
        self.twist.angular.z = joymsg.axes[0] * self.max_ang_vel

    def cb_timer(self):
        self.timer_inc+=1
        if self.auto_mode == False:
            self.pub_twist.publish(self.twist)

def main(args=None):
    rclpy.init(args=args)
    teleop_joy =  TeleopJoyNode()
    rclpy.spin(teleop_joy)

    teleop_joy.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
