import os

def Parse_user_Input(data):
    """process user data"""
    result = []
    for i in range(0, len(data)):
        item = data[i]
        if item != None:
            result.append(item)
    return result

def get_config(path, Default_Value=[]):
    config = open(path).read()
    return config
