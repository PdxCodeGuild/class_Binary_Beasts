"""

all codes are written and created by John Robson Thu Mar 18, 2021

"""

import requests

while True:
    
    print("Welcome to the Computer Programmer Joke Teller.")
        
    url = "https://official-joke-api.appspot.com/jokes/programming/random"

    response = requests.get(url);
    response = response.json()
    print("\n\nJOKE:")
    print(response[0]["setup"])
    print(response[0]["punchline"] + "\n")
    
    again = ""
    while again not in ["yes", "no"]:
        again = input("Get another joke?").lower()
        
    if again == "no":
        print("Goodbye.")
        break