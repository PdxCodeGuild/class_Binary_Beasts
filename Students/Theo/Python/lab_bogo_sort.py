'''
Theo Cocco
Monday, March 22, 2021
Lab Bogo Sort
'''

from random import randint

def rlist(x):
    l =[]
    for i in range(x):
        l.append(randint(0, 100))
    return l

def shuffle(x):
    a = 0
    for i in x:
        r = randint(0, 9)
        x[a], x[r] = x[r], x[a] 
        a += 1

def is_sorted(x):
    a = 0
    for i in x:
        if a == len(x) - 1:
            break
        if x[a] > x[a+1]:
            return False
        a += 1
    return True

def bogosort(x):
    l = rlist(x)
    while True:
        if is_sorted(l) == False:
            shuffle(l)
        else:
            break
    print(l)

bogosort(10)













