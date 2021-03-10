import random

up_charachter_choice_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low_charachter_choice_list = "abcdefghijklmnopqrstuvwxyz"
special_charachter_choice_list = "!@#$%^&*()_+-=\""
number_charachter_choice_list = "1234567890"

uppercase_choice_amount =  int(input("Welcome to the amazing password generator, please enter a desired number of uppercase letters in the password you want to create: "))

lowercase_choice_amount = int(input("Please enter a desired number of lowercase letters in the password you want to create: "))

special_char_choice_amount = int(input("Please enter a desired number of special charachters in the password you want to create: "))

number_choice_amount = int(input("Please enter a desired number of numbers in the password you want to create: "))



generated_password = {}

x = 0
while x < uppercase_choice_amount:
    generated_password[x] = random.choice(up_charachter_choice_list)
    x+=1

x = 0
while x < lowercase_choice_amount:
    generated_password[x+len(generated_password)] = random.choice(low_charachter_choice_list)
    x+=1

x = 0
while x < special_char_choice_amount:
    generated_password[x+len(generated_password)] = random.choice(special_charachter_choice_list)
    x+=1


x = 0
while x < number_choice_amount:
    generated_password[x+len(generated_password)] = random.choice(number_charachter_choice_list)
    x+=1



passwordList = list(generated_password.values())
random.shuffle(passwordList)
print(passwordList)

#Attempted to use a dictionary to return the values in a naturally unordered way but python seems to have changed this functionality since python 3.6. Dictionaries now return ordered lists.