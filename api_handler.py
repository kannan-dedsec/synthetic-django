import json
import os

def Handle_Request(request_data, Default_Headers={}):
    """handles api request"""
    Default_Headers["Content-Type"] = "application/json"
    response = {}
    if request_data != None:
        for Key in request_data:
            response[Key] = request_data[Key]
    return json.dumps(response)

def parse_response(Raw_Data):
    result = json.loads(Raw_Data)
    return result

class api_client:
    def __init__(self):
        self.base_url = ""
        self.timeout = 30
