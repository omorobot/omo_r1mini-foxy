# generated from rosidl_generator_py/resource/_idl.py.em
# with input from omo_r1mini_interfaces:srv/SaveColor.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SaveColor_Request(type):
    """Metaclass of message 'SaveColor_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('omo_r1mini_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'omo_r1mini_interfaces.srv.SaveColor_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__save_color__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__save_color__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__save_color__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__save_color__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__save_color__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SaveColor_Request(metaclass=Metaclass_SaveColor_Request):
    """Message class 'SaveColor_Request'."""

    __slots__ = [
        '_red',
        '_green',
        '_blue',
    ]

    _fields_and_field_types = {
        'red': 'int64',
        'green': 'int64',
        'blue': 'int64',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int64'),  # noqa: E501
        rosidl_parser.definition.BasicType('int64'),  # noqa: E501
        rosidl_parser.definition.BasicType('int64'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.red = kwargs.get('red', int())
        self.green = kwargs.get('green', int())
        self.blue = kwargs.get('blue', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.red != other.red:
            return False
        if self.green != other.green:
            return False
        if self.blue != other.blue:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def red(self):
        """Message field 'red'."""
        return self._red

    @red.setter
    def red(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'red' field must be of type 'int'"
            assert value >= -9223372036854775808 and value < 9223372036854775808, \
                "The 'red' field must be an integer in [-9223372036854775808, 9223372036854775807]"
        self._red = value

    @property
    def green(self):
        """Message field 'green'."""
        return self._green

    @green.setter
    def green(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'green' field must be of type 'int'"
            assert value >= -9223372036854775808 and value < 9223372036854775808, \
                "The 'green' field must be an integer in [-9223372036854775808, 9223372036854775807]"
        self._green = value

    @property
    def blue(self):
        """Message field 'blue'."""
        return self._blue

    @blue.setter
    def blue(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'blue' field must be of type 'int'"
            assert value >= -9223372036854775808 and value < 9223372036854775808, \
                "The 'blue' field must be an integer in [-9223372036854775808, 9223372036854775807]"
        self._blue = value


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_SaveColor_Response(type):
    """Metaclass of message 'SaveColor_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('omo_r1mini_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'omo_r1mini_interfaces.srv.SaveColor_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__save_color__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__save_color__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__save_color__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__save_color__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__save_color__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SaveColor_Response(metaclass=Metaclass_SaveColor_Response):
    """Message class 'SaveColor_Response'."""

    __slots__ = [
    ]

    _fields_and_field_types = {
    }

    SLOT_TYPES = (
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)


class Metaclass_SaveColor(type):
    """Metaclass of service 'SaveColor'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('omo_r1mini_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'omo_r1mini_interfaces.srv.SaveColor')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__save_color

            from omo_r1mini_interfaces.srv import _save_color
            if _save_color.Metaclass_SaveColor_Request._TYPE_SUPPORT is None:
                _save_color.Metaclass_SaveColor_Request.__import_type_support__()
            if _save_color.Metaclass_SaveColor_Response._TYPE_SUPPORT is None:
                _save_color.Metaclass_SaveColor_Response.__import_type_support__()


class SaveColor(metaclass=Metaclass_SaveColor):
    from omo_r1mini_interfaces.srv._save_color import SaveColor_Request as Request
    from omo_r1mini_interfaces.srv._save_color import SaveColor_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
