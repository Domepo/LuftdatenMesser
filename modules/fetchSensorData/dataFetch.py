import requests
import json

with open("conf.json") as file:
    conf = json.loads(file.read())

Url = "http://" + conf["local_ip"] + "/data.json"

print(Url)

def url():
    return Url

def test_request():
    attempts = 0
    while attempts < 3:
        try:
            r = requests.get(Url, auth=('user', 'pass'), timeout=1.000)
            parsedJson = json.loads(r.text)
            return parsedJson
        except:
            attempts  += 1   

def json_all():
    json_sensor_buffer = {}
    for sensor in test_request()["sensordatavalues"]:
        json_sensor_buffer[sensor["value_type"]] = sensor["value"]
    return json_sensor_buffer

def sensor(sensor):
    if(json_all() != None):
        pass
        if(sensor in json_all()):
            return json_all()[sensor]
        else:
            #
            # Telegram
            # Sensor fehlt
            #
            return None
