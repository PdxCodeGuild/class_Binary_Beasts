import string

english = string.ascii_lowercase
rot = 13

DO A DICTIONARY

def rotate(x):
    print(x)
    for i in x:
        i = int(i)
        i = i - rot
        i = str(i)

while True:
    translate = input("Enter a string to encode.\n> ").lower()

    print(rotate(translate))