"""

all codes are written and created by John Robson Wed Mar 10, 2021

"""

import random

# Approach 1

choices = ["rock", "paper", "scissors"]

def run_approach1():

    while True:

        print("Welcome to Rock, Paper, Scissors. Type 'done' at any time to exit")
        computer = random.choice(choices)
        user = ""

        while user not in choices:
            user = input(
                'Choose either: "rock", "paper", or "scissors":').lower()
            if user == "done":
                break

        if user == "done":
            break

        u = choices.index(user)
        c = choices.index(computer)
        if c - 1 < 0:
            c = 3
        if user == computer:
            print("You tied")
        elif u == (c - 1):
            print("You lose!")
        else:
            print("You win!")
        print(f"You chose {user}, computer chose {computer}")


# Approach 2

def run_approach2():
    win = [(0, 2), (1, 0), (2, 1)]

    while True:

        print("Welcome to Rock, Paper, Scissors. Type 'done' at any time to exit")
        computer = random.choice(choices)
        user = ""

        while user not in choices:
            user = input(
                'Choose either: "rock", "paper", or "scissors":').lower()
            if user == "done":
                break

        if user == "done":
            break

        if user == computer:
            print("You tied")
        elif (choices.index(user), choices.index(computer)) in win:
            print("You win")
        else:
            print("you lose")

        print(f"You chose {user}, computer chose {computer}")


approaches = [run_approach1, run_approach2]

while True:
    strategy = 0

    print('Welcome. You can type "done" at any time to exit.')

    m = len(approaches)
    
    while strategy not in range(1, m + 1):
        try:
            strategy = input(f"Which approach would you like to run: 1 - {m}")
            if strategy == "done":
                break
            strategy = int(strategy)
        except:
            continue
        if strategy == "done":
            break

    strategy = approaches[strategy - 1]

    strategy()