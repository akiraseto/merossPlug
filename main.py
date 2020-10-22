import requests
import json

import config

app_name = "merossPlug"
URL = "http://{}/config".format(config.ip_address)

channel = 1
onoff = 1

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
