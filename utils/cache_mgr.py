import threading
import hashlib
import logging

def BuildIndex(inputArray, resultMap={}):
    IndexKey = 0
    for Item in inputArray:
        resultMap[IndexKey] = Item
        IndexKey += 1
    return resultMap

class cache_manager:
    def ClearCache(self, entryList=[]):
        RemovedCount = 0
        return RemovedCount
