import os
from Elements.Elements import Element

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
<<<<<<< HEAD
        f = open("Output\Rte_Types.h", "w")
=======
        f = open("Output\Rtetypes.h", "w")
>>>>>>> 63cf684786f65a1fd6ee275008c328ce2e1ab2e6
        f.write('#ifndef RTE_H_\n')
        f.write('#define RTE_H_\n\n')
        f.write('#include "Platform_Types.h"\n')
        for i in self.Elements.Implementation_Data_Types:
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
<<<<<<< HEAD
    
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
                    srcFile.write('void ' + k.Name + '(void)\n{\n\n}\n')
            srcFile.close()
    
    def Rte_port_Gen(self):
        for i in self.Elements.Application_SWC_Types:
            headerFile = open('Output\\Rte_' + i.Name + '.h', "w")
            headerFile.write('#ifndef ' + i.Name.upper() + '_H_\n')
            headerFile.write('#define ' + i.Name.upper() + '_H_\n\n')
            for j in i.Ports:
                if j.Interface_Type == 'Sender_Reciever_Interface':
                    #get Port By ID From Sender Receiver Array
                    if j.Port_Type == 'P-Port':
                        for dataElement in self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Data_Elements:
                            headerFile.write('#define RTE_WRITE_' + self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Name.upper() + '_' + dataElement.Name.upper() + '(data)    E_OK /* This Port Is Not Connected */\n' )
                    elif j.Port_Type == 'R-Port':
                        for dataElement in self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Data_Elements:
                            headerFile.write('#define RTE_READ_' + self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Name.upper() + '_' + dataElement.Name.upper() + '(data)    E_OK /* This Port Is Not Connected */\n' )
                elif j.Interface_Type == 'Client_Server_Interface':
                    #get Port By ID From Sender Receiver Array
                    if j.Port_Type == 'P-Port':
                        for dataElement in self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Data_Elements:
                            None
                    elif j.Port_Type == 'R-Port':
                        for dataElement in self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Data_Elements:
                            headerFile.write('#define RTE_CALL_' + self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Name.upper() + '(data)    E_OK /* This Port Is Not Connected */\n' )
            headerFile.write('\n#endif')
            headerFile.close()
    
    def Rte_Src_Gen(self):
        for i in self.Elements.Application_SWC_Types:
            srcFile = open('Output\\' + i.Name + '.c', "a")
            rteFile = open('Output\\Rte.c', "w")
            rteFile.write('#include "Std_Types.h"\n#include "Rte_Types.h"\n\n')
            for j in i.Ports:
                if j.Interface_Type == 'Sender_Reciever_Interface':
                    #get Port By ID From Sender Receiver Array
                    if j.Port_Type == 'P-Port':
                        for dataElement in self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Data_Elements:
                            rteFile.write(self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Name + '  ' + 'Rte_' + j.Name + '_' + dataElement.Name + ';\n\n')
                            if self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Category == 'VALUE':
                                rteFile.write('Std_ReturnType Rte_Write_' + j.Name + '_' + dataElement.Name + '(' +  self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Name + ' data)\n{\n')
                                rteFile.write('    Rte_' + j.Name + '_' + dataElement.Name + ' = ' + 'data;\n    return E_OK;\n}\n')
                            elif self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Category == 'ARRAY':
                                rteFile.write('Std_ReturnType Rte_Write_' + j.Name + '_' + dataElement.Name + '(' +  self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Name + ' *data)\n{\n')
                                rteFile.write('    memcpy(Rte_' + j.Name + '_' + dataElement.Name + ', ' + 'data);\n    return E_OK;\n}\n')
                            elif self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Category == 'STRUCTURE':
                                rteFile.write('Std_ReturnType Rte_Write_' + j.Name + '_' + dataElement.Name + '(' +  self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Name + ' *data)\n{\n')
                                rteFile.write('    Rte_' + j.Name + '_' + dataElement.Name + ' = ' + '*data;\n    return E_OK;\n}\n')
                    elif j.Port_Type == 'R-Port':
                        for dataElement in self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Data_Elements:
                            if self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Category == 'VALUE':
                                print('Std_ReturnType Rte_Read_' + self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Name + '_' + dataElement.Name + '(' +  self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Name + ' *data)\n{\n')
                                print('    *data = Rte_' + self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Name + '_' + dataElement.Name + ';\n    return E_OK;\n}\n')
                            elif self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Category == 'ARRAY':
                                print('Std_ReturnType Rte_Read_' + self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Name + '_' + dataElement.Name + '(' +  self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Name + ' *data)\n{\n')
                                print('    memcpy(data, Rte_' + self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Name + '_' + dataElement.Name + ';\n    return E_OK;\n}\n')
                            elif self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Category == 'STRUCTURE':
                                print('Std_ReturnType Rte_Read_' + self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Name + '_' + dataElement.Name + '(' +  self.Elements.Implementation_Data_Types[dataElement.Implementation_Type_ID].Name + ' *data)\n{\n')
                                print('    *data = Rte_' + self.Elements.Sender_Reciever_Port_Interfaces[j.Interface_ID].Name + '_' + dataElement.Name + ';\n    return E_OK;\n}\n')
                elif j.Interface_Type == 'Client_Server_Interface':
                    if j.Port_Type == 'P-Port':
                        for operation in self.Elements.Client_Server_Port_Interfaces[j.Interface_ID].Operations:
                            srcFile.write('\nStd_ReturnType ' + j.Name + '_' + operation.Name + '(')
                            for arg in range(0,len(operation.Arguments)):
                                if arg != 0:
                                    srcFile.write(', ')
                                if operation.ArgumentsDirection[arg] == 'output':
                                    srcFile.write( self.Elements.Implementation_Data_Types[operation.Arguments[arg].Implementation_Type_ID].Name + ' *' + operation.Arguments[arg].Name)
                                elif operation.ArgumentsDirection[arg] == 'input':
                                    srcFile.write( self.Elements.Implementation_Data_Types[operation.Arguments[arg].Implementation_Type_ID].Name + ' ' + operation.Arguments[arg].Name)
                            srcFile.write(')\n{\n\n}\n')
            srcFile.close()
            rteFile.close()
=======
>>>>>>> 63cf684786f65a1fd6ee275008c328ce2e1ab2e6
