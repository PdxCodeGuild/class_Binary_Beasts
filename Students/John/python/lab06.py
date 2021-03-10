import random
import string

nextPassword = True
password = ""

letters = int(input("How many letters? "))
numbers = int(input("How many numbers? "))
special = int(input("How many special characters? "))

letters = random.choices(string.ascii_letters, k=letters)
numbers = random.choices(string.digits, k=numbers)
special = random.choices(string.punctuation)

characters = letters + numbers + special
random.shuffle(characters)
password = ''.join(characters)
print(f"Your password is: {password}")