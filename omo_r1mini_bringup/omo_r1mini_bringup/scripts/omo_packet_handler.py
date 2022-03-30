#!/usr/bin/env python
import rclpy
from rclpy.node import Node
from rclpy.logging import get_logger

import serial
#import rospy
import io
from time import sleep

class PacketHandler:
   def __init__(self, _port_name, _baud_rate):
      #port_name = rospy.get_param('~port', '/dev/ttyMotor')
      #baud_rate = rospy.get_param('~baud', 115200)
      #_port_name = self.get_parameter_or('/port/name', Parameter('/port/name', Parameter.Type.STRING, '/dev/ttyTHS1')).get_parameter_value().string_value
      #_port_baudrate = self.get_parameter_or('/port/baudrate', Parameter('/port/baudrate', Parameter.Type.INTEGER, 115200)).get_parameter_value().integer_value
      self.port_name = _port_name
      self.baud_rate = _baud_rate
      self.ser = serial.Serial(self.port_name, self.baud_rate)
      self.ser_io = io.TextIOWrapper(io.BufferedRWPair(self.ser, self.ser, 1), 
                                       newline = '\r', 
                                       line_buffering = True)

      self.stop_periodic_comm()
      self.ser.reset_input_buffer() 
      self.ser.reset_output_buffer() 

      self.robot_state = {
            "ENCOD" : [0., 0.],
            "VW" : [0., 0.],
            "ODO" : [0., 0.],
            "POSE" : [0.,0.,0.],
            "ACCL" : [0., 0., 0.],
            "GYRO" : [0., 0., 0.],
            "BAT" : [0., 0., 0.],
      }

      self.incomming_info = ['ODO', 'VW', 'POSE', 'ACCL', 'GYRO']
      print('Serial port: %s'%(self.port_name))
      #rospy.loginfo('Serial port: %s', _port_name)
      #rospy.loginfo('Serial baud rate: %s', _baud_rate)

   def get_port_state(self):
      return self.ser.isOpen()

   def read_port(self):
      try:
         return self.ser_io.readline()
      except UnicodeDecodeError:
         print('UnicodeDecodeError during serial comm. start byte')

   def write_port(self, buffer):
      if self.get_port_state() == True:
         self.ser.write((buffer + "\r\n").encode())
      else:
         print('Serial Port %s is not Opened in Writing process'%(self.port_name))

   def read_packet(self):
      if self.get_port_state() == True:
         return self.read_port()
      else:
         print('Serial Port %s is not Opened in Reading process'%(self.port_name))

   def update_battery_state(self):
      self.write_port("$qBAT")
      sleep(0.01)

   def parser(self):
      raw_data_o = self.read_packet()

      try:
         raw_data = raw_data_o.replace('\r', '')
         raw_data = raw_data.replace('\n', '')
         raw_data = raw_data.split('#')

         raw_data_split = raw_data[-1].split(',')
         key = raw_data_split[0]
      except AttributeError:
         #rospy.logwarn("AttributeError: 'NoneType' object has no attribute 'replace' : %s ")
         self.write_port("$cPEEN,1")

      if key in list(self.robot_state.keys()):
         try:
            self.robot_state[key] = [float(each) for each in raw_data_split[1:]]
         except ValueError:
            #rospy.logwarn("ValueError occupied in parser_R1mini. %s ", raw_data_o)
            self.write_port("$cPEEN,1")

      return raw_data_o

   def set_periodic_info(self):
      for idx, each in enumerate(self.incomming_info):
         #print("$cREGI," + str(idx) + "," + each)
         self.write_port("$cREGI," + str(idx) + "," + each)

      self.update_battery_state()
      self.write_port("$cPERI,100")
      sleep(0.01)
      self.write_port("$ENCOD,0")
      self.write_port("$cPEEN,1")
      sleep(0.01)
      self.write_port("$cPEEN,1")

   def stop_periodic_comm(self):
      self.write_port("$cPEEN,0")
      sleep(0.01)
      self.write_port("$cODO,0")
      sleep(0.01)

   def set_wheel_velocity(self, l_vel, r_vel):
      self.write_port('$cVW,{:.0f},{:.0f}'.format(l_vel, r_vel))

   def set_thrust_steer(self, thrust, steer):
      self.write_port('$cSVO,{:.0f},{:.0f}'.format(thrust, steer))