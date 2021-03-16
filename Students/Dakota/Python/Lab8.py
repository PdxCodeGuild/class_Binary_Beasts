"""
#Lab 8 Version 1
#import modules
import random
#assign x to a random number 1 through 10
x = random.randint(1,10)
#ask for user input
user_guess = int(input('Guess the number '))
i = 0 
#assign count to 0
count = 0
#keep track of count by adding one
count += 1
while i < 9:
    #if user guesses the random number
    if user_guess == x:
        print(f'correct! you guessed {count} times.')
    #if user does not guess the random number 
    else:
        if i < 10:
            print('try again!')
            print(int(input('Guess the number ')))
            #increment by 1
            i += 1
        if i == 10:
            print(f'You have guessed 10 times')

#Lab 8 Version 2
#import modules
import random
#assign x to a random number 1 through 10
x = random.randint(1,10)
#ask for user input
user_guess = int(input('Guess the number '))
#assign count to 0
count = 0
count += 1
#begin Repl
while True:
    #if user guesses the random number
    if user_guess == x:
        print(f'correct! you guessed {count} times.')
        break
    #if user does not guess the random number 
    else:
        if user_guess != x:
            print('try again!')
            print(int(input('Guess the number ')))
            continue
        if user_guess == x:
            print(f'You have guessed {count} times')
            break
"""
#Lab 8 Version 3
#import modules
import random
#assign x to a random number 1 through 10
x = random.randint(1,10)
#assign count to 0
count = 0
#begin Repl
while True:
    #ask for user input
    user_guess = int(input('Guess the number '))
    #if user guesses the random number
    if user_guess == x:
        print(f'correct! you guessed {count} times.')
        break
    #if user does not guess the random number 
    elif user_guess < x:
        print('too low!')
        count += 1
    elif user_guess > x:
        print('too high!')
        count += 1