
conversion = { # Dictionary holding my key value pairs
    'feet': 0.3048,
    'mile': 1609.34,
    'meter': 1,
    'km': 1000,
    'yard': 0.9144,
    'inch': 0.0254
}
distance = float(input('What is the distance you wish to convert? ')) # input for distance
unit_from = input('What is the unit you would like to convert from? ') # input for unit from
unit_to = input('What is the unit you would like to convert to? ') # input for unit to
result = (conversion[unit_from] * distance / conversion[unit_to]) # creates result of unit_from * distance / unit_to
print(f'{distance} {unit_from} is {result} {unit_to}') # And this prints a work of art LOL
