'''
Theo Cocco
Monday November 22, 2021
Lab 20, Pick 6
'''

from random import randint

# Version 1

x = 10000

m = 0


def p6():
    x = []
    for i in range(6):
        n = randint(0, 99)
        x.append(n)
    return x

def match(x,y):
    n = 0
    c = 0
    for i in x:
        if x[n] == y[n]:
            c += 1
        n += 1
    return c

def win(x):
    t = 0
    if x == 1:
        t += 4
    elif x == 2:
        t += 7
    elif x == 3:
        t += 100
    elif x == 4:
        t += 50000
    elif x == 5:
        t += 1000000
    elif x == 6:
        t += 25000000
    t -= 2
    return t

for i in range(x):
    m += win(match(p6(), p6()))

print(m)

# Version 2(ROI)

roi = m / (x * 2)
print(roi)






    

