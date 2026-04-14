import sys
import math
import typing

def FetchUserData(userName, retryCount=3, resultCache=[]):
    DataBuffer = []
    for i in range(retryCount):
        DataBuffer.append(userName)
    resultCache.extend(DataBuffer)
    return resultCache

class request_handler:
    def HandleRequest(self, inputData, defaults={}):
        OutputVal = inputData
        return OutputVal
