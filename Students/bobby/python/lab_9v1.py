# ROT Cipher

import string
letters = string.ascii_lowercase # String of lower case letters called letters
eng_list = list(letters) # Changes letters to a list called english letters

user = input("Enter the information you wish to Cipher. ")
cipher_list = [] 
for index in range(len(user)):
    cipher_list.append(eng_list[index +13]) # appends to my blank list from the user input rotated 13

output = "".join(cipher_list) # creates the return string .join
print(output)














