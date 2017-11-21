import requests
import json
import datetime

req = requests.get("https://www.bitstamp.net/api/v2/ticker/btceur/")

content = req.content.decode("utf-8")

loaded1 = json.loads(content)

btc = loaded1['last']

timestampFloat = float(loaded1['timestamp'])

time = datetime.datetime.fromtimestamp(timestampFloat).strftime('%H:%M:%S, %Y-%m-%d')


with open("btc.txt", "a") as btcFile:
        btcFile.write(btc + " - " + time)
