import random

user_input = int(input("Welcome to Guess the Number, you have 10 tries, \n please try to guess the number between 1-10: "))

number = random.randint(1,10)
guess_count = 0
while True:
    guess_count += 1 

   # if guess_count == 10:
   #     break

    if user_input == number:
        print(f"correct! you guessed {guess_count} times")
        break
    else:
        print("try again!")
        if user_input > number:
            print("Too high!")
        else:
            print("Too low!")
        user_input = int(input("guess the number: "))
        