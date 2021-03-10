import random

eyes = [
    ':',
    ';',
    '=',
    '>:',
    'x',
]

noses = [
    '',
    '-',
    '^',
    'c',
]

mouths = [
    ')',
    ']',
    '}',
    'o',
    'D',
    '3',
]

emojis = 0

while emojis != 5:
    emojis += 1
    print(f'{random.choice(eyes)}{random.choice(noses)}{random.choice(mouths)}')