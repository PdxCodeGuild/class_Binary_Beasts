from random import choice
eyes = ['-', '*', 'o', '^',]
mouths = ['.', ',', '_',]
earleft = ['(', '[', '{',]
emoticons = []
blank = ' '
while len(emoticons) <5:
    eye = choice(eyes)
    ear1 = choice(earleft)
    if ear1 == '(':
        ear2 = ')'
    elif ear1 == '[':
        ear2 = ']'
    elif ear1 == '{':
        ear2 = '}'
    emoticon = ear1 + eye + choice(mouths) + eye + ear2
    emoticons.append(emoticon)

emoticons = blank.join(emoticons)
print(emoticons)

