import random # Imported the module random

play_again = 'yes' # loop control
while play_again == 'yes': # Will play until control is false
    print ("Welcome to the Magic 8 Ball") # Welcome statement
    question = input("Ask the Magic 8 Ball a question ") # User input the question
    random_answers = ["Try Again", "Dont", "Please Do", "Of Course"] # List of random answers
    random_answers = random.choice(random_answers) # Random.choice picks from the list


    print (random_answers) # Prints the answer
    play_again = input('Do you want to play again? yes/no: ') # Alows the loop to continue or break