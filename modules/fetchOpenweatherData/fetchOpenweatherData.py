import requests
import json

with open("conf.json") as file:
    conf = json.loads(file.read())

url = "https://api.openweathermap.org/data/2.5/weather?id="+conf["openweather_api_city_id"]+"&APPID="+conf["openwather_api_token"]+"&units=metric"
r = requests.get(url, auth=('user', 'pass'), timeout=3.000)
weather_data = json.loads(r.text)


def basic_weather_data():
    # basic_weather_json DATA:
    # temperature, feels_like, temp_min, temp_max, pressure, humidity,
    basic_weather_json = {}

    for basic_attr in weather_data["main"]:
        basic_weather_json[basic_attr] = weather_data["main"][basic_attr]

    for basic_attr in weather_data["weather"][0]:
        basic_weather_json[basic_attr] = weather_data["weather"][0][basic_attr]
    return basic_weather_json


def wind_cloud_weather_data():
    # wind_cloud_weather_json DATA:
    # speed, deg, clouds, visibility,
    wind_cloud_weather_json = {}
    for wind_cloud_attr in weather_data["wind"]:
        wind_cloud_weather_json[wind_cloud_attr] = weather_data["wind"][wind_cloud_attr]

    wind_cloud_weather_json["visibility"] = weather_data["visibility"]
    return wind_cloud_weather_json