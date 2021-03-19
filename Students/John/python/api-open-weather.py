"""

all codes are written and created by John Robson Thu Mar 18, 2021

"""

import requests

key = "884cfd64f3a52a3354c76c381207cf1e"
city = ""

while True:

    print("Welcome. Find the weather info in your city.")
    if city == "":
        city = input("Please enter city name: ")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

    response = requests.get(url);
    response = response.json()
    
    options = ["humidity", "temperature", "feels like", "low", "high", "pressure"]
    keys = ["humidity", "temp", "feels_like", "temp_min", "temp_max", "pressure"]
    
    print("What would you like to know?")
    while True:
        option = input("The options are: Humidity, Temperature, Feels Like, Low, High, or Pressure.\n").lower()
        
        if option in options:
            break
        else:
            print("Invalid answer.")
    
    opt = response["main"][keys[options.index(option)]]
    print(f"The {option} in {city} is {opt}")
    
    again = ""
    while again not in ["yes", "no"]:
        again = input("Check more info?").lower()
        
    if again == "no":
        print("Goodbye.")
        break
    
    same = ""
    while same not in ["yes", "no"]:
        same = input("Use the same city?").lower()
        
    if same == "no":
        city = ""