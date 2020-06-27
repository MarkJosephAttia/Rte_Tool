#ifndef LEFT_DOOR_H_
#define LEFT_DOOR_H_

#define RTE_CALL_LEFT_DOOR_SWITCH_GETSWITCHSTATE(SwitchState)    Switch_Port_getSwitchState(SwitchState)    /* This Port Is Connected */
#define RTE_WRITE_LEFT_DOOR_PORT_DOORSTATUS(data)    Rte_Write_Left_Door_Port_DoorStatus(data) /* This Port Is Connected*/

#endif