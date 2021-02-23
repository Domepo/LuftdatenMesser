import matplotlib.pyplot as plt

import sqlite3

#   connect to the sqliteDB
con = sqlite3.connect("SensorDaten.db")

cur = con.cursor()
pm10= []
time = []
temperature= []

# SQL DATA (SDS011, BME280)
# +----------+----------+-------------+----------+-----------+-------+------+-------------+
# |   day    |   time   | temperature | humidity | pressure  | pm2_5 | pm10 | wlan_signal |
# +----------+----------+-------------+----------+-----------+-------+------+-------------+
# | 23.02.21 | 01:45:01 |       23.73 |    31.48 | 100207.47 |  5.65 |    9 |         -63 |
# | 23.02.21 | 01:50:01 |       23.76 |    31.32 | 100206.97 |  5.68 | 8.65 |         -63 |
# | 23.02.21 | 01:55:01 |       23.72 |    31.32 | 100212.09 |   6.3 | 9.43 |         -64 |
# | 23.02.21 | 02:00:01 |       23.74 |    31.33 | 100217.28 |  5.43 | 9.38 |         -63 |
# | 23.02.21 | 02:05:01 |       23.74 |    31.33 | 100217.28 |  5.43 | 9.38 |         -63 |
# | 23.02.21 | 02:10:02 |       23.72 |    31.07 | 100209.38 |  5.68 | 8.63 |         -64 |
# | 23.02.21 | 02:15:02 |       23.74 |    31.52 | 100209.13 |  5.63 | 8.47 |         -63 |
# | 23.02.21 | 02:20:02 |       23.73 |    31.12 | 100202.03 |   6.1 | 8.88 |         -64 |
# +----------+----------+-------------+----------+-----------+-------+------+-------------+



#   row = (15.0,)
#   data = 15.0


for row in cur.execute('SELECT pm10 FROM sensordaten;'):
    # row from pm10 = (9, 8.65, 9.43 ...) 
    for data in row:
        # data from row = 
        # 9 
        # 8.65 
        # 9.43
        pm10.append(data)

for row in cur.execute('SELECT time FROM sensordaten;'):
    for data in row:
        time.append(data)

for row in cur.execute('SELECT temperature FROM sensordaten;'):
    for data in row:
        temperature.append(data)

plt.plot(time,pm10)
plt.plot(time,temperature)

plt.show()
con.close()
