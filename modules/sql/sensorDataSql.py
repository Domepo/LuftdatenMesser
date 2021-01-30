import sqlite3


class SensorDataSQL:
    def __init__(self, uhrzeit, temperatur, luftfeuchtigkeit, pm2_5, pm10, wlan_signal):
        self.uhrzeit = uhrzeit
        self.temperatur = temperatur
        self.luftfeuchtigkeit = luftfeuchtigkeit
        self.pm2_5 = pm2_5
        self.pm10 = pm10
        self.wlan_signal = wlan_signal

    def __repr__(self):
        return "Sensordaten('{}', {}, {},{}, {}, '{}')".format(self.uhrzeit, self.temperatur, self.luftfeuchtigkeit, self.pm2_5, self.pm10, self.wlan_signal)

    def insert_data(self):
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
        with connection:
            cc.execute("""INSERT INTO sensordaten VALUES(:uhrzeit,:temperatur,:luftfeuchtigkeit,:pm2_5,:pm10,:wlan_signal)""",{
                "uhrzeit": self.uhrzeit,
                "temperatur": self.temperatur,
                "luftfeuchtigkeit": self.luftfeuchtigkeit,
                "pm2_5": self.pm2_5,
                "pm10": self.pm10,
                "wlan_signal":self.wlan_signal})
        connection.close()

#     def pushSQL(self):
#         insert_data(pp)



# pp= SensorDataSQL("00:01","asd","as","f","g","46 Db")        
