import requests

API_key = "e88c57203580be0fd0cdcacd5106a024"

country_code = "us"
zip_code = '97217'

response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?zip={zip_code},us&units=imperial&appid={API_key}")
data = response.json()

best_day = []

for x in range(len(data['list'])):
    best_day.append(data['list'][x]['main']['temp_max'])
    best_day.sort()

print(f"The highest temperature in the next five days will be: {best_day[-1]}")