from urllib.parse import quote
import requests
import json
import time
from ruuvitag_sensor.ruuvi import RuuviTagSensor

macs = [
    'E5:FC:01:6E:36:3F'
]

# This should be enough that we find at least one result for each
timeout_in_sec = 4

url = 'https://co2.awareframework.com:8443/insert'

datas = RuuviTagSensor.get_data_for_sensors(macs, timeout_in_sec)

# Use Requests to POST datas in json-format
# Encode mac as it contains semicolon, which is reserved character
for key, value in datas.items():
    # url e.g.: http://localhost:8000/data/F4%3AA5%3A74%3A89%3A16%3A57
    # json e.g.: {"temperature": 24.0, "humidity": 38.0, "pressure": 1018.0}
	
    ruuviData = {
        "tableName": "IndoorsTag",
	"deviceId" : macs[0],
        "timestamp" : int(round(time.time() * 1000)),
        "data" : json.dumps(value)
    }

    requests.post(url, json=ruuviData)
