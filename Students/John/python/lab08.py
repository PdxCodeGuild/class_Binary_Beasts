# Version 1
import random


def runVersion1():
    x = random.randint(1, 10)
    guess = -1
    count = 1

    while True:
        if count == 11:
            print("You lose")
            break
        guess = int(input("Choose a number?"))

        if (guess == x):
            print("You win!")
        else:
            print(f"Try again. You have guessed {count} time(s).")

        count += 1


# Version 2

def runVersion2():
    x = random.randint(1, 10)
    guess = -1
    count = 1

    while True:
        guess = int(input("Choose a number?"))

        if (guess == x):
            print("You win!")
            break
        else:
            print(f"Try again. You have guessed {count} times.")

        count += 1


# Version 3

def runVersion3():
    x = random.randint(1, 10)
    guess = -1
    count = 1

    while True:
        guess = int(input("Choose a number?"))

        if (guess == x):
            print("You win!")
            break
        else:
            if guess > x:
                print("Too high!")
            else:
                print("Too low!")
            print(f"Try again. You have guessed {count} times.")

        count += 1


# Version 4

def runVersion4():
    x = random.randint(1, 10)
    guess = -1
    count = 1
    lastGuess = 0

    while True:
        guess = int(input("Choose a number?"))

        if (guess == x):
            print("You win!")
            break
        else:
            if abs(x - lastGuess) < abs(x - guess):
                print("Last guess was closer than current")
            else:
                print("Current guess is closer than last")
            if guess > x:
                print("Too high!")
            else:
                print("Too low!")
            print(f"Try again. You have guessed {count} times.")

        lastGuess = guess
        count += 1


# Version 5

def runVersion5():
    x = int(input("Pick a number 1-10"))
    count = 1

    if x < 1 or x > 10:
        print("Your number was out of the range. Try again:")
        runVersion5()
    else:
        while True:
            guess = random.randint(1, 10)

            if (guess == x):
                print("You win!")
                break
            else:
                print(f"Try again. You have guessed {count} times.")

            count += 1
