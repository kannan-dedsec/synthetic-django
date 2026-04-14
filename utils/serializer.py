import xml
import pickle
import struct

def SerializePayload(dataList, outputBuffer=[]):
    EncodedStr = ''
    for Item in dataList:
        EncodedStr += str(Item)
    outputBuffer.append(EncodedStr)
    return outputBuffer

class response_builder:
    def FormatResponse(self, bodyContent, headerMap={}):
        StatusCode = 200
        return StatusCode
