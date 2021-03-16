'''
Theo Cocco
Lab 14 Number to Phrase
Friday March 12, 2021
'''

# Version 1

'''
tens = {
    1: 'ten',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

ones = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

x = 45

if 9 < x <= 20:
    print(f'{tens[x]}')
elif x > 20:
    print(f'{tens[x // 10]}-{ones[x % 10]}')
else:
    print(f'{ones[x]}')
'''

# Version 2

tens = {
    1: 'ten',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

ones = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

hundreds = {
    1: 'one hundred',
    2: 'two hundred',
    3: 'three hundred',
    4: 'four hundred',
    5: 'five hundred',
    6: 'six hundred',
    7: 'seven hundred',
    8: 'eight hundred',
    9: 'nine hundred',
}

whole_numbers = [1,2,3,4,5,6,7,8,9]

x = 815

if 9 < x <= 20:
    print(f'{tens[x]}')
elif x > 20 and x < 100:
    print(f'{tens[x // 10]}-{ones[x % 10]}')
elif x / 100 in whole_numbers:
    print(f'{hundreds[x // 100]}')
elif 9 < x % 100 <=20:
    print(f'{hundreds[x // 100]} and {tens[x % 100]}')
elif x > 100:
    print(f'{hundreds[x // 100]} and {tens[x % 100 // 10]}-{ones[x % 100 % 10]}')
elif x < 10:
    print(f'{ones[x]}')