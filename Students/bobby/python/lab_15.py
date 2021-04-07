import requests
# response = requests.get("https://http://www.gutenberg.org/files/64863/64863-0.txt")
# response.encoding = 'utf-8'
# print(response.text)

with open("text_file.txt", "r", encoding="utf-8") as file:
    text = file.read()
lower_string = text.lower()

import string
string.punctuation
for punc in string.punctuation:
    lower_string = lower_string.replace(punc, "")

word_list = lower_string.split(" ") # This tells it to split the string at the spaces
banned = [""]

word_dict = {}
for x in word_list:
    if x not in banned:
        if x in word_dict:
            word_dict[x] += 1
        else:
            word_dict[x] = 1
        
words = list(word_dict.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(words[i])        





  
    