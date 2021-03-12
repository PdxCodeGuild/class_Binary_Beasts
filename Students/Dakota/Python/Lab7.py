#Lab 7
#import modules
import random
#define list of choices
choices = ('✊', '✋', '✌')
#Ask user what their choice would like to be
user_move = input('What is your move: ✊, ✋, ✌')
#define computer move using random.choice
computer_move = random.choice(choices)
#prints users input
print(f'You chose {user_move}')
#prints computers choice
print(f'The computer chose {computer_move}')
while True: 

    #user and computer choose the same move
    if user_move == computer_move:
        print('Looks like yall tied')
        break
    #user chooses rock scenarios
    elif user_move == "✊":
        # check to see who won
        if computer_move == "✌":
            print("You win!")
            break
    elif user_move == "✊":
        # check to see who won
        if computer_move == "✋":
            print("You lose!")
            break
    #user chooses paper scenarios
    elif user_move == "✋":
        # check to see who won
        if computer_move == "✌":
            print("You lose!")
            break
    elif user_move == "✋":
        # check to see who won
        if computer_move == "✊":
            print("You win!")
            break
    #user chooses paper scenarios
    elif user_move == "✌":
        # check to see who won
        if computer_move == "✊":
            print("You lose!")
            break
    elif user_move == "✌":
        # check to see who won
        if computer_move == "✋":
            print("You win!")
            break