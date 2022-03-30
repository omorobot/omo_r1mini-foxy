// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from omo_r1mini_interfaces:srv/Color.idl
// generated code does not contain a copyright notice
#include "omo_r1mini_interfaces/srv/detail/color__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "omo_r1mini_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "omo_r1mini_interfaces/srv/detail/color__struct.h"
#include "omo_r1mini_interfaces/srv/detail/color__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _Color_Request__ros_msg_type = omo_r1mini_interfaces__srv__Color_Request;

static bool _Color_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Color_Request__ros_msg_type * ros_message = static_cast<const _Color_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: red
  {
    cdr << ros_message->red;
  }

  // Field name: green
  {
    cdr << ros_message->green;
  }

  // Field name: blue
  {
    cdr << ros_message->blue;
  }

  return true;
}

static bool _Color_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Color_Request__ros_msg_type * ros_message = static_cast<_Color_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: red
  {
    cdr >> ros_message->red;
  }

  // Field name: green
  {
    cdr >> ros_message->green;
  }

  // Field name: blue
  {
    cdr >> ros_message->blue;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_omo_r1mini_interfaces
size_t get_serialized_size_omo_r1mini_interfaces__srv__Color_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Color_Request__ros_msg_type * ros_message = static_cast<const _Color_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name red
  {
    size_t item_size = sizeof(ros_message->red);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name green
  {
    size_t item_size = sizeof(ros_message->green);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name blue
  {
    size_t item_size = sizeof(ros_message->blue);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _Color_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_omo_r1mini_interfaces__srv__Color_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_omo_r1mini_interfaces
size_t max_serialized_size_omo_r1mini_interfaces__srv__Color_Request(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: red
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: green
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: blue
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _Color_Request__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_omo_r1mini_interfaces__srv__Color_Request(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_Color_Request = {
  "omo_r1mini_interfaces::srv",
  "Color_Request",
  _Color_Request__cdr_serialize,
  _Color_Request__cdr_deserialize,
  _Color_Request__get_serialized_size,
  _Color_Request__max_serialized_size
};

static rosidl_message_type_support_t _Color_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Color_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, omo_r1mini_interfaces, srv, Color_Request)() {
  return &_Color_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "omo_r1mini_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "omo_r1mini_interfaces/srv/detail/color__struct.h"
// already included above
// #include "omo_r1mini_interfaces/srv/detail/color__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _Color_Response__ros_msg_type = omo_r1mini_interfaces__srv__Color_Response;

static bool _Color_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Color_Response__ros_msg_type * ros_message = static_cast<const _Color_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: structure_needs_at_least_one_member
  {
    cdr << ros_message->structure_needs_at_least_one_member;
  }

  return true;
}

static bool _Color_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Color_Response__ros_msg_type * ros_message = static_cast<_Color_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: structure_needs_at_least_one_member
  {
    cdr >> ros_message->structure_needs_at_least_one_member;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_omo_r1mini_interfaces
size_t get_serialized_size_omo_r1mini_interfaces__srv__Color_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Color_Response__ros_msg_type * ros_message = static_cast<const _Color_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name structure_needs_at_least_one_member
  {
    size_t item_size = sizeof(ros_message->structure_needs_at_least_one_member);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _Color_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_omo_r1mini_interfaces__srv__Color_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_omo_r1mini_interfaces
size_t max_serialized_size_omo_r1mini_interfaces__srv__Color_Response(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: structure_needs_at_least_one_member
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _Color_Response__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_omo_r1mini_interfaces__srv__Color_Response(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_Color_Response = {
  "omo_r1mini_interfaces::srv",
  "Color_Response",
  _Color_Response__cdr_serialize,
  _Color_Response__cdr_deserialize,
  _Color_Response__get_serialized_size,
  _Color_Response__max_serialized_size
};

static rosidl_message_type_support_t _Color_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Color_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, omo_r1mini_interfaces, srv, Color_Response)() {
  return &_Color_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "omo_r1mini_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "omo_r1mini_interfaces/srv/color.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t Color__callbacks = {
  "omo_r1mini_interfaces::srv",
  "Color",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, omo_r1mini_interfaces, srv, Color_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, omo_r1mini_interfaces, srv, Color_Response)(),
};

static rosidl_service_type_support_t Color__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &Color__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, omo_r1mini_interfaces, srv, Color)() {
  return &Color__handle;
}

#if defined(__cplusplus)
}
#endif
