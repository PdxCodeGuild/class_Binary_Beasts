import requests

name = input("Enter your name, and I'll tell you the most common age of people with your name:  ")

age = requests.get(f"https://api.agify.io?name={name}&country_id=US")
data = age.json()

print(f"The average age of someone with the name {data['name']}, out of {data['count']} in the US is {data['age']}")