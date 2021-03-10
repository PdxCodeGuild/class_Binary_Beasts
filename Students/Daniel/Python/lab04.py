import random

print("Welcome to the Magic 8 Ball")

prediction_list = ["It is certain","It is decidedly so", "Without a doubt", "Yes definitely","Reply hazy try again", "My reply is no"]

continue_loop_variable = 1

while continue_loop_variable == 1:
    
    user_question = input("Please ask the Magic 8-ball a question: ")

    print(random.choice(prediction_list))

    continue_loop_variable = int(input("Continue? Enter 1 for Yes and 2 for No: "))