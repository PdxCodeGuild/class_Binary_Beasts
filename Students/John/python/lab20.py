"""

all codes are written and created by John Robson Fri Mar 12, 2021

"""

import random

#Version 1 and 2

while True:
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
        
        if match == 1:
            balance += 4
            earnings += 4
        elif match == 2:
            balance += 7
            earnings += 7
        elif match == 3:
            balance += 100
            earnings += 100
        elif match == 4:
            balance += 50000
            earnings += 50000
        elif match == 5:
            balance += 1000000
            earnings += 1000000
        elif match == 6:
            balance += 25000000
            earnings += 25000000
            
        i += 1
        
    roi = (earnings - expenses) / expenses
            
    print(balance)
    print(roi)
    
    again = ""
    while again != "no" and again != "yes":
        again = input("Try again?")
    
    if again == "no":
        break