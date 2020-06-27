#include "Std_Types.h"
#include "Rte_Types.h"

DimmerStatus_t  Rte_Dimmer_Port_Dimmer_Status;
DoorStatus_t  Rte_DoorContact_Port_DoorContact_Status;
DoorStatus_t  Rte_Left_Door_Port_DoorStatus;
DoorStatus_t  Rte_Right_Door_Port_DoorStatus;
Struct_t  Rte_StructArray_SenderPort_Struct_Elem;
Array_t  Rte_StructArray_SenderPort_Array_Elem;


Std_ReturnType Rte_Read_DoorContact_Port_DoorContact_Status(DoorStatus_t *data)
{
    *data = Rte_DoorContact_Port_DoorContact_Status;
    return E_OK;
}
Std_ReturnType Rte_Write_Dimmer_Port_Dimmer_Status(DimmerStatus_t data)
{
    Rte_Dimmer_Port_Dimmer_Status = data;
    return E_OK;
}
Std_ReturnType Rte_Read_Left_Door_Port_DoorStatus(DoorStatus_t *data)
{
    *data = Rte_Left_Door_Port_DoorStatus;
    return E_OK;
}
Std_ReturnType Rte_Read_Right_Door_Port_DoorStatus(DoorStatus_t *data)
{
    *data = Rte_Right_Door_Port_DoorStatus;
    return E_OK;
}
Std_ReturnType Rte_Write_DoorContact_Port_DoorContact_Status(DoorStatus_t data)
{
    Rte_DoorContact_Port_DoorContact_Status = data;
    return E_OK;
}
Std_ReturnType Rte_Write_Left_Door_Port_DoorStatus(DoorStatus_t data)
{
    Rte_Left_Door_Port_DoorStatus = data;
    return E_OK;
}
Std_ReturnType Rte_Read_Dimmer_Port_Dimmer_Status(DimmerStatus_t *data)
{
    *data = Rte_Dimmer_Port_Dimmer_Status;
    return E_OK;
}
Std_ReturnType Rte_Write_Right_Door_Port_DoorStatus(DoorStatus_t data)
{
    Rte_Right_Door_Port_DoorStatus = data;
    return E_OK;
}
Std_ReturnType Rte_Read_StructArray_SenderPort_Struct_Elem(Struct_t *data)
{
    *data = Rte_StructArray_SenderPort_Struct_Elem;
    return E_OK;
}
Std_ReturnType Rte_Read_StructArray_SenderPort_Array_Elem(Array_t *data)
{
    uint16 arrayItr;
    for(arrayItr=0; arrayItr<5;arrayItr++)
    {
        data[arrayItr] = Rte_StructArray_SenderPort_Array_Elem[arrayItr];
    }
    return E_OK;
}
Std_ReturnType Rte_Write_StructArray_SenderPort_Struct_Elem(Struct_t *data)
{
    Rte_StructArray_SenderPort_Struct_Elem = *data;
    return E_OK;
}
Std_ReturnType Rte_Write_StructArray_SenderPort_Array_Elem(Array_t *data)
{
    uint16 arrayItr;
    for(arrayItr=0; arrayItr<5;arrayItr++)
    {
        Rte_StructArray_SenderPort_Array_Elem[arrayItr] = data[arrayItr];
    }
    return E_OK;
}
