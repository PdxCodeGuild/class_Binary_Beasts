'''
**************************
Theo Cocco
Lab7: Rock, Paper, Scissors
**************************
'''

from random import choice

def winner(x,y):
    if x == y:
        return 'you tied'
    elif x == 'rock' and y == 'scissors':
        return 'you win'
    elif x == 'rock' and y == 'lizard':
        return 'you win'
    elif x == 'paper' and y == 'rock':
        return 'you win'
    elif x == 'paper' and y == 'spock':
        return 'you win'
    elif x == 'scissors' and y == 'lizard':
        return 'you win'
    elif x == 'scissors' and y == 'paper':
        return 'you win'
    elif x == 'lizard' and y == 'paper':
        return 'you win'
    elif x == 'lizard' and y == 'spock':
        return 'you win'
    elif x == 'spock' and y == 'rock':
        return 'you win'
    elif x == 'spock' and y == 'scissors':
        return 'you win'
    else:
        return 'you lose'

while True:
    choices =['rock', 'paper', 'scissors', 'lizard', 'spock']

    user = input('rock, paper, scissors, lizard, or spock? ')
     
    computer = choice(choices)
    

    print(f'You chose {user}, and the computer chose {computer}, {winner(user, computer)}.')
    
    play_again = input('Would you like to play again? Yes or no: ')
    if play_again == 'no':
        print('Good bye')
        break