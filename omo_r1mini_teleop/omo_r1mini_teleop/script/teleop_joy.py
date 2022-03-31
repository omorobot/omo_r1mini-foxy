#!/usr/bin/env python

# Author: Kyuhyong You

from tokenize import Double
import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from rclpy.logging import get_logger

from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from rclpy.qos import QoSProfile

from omo_r1mini_interfaces.srv import Battery
from omo_r1mini_interfaces.srv import Color
from omo_r1mini_interfaces.srv import SaveColor
from omo_r1mini_interfaces.srv import ResetOdom
from omo_r1mini_interfaces.srv import Onoff
from omo_r1mini_interfaces.srv import Calg

OMO_R1MINI_MAX_LIN_VEL = 0.50
OMO_R1MINI_MAX_ANG_VEL = 5.70

LIN_VEL_STEP_SIZE = 0.01
ANG_VEL_STEP_SIZE = 0.1

class TeleopJoyNode(Node):

    def __init__(self):
        super().__init__('teleop_joy_node')
        self.declare_parameters(
            namespace='',
            parameters=[
                ('max_fwd_m_s', None),
                ('max_rev_m_s', None),
                ('max_deg_s', None),
            ])
        self.timer_inc = 0
        self.auto_mode = False
        self.headlight_on = False
        self.mode_button_last = 0
        self.colorIdx = 0
        self.colors = [ [255, 0, 0], [255,50, 0], [255,255,0], [0,255,0], 
            [0,0,255], [0,5,255], [100,0,255], [255,255,255] ]
        print(' R1mini Teleop Joystick controller')
        # Get parameter values
        self.max_fwd_vel = self.get_parameter_or('max_fwd_m_s', Parameter('max_fwd_m_s', Parameter.Type.DOUBLE, 0.2)).get_parameter_value().double_value
        self.max_rev_vel = self.get_parameter_or('max_rev_m_s', Parameter('max_rev_m_s', Parameter.Type.DOUBLE, 0.2)).get_parameter_value().double_value
        self.max_ang_vel = self.get_parameter_or('max_deg_s', Parameter('max_deg_s', Parameter.Type.DOUBLE, 0.2)).get_parameter_value().double_value
        print('Param max fwd: %s m/s, max rev: -%s m/s, max ang: %s dev/s'%
            (self.max_fwd_vel,
            self.max_rev_vel,
            self.max_ang_vel)
        )
        self.qos = QoSProfile(depth=10)
        self.pub_twist = self.create_publisher(Twist, 'cmd_vel', self.qos)
        self.sub = self.create_subscription(Joy, 'joy', self.cb_joy, 10)
        self.timer = self.create_timer(0.05, self.cb_timer)
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
        print('V= %.2f m/s, W= %.2f deg/s'%(self.twist.linear.x, self.twist.angular.z))

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
