"""

all codes are written and created by John Robson Wed Mar 10, 2021

"""

from string import ascii_lowercase as lowers
from string import ascii_uppercase as uppers
from string import punctuation as specials
from string import digits as numbers


#Version 1

def run_version1():
    index = 0
    
    string = input("Please input your phrase")
    buf = ""
    
    for i in string:
        if i == " ":
            buf += " "
        else:
            index = lowers.find(i)
            index -= 13
            buf += lowers[index]
        
    print(buf)
    
#Version 2

def run_version2():
    index = 0
    rot = int(input("How many numbers should we offset?"))
    
    string = input("Please input your phrase")
    buf = ""
    
    for i in string:
        if i == " ":
            buf += " "
        else:
            index = lowers.find(i)
            index -= rot
            buf += lowers[index]
        
    print(buf)
    
#Version 3

def run_version3():
    all = lowers + uppers + specials + numbers
    
    index = 0
    rot = int(input("How many numbers should we offset?"))
    
    string = input("Please input your phrase")
    buf = ""
    
    for i in string:
        if i == " ":
            buf += " "
        else:
            index = all.find(i)
            index -= rot
            buf += all[index]
        
    print(buf)

    
versions = [run_version1, run_version2, run_version3]

while True:
    strategy = 0

    print('Welcome. You can type "done" at any time to exit.')

    m = len(versions)

    while strategy not in range(1, m + 1):
        try:
            strategy = input(f"Which version would you like to run: 1 - {m}")
            if strategy == "done":
                break
            strategy = int(strategy)
        except:
            continue
        if strategy == "done":
            break

    strategy = versions[strategy - 1]

    strategy()