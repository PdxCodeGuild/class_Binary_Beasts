import requests
word_dict = {}
response = requests.get("https://www.gutenberg.org/files/62897/62897-0.txt")
response.encoding = 'utf-8'
response = response.text.strip().replace(",", "").replace(".", "").lower().split()




for word in response:
    if word in word_dict:
        word_dict[word] = word_dict[word] + 1
    else:
        word_dict[word] = 1

words = list(word_dict.items()) 
words.sort(key=lambda tup: tup[1], reverse=True) 
for i in range(min(10, len(words))):
    print(words[i])