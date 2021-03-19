import requests
import random


class RandomCatFact:

        def make_request(self):
            x = requests.get(f"https://cat-fact.herokuapp.com/facts")

            x = x.json()

            response_list = []

            for response in range(0,len(x),1):
                response_list.append(x[response]['text'])
            return random.choice(response_list)

r1 = RandomCatFact()
while True:
    user_choice = input("Would you like to see a random cat fact? Y for Yes and N for No: ")
    if user_choice == "Y":
        print(r1.make_request())
    else:
        print("This program is not for you. ")
        break

