import requests
import json
import sys

import config

args = sys.argv

channel = None
onoff = None

if len(args) <= 2:
    print('2 arguments are required.')
    exit()

channel = args[1]
if args[2] == "on":
    onoff = 1
elif args[2] == "off":
    onoff = 0

app_name = "merossPlug"
URL = "http://{}/config".format(config.ip_address)

header = {
    "from": URL,
    "messageId": config.messageId,
    "method": "SET",
    "namespace": "Appliance.Control.ToggleX",
    "payloadVersion": 1,
    "sign": config.sign,
    "timestamp": config.timestamp,
    "triggerSrc": app_name
}

payload = {
    "togglex": {
        "channel": channel,
        "onoff": onoff
    }
}

data = {"header": header, "payload": payload}
headers = {'content-type': 'application/json'}

response = requests.request("POST", URL, data=json.dumps(data), headers=headers)

print(response)
