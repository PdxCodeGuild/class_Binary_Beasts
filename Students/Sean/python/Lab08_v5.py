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

count = 0
lastguess = 0

while True:
    try:
        com = int(input("Pick a number between 1 and 10:    "))
        if com > 0 and com < 11:
            while True:
                count += 1
                guess = random.randint(1,10)
                guesser(guess)
                if guess == com:
                    break
                else:
                    lastguess = guess                
    except Exception as exc:
        print(exc)
