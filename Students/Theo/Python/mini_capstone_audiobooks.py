'''
Theo Cocco
Wednesday March 24, 2021
Automation Mini Capstone, Audiobooks
'''

import requests
import pyttsx3

engine = pyttsx3.init()

def save_book_from_web(x, y):
    book = requests.get(x)
    book.encoding = 'utf-8'
    engine.save_to_file(book, y + '.mp3')
    engine.runAndWait()

def save_book_from_computer(x, y):
    with open(x, 'r', encoding='utf-8') as file:
        book = file.read()
    engine.save_to_file(book, y + '.mp3')
    engine.runAndWait()

def listen_to_book_from_web(x):
    book = requests.get(x)
    book.encoding = 'utf-8'
    engine.say(book)
    engine.runAndWait()

def listen_to_book_on_computer(x):
    with open(x, 'r', encoding='utf-8') as file:
        book = file.read()
    engine.say(book)
    engine.runAndWait()

def web():
    url = input('Please enter in the book\'s url: ')
    play_or_save = input('Would you like to play or save your audiobook? ').lower()
    if play_or_save == 'play':
        listen_to_book_from_web(url)
    elif play_or_save == 'save':
        file_name = input('What would you like to save your audiobook as? ')
        save_book_from_web(url, file_name)

def comp():
    comp_file = input('What is your book saved under? ')
    play_or_save = input('Would you like to play or save your audiobook? ').lower()
    if play_or_save == 'play':
        listen_to_book_from_computer(comp_file)
    elif play_or_save == 'save':
        file_name = input('What would you like to save your audiobook as? ')
        save_book_from_computer(comp_file, file_name)

web_or_comp = input('Would you like to make an audio book off the web or off your computer? Type, "web" or "computer" ').lower()

if web_or_comp == 'web':
    web()

elif web_or_comp == 'computer':
    comp()
    



