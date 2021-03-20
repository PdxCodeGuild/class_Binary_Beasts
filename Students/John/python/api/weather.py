"""

all codes are written and created by John Robson Thu Mar 18, 2021

"""

import requests
from string import ascii_letters as letters

key = "884cfd64f3a52a3354c76c381207cf1e"
key1 = "8af2aa7fa978da0c3dc608a85406875c"
city = ""

while True:

    print("Welcome. Find the weather info in your city.")
    
    if city == "":
        while True:
            city = input("Please enter city name: ")
            if all(x in (letters + " ") for x in city):
                break

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

    response = requests.get(url);
    response = response.json()
    print(response)
    
    if int(response["cod"]) != 200:
        response = requests.get(url + "1")
        response = response.json()
    
    print(response)
    
    options = ["humidity", "temperature", "feels like", "low", "high", "pressure", "all"]
    keys = ["humidity", "temp", "feels_like", "temp_min", "temp_max", "pressure"]
    
    print("What would you like to know?")
    while True:
        option = input("The options are: Humidity, Temperature, Feels Like, Low, High, Pressure, or All.\n").lower()
        
        if option in options:
            break
        else:
            print("Invalid answer.")
    
    try:
        if option == "all":
            for k in keys:
                data = response["main"][k]
                print(f"The {options[keys.index(k)]} in {city.capitalize()} is {data}.")
        else:
            opt = response["main"][keys[options.index(option)]]
            print(f"The {option} in {city.capitalize()} is {opt}")
    except:
        print("Unable to retrieve data. Please try again.")
        city = ""
        continue  
    
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