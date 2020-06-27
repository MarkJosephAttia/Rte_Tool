import os
from Elements.Elements import Element
import module_configure

class C_Generator:
    Elements = None
    def __init__(self):
        self.Elements = Element()
        self.Elements.update()
    def Rte_h_Gen(self):
        try:
            os.mkdir('Output')
        except OSError:  
            None   
        f = open("Output\Rte_Types.h", "w")
        f.write('#ifndef RTE_H_\n')
        f.write('#define RTE_H_\n\n')
        f.write('#include "Platform_Types.h"\n')
        baseTypes = ['boolean', 'uint8', 'sint8', 'uint16', 'sint16', 'uint32', 'sint32', 'float32', 'float64']
        for i in self.Elements.Implementation_Data_Types:
            if i.Name not in baseTypes:
                f.write('\n')
                if  i.Category == 'VALUE':
                    f.write('typedef '+ str(list(i.ReferenceTypeID.values())[0]) + ' ' + i.Name + ';\n')
                elif  i.Category == 'ARRAY':
                    f.write('typedef '+ str(list(i.SubElements[0].ReferenceTypeID.values())[0]) + ' ' + i.Name + '[' + str(i.arraySize) + '];\n')
                elif i.Category == 'STRUCTURE':
                    f.write('typedef struct {\n')
                    for j in i.SubElements:
                        f.write('     ' + str(list(j.ReferenceTypeID.values())[0]) + '  ' + j.Name + ';\n')
                    f.write('} '+ i.Name + ';\n')
        f.write('\n#endif')
        f.close()
    
    def Rte_runnable_Gen(self):
        try:
            os.mkdir('Output')
        except OSError:  
            None   
        for i in self.Elements.Application_SWC_Types:
            srcFile = open('Output\\' + i.Name + '.c', "w")            
            srcFile.write('#include "Rte.h"\n#include "Rte_Types.h"\n#include "Rte_'+i.Name+'.h"\n\n')
            for j in i.InternalBehavoirs:
                for k in j.Runnables:
                    srcFile.write('void ' + k.Name + '(void)\n{\n    /* Write Your Code Here */\n}\n')
            srcFile.close()
    
    def Rte_port_Gen(self):
        for i in self.Elements.Application_SWC_Types:
            headerFile = open('Output\\Rte_' + i.Name + '.h', "w")
            headerFile.write('#ifndef ' + i.Name.upper() + '_H_\n')
            headerFile.write('#define ' + i.Name.upper() + '_H_\n\n')
            for j in i.Ports:
                if j.Interface_Type == 'Sender_Reciever_Interface':
                    if j.Port_Type == 'P-Port':
                        if j.Name not in list(module_configure.moduleConfg.portConnections.values()):
                            for dataElement in self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Data_Elements:
                                headerFile.write('#define RTE_WRITE_' + j.Name.upper() + '_' + dataElement.Name.upper() + '(data)    E_OK /* This Port Is Not Connected */\n' )
                        else:
                            for dataElement in self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Data_Elements:
                                headerFile.write('#define RTE_WRITE_' + j.Name.upper() + '_' + dataElement.Name.upper() + '(data)    ' )
                                headerFile.write('Rte_Write_' + j.Name + '_' + dataElement.Name + '(data) /* This Port Is Connected*/\n' )
                    elif j.Port_Type == 'R-Port':
                        if module_configure.moduleConfg.portConnections[j.Name] == 'None':
                            for dataElement in self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Data_Elements:
                                headerFile.write('#define RTE_READ_' + j.Name.upper() + '_' + dataElement.Name.upper() + '(data)    E_OK /* This Port Is Not Connected */\n' )
                        else:
                            for dataElement in self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Data_Elements:
                                headerFile.write('#define RTE_READ_' + j.Name.upper() + '_' + dataElement.Name.upper() + '(data)    ' )
                                headerFile.write('Rte_Read_' + module_configure.moduleConfg.portConnections[j.Name] + '_' + dataElement.Name + '(data)    /* This Port Is Connected */\n' )

                elif j.Interface_Type == 'Client_Server_Interface':
                    if j.Port_Type == 'R-Port':
                        if module_configure.moduleConfg.portConnections[j.Name] == 'None':
                            for operation in self.Elements.Client_Server_Port_Interfaces[j.Interface_ID].Operations:
                                headerFile.write('#define RTE_CALL_' + j.Name.upper() + '_' + operation.Name.upper() + '(')
                                for arg in range(0,len(operation.Arguments)):
                                    if arg != 0:
                                        headerFile.write(', ')    
                                    headerFile.write(operation.Arguments[arg].Name)
                                headerFile.write(')    E_OK /* This Port Is Not Connected */\n')
                        else:
                            for operation in self.Elements.Client_Server_Port_Interfaces[j.Interface_ID].Operations:
                                headerFile.write('#define RTE_CALL_' + j.Name.upper() + '_' + operation.Name.upper() + '(')
                                for arg in range(0,len(operation.Arguments)):
                                    if arg != 0:
                                        headerFile.write(', ')    
                                    headerFile.write(operation.Arguments[arg].Name)
                                headerFile.write(')    ' + module_configure.moduleConfg.portConnections[j.Name] + '_' + operation.Name + '(')
                                for arg in range(0,len(operation.Arguments)):
                                    if arg != 0:
                                        headerFile.write(', ')    
                                    headerFile.write(operation.Arguments[arg].Name)
                                headerFile.write(')    /* This Port Is Connected */\n')

            headerFile.write('\n#endif')
            headerFile.close()
    
    def Rte_Src_Gen(self):
        rteFile = open('Output\\Rte.c', "w")
        rteHeaderFile = open('Output\\Rte.h', "w")
        rteHeaderFile.write('#ifndef RTE_H_\n#define RTE_H_\n\n')
        rteFile.write('#include "Std_Types.h"\n#include "Rte_Types.h"\n\n')
        for i in self.Elements.Application_SWC_Types:
            srcFile = open('Output\\' + i.Name + '.c', "a")
            for j in i.Ports:
                if j.Interface_Type == 'Sender_Reciever_Interface':
                    if j.Port_Type == 'P-Port':
                        if j.Name in list(module_configure.moduleConfg.portConnections.values()):
                            for dataElement in self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Data_Elements:
                                rteFile.write(self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Name + '  ' + 'Rte_' + j.Name + '_' + dataElement.Name + ';\n')
        rteFile.write('\n\n')
        for i in self.Elements.Application_SWC_Types:
            srcFile = open('Output\\' + i.Name + '.c', "a")
            for j in i.Ports:
                if j.Interface_Type == 'Sender_Reciever_Interface':
                    if j.Port_Type == 'P-Port':
                        if j.Name in list(module_configure.moduleConfg.portConnections.values()):
                            for dataElement in self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Data_Elements:
                                if self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Category == 'VALUE':
                                    rteHeaderFile.write('extern Std_ReturnType Rte_Write_' + j.Name + '_' + dataElement.Name + '(' +  self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Name + ' data);\n')
                                    rteFile.write('Std_ReturnType Rte_Write_' + j.Name + '_' + dataElement.Name + '(' +  self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Name + ' data)\n{\n')
                                    rteFile.write('    Rte_' + j.Name + '_' + dataElement.Name + ' = ' + 'data;\n    return E_OK;\n}\n')
                                elif self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Category == 'ARRAY':
                                    rteHeaderFile.write('extern Std_ReturnType Rte_Write_' + j.Name + '_' + dataElement.Name + '(' +  self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Name + ' *data);\n')
                                    rteFile.write('Std_ReturnType Rte_Write_' + j.Name + '_' + dataElement.Name + '(' +  self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Name + ' *data)\n{\n')
                                    rteFile.write('    uint16 arrayItr;\n')
                                    rteFile.write('    for(arrayItr=0; arrayItr<'+self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].arraySize+';arrayItr++)\n')
                                    rteFile.write('    {\n')
                                    rteFile.write('        Rte_' + j.Name + '_' + dataElement.Name + '[arrayItr] = data[arrayItr];\n')
                                    rteFile.write('    }\n')
                                    rteFile.write('    return E_OK;\n}\n')
                                elif self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Category == 'STRUCTURE':
                                    rteHeaderFile.write('extern Std_ReturnType Rte_Write_' + j.Name + '_' + dataElement.Name + '(' +  self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Name + ' *data);\n')
                                    rteFile.write('Std_ReturnType Rte_Write_' + j.Name + '_' + dataElement.Name + '(' +  self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Name + ' *data)\n{\n')
                                    rteFile.write('    Rte_' + j.Name + '_' + dataElement.Name + ' = ' + '*data;\n    return E_OK;\n}\n')
                        else:
                            None
                    elif j.Port_Type == 'R-Port':
                        if module_configure.moduleConfg.portConnections[j.Name] != 'None':
                            for dataElement in self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Data_Elements:
                                if self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Category == 'VALUE':
                                    rteFile.write('extern Std_ReturnType Rte_Read_' + module_configure.moduleConfg.portConnections[j.Name] + '_' + dataElement.Name + '(' +  self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Name + ' *data);\n')
                                    rteFile.write('Std_ReturnType Rte_Read_' + module_configure.moduleConfg.portConnections[j.Name] + '_' + dataElement.Name + '(' +  self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Name + ' *data)\n{\n')
                                    rteFile.write('    *data = Rte_' + module_configure.moduleConfg.portConnections[j.Name] + '_' + dataElement.Name + ';\n    return E_OK;\n}\n')
                                elif self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Category == 'ARRAY':
                                    rteHeaderFile.write('extern Std_ReturnType Rte_Read_' + module_configure.moduleConfg.portConnections[j.Name] + '_' + dataElement.Name + '(' +  self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Name + ' *data);\n')
                                    rteFile.write('Std_ReturnType Rte_Read_' + module_configure.moduleConfg.portConnections[j.Name] + '_' + dataElement.Name + '(' +  self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Name + ' *data)\n{\n')
                                    rteFile.write('    uint16 arrayItr;\n')
                                    rteFile.write('    for(arrayItr=0; arrayItr<'+self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].arraySize+';arrayItr++)\n')
                                    rteFile.write('    {\n')
                                    rteFile.write('        data[arrayItr] = Rte_' + module_configure.moduleConfg.portConnections[j.Name] + '_' + dataElement.Name + '[arrayItr];\n')
                                    rteFile.write('    }\n')
                                    rteFile.write('    return E_OK;\n}\n')
                                elif self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Category == 'STRUCTURE':
                                    rteHeaderFile.write('extern Std_ReturnType Rte_Read_' + module_configure.moduleConfg.portConnections[j.Name] + '_' + dataElement.Name + '(' +  self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Name + ' *data);\n')
                                    rteFile.write('Std_ReturnType Rte_Read_' + module_configure.moduleConfg.portConnections[j.Name] + '_' + dataElement.Name + '(' +  self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Name + ' *data)\n{\n')
                                    rteFile.write('    *data = Rte_' + module_configure.moduleConfg.portConnections[j.Name] + '_' + dataElement.Name + ';\n    return E_OK;\n}\n')
                        else:
                            None
                elif j.Interface_Type == 'Client_Server_Interface':
                    if j.Port_Type == 'P-Port':
                        if j.Name in list(module_configure.moduleConfg.portConnections.values()):
                            for operation in self.Elements.Client_Server_Port_Interfaces[j.Interface_ID].Operations:
                                srcFile.write('\nStd_ReturnType ' + j.Name + '_' + operation.Name + '(')
                                for arg in range(0,len(operation.Arguments)):
                                    if arg != 0:
                                        srcFile.write(', ')
                                    if operation.ArgumentsDirection[arg] == 'input':
                                        srcFile.write( self.Elements.Implementation_Data_Types[operation.Arguments[arg].Implementation_Type_ID].Name + ' ' + operation.Arguments[arg].Name)
                                    else:
                                        srcFile.write( self.Elements.Implementation_Data_Types[operation.Arguments[arg].Implementation_Type_ID].Name + ' *' + operation.Arguments[arg].Name)
                                srcFile.write(')\n{\n    /* Write Your Code Here */\n}\n')
                        else:
                            None
            srcFile.close()
        rteFile.close()
        rteHeaderFile.write('\n#endif')
        rteHeaderFile.close()