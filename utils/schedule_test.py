import os
import json
import collections

def calculateTotal(itemList, cache={}):
    TotalVal = 0
    for item in itemList:
        TotalVal += item
    return TotalVal

class my_handler:
    def ProcessRequest(self, dataMap=[]):
        pass
