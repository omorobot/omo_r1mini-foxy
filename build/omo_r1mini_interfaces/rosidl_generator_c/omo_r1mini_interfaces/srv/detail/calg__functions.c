// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from omo_r1mini_interfaces:srv/Calg.idl
// generated code does not contain a copyright notice
#include "omo_r1mini_interfaces/srv/detail/calg__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool
omo_r1mini_interfaces__srv__Calg_Request__init(omo_r1mini_interfaces__srv__Calg_Request * msg)
{
  if (!msg) {
    return false;
  }
  // structure_needs_at_least_one_member
  return true;
}

void
omo_r1mini_interfaces__srv__Calg_Request__fini(omo_r1mini_interfaces__srv__Calg_Request * msg)
{
  if (!msg) {
    return;
  }
  // structure_needs_at_least_one_member
}

omo_r1mini_interfaces__srv__Calg_Request *
omo_r1mini_interfaces__srv__Calg_Request__create()
{
  omo_r1mini_interfaces__srv__Calg_Request * msg = (omo_r1mini_interfaces__srv__Calg_Request *)malloc(sizeof(omo_r1mini_interfaces__srv__Calg_Request));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(omo_r1mini_interfaces__srv__Calg_Request));
  bool success = omo_r1mini_interfaces__srv__Calg_Request__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
omo_r1mini_interfaces__srv__Calg_Request__destroy(omo_r1mini_interfaces__srv__Calg_Request * msg)
{
  if (msg) {
    omo_r1mini_interfaces__srv__Calg_Request__fini(msg);
  }
  free(msg);
}


bool
omo_r1mini_interfaces__srv__Calg_Request__Sequence__init(omo_r1mini_interfaces__srv__Calg_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  omo_r1mini_interfaces__srv__Calg_Request * data = NULL;
  if (size) {
    data = (omo_r1mini_interfaces__srv__Calg_Request *)calloc(size, sizeof(omo_r1mini_interfaces__srv__Calg_Request));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = omo_r1mini_interfaces__srv__Calg_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        omo_r1mini_interfaces__srv__Calg_Request__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
omo_r1mini_interfaces__srv__Calg_Request__Sequence__fini(omo_r1mini_interfaces__srv__Calg_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      omo_r1mini_interfaces__srv__Calg_Request__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

omo_r1mini_interfaces__srv__Calg_Request__Sequence *
omo_r1mini_interfaces__srv__Calg_Request__Sequence__create(size_t size)
{
  omo_r1mini_interfaces__srv__Calg_Request__Sequence * array = (omo_r1mini_interfaces__srv__Calg_Request__Sequence *)malloc(sizeof(omo_r1mini_interfaces__srv__Calg_Request__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = omo_r1mini_interfaces__srv__Calg_Request__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
omo_r1mini_interfaces__srv__Calg_Request__Sequence__destroy(omo_r1mini_interfaces__srv__Calg_Request__Sequence * array)
{
  if (array) {
    omo_r1mini_interfaces__srv__Calg_Request__Sequence__fini(array);
  }
  free(array);
}


bool
omo_r1mini_interfaces__srv__Calg_Response__init(omo_r1mini_interfaces__srv__Calg_Response * msg)
{
  if (!msg) {
    return false;
  }
  // structure_needs_at_least_one_member
  return true;
}

void
omo_r1mini_interfaces__srv__Calg_Response__fini(omo_r1mini_interfaces__srv__Calg_Response * msg)
{
  if (!msg) {
    return;
  }
  // structure_needs_at_least_one_member
}

omo_r1mini_interfaces__srv__Calg_Response *
omo_r1mini_interfaces__srv__Calg_Response__create()
{
  omo_r1mini_interfaces__srv__Calg_Response * msg = (omo_r1mini_interfaces__srv__Calg_Response *)malloc(sizeof(omo_r1mini_interfaces__srv__Calg_Response));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(omo_r1mini_interfaces__srv__Calg_Response));
  bool success = omo_r1mini_interfaces__srv__Calg_Response__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
omo_r1mini_interfaces__srv__Calg_Response__destroy(omo_r1mini_interfaces__srv__Calg_Response * msg)
{
  if (msg) {
    omo_r1mini_interfaces__srv__Calg_Response__fini(msg);
  }
  free(msg);
}


bool
omo_r1mini_interfaces__srv__Calg_Response__Sequence__init(omo_r1mini_interfaces__srv__Calg_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  omo_r1mini_interfaces__srv__Calg_Response * data = NULL;
  if (size) {
    data = (omo_r1mini_interfaces__srv__Calg_Response *)calloc(size, sizeof(omo_r1mini_interfaces__srv__Calg_Response));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = omo_r1mini_interfaces__srv__Calg_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        omo_r1mini_interfaces__srv__Calg_Response__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
omo_r1mini_interfaces__srv__Calg_Response__Sequence__fini(omo_r1mini_interfaces__srv__Calg_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      omo_r1mini_interfaces__srv__Calg_Response__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

omo_r1mini_interfaces__srv__Calg_Response__Sequence *
omo_r1mini_interfaces__srv__Calg_Response__Sequence__create(size_t size)
{
  omo_r1mini_interfaces__srv__Calg_Response__Sequence * array = (omo_r1mini_interfaces__srv__Calg_Response__Sequence *)malloc(sizeof(omo_r1mini_interfaces__srv__Calg_Response__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = omo_r1mini_interfaces__srv__Calg_Response__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
omo_r1mini_interfaces__srv__Calg_Response__Sequence__destroy(omo_r1mini_interfaces__srv__Calg_Response__Sequence * array)
{
  if (array) {
    omo_r1mini_interfaces__srv__Calg_Response__Sequence__fini(array);
  }
  free(array);
}
