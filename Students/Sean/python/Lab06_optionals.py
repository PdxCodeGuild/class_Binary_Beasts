import random
import string

lowers = string.ascii_lowercase
uppers = string.ascii_uppercase
numbers = string.digits
specials = string.punctuation

while True:
    password = ''

    try:
        lower_choice = int(input("How many lowercase letters do you want in your password?\n>"))
        upper_choice = int(input("How many uppercase letters do you want in your password?\n>"))
        number_choice = int(input("How many numbers do you want in your password?\n>"))
        special_choice = int(input("How many special characters do you want in your password?\n>"))
    except Exception as exc:
        print(exc)
        continue
    for x in range(lower_choice):
        password += random.choice(lowers)

    for x in range(upper_choice):
        password += random.choice(uppers)

    for x in range(number_choice):
        password += random.choice(numbers)

    for x in range(special_choice):
        password += random.choice(specials)

    shuffling = list(password)
    random.shuffle(shuffling)
    shuffled = ''.join(shuffling)

    print(shuffled)