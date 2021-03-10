import random

eyes = [
    '^',
    'x',
    '$',
    '>',
    '-',
]

bodies_left = [
    '(',
    '<(',
    'd[',
]

bodies_right = [
    ')',
    ')>',
    ']b',
]

mouths = [
    '_',
    'x',
    'o',
    '.',
    'O',
    '3',
]

emojis = 0

while emojis != 5:
    emojis += 1
    print(f'{random.choice(bodies_left)}{random.choice(eyes)}{random.choice(mouths)}{random.choice(eyes)}{random.choice(bodies_right)}')