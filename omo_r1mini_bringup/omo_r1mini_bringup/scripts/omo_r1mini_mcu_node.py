import rclpy
from rclpy.node import Node
from rclpy.logging import get_logger
from rclpy.parameter import Parameter
from time import sleep
import time
import copy
import math
from geometry_msgs.msg import Twist, Pose, Point, Vector3, Quaternion, TransformStamped
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu, JointState
from tf2_ros import TransformBroadcaster

from omo_r1mini_interfaces.srv import Battery
from omo_r1mini_interfaces.srv import Color
from omo_r1mini_interfaces.srv import SaveColor
from omo_r1mini_interfaces.srv import ResetOdom
from omo_r1mini_interfaces.srv import Onoff
from omo_r1mini_interfaces.srv import Calg

from .calc.quaternion_from_euler import *
from .omo_packet_handler import PacketHandler

class OdomPose(object):
  x = 0.0
  y = 0.0
  theta = 0.0
  timestamp = 0
  pre_timestamp = 0

class OdomVel(object):
  x = 0.0
  y = 0.0
  w = 0.0

class Joint(object):
  joint_name = ['wheel_left_joint', 'wheel_right_joint']
  joint_pos = [0.0, 0.0]
  joint_vel = [0.0, 0.0]

class ComplementaryFilter():
  def __init__(self):
    self.theta = 0.
    self.pre_theta = 0.
    self.wheel_ang = 0.
    self.filter_coef = 2.5
    self.gyro_bias = 0.
    self.count_for_gyro_bias = 110

  def gyro_calibration(self, gyro):
    self.count_for_gyro_bias -= 1

    if self.count_for_gyro_bias > 100:
      return "Prepare for gyro_calibration"

    self.gyro_bias += gyro
    if self.count_for_gyro_bias == 1:
      self.gyro_bias /= 100
      self.get_logger().info('Complete : Gyro calibration')
      return "gyro_calibration OK"

    return "During gyro_calibration"

  def calc_filter(self, gyro, d_time):

    if self.count_for_gyro_bias != 1:
      tmp = self.gyro_calibration(gyro)
      return 0

    gyro -= self.gyro_bias
    self.pre_theta = self.theta
    temp = -1/self.filter_coef * (-self.wheel_ang + self.pre_theta) + gyro
    self.theta = self.pre_theta + temp*d_time
    #print self.theta*180/3.141, self.wheel_ang*180/3.141, gyro, d_time
    return self.theta

