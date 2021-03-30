# #Lab 13
# #Version 1
# distance = {
#     'feet': 0.3048,
#     }
# quantity = input('what is the distance in feet? ')
# quantity_float = float(quantity)
# dist_in_meters = distance['feet']
# ft_2_m = quantity_float * dist_in_meters
# print(f'{quantity} ft is {ft_2_m:.4f} m')

# #Version 2
# distance = {
#     'ft': 0.3048,
#     'mi': 1609.34,
#     'm': 1,
#     'km': 1000
# }
# quantity_dist = input('what is the distance? ')
# units = input('what are the units? ')
# units_choice = distance[units]
# quantity_float = float(quantity_dist)
# user_input_dist = quantity_float * units_choice
# print(f'{quantity_dist} {units} is {user_input_dist} m')

# #Version 3
# distance = {
#     'ft': 0.3048,
#     'mi': 1609.34,
#     'm': 1,
#     'km': 1000,
#     'yd': 0.9144,
#     'in': 0.0254,
# }
# quantity_dist = input('what is the distance? ')
# units = input('what are the units? ')
# units_choice = distance[units]
# quantity_float = float(quantity_dist)
# user_input_dist = quantity_float * units_choice
# print(f'{quantity_dist} {units} is {user_input_dist} m')

#Version 4
distance = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254,
}
quantity_dist = input('what is the distance? ')
units = input('what are the units? ')
output_units = input('what are the output units? ')
units_choice = distance[units]
quantity_float = float(quantity_dist)
user_input_dist = quantity_float * units_choice
user_output_units = user_input_dist / distance[output_units]
print(f'{quantity_dist} {units} is {user_output_units} {output_units}')