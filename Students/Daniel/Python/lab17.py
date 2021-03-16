import requests
from datetime import datetime
# turn a string into a datetime object
date = datetime.strptime('25-MAR-2016', '%d-%b-%Y')

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')
print(response.text)
with open('hayden_island.rain', 'r') as file:
    text = file.read()
print(text)