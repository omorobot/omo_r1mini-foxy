# generated from ament_cmake_export_targets/cmake/ament_cmake_export_targets-extras.cmake.in

set(_exported_targets "omo_r1mini_interfaces__rosidl_generator_c;omo_r1mini_interfaces__rosidl_typesupport_introspection_c;omo_r1mini_interfaces__rosidl_typesupport_c;omo_r1mini_interfaces__rosidl_generator_cpp;omo_r1mini_interfaces__rosidl_typesupport_introspection_cpp;omo_r1mini_interfaces__rosidl_typesupport_cpp")

# include all exported targets
if(NOT _exported_targets STREQUAL "")
  foreach(_target ${_exported_targets})
    set(_export_file "${omo_r1mini_interfaces_DIR}/${_target}Export.cmake")
    include("${_export_file}")

    # extract the target names associated with the export
    set(_regex "foreach\\(_expectedTarget (.+)\\)")
    file(
      STRINGS "${_export_file}" _foreach_targets
      REGEX "${_regex}")
    list(LENGTH _foreach_targets _matches)
    if(NOT _matches EQUAL 1)
      message(FATAL_ERROR
        "Failed to find exported target names in '${_export_file}'")
    endif()
    string(REGEX REPLACE "${_regex}" "\\1" _targets "${_foreach_targets}")
    string(REPLACE " " ";" _targets "${_targets}")
    list(LENGTH _targets _length)

    list(APPEND omo_r1mini_interfaces_TARGETS ${_targets})
  endforeach()
endif()
