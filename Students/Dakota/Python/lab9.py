"""
#Lab9.py
#Version 1
#import modules
import string
english_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
rot = ['n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m']
#Ask the user for their input
user_input = str(input('Please enter a letter to be decoded: '))
list_word = list(user_input)

for letter in list_word:
    if letter in english_list:
        user_alpha = english_list.index(letter)
        decode = rot[user_alpha]
        print(decode,end="")
"""
#Lab9.py
#Version 2
#import modules
import string
english_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#Ask the user for their input
user_input = str(input('Please enter a word to be decoded: '))
#Ask the user for their rotation
rotation = int(input('How much rotation would you like to have? '))
list_word = list(user_input)

for letter in list_word:
    if letter in english_list:
        user_alpha = english_list.index(letter)
        decode_rot = (user_alpha + rotation)%26
        english_decoded = english_list[decode_rot]
        print(english_decoded,end="")

#modulous operator to loop through list