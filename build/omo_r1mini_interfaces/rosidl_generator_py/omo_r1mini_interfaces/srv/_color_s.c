// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from omo_r1mini_interfaces:srv/Color.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "omo_r1mini_interfaces/srv/detail/color__struct.h"
#include "omo_r1mini_interfaces/srv/detail/color__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool omo_r1mini_interfaces__srv__color__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[47];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("omo_r1mini_interfaces.srv._color.Color_Request", full_classname_dest, 46) == 0);
  }
  omo_r1mini_interfaces__srv__Color_Request * ros_message = _ros_message;
  {  // red
    PyObject * field = PyObject_GetAttrString(_pymsg, "red");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->red = PyLong_AsLongLong(field);
    Py_DECREF(field);
  }
  {  // green
    PyObject * field = PyObject_GetAttrString(_pymsg, "green");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->green = PyLong_AsLongLong(field);
    Py_DECREF(field);
  }
  {  // blue
    PyObject * field = PyObject_GetAttrString(_pymsg, "blue");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->blue = PyLong_AsLongLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * omo_r1mini_interfaces__srv__color__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Color_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("omo_r1mini_interfaces.srv._color");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Color_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  omo_r1mini_interfaces__srv__Color_Request * ros_message = (omo_r1mini_interfaces__srv__Color_Request *)raw_ros_message;
  {  // red
    PyObject * field = NULL;
    field = PyLong_FromLongLong(ros_message->red);
    {
      int rc = PyObject_SetAttrString(_pymessage, "red", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // green
    PyObject * field = NULL;
    field = PyLong_FromLongLong(ros_message->green);
    {
      int rc = PyObject_SetAttrString(_pymessage, "green", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // blue
    PyObject * field = NULL;
    field = PyLong_FromLongLong(ros_message->blue);
    {
      int rc = PyObject_SetAttrString(_pymessage, "blue", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "omo_r1mini_interfaces/srv/detail/color__struct.h"
// already included above
// #include "omo_r1mini_interfaces/srv/detail/color__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool omo_r1mini_interfaces__srv__color__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[48];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("omo_r1mini_interfaces.srv._color.Color_Response", full_classname_dest, 47) == 0);
  }
  omo_r1mini_interfaces__srv__Color_Response * ros_message = _ros_message;
  ros_message->structure_needs_at_least_one_member = 0;

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * omo_r1mini_interfaces__srv__color__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Color_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("omo_r1mini_interfaces.srv._color");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Color_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  (void)raw_ros_message;

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
