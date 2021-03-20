'''
Theo Cocco
API lab
Thursday March 18, 2021
'''

import requests

# Weather API

'''
while True:
    city = input('What city would you like to check the weather of? ').capitalize()

    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=8af2aa7fa978da0c3dc608a85406875c')
    data = response.json()
    print(f"""The current weather of {city} is {data['weather'][0]['description']}. 
    The temperature is {data['main']['temp']} degrees farenheit.""")

    again = input('Would you like to try again? Enter no to quit. ')
    if again == 'no':
        break
'''

# Public API(Genre Generator)


while True:
    x = input('Are you ready to create a new Genre? "Yes or No?" ').lower()

    if x == 'yes':
        y = requests.get('https://binaryjazz.us/wp-json/genrenator/v1/genre')
        print(f'Your genre is {x.text}. Time to get started!')
        break

    elif x == 'no':
        print('Maybe next time then!')
        break

    else:
        print('Please type "yes" or "no"')


