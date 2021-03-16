import random

def guesser(x):
    if guess == com:
        return f"You guessed my number: {com}, after only {count} guesses!"

    elif lastguess != 0:
        if guess < com:
            if abs(guess-com) > abs(lastguess-com):
                print(f"Wrong {count} times so far!")
                return f"Getting colder! Guess higher!"

            elif abs(guess-com) < abs(lastguess-com):
                print(f"Wrong {count} times so far!")
                return f"Getting warmer! Guess higher!"

        elif guess > com:            
            if abs(guess-com) > abs(lastguess-com):
                print(f"Wrong {count} times so far!")
                return f"Getting colder! Guess lower!"

            elif abs(guess-com) < abs(lastguess-com):
                print(f"Wrong {count} times so far!")
                return f"Getting warmer! Guess lower!"
    else:
        if guess < com:
            print(f"Wrong {count} times so far!")
            return "Guess higher!"



com = random.randint(1,10)
count = 0
lastguess = 0





while True:
    count += 1
    guess = int(input("Guess the number I've chosen between 1 and 10.\n> "))
    print(guesser(guess))
    lastguess += guess
