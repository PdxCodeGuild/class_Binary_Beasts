'''
Theo Cocco
Monday, March 22, 2021
Credit Card Validation Lab
'''

ccn = '4556737586899855'


def make_list(x):
    l = list(x)
    m = map(int, l)
    y = list(m)
    return y


def double(x):
    y = 0
    for i in range(len(x)//2 + len(x) % 2):
        d = x[y] * 2
        x[y] = d
        y += 2

def sub9(x):
    y = 0
    for i in x:
        if x[y] >= 10:
            s = x[y] - 9
            x[y] = s
        y += 1

def check(x, y):
    if sum(x) % 10 == y:
        return True

def run(x):
    l = make_list(x)
    c = l[-1]
    l.pop()
    l.reverse()
    double(l)
    sub9(l)
    if check(l, c) == True:
        print('Valid!')
    else:
        print('Not Valid')

run(ccn)

