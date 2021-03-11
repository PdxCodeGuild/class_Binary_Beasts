import random

choices = ["rock", "paper", "scissors"]
winning_outcomes = ['rockpaper','rockscissors', 'paperrock','scissorspaper']

user_choice = input("Welcome to Rock Paper Scissors, please enter one of the three: ")
computer_choice = random.choice(choices)

if user_choice == computer_choice:
        print(f"Tie! The computer chose {computer_choice} and you chose {user_choice}")
elif user_choice + computer_choice in winning_outcomes:
        print(f"You won! The computer chose {computer_choice} and you chose {user_choice}")
else:
        print(f"You lose! :( The computer chose {computer_choice} and you chose {user_choice}")
