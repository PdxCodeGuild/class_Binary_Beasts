from random import randint as random

computer = random(1,10)

count = 0

last_guess = 0

while True:
    user = input('Pick a number between 1 and 10: ')
    
    user = int(user)
    
    count += 1
    
    if user == computer:
        print(f'Correct! You guessed {count} times.')
        break
    
    if count > 1:
        if abs(user - computer) > abs(last_guess - computer):
            print('Colder')
        elif abs(user - computer) < abs(last_guess - computer):
            print('Warmer')
            
    elif user > computer:
        print('Too high!')

    
    elif user < computer:
        print('Too low!')
    
    last_guess = user



