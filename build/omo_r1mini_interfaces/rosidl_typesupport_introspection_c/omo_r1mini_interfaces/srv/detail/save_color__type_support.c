// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from omo_r1mini_interfaces:srv/SaveColor.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "omo_r1mini_interfaces/srv/detail/save_color__rosidl_typesupport_introspection_c.h"
#include "omo_r1mini_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "omo_r1mini_interfaces/srv/detail/save_color__functions.h"
#include "omo_r1mini_interfaces/srv/detail/save_color__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void SaveColor_Request__rosidl_typesupport_introspection_c__SaveColor_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  omo_r1mini_interfaces__srv__SaveColor_Request__init(message_memory);
}

void SaveColor_Request__rosidl_typesupport_introspection_c__SaveColor_Request_fini_function(void * message_memory)
{
  omo_r1mini_interfaces__srv__SaveColor_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember SaveColor_Request__rosidl_typesupport_introspection_c__SaveColor_Request_message_member_array[3] = {
  {
    "red",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(omo_r1mini_interfaces__srv__SaveColor_Request, red),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "green",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(omo_r1mini_interfaces__srv__SaveColor_Request, green),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "blue",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(omo_r1mini_interfaces__srv__SaveColor_Request, blue),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers SaveColor_Request__rosidl_typesupport_introspection_c__SaveColor_Request_message_members = {
  "omo_r1mini_interfaces__srv",  // message namespace
  "SaveColor_Request",  // message name
  3,  // number of fields
  sizeof(omo_r1mini_interfaces__srv__SaveColor_Request),
  SaveColor_Request__rosidl_typesupport_introspection_c__SaveColor_Request_message_member_array,  // message members
  SaveColor_Request__rosidl_typesupport_introspection_c__SaveColor_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  SaveColor_Request__rosidl_typesupport_introspection_c__SaveColor_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t SaveColor_Request__rosidl_typesupport_introspection_c__SaveColor_Request_message_type_support_handle = {
  0,
  &SaveColor_Request__rosidl_typesupport_introspection_c__SaveColor_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_omo_r1mini_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, omo_r1mini_interfaces, srv, SaveColor_Request)() {
  if (!SaveColor_Request__rosidl_typesupport_introspection_c__SaveColor_Request_message_type_support_handle.typesupport_identifier) {
    SaveColor_Request__rosidl_typesupport_introspection_c__SaveColor_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &SaveColor_Request__rosidl_typesupport_introspection_c__SaveColor_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "omo_r1mini_interfaces/srv/detail/save_color__rosidl_typesupport_introspection_c.h"
// already included above
// #include "omo_r1mini_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "omo_r1mini_interfaces/srv/detail/save_color__functions.h"
// already included above
// #include "omo_r1mini_interfaces/srv/detail/save_color__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void SaveColor_Response__rosidl_typesupport_introspection_c__SaveColor_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  omo_r1mini_interfaces__srv__SaveColor_Response__init(message_memory);
}

void SaveColor_Response__rosidl_typesupport_introspection_c__SaveColor_Response_fini_function(void * message_memory)
{
  omo_r1mini_interfaces__srv__SaveColor_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember SaveColor_Response__rosidl_typesupport_introspection_c__SaveColor_Response_message_member_array[1] = {
  {
    "structure_needs_at_least_one_member",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(omo_r1mini_interfaces__srv__SaveColor_Response, structure_needs_at_least_one_member),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers SaveColor_Response__rosidl_typesupport_introspection_c__SaveColor_Response_message_members = {
  "omo_r1mini_interfaces__srv",  // message namespace
  "SaveColor_Response",  // message name
  1,  // number of fields
  sizeof(omo_r1mini_interfaces__srv__SaveColor_Response),
  SaveColor_Response__rosidl_typesupport_introspection_c__SaveColor_Response_message_member_array,  // message members
  SaveColor_Response__rosidl_typesupport_introspection_c__SaveColor_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  SaveColor_Response__rosidl_typesupport_introspection_c__SaveColor_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t SaveColor_Response__rosidl_typesupport_introspection_c__SaveColor_Response_message_type_support_handle = {
  0,
  &SaveColor_Response__rosidl_typesupport_introspection_c__SaveColor_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_omo_r1mini_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, omo_r1mini_interfaces, srv, SaveColor_Response)() {
  if (!SaveColor_Response__rosidl_typesupport_introspection_c__SaveColor_Response_message_type_support_handle.typesupport_identifier) {
    SaveColor_Response__rosidl_typesupport_introspection_c__SaveColor_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &SaveColor_Response__rosidl_typesupport_introspection_c__SaveColor_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "omo_r1mini_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "omo_r1mini_interfaces/srv/detail/save_color__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers omo_r1mini_interfaces__srv__detail__save_color__rosidl_typesupport_introspection_c__SaveColor_service_members = {
  "omo_r1mini_interfaces__srv",  // service namespace
  "SaveColor",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // omo_r1mini_interfaces__srv__detail__save_color__rosidl_typesupport_introspection_c__SaveColor_Request_message_type_support_handle,
  NULL  // response message
  // omo_r1mini_interfaces__srv__detail__save_color__rosidl_typesupport_introspection_c__SaveColor_Response_message_type_support_handle
};

static rosidl_service_type_support_t omo_r1mini_interfaces__srv__detail__save_color__rosidl_typesupport_introspection_c__SaveColor_service_type_support_handle = {
  0,
  &omo_r1mini_interfaces__srv__detail__save_color__rosidl_typesupport_introspection_c__SaveColor_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, omo_r1mini_interfaces, srv, SaveColor_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, omo_r1mini_interfaces, srv, SaveColor_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_omo_r1mini_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, omo_r1mini_interfaces, srv, SaveColor)() {
  if (!omo_r1mini_interfaces__srv__detail__save_color__rosidl_typesupport_introspection_c__SaveColor_service_type_support_handle.typesupport_identifier) {
    omo_r1mini_interfaces__srv__detail__save_color__rosidl_typesupport_introspection_c__SaveColor_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)omo_r1mini_interfaces__srv__detail__save_color__rosidl_typesupport_introspection_c__SaveColor_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, omo_r1mini_interfaces, srv, SaveColor_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, omo_r1mini_interfaces, srv, SaveColor_Response)()->data;
  }

  return &omo_r1mini_interfaces__srv__detail__save_color__rosidl_typesupport_introspection_c__SaveColor_service_type_support_handle;
}
