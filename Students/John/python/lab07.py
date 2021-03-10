"""

all codes are written and created by John Robson Wed Mar 10, 2021

"""

import random

choices = ["rock", "paper", "scissors"]

while True:

    print("Welcome to Rock, Paper, Scissors. Type 'done' at any time to exit")
    computer = random.choice(choices)
    user = ""

    while user not in choices:
        user = input('Choose either: "rock", "paper", or "scissors":').lower()
        if user == "done":
            break
        
    if user == "done":
        break

    if user == computer:
        print("You tied")
    elif (user == "rock" and computer == "scissors") or \
        (user == "paper" and computer == "rock") or \
        (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")
