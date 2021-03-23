"""

all codes are written and created by John Robson Fri Mar 12, 2021

"""

import random

#Version 1 and 2

while True:
    high = 0
    wins = []
    while len(wins) < 6:
        wins.append(random.randint(1, 99))
    balance = 0
    earnings = 0
    expenses = 0
    
    i = 0
    while i < 100000:
        balance -= 2
        expenses += 2
        card = []
        while len(card) < 6:
            card.append(random.randint(1, 99))
        
        x = 0
        match = 0
        while x < 6:
            if wins[x] == card[x]:
                match += 1
            x += 1
        
        cashout = [(1, 4), (2, 7), (3, 100), (4, 50000), (5, 1000000), (6, 25000000)]

        for x, y in cashout:
            if x == match:
                if y > high:
                    high = y
                earnings += y
                balance += y
            
        i += 1
        
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