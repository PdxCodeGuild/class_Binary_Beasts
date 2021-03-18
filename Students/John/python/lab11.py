"""

all codes are written and created by John Robson Wed Mar 10, 2021

"""

# Version 1

def run_version1(amount):

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

def run_version2(amount):
    coins = [
        ("half-dollars", 0.50),
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

def run_version3(amount):
    coins = {
        "half-dollars": 0.5,
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
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

    strategy(amount)