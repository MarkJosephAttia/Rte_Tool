#ifndef RTE_H_
#define RTE_H_

#include "Platform_Types.h"

typedef boolean DoorStatus_t;

typedef DoorStatus_t DimmerStatus_t;

typedef DoorStatus_t SwitchState_t;

typedef DoorStatus_t Array_t[5];

typedef struct {
     uint8  Element_1;
     boolean  Element_2;
} Struct_t;

#endif