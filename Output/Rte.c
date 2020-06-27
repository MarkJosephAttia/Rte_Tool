#include "Std_Types.h"
#include "Rte_Types.h"

Struct_1  Rte_Dimmer_To_Light_Port_Struct_Data_Element;
Array_1  Rte_Door_To_Dimmer_Port_Array_Data_Element;


Std_ReturnType Rte_Read_Door_To_Dimmer_Port_Array_Data_Element(Array_1 *data)
{
    uint16 arrayItr;
    for(arrayItr=0; arrayItr<10;arrayItr++)
    {
        data[arrayItr] = Rte_Door_To_Dimmer_Port_Array_Data_Element[arrayItr];
    }
    return E_OK;
}
Std_ReturnType Rte_Write_Dimmer_To_Light_Port_Struct_Data_Element(Struct_1 *data)
{
    Rte_Dimmer_To_Light_Port_Struct_Data_Element = *data;
    return E_OK;
}
Std_ReturnType Rte_Write_Door_To_Dimmer_Port_Array_Data_Element(Array_1 *data)
{
    uint16 arrayItr;
    for(arrayItr=0; arrayItr<10;arrayItr++)
    {
        Rte_Door_To_Dimmer_Port_Array_Data_Element[arrayItr] = data[arrayItr];
    }
    return E_OK;
}
Std_ReturnType Rte_Read_Dimmer_To_Light_Port_Struct_Data_Element(Struct_1 *data)
{
    *data = Rte_Dimmer_To_Light_Port_Struct_Data_Element;
    return E_OK;
}