class OMOR1MiniNode(Node):
  def __init__(self):
    super().__init__('omo_r1mini_motor_setting')
    # Declare parameters from YAML
    self.declare_parameters(
      namespace='',
      parameters=[
        ('port.name', None),
        ('port.baudrate', None),
        ('motor.gear_ratio', None),
        ('motor.max_lin_vel_x', None),
        ('sensor.enc_pulse', None),
      ])
    # Get parameter values
    _port_name = self.get_parameter_or('port.name', Parameter('port.name', Parameter.Type.STRING, '/dev/ttyTHS1')).get_parameter_value().string_value
    _port_baudrate = self.get_parameter_or('port.baudrate', Parameter('port.baudrate', Parameter.Type.INTEGER, 115200)).get_parameter_value().integer_value
    self.gear_ratio = self.get_parameter_or('motor.gear_ratio', Parameter('motor.gear_ratio', Parameter.Type.DOUBLE, 21.3)).get_parameter_value().double_value
    self.wheel_separation = self.get_parameter_or('wheel.separation', Parameter('wheel.separation', Parameter.Type.DOUBLE, 0.17)).get_parameter_value().double_value # 0.085 cm x 2
    self.wheel_radius = self.get_parameter_or('wheel.radius', Parameter('wheel.radius', Parameter.Type.DOUBLE, 0.0335)).get_parameter_value().double_value
    self.enc_pulse = self.get_parameter_or('sensor.enc_pulse', Parameter('sensor.enc_pulse', Parameter.Type.DOUBLE, 44.0)).get_parameter_value().double_value
    self.use_gyro = self.get_parameter_or('sensor.use_gyro', Parameter('sensor.use_gyro', Parameter.Type.BOOL, False)).get_parameter_value().bool_value
    print('GEAR RATIO:\t\t%s'%(self.gear_ratio))
    print('WHEEL SEPARATION:\t%s'%(self.wheel_separation))
    print('WHEEL RADIUS:\t\t%s'%(self.wheel_radius))
    print('ENC_PULSES:\t\t%s'%(self.enc_pulse))

    self.distance_per_pulse = 2*math.pi*self.wheel_radius / self.enc_pulse / self.gear_ratio
    print('DISTANCE PER PULSE \t:%s'%(self.distance_per_pulse))
    # Packet handler
    self.ph = PacketHandler(_port_name, _port_baudrate)
    self.calc_yaw = ComplementaryFilter()

    self.ph.robot_state = {
      "VW" : [0., 0.],
      "ODO" : [0., 0.],
      "ACCL" : [0., 0., 0.],
      "GYRO" : [0., 0., 0.],
      "POSE" : [0., 0., 0.],
      "BAT" : [0., 0., 0.],
    }
    self.ph.incomming_info = ['ODO', 'VW', "POSE", "GYRO"]
    self.ph.set_periodic_info(50)

    self.max_lin_vel_x = self.get_parameter_or('/motor/max_lin_vel_x', 
                Parameter('/motor/max_lin_vel_x', Parameter.Type.DOUBLE, 1.2)).get_parameter_value().double_value
    self.max_ang_vel_z = self.get_parameter_or('/motor/max_ang_vel_z', 
                Parameter('/motor/max_ang_vel_z', Parameter.Type.DOUBLE, 2.5)).get_parameter_value().double_value
    self.odom_pose = OdomPose()
    self.odom_pose.timestamp = self.get_clock().now()
    self.odom_pose.pre_timestamp = self.get_clock().now()
    self.odom_vel = OdomVel()
    self.joint = Joint()
  
    # Services
    self.srvHeadlight = self.create_service(Onoff, 'set_headlight', self.cbSrv_headlight)
    self.srvSetColor = self.create_service(Color, 'set_rgbled', self.cbSrv_setColor)
    self.srvResetODOM = self.create_service(ResetOdom, 'reset_odom', self.cbSrv_resetODOM)
    self.srvCheckBAT = self.create_service(Battery, 'check_battery', self.cbSrv_checkBattery)

    # Set subscriber
    self.subCmdVelMsg = self.create_subscription(Twist, 'cmd_vel', self.cbCmdVelMsg, 10)
    
    # Set publisher
    self.pub_JointStates = self.create_publisher(JointState, 'joint_states', 10)
    self.pub_IMU = self.create_publisher(Imu, 'imu', 10)
    self.pub_Odom = self.create_publisher(Odometry, 'odom', 10)
    self.pub_OdomTF = TransformBroadcaster(self)
    self.pub_pose = self.create_publisher(Pose, 'pose', 10)

    # Set Periodic data
    self.ph.incomming_info = ['ODO', 'VW', "POSE", "GYRO"]
    self.ph.update_battery_state()
    #self.ph.set_periodic_info()
    sleep(0.01)
    self.ph.set_periodic_info(50)
    
    # Set timer proc
    self.timerProc = self.create_timer(0.01, self.update_robot)

    # def __del__(self):
    #   self.destroy_timer(self.timerProc)

  def convert2odo_from_each_wheel(self, enc_l, enc_r):
    return enc_l * self.distance_per_pulse, enc_r * self.distance_per_pulse

  def update_odometry(self, odo_l, odo_r, trans_vel, orient_vel, vel_z):
    odo_l /= 1000.
    odo_r /= 1000.
    trans_vel /= 1000.
    orient_vel /= 1000.

    self.odom_pose.timestamp = self.get_clock().now()
    dt = (self.odom_pose.timestamp - self.odom_pose.pre_timestamp).nanoseconds * 1e-9
    self.odom_pose.pre_timestamp = self.odom_pose.timestamp

    if self.use_gyro:
        self.calc_yaw.wheel_ang += orient_vel * dt
        self.odom_pose.theta = self.calc_yaw.calc_filter(vel_z*math.pi/180., dt)
        self.get_logger().info('R1mini state : whl pos %1.2f, %1.2f, gyro : %1.2f, whl odom : %1.2f, robot theta : %1.2f' 
                    %(odo_l, odo_r, vel_z,
                    self.calc_yaw.wheel_ang*180/math.pi, 
                    self.d_odom_pose['theta']*180/math.pi ))
    else:
        self.odom_pose.theta += orient_vel * dt

    d_x = trans_vel * math.cos(self.odom_pose.theta) 
    d_y = trans_vel * math.sin(self.odom_pose.theta) 
    self.odom_pose.x += d_x * dt
    self.odom_pose.y += d_y * dt
    #print('ODO L:%.2f, R:%.2f, V:%.2f, W=%.2f --> X:%.2f, Y:%.2f, Theta:%.2f'
    #  %(odo_l, odo_r, trans_vel, orient_vel, 
    #  self.odom_pose.x,self.odom_pose.y,self.odom_pose.theta))
    q = quaternion_from_euler(0, 0, self.odom_pose.theta)

    self.odom_vel.x = trans_vel
    self.odom_vel.y = 0.
    self.odom_vel.w = orient_vel

    timestamp_now = self.get_clock().now().to_msg()
    # Set odometry data
    odom = Odometry()
    odom.header.frame_id = "odom"
    odom.child_frame_id = "base_footprint"
    odom.header.stamp = timestamp_now
    odom.pose.pose.position.x = self.odom_pose.x
    odom.pose.pose.position.y = self.odom_pose.y
    odom.pose.pose.position.z = 0.0
    odom.pose.pose.orientation.x = q[0]
    odom.pose.pose.orientation.y = q[1]
    odom.pose.pose.orientation.z = q[2]
    odom.pose.pose.orientation.w = q[3]

    odom.twist.twist.linear.x = trans_vel
    odom.twist.twist.linear.y = 0.0
    odom.twist.twist.angular.z = orient_vel

    self.pub_Odom.publish(odom)

    # Set odomTF data
    odom_tf = TransformStamped()
    odom_tf.header.frame_id = odom.header.frame_id
    odom_tf.child_frame_id = odom.child_frame_id
    odom_tf.header.stamp = timestamp_now

    odom_tf.transform.translation.x = odom.pose.pose.position.x
    odom_tf.transform.translation.y = odom.pose.pose.position.y
    odom_tf.transform.translation.z = odom.pose.pose.position.z
    odom_tf.transform.rotation = odom.pose.pose.orientation
    self.pub_OdomTF.sendTransform(odom_tf)

  def updatePoseStates(self, roll, pitch, yaw):
    #Added to publish pose orientation of IMU
    pose = Pose()
    pose.orientation.x = roll
    pose.orientation.y = pitch
    pose.orientation.z = yaw
    self.pub_pose.publish(pose)

  def updateJointStates(self, odo_l, odo_r, trans_vel, orient_vel):
    odo_l /= 1000.
    odo_r /= 1000.

    wheel_ang_left = odo_l / self.wheel_radius
    wheel_ang_right = odo_r / self.wheel_radius

    wheel_ang_vel_left = (trans_vel - (self.wheel_separation / 2.0) * orient_vel) / self.wheel_radius
    wheel_ang_vel_right = (trans_vel + (self.wheel_separation / 2.0) * orient_vel) / self.wheel_radius

    self.joint.joint_pos = [wheel_ang_left, wheel_ang_right]
    self.joint.joint_vel = [wheel_ang_vel_left, wheel_ang_vel_right]
    
    timestamp_now = self.get_clock().now().to_msg()

    joint_states = JointState()
    joint_states.header.frame_id = "base_link"
    joint_states.header.stamp = timestamp_now
    joint_states.name = self.joint.joint_name
    joint_states.position = self.joint.joint_pos
    joint_states.velocity = self.joint.joint_vel
    joint_states.effort = []
    self.pub_JointStates.publish(joint_states)

  def update_robot(self):
    #raw_data = self.ph.parser()
    self.ph.read_packet()
    odo_l = self.ph._wodom[0]
    odo_r = self.ph._wodom[1]
    trans_vel = self.ph._vel[0]
    orient_vel = self.ph._vel[1]
    vel_z = self.ph._gyro[2]
    roll_imu = self.ph._imu[0]
    pitch_imu = self.ph._imu[1]
    yaw_imu = self.ph._imu[2]

    self.update_odometry(odo_l, odo_r, trans_vel, orient_vel, vel_z)
    self.updateJointStates(odo_l, odo_r, trans_vel, orient_vel)
    self.updatePoseStates(roll_imu, pitch_imu, yaw_imu)

  def cbCmdVelMsg(self, cmd_vel_msg):
    lin_vel_x = cmd_vel_msg.linear.x
    ang_vel_z = cmd_vel_msg.angular.z

    lin_vel_x = max(-self.max_lin_vel_x, min(self.max_lin_vel_x, lin_vel_x))
    ang_vel_z = max(-self.max_ang_vel_z, min(self.max_ang_vel_z, ang_vel_z))
    #print("CMD_VEL V_x:%s m/s, Rot_z:%s deg/s"%(lin_vel_x, ang_vel_z))
    self.ph.write_base_velocity(lin_vel_x*1000, ang_vel_z*1000)

  def cbSrv_headlight(self, request, response):
    onoff = '0'
    if request.set == True:
      onoff = '1'
      #self.d_setHDLT['switch'] = 1
    #else:
    #  self.d_setHDLT['switch'] = 0
    command = "$cHDLT," + onoff
    self.ph.write_port(command)
    print('SERVICE: Headlight: %s'%(onoff))
    return response
  
  def cbSrv_setColor(self, request, response):
    command = "$cCOLOR,"+str(request.red) + ','+str(request.green) + ','+str(request.blue)
    print("SERVICE: SET COLOR: R(%s)G(%s)B(%s)"
      %(request.red, request.green, request.blue))
    #self.packet.write_data('COLOR', self.d_setCOLOR)
    return response

  def cbSrv_checkBattery(self, request, response):
    self.ph.update_battery_state()
    #bat_status = self.ph.robot_state['BAT']
    bat_status = self.ph.get_battery_status()
    if len(bat_status) == 3:
      print("SERVICE: Battery V:%s, SOC: %s, Current %s"
            %(bat_status[0], bat_status[1], bat_status[2]))
      response.volt  = bat_status[0]*0.1
      response.soc = bat_status[1]
      response.current = bat_status[2]*0.001
      return response

  def cbSrv_resetODOM(self, request, response):
    self.odom_pose.x = request.x
    self.odom_pose.y = request.y
    self.odom_pose.theta = request.theta
    print("SERVICE: RESET ODOM X:%s, Y:%s, Theta:%s"%
        (request.x, request.y, request.theta))
    return response
  
  def cbSrv_setBuzzer(self, request, response):
    onoff = '0'
    if request.set == True:
        onoff = '1'
    command = "$sBUZEN," + onoff
    print("SERVICE: SET BUZZER : %s"%(onoff))
    self.ph.write_port(command)
    return OnoffResponse()

  def calibrate_gyro(self, request):
    command = "$sCALG,1"
    printf("SERVICE: CALIBRATE GYRO")
    self.ph.write_port(command)
    return CalgResponse()

def main(args=None):
  rclpy.init(args=args)
  omoR1MiniNode = OMOR1MiniNode()
  rclpy.spin(omoR1MiniNode)

  omoR1MiniNode.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
