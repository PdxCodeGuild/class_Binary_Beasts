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
            break;

    url = f"https://api.nationalize.io?name={name}"

    response = requests.get(url);
    response = response.json()
    print(response)
    
    print(f"Name: {name.capitalize()}")
    print(f"First Guess: {response['country'][0]['country_id']} | Probability: "\
        f"{round(response['country'][0]['probability'], 3)}%")
    print(f"Second Guess: {response['country'][1]['country_id']} | Probability: "\
        f"{round(response['country'][1]['probability'], 3)}%")
    print(f"Third Guess: {response['country'][2]['country_id']} | Probability: "\
        f"{round(response['country'][2]['probability'], 3)}%")
    
    again = ""
    while again not in ["yes", "no"]:
        again = input("Check another name?").lower()
        
    if again == "no":
        print("Goodbye.")
        break