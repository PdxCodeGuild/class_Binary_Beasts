"""

all codes are written and created by John Robson Wed Mar 10, 2021

"""

import random

# Version 1

def run_version1():
    x = random.randint(1, 10)
    count = 1

    while True:
        if count == 11:
            print("You lose")
            break
        guess = int(input("Choose a number:"))

        if (guess == x):
            print("You win!")
        else:
            print(f"Try again. You have guessed {count} time(s).")

        count += 1


# Version 2

def run_version2():
    x = random.randint(1, 10)
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

def run_version3():
    x = random.randint(1, 10)
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

def run_version4():
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
            if lastGuess != 0:
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

def run_version5():
    x = int(input("Pick a number 1-10"))
    count = 1

    if x < 1 or x > 10:
        print("Your number was out of the range. Try again:")
        run_version5()
    else:
        while True:
            guess = random.randint(1, 10)

            if (guess == x):
                print("You win!")
                break
            else:
                print(f"Try again. You have guessed {count} times.")

            count += 1


versions = [run_version1, run_version2, run_version3, run_version4, run_version5]

while True:
    strategy = 0

    print('Welcome. You can type "done" at any time to exit.')

    m = len(versions)

    while strategy not in range(1, m + 1):
        try:
            strategy = input(f"Which version would you like to run: 1 - {m}")
            if strategy == "done":
                break
            strategy = int(strategy)
        except:
            continue
        if strategy == "done":
            break

    strategy = versions[strategy - 1]

    strategy()
