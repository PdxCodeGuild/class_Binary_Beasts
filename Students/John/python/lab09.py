"""

all codes are written and created by John Robson Wed Mar 10, 2021

"""

from string import ascii_lowercase as lowers
from string import ascii_uppercase as uppers
from string import punctuation as specials
from string import digits as numbers


#Version 1

def runVersion1():
    index = 0
    
    string = input("Please input your phrase")
    buf = ""
    
    for i in string:
        if i == " ":
            buf += " "
        else:
            index = lowers.find(i)
            index += 13
            if index > len(lowers) - 1:
                index = index - len(lowers)
            buf += lowers[index]
        
    print(buf)
    
#Version 2

def runVersion2():
    index = 0
    offset = int(input("How many numbers should we offset?"))
    
    string = input("Please input your phrase")
    buf = ""
    
    for i in string:
        if i == " ":
            buf += " "
        else:
            index = lowers.find(i)
            index += offset
            if index > len(lowers) - 1:
                index = index - len(lowers)
            buf += lowers[index]
        
    print(buf)
    
#Version 3

def runVersion3():
    all = lowers + uppers + specials + numbers
    
    index = 0
    offset = int(input("How many numbers should we offset?"))
    
    string = input("Please input your phrase")
    buf = ""
    
    for i in string:
        if i == " ":
            buf += " "
        else:
            index = all.find(i)
            index += offset
            if index > len(all) - 1:
                index = index - len(all)
            buf += all[index]
        
    print(buf)

    
versions = [runVersion1, runVersion2, runVersion3]

while True:
    strategy = 0

    print('Welcome. You can type "done" at any time to exit.')

    while strategy < 1 or strategy > 3:
        strategy = int(input("Which version would you like to run: 1 - 3"))
        if strategy == "done":
            break
        
    if strategy == "done":
        break

    strategy = versions[strategy - 1]

    strategy()