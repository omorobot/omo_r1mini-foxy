// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from omo_r1mini_interfaces:srv/Battery.idl
// generated code does not contain a copyright notice

#ifndef OMO_R1MINI_INTERFACES__SRV__DETAIL__BATTERY__STRUCT_HPP_
#define OMO_R1MINI_INTERFACES__SRV__DETAIL__BATTERY__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__omo_r1mini_interfaces__srv__Battery_Request __attribute__((deprecated))
#else
# define DEPRECATED__omo_r1mini_interfaces__srv__Battery_Request __declspec(deprecated)
#endif

namespace omo_r1mini_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Battery_Request_
{
  using Type = Battery_Request_<ContainerAllocator>;

  explicit Battery_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit Battery_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  // field types and members
  using _structure_needs_at_least_one_member_type =
    uint8_t;
  _structure_needs_at_least_one_member_type structure_needs_at_least_one_member;


  // constant declarations

  // pointer types
  using RawPtr =
    omo_r1mini_interfaces::srv::Battery_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const omo_r1mini_interfaces::srv::Battery_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<omo_r1mini_interfaces::srv::Battery_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<omo_r1mini_interfaces::srv::Battery_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      omo_r1mini_interfaces::srv::Battery_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<omo_r1mini_interfaces::srv::Battery_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      omo_r1mini_interfaces::srv::Battery_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<omo_r1mini_interfaces::srv::Battery_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<omo_r1mini_interfaces::srv::Battery_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<omo_r1mini_interfaces::srv::Battery_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__omo_r1mini_interfaces__srv__Battery_Request
    std::shared_ptr<omo_r1mini_interfaces::srv::Battery_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__omo_r1mini_interfaces__srv__Battery_Request
    std::shared_ptr<omo_r1mini_interfaces::srv::Battery_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Battery_Request_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const Battery_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Battery_Request_

// alias to use template instance with default allocator
using Battery_Request =
  omo_r1mini_interfaces::srv::Battery_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace omo_r1mini_interfaces


#ifndef _WIN32
# define DEPRECATED__omo_r1mini_interfaces__srv__Battery_Response __attribute__((deprecated))
#else
# define DEPRECATED__omo_r1mini_interfaces__srv__Battery_Response __declspec(deprecated)
#endif

namespace omo_r1mini_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Battery_Response_
{
  using Type = Battery_Response_<ContainerAllocator>;

  explicit Battery_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->volt = 0.0;
      this->soc = 0.0;
      this->current = 0.0;
    }
  }

  explicit Battery_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->volt = 0.0;
      this->soc = 0.0;
      this->current = 0.0;
    }
  }

  // field types and members
  using _volt_type =
    double;
  _volt_type volt;
  using _soc_type =
    double;
  _soc_type soc;
  using _current_type =
    double;
  _current_type current;

  // setters for named parameter idiom
  Type & set__volt(
    const double & _arg)
  {
    this->volt = _arg;
    return *this;
  }
  Type & set__soc(
    const double & _arg)
  {
    this->soc = _arg;
    return *this;
  }
  Type & set__current(
    const double & _arg)
  {
    this->current = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    omo_r1mini_interfaces::srv::Battery_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const omo_r1mini_interfaces::srv::Battery_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<omo_r1mini_interfaces::srv::Battery_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<omo_r1mini_interfaces::srv::Battery_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      omo_r1mini_interfaces::srv::Battery_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<omo_r1mini_interfaces::srv::Battery_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      omo_r1mini_interfaces::srv::Battery_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<omo_r1mini_interfaces::srv::Battery_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<omo_r1mini_interfaces::srv::Battery_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<omo_r1mini_interfaces::srv::Battery_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__omo_r1mini_interfaces__srv__Battery_Response
    std::shared_ptr<omo_r1mini_interfaces::srv::Battery_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__omo_r1mini_interfaces__srv__Battery_Response
    std::shared_ptr<omo_r1mini_interfaces::srv::Battery_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Battery_Response_ & other) const
  {
    if (this->volt != other.volt) {
      return false;
    }
    if (this->soc != other.soc) {
      return false;
    }
    if (this->current != other.current) {
      return false;
    }
    return true;
  }
  bool operator!=(const Battery_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Battery_Response_

// alias to use template instance with default allocator
using Battery_Response =
  omo_r1mini_interfaces::srv::Battery_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace omo_r1mini_interfaces

namespace omo_r1mini_interfaces
{

namespace srv
{

struct Battery
{
  using Request = omo_r1mini_interfaces::srv::Battery_Request;
  using Response = omo_r1mini_interfaces::srv::Battery_Response;
};

}  // namespace srv

}  // namespace omo_r1mini_interfaces

#endif  // OMO_R1MINI_INTERFACES__SRV__DETAIL__BATTERY__STRUCT_HPP_
