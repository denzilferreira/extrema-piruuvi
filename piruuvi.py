from urllib.parse import quote
import requests
import json
import time
from ruuvitag_sensor.ruuvi import RuuviTagSensor

macs = [
    'E8:43:8F:32:C0:76'
]

timeout_in_sec = 4
url = 'https://pehmo.awareframework.com:8080/index.php/1/4lph4num3ric/ruuvi/insert'

datas = RuuviTagSensor.get_data_for_sensors(macs, timeout_in_sec)
datas[macs[0]]["timestamp"] = int(round(time.time() * 1000))

for key, value in datas.items():
    ruuviData = {
	"device_id" : macs[0],
        "data" : json.dumps([value])
    }

    print("Sent to server: %s", ruuviData)

    requests.post(url, ruuviData)
