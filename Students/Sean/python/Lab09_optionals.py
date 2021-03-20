lows = {
    'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12,
    'n':13, 'o':14,'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25
}

upps = {
    'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12,
    'N':13, 'O':14,'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25,
}

spec = {
    '!':0, '@':1, '#':2, '$':3, '%':4, '^':5, '&':6, '*':7, '(':8, ')':9, '-':10, '_':11, '+':12, '=':13,
    '1':14, '2':15, '3':16, '4':17, '5':18, '6':19, '7':20, '8':21, '9':22, '0':23, '/':24, '?':25,
}

def rotate(x):
    letterlist = []
    numbers_before = []
    numbers_after = []
    for i in x:
        if i in lows:
            numbers_before.append(lows[i])
            for num in numbers_before:
                num += rot
                numbers_after.append(num % 26)
            for num in numbers_after:
                for letter in lows:
                    if num == lows[letter]:
                        letterlist.append(letter)


        if i in upps:
            numbers_before.append(upps[i])
            for num in numbers_before:
                num += rot
                numbers_after.append(num % 26)
            for num in numbers_after:
                for letter in upps:
                    if num == upps[letter]:
                        letterlist.append(letter)

        
        if i in spec:
            numbers_before.append(spec[i])
            for num in numbers_before:
                num += rot
                numbers_after.append(num % 26)
            for num in numbers_after:
                for letter in spec:
                    if num == spec[letter]:
                        letterlist.append(letter)
                 
    return letterlist

rot = int(input("How much would you like to rotate by?"))
print(rotate(input("Enter something to rotate.\n> ")))