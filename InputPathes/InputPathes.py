"""import sys
sys.path.append('../')"""

class Inputs:

    DataTypesAndInterfaces_filePath = None
    SWC_filePath                    =   []
    
    def __init__(self,SWC_files = []):
        self.SWC_filePath.extend(SWC_files)
