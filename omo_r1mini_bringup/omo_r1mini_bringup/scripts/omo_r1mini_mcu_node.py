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
    # Get parameter values
    _port_name = self.get_parameter_or('/port/name', Parameter('/port/name', Parameter.Type.STRING, '/dev/ttyTHS1')).get_parameter_value().string_value
    _port_baudrate = self.get_parameter_or('/port/baudrate', Parameter('/port/baudrate', Parameter.Type.INTEGER, 115200)).get_parameter_value().integer_value

    self.gear_ratio = self.get_parameter_or('/motor/gear_ratio', Parameter('/motor/gear_ratio', Parameter.Type.INTEGER, 213)).get_parameter_value().integer_value
    self.wheel_separation = self.get_parameter_or('/wheel/separation', Parameter('/wheel/separation', Parameter.Type.DOUBLE, 0.17)).get_parameter_value().double_value # 0.085 cm x 2
    self.wheel_radius = self.get_parameter_or('/wheel/radius', Parameter('/wheel/radius', Parameter.Type.DOUBLE, 0.0335)).get_parameter_value().double_value
    self.enc_pulse = self.get_parameter_or('/sensor/enc_pulse', Parameter('/sensor/enc_pulse', Parameter.Type.INTEGER, 44)).get_parameter_value().integer_value
    self.use_gyro = self.get_parameter_or('/sensor/use_gyro', Parameter('/sensor/use_gyro', Parameter.Type.BOOL, False)).get_parameter_value().bool_value
    self.distance_per_pulse = 2*math.pi*self.wheel_radius / self.enc_pulse / self.gear_ratio

    # Packet handler
    self.ph = PacketHandler(_port_name, _port_baudrate)
    self.ph.ser.reset_input_buffer() 
    self.ph.ser.reset_output_buffer() 
    self.ph.stop_periodic_comm()
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
    self.max_lin_vel_x = self.get_parameter_or('/motor/max_lin_vel_x', 
                Parameter('/motor/max_lin_vel_x', Parameter.Type.DOUBLE, 1.2)).get_parameter_value().double_value#rospy.get_param("~max_lin_vel_x")
    self.max_ang_vel_z = self.get_parameter_or('/motor/max_ang_vel_z', 
                Parameter('/motor/max_ang_vel_z', Parameter.Type.DOUBLE, 2.5)).get_parameter_value().double_value#rospy.get_param("~max_ang_vel_z")
    self.odom_pose = OdomPose()
    self.odom_pose.timestamp = self.get_clock().now()
    self.odom_pose.pre_timestamp = self.get_clock().now()
    self.odom_vel = OdomVel()
    self.joint = Joint()
  
    # Services
    self.srvHeadlight = self.create_service(Onoff, 'set_headlight', self.cbSrv_headlight)
    self.srvSetColor = self.create_service(Color, 'set_rgbled', self.cbSrv_setColor)
    self.srvResetODOM = self.create_service(Onoff, 'reset_odom', self.cbSrv_resetODOM)
    self.srvCheckBAT = self.create_service(Battery, 'check_battery', self.cbSrv_checkBattery)

    # Init data
    self.d_odom_pose = \
    {
      'x': 0.0,
      'y': 0.0,
      'theta': 0.0,
      'time_now': self.get_clock().now(),
      'time_prev': self.get_clock().now()
    }

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
    self.ph.set_periodic_info()
    sleep(0.1)
    self.ph.set_periodic_info()
    
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
        #self.d_odom_pose['theta'] += orient_vel * dt
        self.odom_pose.theta += orient_vel * dt
        #rospy.loginfo('R1mini state : wheel pos %s, %s, speed %s, %s',
        #                odo_l, odo_r, trans_vel, orient_vel)

    d_x = trans_vel * math.cos(self.odom_pose.theta) 
    d_y = trans_vel * math.sin(self.odom_pose.theta) 
    self.odom_pose.x += d_x * dt
    self.odom_pose.y += d_y * dt
    self.get_logger().info('ODO X:%s, Y:%s, Theta:%s'
        %(self.odom_pose.x,self.odom_pose.y,self.odom_pose.theta))
    odom_orientation_quat = quaternion_from_euler(0, 0, self.odom_pose.theta)

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
    raw_data = self.ph.parser()
    try:
      [trans_vel, orient_vel] = self.ph.robot_state['VW']
      [odo_l, odo_r] = self.ph.robot_state['ODO']
      [vel_x, vel_y, vel_z] = self.ph.robot_state['GYRO']
      [acc_x, acc_y, acc_z] = self.ph.robot_state['ACCL']
      [roll_imu, pitch_imu, yaw_imu] = self.ph.robot_state['POSE']

      self.update_odometry(odo_l, odo_r, trans_vel, orient_vel, vel_z)
      self.updateJointStates(odo_l, odo_r, trans_vel, orient_vel)
      self.updatePoseStates(roll_imu, pitch_imu, yaw_imu)
        
    except ValueError:
      self.get_logger().info("ValueError occupied during read robot status in update_robot state. \n\r Raw_data : %s"
                  %(raw_data))

  def cbSrv_headlight(self, request, response):
    onoff = 0
    if request.set == True:
      onoff = 1
      self.d_setHDLT['switch'] = 1
    else:
      self.d_setHDLT['switch'] = 0
    #command = "$cHDLT," + onoff
    self.get_logger().info('Service call Headlight:%s'%(onoff))
    self.packet.write_data('HDLT', self.d_setHDLT)
    return response
  
  def cbSrv_setColor(self, request, response):
    self.d_setCOLOR['red'] = request.red
    self.d_setCOLOR['green'] = request.green
    self.d_setCOLOR['blue'] = request.blue
    self.get_logger().info("SET COLOR R(%s)G(%s)B(%s)"
      %(request.red, request.green, request.blue))
    self.packet.write_data('COLOR', self.d_setCOLOR)
    return response

  def cbSrv_checkBattery(self, request, response):
    self.d_getBAT = self.packet.read_data('BAT')
    self.get_logger().info("Battery V:%s, SOC: %s, Current %s"
      %(self.d_getBAT['voltage'], self.d_getBAT['soc'], self.d_getBAT['current_hour']))
    response.volt = float(self.d_getBAT['voltage'])/10.0
    response.soc = float(self.d_getBAT['soc'])
    response.current = float(self.d_getBAT['current_hour'])
    return response

  def cbSrv_resetODOM(self, request, response):
    if request.set == True:
      self.packet.write_data('ODO', self.d_setODO)
      self.get_logger().info('RESET ODO')
    return response
  
  def cbSrv_setBuzzer(self, request, response):
    onoff = '0'
    if request.set == True:
        onoff = '1'
    command = "$sBUZEN," + onoff
    self.ph.write_port(command)
    return OnoffResponse()

  def calibrate_gyro(self, req):
    command = "$sCALG,1"
    self.ph.write_port(command)
    return CalgResponse()
      
  def cbCmdVelMsg(self, cmd_vel_msg):
    lin_vel_x = cmd_vel_msg.linear.x
    ang_vel_z = cmd_vel_msg.angular.z

    lin_vel_x = max(-self.max_lin_vel_x, min(self.max_lin_vel_x, lin_vel_x))
    ang_vel_z = max(-self.max_ang_vel_z, min(self.max_ang_vel_z, ang_vel_z))

    self.ph.set_wheel_velocity(lin_vel_x*1000, ang_vel_z*1000)
    #self.d_target_twist['linear'] = int(msg.linear.x * 1000)
    #self.d_target_twist['angular'] = int(msg.angular.z * 1000)

  def cbTimerProc(self):
    a = self.get_clock().now()
    # write data to mcu
    self.packet.write_data('VW', self.d_target_twist)
    # self.packet.write_data('VW', {'linear': 0.070162236 * 1000.0, 'angular': 0.0  * 1000.0}) # 0.070162236 -> 20 rpm
    # self.packet.write_data('VW', {'linear': 0.0 * 1000.0, 'angular': 1.570796327  * 1000.0}) # 1570.796327 -> pi/2 rad / sec
    # self.packet.write_data('RPM', {'left': -38.059701493, 'right':38.059701493})

    # read data from mcu
    self.d_current_gyro = self.packet.read_data('GYRO')
    self.d_current_gyro['yaw_per_s'] = float(self.d_current_gyro['yaw_per_s']) * 1.017524025 # TODO:: solve the bias problem
    self.d_current_accl = self.packet.read_data('ACCL')
    self.d_current_pose = self.packet.read_data('POSE')
    self.d_current_odo = self.packet.read_data('ODO')
    self.d_current_diffv = self.packet.read_data('DIFFV')
    self.d_current_twist = self.packet.read_data('VW')
    self.d_current_twist['linear'] = float(self.d_current_twist['linear']) * 0.99009901 # TODO:: solve the bias problem
    self.d_current_twist['angular'] = float(self.d_current_twist['angular']) * 0.991337255 # TODO:: solve the bias problem
    ########################
    # max 23 msec until here
    ########################
    
    # update datas(for publish : odom, joint state, etc)
    self.fnPubSensorData()
    b = self.get_clock().now()
    #self.get_logger().info('looptime : %s' % (b-a).nanoseconds)
    
    ########################
    # needs to be done in 45 msec until here (reserve 5 msec for meeting 50 msec control interval)
    ########################

  def fnPubSensorData(self):
    # Odometry calculation
    # Time check
    self.d_odom_pose['now_time'] = self.get_clock().now()
    dt = (self.d_odom_pose['now_time'] - self.d_odom_pose['prev_time']).nanoseconds * 1e-9
    self.d_odom_pose['prev_time'] = self.d_odom_pose['now_time']

    # Linear delta calculation    
    ds = float(self.d_current_twist['linear']) * dt * 1e-3

    # Angular delta calculation
    dtheta = float(self.d_current_gyro['yaw_per_s']) * math.pi * dt / 180.0
    self.d_odom_pose['theta'] += dtheta

    dx = ds * math.cos(self.d_odom_pose['theta'] + (dtheta / 2.0))# * dt
    dy = ds * math.sin(self.d_odom_pose['theta'] + (dtheta / 2.0))# * dt
    self.d_odom_pose['x'] += dx
    self.d_odom_pose['y'] += dy

    timestamp_now = self.get_clock().now().to_msg()
    # Set odometry data
    odom_msg = Odometry()
    odom_msg.header.frame_id = 'odom'
    odom_msg.child_frame_id = 'base_footprint'
    odom_msg.header.stamp = timestamp_now

    odom_msg.pose.pose.position.x = self.d_odom_pose['x']
    odom_msg.pose.pose.position.y = self.d_odom_pose['y']
    odom_msg.pose.pose.position.z = 0.0

    q = quaternion_from_euler(0.0, 0.0, self.d_odom_pose['theta'])
    odom_msg.pose.pose.orientation.x = q[0]
    odom_msg.pose.pose.orientation.y = q[1]
    odom_msg.pose.pose.orientation.z = q[2]
    odom_msg.pose.pose.orientation.w = q[3]
    
    odom_msg.twist.twist.linear.x = ds / dt
    odom_msg.twist.twist.linear.y = 0.0
    odom_msg.twist.twist.angular.z = dtheta / dt
    self.pubOdom.publish(odom_msg)

    # Set odomTF data
    odom_tf = TransformStamped()
    odom_tf.header.frame_id = odom_msg.header.frame_id
    odom_tf.child_frame_id = odom_msg.child_frame_id
    odom_tf.header.stamp = timestamp_now

    odom_tf.transform.translation.x = odom_msg.pose.pose.position.x
    odom_tf.transform.translation.y = odom_msg.pose.pose.position.y
    odom_tf.transform.translation.z = odom_msg.pose.pose.position.z
    odom_tf.transform.rotation = odom_msg.pose.pose.orientation
    self.pubOdomTF.sendTransform(odom_tf)

    # Set imu data
    imu_msg = Imu()
    imu_msg.header.frame_id = 'imu_link'
    imu_msg.header.stamp = timestamp_now
    
    imu_msg.orientation.w = q[0]
    imu_msg.orientation.x = q[1]
    imu_msg.orientation.y = q[2]
    imu_msg.orientation.z = q[3]
    # imu_msg.orientation_covariance[0] = 0.0025;
    # imu_msg.orientation_covariance[1] = 0;
    # imu_msg.orientation_covariance[2] = 0;
    # imu_msg.orientation_covariance[3] = 0;
    # imu_msg.orientation_covariance[4] = 0.0025;
    # imu_msg.orientation_covariance[5] = 0;
    # imu_msg.orientation_covariance[6] = 0;
    # imu_msg.orientation_covariance[7] = 0;
    # imu_msg.orientation_covariance[8] = 0.0025;
    imu_msg.angular_velocity.x = float(self.d_current_gyro['roll_per_s']) * math.pi / 180.0
    imu_msg.angular_velocity.y = float(self.d_current_gyro['pitch_per_s']) * math.pi / 180.0
    imu_msg.angular_velocity.z = float(self.d_current_gyro['yaw_per_s']) * math.pi / 180.0
    # imu_msg.angular_velocity_covariance[0] = 0.02;
    # imu_msg.angular_velocity_covariance[1] = 0;
    # imu_msg.angular_velocity_covariance[2] = 0;
    # imu_msg.angular_velocity_covariance[3] = 0;
    # imu_msg.angular_velocity_covariance[4] = 0.02;
    # imu_msg.angular_velocity_covariance[5] = 0;
    # imu_msg.angular_velocity_covariance[6] = 0;
    # imu_msg.angular_velocity_covariance[7] = 0;
    # imu_msg.angular_velocity_covariance[8] = 0.02;
    imu_msg.linear_acceleration.x = float(self.d_current_accl['a_x'])
    imu_msg.linear_acceleration.y = float(self.d_current_accl['a_y'])
    imu_msg.linear_acceleration.z = -float(self.d_current_accl['a_z_inversed'])
    # imu_msg.linear_acceleration_covariance[0] = 0.04;
    # imu_msg.linear_acceleration_covariance[1] = 0;
    # imu_msg.linear_acceleration_covariance[2] = 0;
    # imu_msg.linear_acceleration_covariance[3] = 0;
    # imu_msg.linear_acceleration_covariance[4] = 0.04;
    # imu_msg.linear_acceleration_covariance[5] = 0;
    # imu_msg.linear_acceleration_covariance[6] = 0;
    # imu_msg.linear_acceleration_covariance[7] = 0;
    # imu_msg.linear_acceleration_covariance[8] = 0.04;
    self.pubIMU.publish(imu_msg)

    # Set jointstates data
    joint_state_msg = JointState()
    joint_state_msg.header.frame_id = 'base_link'
    joint_state_msg.header.stamp = timestamp_now

    joint_state_msg.name = ['wheel_left_joint', 'wheel_right_joint']

    now_pos = [float(self.d_current_odo['left']) * 1e-3 / (self.wheel_radius) * 1.372495196, float(self.d_current_odo['right']) * 1e-3 / (self.wheel_radius) * 1.372495196] # TODO: Remove bias : 1.372495196
    joint_state_msg.position = now_pos

    joint_state_msg.velocity = [float(self.d_current_diffv['left']), float(self.d_current_diffv['right'])]
    self.pubJointStates.publish(joint_state_msg)

def main(args=None):
  rclpy.init(args=args)
  omoR1MiniNode = OMOR1MiniNode()
  rclpy.spin(omoR1MiniNode)

  omoR1MiniNode.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
