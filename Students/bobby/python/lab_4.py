import random # Imported the module random

print ("Welcome to the Magic 8 Ball") # Welcome statement
question = input("Ask the Magic 8 Ball a question ") # User input the question
random_answers = ["Try Again", "Dont", "Please Do", "Of Course", "Most Likely", "Yes", "No", "Maybe"] # List of random answers
random_answers = random.choice(random_answers) # Random.choice picks from the list


print (random_answers) # Prints the answer