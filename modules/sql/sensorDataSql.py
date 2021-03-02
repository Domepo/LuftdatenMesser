import sqlite3


class SensorDataSQL:
    def __init__(self, day, time, temperature, humidity, pressure, pm2_5, pm10, wlan_signal, owm_temperature, owm_pressure, owm_humidity, owm_speed, owm_deg, owm_id):
        # sensor
        self.day = day
        self.time = time
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.pm2_5 = pm2_5
        self.pm10 = pm10
        self.wlan_signal = wlan_signal
        # omw
        self.owm_temperature = owm_temperature
        self.owm_pressure = owm_pressure
        self.owm_humidity = owm_humidity
        self.owm_speed = owm_speed
        self.owm_deg = owm_deg
        self.owm_id = owm_id

    def __repr__(self):
        return "Sensordaten('{}', '{}', {} , {} , {} , {} , {} , '{}', {} , {} , {} , {} , {} ,{})".format(
        # sensor
        self.day,
        self.time, 
        self.temperature,
        self.humidity,
        self.pressure, 
        self.pm2_5,
        self.pm10,
        self.wlan_signal,
        # omw
        self.owm_temperature, 
        self.owm_pressure,
        self.owm_humidity,
        self.owm_speed,
        self.owm_deg,
        self.owm_id)

    def insert_data(self):
        connection = sqlite3.connect("modules/sql/sensorDaten.db")
        cc = connection.cursor()
        cc.execute("""CREATE TABLE IF NOT EXISTS sensordaten(
                day text,
                time text,
                temperature integer,
                humidity REAL,
                pressure REAL,
                pm2_5 REAL,
                pm10 REAL,
                wlan_signal text,
                owm_temperature REAL,
                owm_pressure REAL,
                owm_humidity REAL,
                owm_speed REAL,
                owm_deg REAL,
                owm_id integer
            )""")
        with connection:
            cc.execute("""INSERT INTO sensordaten VALUES(:day, 
            :time, 
            :temperature, 
            :humidity, 
            :pressure, 
            :pm2_5,:pm10,
            :wlan_signal ,
            :owm_temperature, 
            :owm_pressure, 
            :owm_humidity, 
            :owm_speed, 
            :owm_deg,
            :owm_id)""",{
                # sensor
                "day": self.day,
                "time": self.time,
                "temperature": self.temperature,
                "humidity": self.humidity,
                "pressure": self.pressure,
                "pm2_5": self.pm2_5,
                "pm10": self.pm10,
                "wlan_signal":self.wlan_signal,
                # omw
                "owm_temperature": self.owm_temperature,
                "owm_pressure": self.owm_pressure,
                "owm_humidity": self.owm_humidity,
                "owm_speed": self.owm_speed,
                "owm_deg": self.owm_deg,
                "owm_id":self.owm_id})
        connection.close()

