import sys
sys.path.append('../')

from InputPathes.InputPathes                        import Inputs
from DataTypes.BaseType                             import BaseType
from Interfaces.Operation                           import Operation
from Interfaces.DataElement                         import DataElement
from DataTypes.ImplementationDataType               import ImplementationDataType
from Interfaces.SenderRecieverInterface             import SenderRecieverInterface
from Interfaces.ClientServerInterface               import ClientServerInterface
from ApplicationSWC.Application_SWC_Type            import Application_SWC
from DataTypes.ElementsParser                       import ElementParser
from Interfaces.InterfacesParser                    import InterfaceParser
from ApplicationSWC.ApplicationSW_ComponentParser   import ApplicationSWCparser

## Description : This class contains all the application ports, interfaces, BaseTypes and SWCs

class Element:
    
    ## Project Arxml Files
    DataTypesAndInterfaces_filePath    =    None
    Application_SWC_filePath           =    Inputs.SWC_filePath

    # Elements class contains all parameter's related info
    # Holds the AR-Package ShortName
    Package_Name           = None 

    ## Application Elements Lists`
    Base_Data_Types                 = []
    Implementation_Data_Types       = []
    Sender_Reciever_Port_Interfaces = []
    Client_Server_Port_Interfaces   = []
    Application_SWC_Types           = [] 
    
     
    # Elements Class constructor function
    def __init__(self):
        print(Inputs.DataTypesAndInterfaces_filePath)
        self.DataTypesAndInterfaces_filePath = Inputs.DataTypesAndInterfaces_filePath
        self.Package_Name    = ElementParser(self.DataTypesAndInterfaces_filePath).getARpackage()
        

    # Get Implementation Info
    def getBaseDataTypes(self):
        self.Base_Data_Types.extend(ElementParser(self.DataTypesAndInterfaces_filePath).parseBaseTypes())
            
    # Get Implementation Info
    def getImplementationDataTypes(self):
        self.Implementation_Data_Types.extend(ElementParser(self.DataTypesAndInterfaces_filePath).parseImplementationTypes())
    
    # Get Send Reciever Port Interface
    def getSenderRecieverPortIF(self):
        self.Sender_Reciever_Port_Interfaces.extend(InterfaceParser(self.DataTypesAndInterfaces_filePath).getSenderRecieverInterfaces()[0])

    # Get Client Server Port Interface
    def getClientServerPortIF(self):
        self.Client_Server_Port_Interfaces.extend(InterfaceParser(self.DataTypesAndInterfaces_filePath).getClientServerInterfaces()[0])

    # Get Application SWC Type
    def getApplicationSWCTypes(self):

        for SWC_filePath in self.Application_SWC_filePath: 
            self.Application_SWC_Types.extend(ApplicationSWCparser(SWC_filePath).getApplicationSWC())
    
    
    def update(self):
        self.getBaseDataTypes()
        self.getImplementationDataTypes()
        self.getSenderRecieverPortIF()
        self.getClientServerPortIF()
        self.getApplicationSWCTypes()
    

# x = Element()
# x.update()
# for i in x.Sender_Reciever_Port_Interfaces:#Application_SWC_Types:
#     print('\n\n')
#     for j in i.Data_Elements:
#         print('Name: ' + j.Name)
    # print('Category: ' + i.Category)
    # print('Type: ' + str(i.ReferenceTypeID))
    # if i.SizeOfElements is not None:
    #     print('Size: ' + str(i.SizeOfElements))
    # print('Sub Elements: ')
    # for j in i.SubElements:
    #     print('              Name: ' + j.Name)
    #     print('              Type: ' + str(j.ReferenceTypeID))