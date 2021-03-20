'''
Theo Cocco
Lab 15 Count Words
Friday March 19, 2021
'''

# Version 1


from string import punctuation
import requests

w_dict = {}

def make_list(x):
    x.encoding = 'utf-8'
    x = x.text
    x = x.lower()
    translator = str.maketrans('','',punctuation)
    x = x.translate(translator)
    x = x.split()
    return x

def add_to_dict(x):
    for y in x:
        if y not in w_dict.keys():
            w_dict[y] = 1
        else:
            w_dict[y] += 1

def top_10(x):
    y = list(x.items())
    y.sort(key=lambda tup: tup[1], reverse=True)
    for i in range(min(10, len(x))):  # print the top 10 words, or all of them, whichever is smaller
        print(y[i])

x = requests.get('http://www.gutenberg.org/files/64870/64870-0.txt')
add_to_dict(make_list(x))
top_10(w_dict)
