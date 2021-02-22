import sqlite3


class SensorDataSQL:
    def __init__(self, day, time, temperature, humidity, pressure, pm2_5, pm10, wlan_signal):
        self.day = day
        self.time = time
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.pm2_5 = pm2_5
        self.pm10 = pm10
        self.wlan_signal = wlan_signal

    def __repr__(self):
        return "Sensordaten('{}', '{}', {} , {} , {} , {} , {} , '{}')".format(self.day, self.time, self.temperature, self.humidity, self.pressure, self.pm2_5, self.pm10, self.wlan_signal)

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
                wlan_signal text
            )""")
        with connection:
            cc.execute("""INSERT INTO sensordaten VALUES(:day, :time, :temperature, :humidity, :pressure, :pm2_5,:pm10,:wlan_signal)""",{
                "day": self.day,
                "time": self.time,
                "temperature": self.temperature,
                "humidity": self.humidity,
                "pressure": self.pressure,
                "pm2_5": self.pm2_5,
                "pm10": self.pm10,
                "wlan_signal":self.wlan_signal})
        connection.close()

