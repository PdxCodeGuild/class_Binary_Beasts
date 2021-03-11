"""

all codes are written and created by John Robson Wed Mar 10, 2021

"""

# Version 1

def unitConverterVersion1():
    v1Dict = {
        "feet": 0.3048
    }
    feet = int(input("What is the distance in feet? "))
    m = feet * v1Dict["feet"]
    m = str(round(m, 4))
    print(f"{feet}ft is {m}m.")
    
# Version 2 + 3

def unitConverterVersion2And3():
    v3Dict = {
        "ft": 0.3048,
        "mi": 1609.34,
        "m": 1,
        "km": 1000,
        "yd": 0.9144,
        "in": 0.0254
    }
    amount = int(input("What is the distance?"))
    unit = input("What is the unit? (ft, mi, m, km, yd, in").lower()
    m = amount * v3Dict[unit]
    m = str(round(m, 4))
    print(f"{amount}{unit} is {m}m")

# Extra Challenge

def unitConverterExtraChallenge():
    fromDict = {
        "ft": 0.3048,
        "mi": 1609.34,
        "m": 1,
        "km": 1000,
        "yd": 0.9144,
        "in": 0.0254
    }
    
    toDict = {
        "ft": 3.28084,
        "mi": 0.000621371,
        "m": 1,
        "km": 0.001,
        "yd": 1.09361,
        "in": 39.3701
    }
    
    fromAmount = int(input("What is the distance?"))
    fromUnit = input("Convert from what unit? (ft, mi, m, km, yd, in)").lower()
    toUnit = input("Convert to what unit? (ft, mi, m, km, yd, in)").lower()
    m = fromAmount * fromDict[fromUnit]
    toAmount = m * toDict[toUnit]
    toAmount = str(round(toAmount, 4))
    print(f"{fromAmount}{fromUnit} is {toAmount}{toUnit}")
    
    
versions = [unitConverterVersion1, unitConverterVersion2And3, unitConverterExtraChallenge]

while True:
    strategy = 0

    print('Welcome. You can type "done" at any time to exit.')

    while strategy < 1 or strategy > 3:
        strategy = int(input("Which version would you like to run: 1 - 3"))
        if strategy == "done":
            break
        
    if strategy == "done":
        break

    strategy = versions[strategy - 1]

    strategy()