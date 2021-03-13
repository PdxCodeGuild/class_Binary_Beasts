'''
Theo Cocco
Lab 13, Unit Converter
Friday March 12, 2021
'''

# Version 1

'''
ft = int(input('What is the distance in ft? '))
m = ft * .3048

print(f'{ft}ft is {m}m')
'''

# Version 2

'''
units = {
    'ft': .3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
}

x = int(input('What is the distance you want converted to m? '))
unit = input('What is the unit you want converted? ').lower()

total = x * units[unit]

print(f'{x}{unit} is {total}m')
'''

# Version 3

'''
units = {
    'ft': .3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': .9144,
    'in': .0254,
}

x = int(input('What is the distance you want converted to m? '))
unit = input('What is the unit you want converted? ').lower()

total = x * units[unit]

print(f'{x}{unit} is {total}m')
'''

# Version 4

'''
units = {
    'ft': .3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': .9144,
    'in': .0254,
}

x = int(input('What is the distance you want converted? '))
unit = input('What is the unit you want converted? ').lower()
output = input('What is the unit you want to conver to? ').lower()

unit_to_m = x * units[unit]
total = unit_to_m / units[output]

print(f'{x}{unit} is {total}{output}')
'''
