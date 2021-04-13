# ROT Cipher

import string
letters = string.ascii_lowercase # String of lower case letters called letters
eng_list = list(letters) # Changes letters to a list called english letters

rot = input("enter the rotation you would like to use in the cipher. ")
rot = int(rot) # changes input to integer
user = input("Enter the information you wish to Cipher. ")
cipher_list = [] 
for index in range(len(user)):
    cipher_list.append(eng_list[index +rot]) # appends to my blank list from the user input & rotates per user input

output = "".join(cipher_list) # creates the return string .join
print(output)