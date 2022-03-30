#!/usr/bin/env python3

# Author: Bishop Pearson

from .port import *
from .template import *

import serial
import io
from time import sleep
import time
import copy

class Packet:
  def __init__(self, port=None):
    # TODO :: if port is not filled
    self.port = port

  def __del__(self):
    self.port.close_port()

  def read_data(self, cmd):
    d = copy.deepcopy(template_read_[cmd]['data'])
    # prev_t = time.time()
    self.port.clear_port()
    self.port.write_port(('$' + template_read_[cmd]['type'] + cmd + '\r\n').encode())
    _ret = self.port.read_port().decode('utf-8')
    # aft_t = time.time()
    # (1) check if the buffer is feedback data
    # (2) check if it is succeeded to get full packet
    if _ret[0] == '#' and '\r\n' in _ret: 
      item = _ret[1:].replace('\r\n', '').split(',')
      # (3) check if the feedback is right data of which is requested
      if item[0] == cmd:
        for i in range (0, template_read_[cmd]['len']):
          d[list(template_read_[cmd]['data'])[i]] = item[i + 1]
      elif item[0] == 'ERR':
        d['err'] = item[1]
        
    # delta_t = aft_t - prev_t
    # print(delta_t)
    return d
      
  def write_data(self, cmd, argv_d):
    param_str = ''
    for i in range(0, template_write_[cmd]['len']):
      param_str += ',' + str(argv_d[list(template_write_[cmd]['data'])[i]])
    self.port.clear_port()
    self.port.write_port(('$' + template_write_[cmd]['type'] + cmd + param_str + '\r\n').encode())