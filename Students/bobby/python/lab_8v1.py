# Guess the number

import random
x = random.randint(1,10) # Picks random # between 1 and 10
play_again = "yes" # Loop control
count = 0
while play_again == "yes" and count <= 10:
    count += 1
    print ("Welcome to guess the number")
    user = int(input("Please pick a number between 1 and 10. "))
    if user == x:
        print (f"You win you guessed {count} times!")
        break
    elif count == 10:
        print ("You Lose!")
        break
    else:
        print ("try Again")
   
    print (f"This was attempt number {count}")
    play_again = input('Do you want to play again? yes/no: ')

