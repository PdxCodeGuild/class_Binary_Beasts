"""

all codes are written and created by John Robson Thu Mar 18, 2021

"""

import requests
from string import ascii_letters as letters

country = ""; url = ""

while True:

    print("Welcome. Get Covid cases info from any country.")
    
    while True:
        country = input('Country (for US enter "US"): ').capitalize()
        if all(x in (letters + " ") for x in country):
            break
        
    if url == "":
        url = f"https://covid-api.mmediagroup.fr/v1/cases?country={country}"
        url2 = f"https://covid-api.mmediagroup.fr/v1/cases?ab=US"
    
    if country.upper() == "US":
        url = url2

    response = requests.get(url);
    response = response.json()
    
    try: 
        responseA = response["All"]
        confirmed = responseA["confirmed"]
        deaths = responseA["deaths"]
        print("\n\nInfo for " + country)
        print("Confirmed cases: " + str(confirmed))
        print("Death cases: " + str(deaths) + "\n")
    except:
        print("Unable to retrieve data. Please try again.")
        continue
    
    if country.upper() == "US":
        while True:
            state = ""
            while state == "":
                state = input("Would you like to see an individual state?")
            
                if state.lower() == "no":
                    break
                else:
                    while True:
                        state = input('Enter state (must capitalize first letter of each word): ')
                        if not all(x in (letters + " ") for x in state):
                            state = ""
                        else:
                            break
                            
            if state == "no":
                break
            else:
                try:
                    responseA = response[state]
                    confirmed = responseA["confirmed"]
                    deaths = responseA["deaths"]
                    print("\n\nInfo for " + state)
                    print("Confirmed cases: " + str(confirmed))
                    print("Death cases: " + str(deaths) + "\n")
                    
                    state = ""
                        
                except:
                    print("Unable to retrieve data. Please try again.")
                    continue
                    
                
    
    again = ""
    while again not in ["yes", "no"]:
        again = input("Check more info?").lower()
        
    if again == "no":
        print("Goodbye.")
        break