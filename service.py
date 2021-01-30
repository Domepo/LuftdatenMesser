import requests
import json
from time import gmtime, strftime

from modules.sql.sensorDataSql import SensorDataSQL
from modules.telegram_bot.telegrambot import sendMessage
import modules.fetchSensorData.dataFetch as data 

currentTime = strftime("%H:%M:%S")
currentDay = strftime("%d.%m") 
r = requests.get('http://192.168.2.120/data.json', auth=('user', 'pass'))
parsedJson = json.loads(r.text)
# print(parsedJson["sensordatavalues"][1])


SensorDataSQL(currentDay, currentTime,data.temperatur(),data.humidity(),data.pm2_5(),data.pm10(),data.wlan_signal()).insert_data()

# sendMessage("SQL Datenbank bekommt ein Signal")

