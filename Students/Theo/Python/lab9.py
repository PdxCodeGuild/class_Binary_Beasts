from string import ascii_lowercase as lowers

english = list(lowers)

word = input('Please enter a word you want encrypted: ').lower()

rot = int(input('Please enter the desired rot: '))

rot_word = ''

for letter in word:
    rot_word += english[(english.index(letter) - rot)]

print(rot_word)



    



