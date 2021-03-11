from random import randint as random

user = input('Pick a number between 1 and 10: ')
user = int(user)

count = 0

last_guess = 0

while True:
    computer = random(1,10)
    
    count += 1
    
    if computer == user:
        print(f'The computer got it! The computer guessed {count} times.')
        break
    
    if count > 1:
        if abs(computer - user) > abs(last_guess - user):
            print('Colder')
        elif abs(computer - user) < abs(last_guess - user):
            print('Warmer')
            
    elif computer > user:
        print('Too high!')

    
    elif computer < user:
        print('Too low!')
    
    last_guess = computer



