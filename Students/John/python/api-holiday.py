"""

all codes are written and created by John Robson Thu Mar 18, 2021

"""

import requests
from string import ascii_letters as letters

while True:
    
    print("Welcome to the Name Nationality Estimator. Enter your name to estimate your nationality.")
    
    while True:
        name = input("Name: ")
        if all(x in letters for x in name):
            break
        
    url = f"https://api.nationalize.io?name={name}"

    response = requests.get(url);
    response = response.json()
    
    try:
        line1 = f"Name: {name.capitalize()}"
        line2 = f"First Guess: {response['country'][0]['country_id']} | Probability: "\
            f"{round(response['country'][0]['probability'] * 100, 1)}%"
        line3 = f"Second Guess: {response['country'][1]['country_id']} | Probability: "\
            f"{round(response['country'][1]['probability'] * 100, 1)}%"
        line4 = f"Third Guess: {response['country'][2]['country_id']} | Probability: "\
            f"{round(response['country'][2]['probability'] * 100, 1)}%"
        print(line1)
        print(line2)
        print(line3)
        print(line4)
    except:
        print("Name not found. Please try again.")
        continue
    
    again = ""
    while again not in ["yes", "no"]:
        again = input("Check another name?").lower()
        
    if again == "no":
        print("Goodbye.")
        break