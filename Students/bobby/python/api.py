import requests
from secrets import op_weather_api # imports the key

print ("Welcome to find the weather")
city = "McMinnville" #input("Enter the city: ").capitalize()
country = "USA" #input("Enter the country: ").upper()

response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={op_weather_api}")

data = response.json()

weather = (data["weather"][0]["description"])
temp = (data["main"]["temp"])
wind_speed = (data["wind"]["speed"])

print (f"The weather in {city} is {weather} with a wind speed of {wind_speed} and the temperature is {temp}. ")

