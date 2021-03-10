"""

all codes are written and created by John Robson Wed Mar 10, 2021

"""

# Version 1

def makeChange(amount):

    change = {"quarters": 0, "dimes": 0, "nickles": 0, "pennies": 0}

    change["quarters"] = int(amount // 0.25)
    amount -= change["quarters"] * 0.25
    change["dimes"] = int(amount // 0.10)
    amount -= change["dimes"] * 0.10
    change["nickles"] = int(amount // 0.05)
    amount -= change["nickles"] * 0.05
    change["pennies"] = int(amount // 0.01)
    amount -= change["pennies"] * 0.01

    print(change)


# Version 2

def makeChange2(amount):
    coins = [
        ("half-dollars", 0.5),
        ("quarters", 0.25),
        ("dimes", 0.10),
        ("nickels", 0.05),
        ("pennies", 0.01)
    ]

    change = {}

    for coin in coins:
        name = ""
        value = 0
        for c in coin:
            if type(c) == str:
                name = c
            else:
                value = c
        change[name] = int(amount // value)
        amount -= change[name] * value

    print(change)

# Version 3 (my own way of doing it)


def makeChange3(amount):
    coins = {
        "half-dollars": 0.5,
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
        }
    
    change = {}
    
    #python 3
    for c, v in coins.items():
        change[c] = int(amount // v)
        amount -= change[c] * v
        
    #python 2
    # for c, v in coins.iteritems():
    #     change[c] = int(amount // v)
    #     amount -= change[c] * v

    print(change)
    
versions = [makeChange, makeChange2, makeChange3]

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
    
    amount = ""
    
    while type(amount) != float:
        amount = float(input("Please enter amount including decimals"))

    strategy(amount)