#!/usr/bin/env python3

# Author: Bishop Pearson

import serial
import io
from time import sleep

class Port:
  def __init__(self, port_name='/dev/ttyTHS1', baudrate=115200):
    self.set_port_name(port_name)
    self.set_baudrate(baudrate)

    self.ser = None
    self.open_port()

  def __del__(self):
    self.close_port()

  def get_port_name(self):
    return self.port_name
  def set_port_name(self, port_name=None):
    self.port_name = port_name

  def get_baudrate(self):
    return self.baudrate
  def set_baudrate(self, baudrate=None):
    self.baudrate = baudrate

  def open_port(self, port_name=None, baudrate=None):
    _port_name = self.get_port_name()
    _baudrate = self.get_baudrate()

    if port_name != None:
      _port_name = port_name

    if baudrate != None:
      _baudrate = baudrate

    self.close_port()
    self.ser = serial.Serial(_port_name, _baudrate)

  def close_port(self):
    if self.ser != None:
      if self.ser.isOpen():
        self.ser.close()

  def read_port(self):
    _res = 0
    if self.ser != None:
      if self.ser.isOpen():
        _res = self.ser.readline()

    return _res
      
  def write_port(self, buf):
    _res = 0
    if self.ser != None:
      if self.ser.isOpen():
        _res = self.ser.write(buf)
    
    return _res

  def clear_port(self):
    if self.ser != None:
      if self.ser.isOpen():
        self.ser.flush()