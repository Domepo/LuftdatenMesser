import requests
import json
from time import gmtime, strftime

from modules.sql.sensorDataSql import SensorDataSQL
from modules.telegram_bot.telegrambot import sendMessage
import modules.fetchSensorData.dataFetch as data

with open("conf.json") as file:
    conf = json.loads(file.read())

currentTime = strftime("%H:%M:%S")
currentDay = strftime("%d.%m.%y")


def push_data_to_sql():
    if(data.test_request() != None):
        SensorDataSQL(currentDay, currentTime, data.sensor("BME280_temperature"),data.sensor("BME280_humidity"),data.sensor("BME280_pressure"), data.sensor("SDS_P2"), data.sensor("SDS_P1"), data.sensor("signal")).insert_data()
        print("Daten wurden in die sql gepushed")
    else:
       print("Es konnte keine Verbindung zu "+data.url()+" hergestellt werden")
       sendMessage("Es konnte keine Verbindung hergestellt werden\n"+str(currentTime)+"\n"+ str(currentDay)+"\n"+"URL: "+data.url())
push_data_to_sql() 
 
