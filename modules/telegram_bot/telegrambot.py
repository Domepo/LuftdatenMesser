import requests
import json
import random


#Config file
with open("conf.json") as file:
    conf = json.loads(file.read())
token = conf["token"]
chat_id = conf["chat_id"]

def sendMessage(text):
    requests.get(f"https://api.telegram.org/bot{token}/getUpdates")
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    params = {"chat_id":chat_id, "text":text}

    requests.post(url, params=params)
