import requests
import json
import datetime

req = requests.get("https://www.bitstamp.net/api/v2/ticker/btceur/")

content = req.content.decode("utf-8")

data = json.loads(content)

btc = data['last']

timestamp = data['timestamp']
timestampFloat = float(timestamp)

time = datetime.datetime.fromtimestamp(timestampFloat).strftime('%H:%M:%S, %Y-%m-%d')


with open("btc.txt", "a") as btcFile:
        btcFile.write(btc + " - " + time)
