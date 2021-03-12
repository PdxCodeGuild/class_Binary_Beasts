"""

all codes are written and created by John Robson Wed Mar 10, 2021

"""

# Version 1

def run_version1():
    units = {
        "feet": 0.3048
    }
    feet = int(input("What is the distance in feet? "))
    m = feet * units["feet"]
    m = str(round(m, 4))
    print(f"{feet}ft is {m}m.")
    
# Version 2 + 3

def run_version2_and_3():
    units = {
        "ft": 0.3048,
        "mi": 1609.34,
        "m": 1,
        "km": 1000,
        "yd": 0.9144,
        "in": 0.0254
    }
    amount = int(input("What is the distance?"))
    unit = input("What is the unit? (ft, mi, m, km, yd, in").lower()
    m = amount * units[unit]
    m = str(round(m, 4))
    print(f"{amount}{unit} is {m}m")

# Extra Challenge

def run_version_extra():
    from_units = {
        "ft": 0.3048,
        "mi": 1609.34,
        "m": 1,
        "km": 1000,
        "yd": 0.9144,
        "in": 0.0254
    }
    
    to_units = {
        "ft": 3.28084,
        "mi": 0.000621371,
        "m": 1,
        "km": 0.001,
        "yd": 1.09361,
        "in": 39.3701
    }
    
    while True:
        try:
            from_amount = int(input("What is the distance? (in whole numbers)"))
            break
        except:
            continue
        
    from_unit = ""
    to_unit = ""
    
    while from_unit not in list(from_units.keys()):
        from_unit = input("Convert from what unit? (ft, mi, m, km, yd, in)").lower()
        
    while to_unit not in list(to_units.keys()):
        to_unit = input("Convert to what unit? (ft, mi, m, km, yd, in)").lower()
        
    m = from_amount * from_units[from_unit]
    to_amount = m * to_units[to_unit]
    to_amount = str(round(to_amount, 4))
    print(f"{from_amount}{from_unit} is {to_amount}{to_unit}")
    
    
versions = [run_version1, run_version2_and_3, run_version_extra]

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