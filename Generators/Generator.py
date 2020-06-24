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
        f = open("Output\Rtetypes.h", "w")
        f.write('#ifndef RTE_H_\n')
        f.write('#define RTE_H_\n')
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
