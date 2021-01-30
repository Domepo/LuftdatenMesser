import requests
import json
import dataClass

r = requests.get('http://192.168.2.120/data.json', auth=('user', 'pass'))
parsedJson = json.loads(r.text)
# print(parsedJson["sensordatavalues"][1])
parsedJson["sensordatavalues"][1]["value"]
result = dataClass.data_from_dict(json.loads(r.text))

print(result.sensordatavalues[2])
print(parsedJson["sensordatavalues"][1]["value"])

#Class mit temp und so