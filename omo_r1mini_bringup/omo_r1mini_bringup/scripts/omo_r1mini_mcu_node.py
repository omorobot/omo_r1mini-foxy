import rclpy
from rclpy.node import Node
from rclpy.logging import get_logger
from rclpy.parameter import Parameter
from time import sleep
import time
import copy
import math
from geometry_msgs.msg import Twist, TransformStamped
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu, JointState
from tf2_ros import TransformBroadcaster

from .driver.packet import *
from .driver.port import *
from .driver.template import *
from .calc.quaternion_from_euler import *

class OMOR1MiniNode(Node):
  def __init__(self):
    super().__init__('omo_r1mini_motor_setting')

    # Get parameter values
    _port_name = self.get_parameter_or('/port/name', Parameter('/port/name', Parameter.Type.STRING, '/dev/ttyTHS1')).get_parameter_value().string_value
    _port_baudrate = self.get_parameter_or('/port/baudrate', Parameter('/port/baudrate', Parameter.Type.INTEGER, 115200)).get_parameter_value().integer_value

    self.motor_gear_ratio = self.get_parameter_or('/motor/gear_ratio', Parameter('/motor/gear_ratio', Parameter.Type.INTEGER, 213)).get_parameter_value().integer_value
    self.wheel_separation = self.get_parameter_or('/wheel/separation', Parameter('/wheel/separation', Parameter.Type.DOUBLE, 0.17)).get_parameter_value().double_value # 0.085 cm x 2
    self.wheel_radius = self.get_parameter_or('/wheel/radius', Parameter('/wheel/radius', Parameter.Type.DOUBLE, 0.0335)).get_parameter_value().double_value
    self.sensor_enc_pulse = self.get_parameter_or('/sensor/enc_pulse', Parameter('/sensor/enc_pulse', Parameter.Type.INTEGER, 44)).get_parameter_value().integer_value

    # Init data
    self.last_pos = [0.0, 0.0]
    self.d_odom_pose = \
    {
      'x': 0.0,
      'y': 0.0,
      'theta': 0.0,
      'now_time': self.get_clock().now(),
      'prev_time': self.get_clock().now()
    }

    self.packet = Packet(Port(_port_name, _port_baudrate))

    self.d_target_twist = copy.deepcopy(template_write_['VW']['data'])
    self.d_current_twist = copy.deepcopy(template_read_['VW']['data'])
    self.d_current_accl = copy.deepcopy(template_read_['ACCL']['data'])
    self.d_current_pose = copy.deepcopy(template_read_['POSE']['data'])
    self.d_current_gyro = copy.deepcopy(template_read_['GYRO']['data'])
    self.d_current_odo = copy.deepcopy(template_read_['ODO']['data'])
    self.d_current_diffv = copy.deepcopy(template_read_['DIFFV']['data'])


    # Set subscriber
    self.subCmdVelMsg = self.create_subscription(Twist, 'cmd_vel', self.cbCmdVelMsg, 10)

    # Set publisher
    self.pubJointStates = self.create_publisher(JointState, 'joint_states', 10)
    self.pubIMU = self.create_publisher(Imu, 'imu', 10)
    self.pubOdom = self.create_publisher(Odometry, 'odom', 10)
    self.pubOdomTF = TransformBroadcaster(self)

    # Set timer proc
    self.timerProc = self.create_timer(0.05, self.cbTimerProc)

  # def __del__(self):
  #   self.destroy_timer(self.timerProc)

  def cbCmdVelMsg(self, msg):
    self.d_target_twist['linear'] = int(msg.linear.x * 1000)
    self.d_target_twist['angular'] = int(msg.angular.z * 1000)

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
    self.get_logger().info('looptime : %s' % (b-a).nanoseconds)
    
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
