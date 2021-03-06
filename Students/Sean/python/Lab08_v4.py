import random

def guesser(x):
    if guess == com:
        print(f"You guessed my number: {com}, after only {count} guesses!")
        
    
    elif lastguess != 0:
        if guess < com:
            if abs(guess-com) > abs(lastguess-com):
                print(f"Wrong {count} times so far!")
                print("Getting colder! Guess higher!")

            elif abs(guess-com) < abs(lastguess-com):
                print(f"Wrong {count} times so far!")
                print("Getting warmer! Guess higher!")

        elif guess > com:            
            if abs(guess-com) > abs(lastguess-com):
                print(f"Wrong {count} times so far!")
                print("Getting colder! Guess lower!")

            elif abs(guess-com) < abs(lastguess-com):
                print(f"Wrong {count} times so far!")
                print("Getting warmer! Guess lower!")
    else:
        if guess < com:
            print(f"Wrong {count} times so far!")
            print("Guess higher!")
        elif guess > com:
            print(f"Wrong {count} times so far!")
            print("Guess lower!")

com = random.randint(1,10)
count = 0
lastguess = 0

while True:
    try:

        guess = int(input("Guess the number I've chosen between 1 and 10.\n> "))
        if guess > 0 and guess < 11:
            count += 1
            guesser(guess)
            if guess == com:
                break
            else:
                lastguess = guess
    except Exception as exc:
        print(exc)