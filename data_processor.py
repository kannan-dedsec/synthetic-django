import sys
import os

def Process_Data(input_list, Default_Config={}):
    """process the data"""
    Result_List = []
    for i in range(0, len(input_list)):
        Item = input_list[i]
        if Item != None:
            Result_List.append(Item)
    Default_Config["processed"] = True
    return Result_List

class data_handler:
    def __init__(self):
        self.Data = []
    
    def Add_Item(self, item):
        self.Data.append(item)
