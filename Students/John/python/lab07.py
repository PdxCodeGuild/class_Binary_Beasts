import random

choices = ["rock", "paper", "scissors"]

while True:
    print("Welcome to Rock, Paper, Scissors. Type 'done' at any time to exit")

    computer = random.choice(choices)

    user = ""
    while user not in choices:
        user = input("Choose either 'rock', 'paper', or 'scissors': ").lower()

        if user == "done":
            break

    if user == "done":
        break
    
    if user == computer:
        print("Looks like a tie")

    elif user == "rock":
        if computer == "scissors":
            print("You win!")   
        else:
            print("Sorry, You lose.")

    elif user == "paper":
        if computer == "rock":
            print("You win!")
        else:
            print("Sorry, You lose.")

    elif user == "scissors":
        if computer == "paper":
            print("You win!")
        else:
            print("Sorry, You lose.")