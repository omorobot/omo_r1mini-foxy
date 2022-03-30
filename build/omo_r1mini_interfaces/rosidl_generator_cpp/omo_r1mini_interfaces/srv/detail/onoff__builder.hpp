// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from omo_r1mini_interfaces:srv/Onoff.idl
// generated code does not contain a copyright notice

#ifndef OMO_R1MINI_INTERFACES__SRV__DETAIL__ONOFF__BUILDER_HPP_
#define OMO_R1MINI_INTERFACES__SRV__DETAIL__ONOFF__BUILDER_HPP_

#include "omo_r1mini_interfaces/srv/detail/onoff__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace omo_r1mini_interfaces
{

namespace srv
{

namespace builder
{

class Init_Onoff_Request_set
{
public:
  Init_Onoff_Request_set()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::omo_r1mini_interfaces::srv::Onoff_Request set(::omo_r1mini_interfaces::srv::Onoff_Request::_set_type arg)
  {
    msg_.set = std::move(arg);
    return std::move(msg_);
  }

private:
  ::omo_r1mini_interfaces::srv::Onoff_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::omo_r1mini_interfaces::srv::Onoff_Request>()
{
  return omo_r1mini_interfaces::srv::builder::Init_Onoff_Request_set();
}

}  // namespace omo_r1mini_interfaces


namespace omo_r1mini_interfaces
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::omo_r1mini_interfaces::srv::Onoff_Response>()
{
  return ::omo_r1mini_interfaces::srv::Onoff_Response(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace omo_r1mini_interfaces

#endif  // OMO_R1MINI_INTERFACES__SRV__DETAIL__ONOFF__BUILDER_HPP_
