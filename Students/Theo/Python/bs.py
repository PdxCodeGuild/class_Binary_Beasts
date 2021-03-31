from bs4 import BeautifulSoup
import requests

genre = input('Enter a genre: ')

url = 'https://www.gutenberg.org/ebooks/search/?query={}&submit_search=Go%21'.format(genre)

page = requests.get(url)

content = BeautifulSoup(page.content, 'html.parser') #lxml

with open('page.html', 'w') as file:
    file.write(str(content))

books = content.select('ul.results li.booklink')

book_choices = {}

for i in range(10):
    books[i] = books[i].select('a span:nth-of-type(2)')
    k = books[i]['span']

    v = 'hi'
    book_choices[k] = v


print(book_choices)