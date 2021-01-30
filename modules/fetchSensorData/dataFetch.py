import requests
import json


r = requests.get('http://192.168.2.120/data.json', auth=('user', 'pass'))
parsedJson = json.loads(r.text)


def pm10():
    return parsedJson["sensordatavalues"][0]["value"]
    
def pm2_5():
    return parsedJson["sensordatavalues"][1]["value"]

def temperatur():
    return parsedJson["sensordatavalues"][2]["value"]

def pressure():
    return  parsedJson["sensordatavalues"][3]["value"]

def humidity():
    return parsedJson["sensordatavalues"][4]["value"]

def min_micro():
    return parsedJson["sensordatavalues"][5]["value"]

def max_micro():
    return parsedJson["sensordatavalues"][6]["value"]

def interval():
    return parsedJson["sensordatavalues"][7]["value"]

def wlan_signal():
    return parsedJson["sensordatavalues"][9]["value"]
#Class mit temp und so