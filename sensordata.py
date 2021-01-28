class SensorData:
    def __init__(self, uhrzeit, temperatur, luftfeuchtigkeit,pm2_5,pm10,wlan_signal):
        self.uhrzeit = uhrzeit
        self.temperatur = temperatur
        self.luftfeuchtigkeit = luftfeuchtigkeit
        self.pm2_5 = pm2_5
        self.pm10 = pm10
        self.wlan_signal = wlan_signal

    def __repr__(self):
        return "Sensordaten('{}', {}, {},{}, {}, '{}')".format(self.uhrzeit, self.temperatur, self.luftfeuchtigkeit,self.pm2_5, self.pm10, self.wlan_signal)