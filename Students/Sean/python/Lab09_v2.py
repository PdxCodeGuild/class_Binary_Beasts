lows = {
    'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12,
    'n':13, 'o':14,'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25
}

#upps = {
#    'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13
#    'N':14, 'O':15,'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26
#}

#spec = {
#    '!':1, '@':2, '#':3, '$':4, '%':5, '^':6, '&':7, '*':8, '(':9, ')':10, '-':11, '_':12, '+':13, '=':14,
#}

def rotate(x):
    letterlist = []
    numbers_before = []
    numbers_after = []
    for i in x:
        for letter in lows:
            if letter == i:
                numbers_before.append(lows[letter])

    for num in numbers_before:
        num += rot
        numbers_after.append(num % 26)

    for num in numbers_after:
        for letter in lows:
            if num == lows[letter]:
                letterlist.append(letter)
                 
    return letterlist

rot = int(input("How much would you like to rotate by?"))
print(rotate(input("Enter something to rotate.\n> ").lower()))