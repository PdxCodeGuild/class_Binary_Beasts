"""

all codes are written and created by John Robson Thu Mar 18, 2021

"""

import requests
from string import ascii_letters as letters
response = ""

while True:
    
    print("Welcome to the Recipe Finder.")
    
    if response == "":
        while True:
            ingredients = input("Please list ingredients to search by separated with a comma (,): ")
            if all(x in (letters + " " + ",") for x in ingredients):
                ingredients = str(ingredients.replace(" ",""))
                break
            
        url = f"http://www.recipepuppy.com/api/?i={ingredients}"

        response = requests.get(url);
        response = response.json()
    
    try:
        i = 0
        x = min(10, len(response["results"]))
        print("\n\nRECIPES: \n")
        while i < x:
            print("Recipe " + str(i + 1) + ": " + response["results"][i]["title"].replace("\n",""))
            i += 1
    except:
        print("Unable to retrieve data. Please try again.")
        continue
    
    while True:
        i = input("\n\nWhich recipe would you like to view? Enter a number between 1 and " + str(x) + " ")
        
        try:
            i = int(i)
            if i in range(1, x + 1):
                i -= 1
                break
        except:
            print("Invalid response. Please enter a recipe number from 1 - " + str(x) + " ")
            continue
        
    print("\n\n\nNAME: " + response["results"][i]["title"])
    print("\nLINK: " + response["results"][i]["href"])
    print("\nINGREDIENTS: " + response["results"][i]["ingredients"] + "\n\n\n")
    
    again = ""
    while again not in ["yes", "no"]:
        again = input("Get another recipe?").lower()
        
    if again == "no":
        print("Goodbye.")
        break
    
    same = ""
    while same not in ["yes", "no"]:
        same = input("Keep same ingredients?").lower()
    
    if same == "no":
        response = ""