# Rock, Paper & Scissors with a while loop

import random

choices = ["rock", "paper", "scissors"]

while True:
    print('Welcome to rock, Paper and Scissors. Type done to exit')
    computer = random.choice(choices)
    user = ""

    while user not in choices:
        user = input("Choose 'Rock, 'Paper' or 'Scissors' ").lower()
        if user == "done":
            print ('Thank you for playing')
            break

    if user == "done":
        break

    if user == computer:
        print ('You tied')
         
    elif user == "rock":
        if computer == "scissors":
            print ('You Win!!!')
        elif computer == "paper":
            print ('You Lose')

    elif user == "paper":
        if computer == "rock":
            print ('You Win!!!')
        elif computer == "scissors":
            print ('You Lose')

    elif user == "scissors":
        if computer == "paper":
            print ('You Win!!!')
        elif computer == "rock":
            print ('You Lose')