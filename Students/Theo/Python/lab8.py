from random import randint as random
computer = random(1,10)
count = 0
while count <10:
    user = input('Pick a number between 1 and 10: ')
    user = int(user)
    count += 1
    if user == computer:
        print(f'Correct! You guessed {count} times.')
        break
    else:
        print('Try again!')
