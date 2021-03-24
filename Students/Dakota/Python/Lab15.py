#Lab15
import requests, string
response = requests.get('http://www.gutenberg.org/files/61085/61085-0.txt')
response.encoding = 'utf-8'
words = response.text
book_dict = dict()
lower_words = words.lower()
split_word = lower_words.split(" ")
for s in split_word:
    if s in book_dict:
        book_dict[s] = book_dict[s] + 1
        s += lower_words.strip(string.punctuation)
    else:
        book_dict[s] = 1
key_tuple = list(book_dict.items())
key_tuple.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(key_tuple[i])