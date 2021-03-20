#API Lab 1
import requests
while True:
    city_name = input('What city would you like weather for? ')
    if city_name != None:
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=d75899b044a505479f7a235d2aae3ced')
        data = response.json()
        print(data)
        temp = (data['main']['temp'])
        print(f'The current Weather for {city_name} is {temp}')
        break
    else:
        print('Please enter a city name: ')
        break

#API Lab 2
#imports requests
import requests
#begins REPL
while True:
    #establishes users country name
    country_name = input('What Country would you like information for? ')
    #if statement for country name
    if country_name != None:
        #pulls user input from api in f string format
        response = requests.get(f'https://restcountries.eu/rest/v2/name/{country_name}?fullText=true')
        data = response.json()
        #Set Country info variables 
        country = data[0]['name']
        capital = data[0]['capital']
        #languages currently only works for up to 2 languages
        languages = data[0]['languages'][0]['name'],data[0]['languages'][1]['name']
        population = data[0]['population']
        borders = data[0]['borders']
        #Variable for if country is an island
        print(f'{country} has the following info:\n Capital: {capital}\n Languages: {languages[0]}\n Population: {population}\n{country} borders: {borders}')
        if borders == []:
            print(f'{country} has no bordering countries')
        break
    #if user needs to enter a country
    else:
        print('Please enter a country name: ')
        break