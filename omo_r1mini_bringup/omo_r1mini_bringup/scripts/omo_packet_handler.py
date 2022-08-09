#!/usr/bin/env python

import serial
import io
from time import sleep

class PacketHandler:
   def __init__(self, _port_name, _baud_rate):
      self.port_name = _port_name
      self.baud_rate = _baud_rate
      self._ser = serial.Serial(self.port_name, self.baud_rate)
      self._ser_io = io.TextIOWrapper(io.BufferedRWPair(self._ser, self._ser, 1), 
                                       newline = '\r', 
                                       line_buffering = True)
      #self.write_periodic_query_enable(0)
      self._ser.flushInput()
      self._ser.reset_input_buffer()
      self._ser.reset_output_buffer()
      self.incomming_info = ['ODO', 'VW', 'POSE', 'ACCL', 'GYRO']
      self._vel = [0.0, 0.0]
      self._enc = [0.0, 0.0]
      self._wodom = [0.0, 0.0]
      self._rpm = [0.0, 0.0]
      self._wvel = [0.0, 0.0]
      self._gyro = [0.0, 0.0, 0.0]
      self._imu = [0.0, 0.0, 0.0]
      self._battery = [0.0, 0.0, 0.0]

   def set_periodic_info(self, param1):
      for idx, each in enumerate(self.incomming_info):
         #print("$cREGI," + str(idx) + "," + each)
         self.write_port("$cREGI," + str(idx) + "," + each)

      self.write_port("$cPERI," + str(param1))
      sleep(0.01)
      self.write_periodic_query_enable(1)

   def get_port_state(self):
      return self._ser.isOpen()
      
   def read_port(self):
      return self._rl.readline()

   def close_port(self):
      print("Port close")
      self._ser.close()

   def read_packet(self):
      if self.get_port_state() == True:
         whole_packet = (self._ser.readline().split(b'\r')[0]).decode("utf-8").strip()
         if whole_packet:
            #print(whole_packet)
            packet = whole_packet.split(',')
            try:
               header = packet[0].split('#')[1]
               if header.startswith('VW'):
                  self._vel = [float(packet[1]), float(packet[2])]
               elif header.startswith('ENCOD'):
                  self._enc = [int(packet[1]), int(packet[2])]
               elif header.startswith('ODO'):
                  self._wodom = [float(packet[1]), float(packet[2])]
               elif header.startswith('RPM'):
                  self._rpm = [int(packet[1]), int(packet[2])]
               elif header.startswith('DIFFV'):
                  self._wvel = [int(packet[1]), int(packet[2])]
               elif header.startswith('GYRO'):
                  self._gyro = [float(packet[1]), float(packet[2]), float(packet[3])]
               elif header.startswith('POSE'):
                  self._imu = [float(packet[1]), float(packet[2]), float(packet[3])]
               elif header.startswith('BAT'):
                  self._battery = [float(packet[1]), float(packet[2]), float(packet[3])]
            except:
               pass
   
   def update_battery_state(self):
      self.write_port("$qBAT")
      sleep(0.01)

   def get_base_velocity(self):
      return self._vel

   def get_wheel_encoder(self):
      return self._enc

   def get_wheel_odom(self):
      return self._wodom

   def get_wheel_rpm(self):
      return self._rpm

   def get_wheel_velocity(self):
      return self._wvel

   def get_battery_status(self):
      return self._battery

   def write_periodic_query_enable(self, param):
      self.write_port("$cPEEN," + str(param))
      sleep(0.05)

   def write_odometry_reset(self):
      self.write_port("$cODO,0")
      sleep(0.05)

   def write_base_velocity(self, lin_vel, ang_vel):
      # lin_vel : mm/s, ang_vel : mrad/s
      self.write_port('$CVW,{:.0f},{:.0f}'.format(lin_vel, ang_vel))

   def write_wheel_velocity(self, wheel_l_lin_vel, wheel_r_lin_vel):
      self.write_port('$CDIFFV,{:.0f},{:.0f}'.format(wheel_l_lin_vel, wheel_r_lin_vel))

   def write_port(self, buffer):
      if self.get_port_state() == True:
         self._ser.write((buffer + "\r\n").encode())