import requests
import json
import random


x = requests.get(f"https://cat-fact.herokuapp.com/facts")
x = json.loads(x.text)
response_list = []
response_list.append(x[0]['text'])
response_list.append(x[1]['text'])
response_list.append(x[2]['text'])
response_list.append(x[3]['text'])
response_list.append(x[4]['text'])

print(random.choice(response_list))
