#Version 1

def runVersion1():
    english = "abcdefghijklmnopqrstuvwxyz"
    index = 0
    
    string = input("Please input your phrase")
    buf = ""
    
    for i in string:
        if i == " ":
            buf += " "
        else:
            index = english.find(i)
            index += 13
            if index > 25:
                index = index - 26
            buf += english[index]
        
    print(buf)
    
#Version 2

def runVersion2():
    english = "abcdefghijklmnopqrstuvwxyz"
    index = 0
    offset = int(input("How many numbers should we offset?"))
    
    string = input("Please input your phrase")
    buf = ""
    
    for i in string:
        if i == " ":
            buf += " "
        else:
            index = english.find(i)
            index += offset
            if index > 25:
                index = index - 26
            buf += english[index]
        
    print(buf)
    
#Version 3

def runVersion3():
    english = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !@#$%^&*()<>?"
    index = 0
    offset = int(input("How many numbers should we offset?"))
    
    string = input("Please input your phrase")
    buf = ""
    
    for i in string:
        index = english.find(i)
        index += offset
        if index > 65:
            index = index - 66
        buf += english[index]
        
    print(buf)