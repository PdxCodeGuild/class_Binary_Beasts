import requests
word_list = {}
response = requests.get("https://www.gutenberg.org/files/62897/62897-0.txt")
response.encoding = 'utf-8'

response = response.text.strip().replace(",", "").replace(".", "").lower().split()
for word in response:
    print(word)
