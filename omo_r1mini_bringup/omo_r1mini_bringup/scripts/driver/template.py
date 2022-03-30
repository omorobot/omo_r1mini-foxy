#!/usr/bin/env python3

# Author: Bishop Pearson

template_write_ = \
{
  'VW': # Twist control
  {
    'type':'c',
    'len':2, # Linear [mm/s], Angular [mrad/s]
    'data':
    {
      'linear':None,
      'angular':None
    }
  },
  'DIFFV': # Velocity control
  {
    'type':'c',
    'len':2, # Left, Right [mm/s]
    'data':
    {
      'left':None,
      'right':None
    }
  },
  'RPM': # RPM control
  {
    'type':'c',
    'len':2, # Left, Right [RPM]
    'data':
    {
      'left':None,
      'right':None
    }
  },
  'ENCOD': # Encoder reset
  {
    'type':'c',
    'len':1, # 0: Reset
    'data':
    {
      'reset_encoder':None
    }
  },
  'ODO': # Odometry(Accumulated left, right wheel dist) reset
  {
    'type':'c',
    'len':1, # 0: Reset
    'data':
    {
      'reset_odometry':None
    }
  },
  'GYRO': # Gyroscope calibration
  {
    'type':'s',
    'len':1, # 1: do calibration
    'data':
    {
      'do_calibration':None
    }
    # TODO:: feedback exists
  },
  'COLOR': # LED Light control
  {
    'type':'c',
    # TODO:: 'c' mode exists
    'len':3, # R, G, B in range(0, 256)
    'data':
    {
      'red':None,
      'green':None,
      'blue':None
    }
  },
  'BREATH': # LED breath effect control
  {
    'type':'s',
    # TODO:: 'c' mode exists
    'len':3, # Interval [ms], On wait time length [ms], Off wait time length [ms]
    'data':
    {
      'interval':None,
      'on_wait_time_length':None,
      'off_wait_time_length':None
    }
  },
  'STROBE': # LED strobe effect control
  {
    'type':'c',
    'len':3, # Interval [ms], Blinking count [count], Repetition [count]
    'data':
    {
      'interval':None,
      'blinking_count':None,
      'repetition':None
    }
  },
  'GEAR': # Gear ratio feedback
  {
    'type':'s',
    'len':1, # Gear ratio
    'data':
    {
      'ratio':None
    }
  },
  'HDLT': # Head light control
  {
    'type':'c',
    'len':1, # 1: Turn on, 0: Turn off
    'data':
    {
      'switch':None
    }
  },
  'SAFEC': # Current safety control
  {
    'type':'s',
    'len':1, # Overcurrent limit [mA], 0: disable setting 
    'data':
    {
      'overcurrent_limit':None
    }
  },
  # TODO:: this needs PQR as well
  # 'FCTRST': # Current safety feedback
  # {
  #   'type':'s',
  #   'len':1, # 1: Factory reset
  # 'data':
  #   {
  #     'item1':None,
  #     'item2':None,
  #     'item3':None,
  #     'item4':None,
  #     'item5':None
  #   }
  # },
  'REGI':
  {
    'type':'c',
    'len':2, # Address 0~4, Command: keys, DUMMY
    'data':
    {
      'address':None,
      'cmd':None
    }
  },
  'PERI':
  {
    'type':'c',
    'len':1, # available period >= 20 (ms)
    'data':
    {
      'period':None
    }
  },
  'PEEN':
  {
    'type':'c',
    'len':1, # 0: stop comm, 1: start comm
    'data':
    {
      'do_comm':None
    }
  },
}

