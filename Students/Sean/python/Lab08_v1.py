import random

com = random.randint(1,10)
count = 0
while count < 10:
    guess = int(input("Guess the number I've chosen between 1 and 10.\n> "))
    count += 1
    if guess == com:
        print(f"You guessed my number: {com}!")
        break
    else:
        print("Wrong!")
if count >= 10:
    print("You've lost.")