# Rock, Paper & Scissors with a while loop

import random

print ("Lets play Rock Paper Scissors")
question = input("Choose rock paper or scissors ")
random_answers = ["rock", "paper", "scissors"]
random_answers = random.choice(random_answers)

# All Tie
if random_answers == question:
    print(f"tie: {question}")
# Rock
if question == "rock" and random_answers == "paper":
    print(f"You Lose: {random_answers}")
if question == "rock" and random_answers == "scissors":
    print(f"You Win: {random_answers}")
# Paper
if question == "paper" and random_answers == "scissors":
    print(f"You Lose: {random_answers}")
if question == "paper" and random_answers == "rock":
    print(f"You Win: {random_answers}")
# Scissors
if question == "scissors" and random_answers == "rock":
    print(f"You Lose: {random_answers}")
if question == "scissors" and random_answers == "paper":
    print(f"You Win: {random_answers}")
