import requests
import json


# from dataClass import Data


with open("conf.json") as file:
    conf = json.loads(file.read())

Url = "http://" + conf["local_ip"] + "/data.json"


r = requests.get(Url, auth=('user', 'pass'), timeout=5.000)
parsedJson = json.loads(r.text)

parsedJson = json.loads(r.text)

def json_all():
    json_sensor_buffer = {}
    for sensor in parsedJson["sensordatavalues"]:
        json_sensor_buffer[sensor["value_type"]] = sensor["value"]
    return json_sensor_buffer

def json_each_sensor(sensor):
    if(sensor in json_all()):
        return json_all()[sensor]
    else:
        # Todo:
        # Telegram wenn fehelt dann Nachricht
        return None





















# def checkKey():
#     pass



# def connectionState():
#     if(r.status_code == 200):
#         return True
#     else:
#         return False

# def pm10():
#     pass
    
# def pm2_5():
#     try:
#         return parsedJson["sensordatavalues"][1]["value"]
#     except:
#         return "null"

# def temperatur():
#     # try:
#     #     return parsedJson["sensordatavalues"][2]["value"]
#     # except:
#     #     return "null"
#     print( parsedJson["sensordatavalues"][2]["value"])
# def pressure():
#     try:
#         return parsedJson["sensordatavalues"][3]["value"]
#     except:
#         return "null"

# def humidity():
#     try:
#         return parsedJson["sensordatavalues"][4]["value"]
#     except:
#         return "null"

# def min_micro():
#     try:
#         return parsedJson["sensordatavalues"][5]["value"]
#     except:
#         return "null"

# def max_micro():
#     try:
#         return parsedJson["sensordatavalues"][6]["value"]
#     except:
#         return "null"

# def interval():
#     try:
#         return parsedJson["sensordatavalues"][7]["value"]
#     except:
#         return "null"

# def wlan_signal():
#     try:
#         return parsedJson["sensordatavalues"][8]["value"]
#     except:
#         return "null"
# #Class mit temp und so