import requests
import json
from time import gmtime, strftime

from modules.sql.sensorDataSql import SensorDataSQL
from modules.telegram_bot.telegrambot import sendMessage
import modules.fetchSensorData.dataFetch as data

with open("conf.json") as file:
    conf = json.loads(file.read())

currentTime = strftime("%H:%M:%S")
currentDay = strftime("%d.%m")

# Todo:
# Falls der Server nicht Antwortet, sollte das Aufgezeichnet werden.
#
# try:
#     SensorDataSQL(currentDay, currentTime, data.temperatur(), data.humidity(), data.pm2_5(), data.pm10(), data.wlan_signal()).insert_data()
# except:
#     SensorDataSQL(None, None, None, None, None,None, None).insert_data()



# if(data.temperatur() or
#         data.humidity() or
#         data.pressure() or
#         data.pm2_5() or
#         data.pm10() or
#         data.wlan_signal() == "null"
#         ):# or data.connectionState() == False):
#     print("asd")

print(data.json_each_sensor("SDS_P1"))

# # sendMessage("SQL Datenbank bekommt ein Signal")
