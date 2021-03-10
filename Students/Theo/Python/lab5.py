from random import choice
eyes = [':', ';', '=',]
noses = ['^', '-', '.',]
mouths = [')', '(', '[', ']', '{', '}', '|', '/', 'o',]
emoticons = []
blank = ' '
while len(emoticons) <5:
    emoticon = choice(eyes) + choice(noses) + choice(mouths)
    emoticons.append(emoticon)

emoticons = blank.join(emoticons)
print(emoticons)
