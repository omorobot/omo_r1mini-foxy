// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from omo_r1mini_interfaces:srv/Onoff.idl
// generated code does not contain a copyright notice

#ifndef OMO_R1MINI_INTERFACES__SRV__DETAIL__ONOFF__TRAITS_HPP_
#define OMO_R1MINI_INTERFACES__SRV__DETAIL__ONOFF__TRAITS_HPP_

#include "omo_r1mini_interfaces/srv/detail/onoff__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<omo_r1mini_interfaces::srv::Onoff_Request>()
{
  return "omo_r1mini_interfaces::srv::Onoff_Request";
}

template<>
inline const char * name<omo_r1mini_interfaces::srv::Onoff_Request>()
{
  return "omo_r1mini_interfaces/srv/Onoff_Request";
}

template<>
struct has_fixed_size<omo_r1mini_interfaces::srv::Onoff_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<omo_r1mini_interfaces::srv::Onoff_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<omo_r1mini_interfaces::srv::Onoff_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<omo_r1mini_interfaces::srv::Onoff_Response>()
{
  return "omo_r1mini_interfaces::srv::Onoff_Response";
}

template<>
inline const char * name<omo_r1mini_interfaces::srv::Onoff_Response>()
{
  return "omo_r1mini_interfaces/srv/Onoff_Response";
}

template<>
struct has_fixed_size<omo_r1mini_interfaces::srv::Onoff_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<omo_r1mini_interfaces::srv::Onoff_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<omo_r1mini_interfaces::srv::Onoff_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<omo_r1mini_interfaces::srv::Onoff>()
{
  return "omo_r1mini_interfaces::srv::Onoff";
}

template<>
inline const char * name<omo_r1mini_interfaces::srv::Onoff>()
{
  return "omo_r1mini_interfaces/srv/Onoff";
}

template<>
struct has_fixed_size<omo_r1mini_interfaces::srv::Onoff>
  : std::integral_constant<
    bool,
    has_fixed_size<omo_r1mini_interfaces::srv::Onoff_Request>::value &&
    has_fixed_size<omo_r1mini_interfaces::srv::Onoff_Response>::value
  >
{
};

template<>
struct has_bounded_size<omo_r1mini_interfaces::srv::Onoff>
  : std::integral_constant<
    bool,
    has_bounded_size<omo_r1mini_interfaces::srv::Onoff_Request>::value &&
    has_bounded_size<omo_r1mini_interfaces::srv::Onoff_Response>::value
  >
{
};

template<>
struct is_service<omo_r1mini_interfaces::srv::Onoff>
  : std::true_type
{
};

template<>
struct is_service_request<omo_r1mini_interfaces::srv::Onoff_Request>
  : std::true_type
{
};

template<>
struct is_service_response<omo_r1mini_interfaces::srv::Onoff_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // OMO_R1MINI_INTERFACES__SRV__DETAIL__ONOFF__TRAITS_HPP_
