# generated from rosidl_generator_py/resource/_idl.py.em
# with input from omo_r1mini_interfaces:srv/Onoff.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Onoff_Request(type):
    """Metaclass of message 'Onoff_Request'."""

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
                'omo_r1mini_interfaces.srv.Onoff_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__onoff__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__onoff__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__onoff__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__onoff__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__onoff__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Onoff_Request(metaclass=Metaclass_Onoff_Request):
    """Message class 'Onoff_Request'."""

    __slots__ = [
        '_set',
    ]

    _fields_and_field_types = {
        'set': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.set = kwargs.get('set', bool())

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
        if self.set != other.set:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property  # noqa: A003
    def set(self):  # noqa: A003
        """Message field 'set'."""
        return self._set

    @set.setter  # noqa: A003
    def set(self, value):  # noqa: A003
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'set' field must be of type 'bool'"
        self._set = value


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_Onoff_Response(type):
    """Metaclass of message 'Onoff_Response'."""

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
                'omo_r1mini_interfaces.srv.Onoff_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__onoff__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__onoff__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__onoff__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__onoff__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__onoff__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Onoff_Response(metaclass=Metaclass_Onoff_Response):
    """Message class 'Onoff_Response'."""

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


class Metaclass_Onoff(type):
    """Metaclass of service 'Onoff'."""

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
                'omo_r1mini_interfaces.srv.Onoff')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__onoff

            from omo_r1mini_interfaces.srv import _onoff
            if _onoff.Metaclass_Onoff_Request._TYPE_SUPPORT is None:
                _onoff.Metaclass_Onoff_Request.__import_type_support__()
            if _onoff.Metaclass_Onoff_Response._TYPE_SUPPORT is None:
                _onoff.Metaclass_Onoff_Response.__import_type_support__()


class Onoff(metaclass=Metaclass_Onoff):
    from omo_r1mini_interfaces.srv._onoff import Onoff_Request as Request
    from omo_r1mini_interfaces.srv._onoff import Onoff_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
