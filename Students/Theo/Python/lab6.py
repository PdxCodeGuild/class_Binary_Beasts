'''
Theo Cocco
Lab 6
'''

from random import choice
from random import shuffle
from string import ascii_lowercase as lowers
from string import ascii_uppercase as uppers
from string import punctuation as spec_chars
from string import digits as numbers

lowers = list(lowers)

uppers = list(uppers)

specials = list(spec_chars)

numbers = list(numbers)

blank = ''

password = []


l = input('How many lowercase letters do you want in your password? ')

l = int(l)

llist = []

u = input('How many uppercase letters do you want in your password? ')

u = int(u)

ulist = []

s = input('How many special characters do you want in your password? ')

s = int(s)

slist = []

n = input('How many numbers do you want in your passowrd?' )

n = int(n)

nlist =[]

total = l + u + s + n


while len(llist) < l:
    lower = choice(lowers)
    llist.append(lower)
while len(ulist) < u:
    upper = choice(uppers)
    ulist.append(upper)
while len(slist) < s:
    special = choice(specials)
    slist.append(special)
while len(nlist) < n:
    number = choice(numbers)
    nlist.append(number)

password = llist + ulist + slist + nlist

shuffle(password)

password = blank.join(password)

print(password)


    
