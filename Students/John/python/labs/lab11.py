"""

all codes are written and created by John Robson Wed Mar 10, 2021

"""

# Version 1

def run_version1(amount):
    
    coins = [("quarters", 25), ("dimes", 10), ("nickles", 5), ("pennies", 1)]
    
    def make_change(amount, value):
        return int(amount // value)
    
    for c, v in coins:
        amount = round(amount, 2) 
        qty_coins = make_change(amount, v)
        amount -= qty_coins * v
        print(f"{c}: {qty_coins}")


# Version 2

def run_version2(amount):
    coins = [
        ("half-dollars", 50),
        ("quarters", 25),
        ("dimes", 10),
        ("nickels", 5),
        ("pennies", 1)
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

def run_version3(amount):
    coins = {
        "half-dollars": 50,
        "quarters": 25,
        "dimes": 10,
        "nickels": 5,
        "pennies": 1
        }
    
    change = {}
    
    for k, v in coins.items():
        change[k] = int(amount // v)
        amount -= change[k] * v

    print(change)
    
    
versions = [run_version1, run_version2, run_version3]

while True:
    strategy = 0

    print('Welcome. You can type "done" at any time to exit.')

    m = len(versions)

    while strategy not in range(1, m + 1):
        try:
            strategy = input(f"Which version would you like to run: 1 - {m}")
            if strategy == "done":
                break
            strategy = int(strategy)
        except:
            continue
        if strategy == "done":
            break

    strategy = versions[strategy - 1]
    
    amount = -1
    
    while True:
        try:
            while amount < 0 or amount > 100:
                amount = float(input("Please enter amount including decimals"))
            break
        except:
            continue

    strategy(amount * 100)