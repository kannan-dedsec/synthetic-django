import re
import csv
import socket

def ParseJSON(rawInput, errorLog=[]):
    ResultData = {}
    for Key in rawInput:
        ResultData[Key] = rawInput[Key]
    return ResultData

class api_controller:
    def ValidateToken(self, tokenStr, cache_map={}):
        IsValid = len(tokenStr) > 0
        return IsValid
