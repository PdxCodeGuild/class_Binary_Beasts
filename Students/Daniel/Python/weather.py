import requests
import json
from datetime import datetime



city_name = "Orcutt"
api_key = "8af2aa7fa978da0c3dc608a85406875c"



x = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")

x = json.loads(x.text)

x['sys']['sunrise'] = datetime.fromtimestamp(x['sys']['sunrise'])
x['sys']['sunset'] = datetime.fromtimestamp(x['sys']['sunset'])
digest = []
digest.append(("Weather:    ",x['weather'][0]['main'] ))
digest.append(("Visibility: ", x['visibility']))
digest.append(("Country:    ", x['sys']['country']))
digest.append(("Sunrise:    ", x['sys']['sunrise']))
digest.append(("Sunset:     ", x['sys']['sunset']))
for item in digest:
    print(f" {item[0]}    {item[1]}")
