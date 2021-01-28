import sqlite3
from sensordata import SensorData
import random
import requests

# import the luftdaten api
r = requests.get('luftdatenURL', auth=('user', 'pass'))
r.status_code
connection = sqlite3.connect("sensorDaten.db")

cc = connection.cursor()

cc.execute("""CREATE TABLE IF NOT EXISTS sensordaten(
        uhrzeit text,
        temperatur REAL,
        luftfeuchtigkeit REAL,
        pm2_5 REAL,
        pm10 REAL,
        wlan_signal text
    )""")

def insert_data(sensor_data):
    with connection:
        cc.execute("""INSERT INTO sensordaten VALUES(:uhrzeit,:temperatur,:luftfeuchtigkeit,:pm2_5,:pm10,:wlan_signal)""",{
            "uhrzeit": sensor_data.uhrzeit,
            "temperatur": sensor_data.temperatur,
            "luftfeuchtigkeit": sensor_data.luftfeuchtigkeit,
            "pm2_5": sensor_data.pm2_5,
            "pm10": sensor_data.pm10,
            "wlan_signal":sensor_data.wlan_signal})

pp= SensorData("00:01",random.randint(1,1239),random.randint(1,1239),random.randint(1,1239),random.randint(1,1239),"46 Db")
insert_data(pp)

connection.close()