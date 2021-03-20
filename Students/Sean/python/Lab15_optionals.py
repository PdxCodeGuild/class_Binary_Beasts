import requests
import string
punc = string.punctuation
book = requests.get('http://www.gutenberg.org/files/42108/42108-0.txt')
book = book.text
for x in book:
    if x in punc:
        book = book.replace(x,'')
book = book.lower()
book = book.split(' ')
word_count = {}



for word in book:
    if prev_word and word:
        if word not in word_count:
            word_count[word] = 0
    word_count[word] += 1

words = list(word_count.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count

for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])