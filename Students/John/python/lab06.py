"""

all codes are written and created by John Robson Wed Mar 10, 2021

"""

from random import *
from string import *

password = ""

letters = int(input("How many letters? "))
numbers = int(input("How many numbers? "))
special = int(input("How many special characters? "))

letters = choices(ascii_letters, k=letters)
numbers = choices(digits, k=numbers)
special = choices(punctuation, k=special)

characters = letters + numbers + special
shuffle(characters)
password = ''.join(characters)
print(f"Your password is: {password}")