"""

all codes are written and created by John Robson Fri Mar 12, 2021

"""

import requests  #run "python3 -m pip install requests" to install this library
from string import *
import re

url = "http://www.gutenberg.org/files/64796/64796-0.txt"

response = requests.get(url)
response.encoding = "utf-8"

strip = punctuation + digits

#Version 1

def run_version1():

    word_dict = {}

    text = response.text.lower()
    for x in strip:
        text = text.replace(x, "")
    text = re.split(" |\n, |\r\n", text)
    
    text = list(filter(None, text))

    for x in text:
        v = word_dict.get(x, 0)
        word_dict[x] = v + 1

    words = list(word_dict.items())
    words.sort(key=lambda tup: tup[1], reverse=True)

    for i in range(min(10, len(words))):
        print(words[i])
    
#Version 2

def run_version2():

    word_dict = {}

    text = response.text.lower()
    for x in strip:
        text = text.replace(x, "")
    text = re.split(" |\n, |\r\n", text)
    
    words = list(filter(None, text))

    i = 0
    while i < len(words) - 2:
        tup = tuple(words[i:i + 2])
        v = word_dict.get(tup, 0)
        word_dict[tup] = v + 1
        i += 1
    
    words = list(word_dict.items())
    words.sort(key=lambda tup: tup[1], reverse=True)
    
    for i in range(min(10, len(words))):
        print(words[i])
        

#Version 3

def run_version3():
    
    word_dict = {}

    text = response.text.lower()
    for x in strip:
        text = text.replace(x, "")
    text = re.split(" |\n, |\r\n", text)
    
    words = list(filter(None, text))

    i = 0
    while i < len(words) - 2:
        tup = tuple(words[i:i + 2])
        v = word_dict.get(tup, 0)
        word_dict[tup] = v + 1
        i += 1
    
    words = list(word_dict.items())
    
    results = []
    
    while results == []:
        word = input("What word would you like to search for?")
        for x, y in words:
            if x[0] == word :
                results.append((x, y))
        if results == []:
            print("Sorry. No results found")
    
    results.sort(key=lambda tup: tup[1], reverse=True)
    
    for i in range(min(10, len(results))):
        print(results[i])
    

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
    
    