"""

all codes are written and created by John Robson Fri Mar 12, 2021

"""

import random

#Version 1 and 2

while True:
    pick = 6
    high = 0
    wins = []
    while len(wins) < pick:
        wins.append(random.randint(1, 99))
    balance = 0
    earnings = 0
    expenses = 0
    
    for _ in range(100_000):
        balance -= 2
        expenses += 2
        card = []
        while len(card) < pick:
            card.append(random.randint(1, 99))
        
        match = 0
        for w, c in list(zip(wins, card)):
            match += 1 if w == c else 0
        
        cashout = [(1, 4), (2, 7), (3, 100), (4, 50_000), (5, 1_000_000), (6, 25_000_000)]

        for m, v in cashout:
            if m == match:
                if v > high:
                    high = v
                earnings += v
                balance += v
        
    roi = (earnings - expenses) / expenses
            
    print(balance)
    print(earnings)
    print(high)
    print(roi)
    
    again = ""
    while again != "no" and again != "yes":
        again = input("Try again?")
    
    if again == "no":
        break