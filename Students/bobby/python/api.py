import requests

print ("Welcome to find the weather")
city = input("Enter the city: ").capitalize()
country = input("Enter the country: ").upper()

response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid=306d729ea7af7b631b2aa2b9cf6654a6")

data = response.json()

weather = (data["weather"][0]["description"])
temp = (data["main"]["temp"])
wind_speed = (data["wind"]["speed"])

print (f"The weather in {city} is {weather} with a wind speed of {wind_speed} and the temperature is {temp}. ")

