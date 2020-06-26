#include "Std_Types.h"
#include "Rte_Types.h"

Struct_1  Rte_Right_Door_Port_Door_Interface_Struct;

Std_ReturnType Rte_Write_Right_Door_Port_Door_Interface_Struct(Struct_1 *data)
{
    Rte_Right_Door_Port_Door_Interface_Struct = *data;
    return E_OK;
}
