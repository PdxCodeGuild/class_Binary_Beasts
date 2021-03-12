import random

com = random.randint(1,10)
count = 0
lastguess = 0

while True:
    guess = int(input("Guess the number I've chosen between 1 and 10.\n> "))
    count += 1
    lastguess += guess
    if guess == com:
        print(f"You guessed my number: {com}, after only {count} guesses!")
        break
        
    elif guess < com:
            print("Guess higher!")

    elif guess > com:            
            print("Guess lower!")

    print(f"Wrong {count} times so far!")