template_read_ = \
{
  'VW': # Twist feedback
  {
    'type':'q',
    'len':2, # Linear [mm/s], Angular [mrad/s]
    'data':
    {
      'linear':None,
      'angular':None,
      'err':''
    }
  },
  'DIFFV': # Velocity feedback
  {
    'type':'q',
    'len':2, # Left, Right [mm/s]
    'data':
    {
      'left':None,
      'right':None,
      'err':''
    }
  },
  'RPM': # RPM feedback
  {
    'type':'q',
    'len':2, # Left, Right [RPM]
    'data':
    {
      'left':None,
      'right':None,
      'err':''
    }
  },
  'ENCOD': # Encoder feedback
  {
    'type':'q',
    'len':2, # Left, Right [count]
    'data':
    {
      'left':None,
      'right':None,
      'err':''
    }
  },
  'ODO': # Odometry(Accumulated left, right wheel dist) feedback
  {
    'type':'q',
    'len':2, # Left, Right
    'data':
    {
      'left':None,
      'right':None,
      'err':''
    }
  },
  'BAT': # Battery status feedback
  {
    'type':'q',
    'len':3, # Voltage in x 10[V], SOC [%], Current hour [mAh]
    'data':
    {
      'voltage':None,
      'soc':None,
      'current_hour':None,
      'err':''
    }
  },
  'POSE': # Robot pose feedback
  {
    'type':'q',
    'len':3, # Roll [deg], Pitch [deg], Yaw[deg]
    'data':
    {
      'roll':None,
      'pitch':None,
      'yaw':None,
      'err':''
    }
  },
  'ACCL': # Accelerometer feedback
  {
    'type':'q',
    'len':3, # x axis [G], y axis [G], z axis inversed [G]
    'data':
    {
      'a_x':None,
      'a_y':None,
      'a_z_inversed':None,
      'err':''
    }
  },
  'GYRO': # Gyroscope feedback
  {
    'type':'q',
    'len':3, # Roll [deg/s], Pitch [deg/s], Yaw[deg/s]
    'data':
    {
      'roll_per_s':None,
      'pitch_per_s':None,
      'yaw_per_s':None,
      'err':''
    }
  },
  'COLOR': # LED Light feedback
  {
    'type':'q',
    'len':3, # R, G, B in range(0, 256)
    'data':
    {
      'red':None,
      'green':None,
      'blue':None,
      'err':''
    }
  },
  'BREATH': # LED breath effect feedback
  {
    'type':'q',
    'len':3, # Interval [ms], On wait time length [ms], Off wait time length [ms]
    'data':
    {
      'interval':None,
      'on_wait_time_length':None,
      'off_wait_time_length':None,
      'err':''
    }    
  },
  'STROBE': # LED strobe effect feedback
  {
    'type':'q',
    'len':3, # Interval [ms], Blinking count [count], Repetition [count]
    'data':
    {
      'interval':None,
      'blinking_count':None,
      'repetition':None,
      'err':''
    }
  },
  'GEAR': # Gear ratio feedback
  {
    'type':'q',
    'len':1, # Gear ratio
    'data':
    {
      'ratio':None,
      'err':''
    }
  },
  'HDLT': # Head light feedback
  {
    'type':'q',
    'len':1, # 1: Turn on, 0: Turn off
    'data':
    {
      'status':None,
      'err':''
    }
  },
  'SAFEC': # Current safety feedback
  {
    'type':'q',
    'len':1, # Overcurrent limit [mA]
    'data':
    {
      'overcurrent_limit':None,
      'err':''
    }
  },
  'REGI':
  {
    'type':'q',
    'len':5, # i.e. ENCOD, DUMMY, ODO, DUMMY, DUMMY
    'data':
    {
      'item1':None,
      'item2':None,
      'item3':None,
      'item4':None,
      'item5':None,
      'err':''
    }
  }
}

template_error_ = \
{
  'ok':'No error',
  'range?':'over range of write parameter',
  'param?':'parameter number is not same of intended',
  'unknown':'inappropriate command',
  'CSQ?':'not supported CSQ',
  'already':'already set in register',
  'PQR?':'command which is not supporting PQR',
  'current?':'overcurrent detected',
  'timeout':'movement timeout',
  'unavail?':'requested data is not supported'
}