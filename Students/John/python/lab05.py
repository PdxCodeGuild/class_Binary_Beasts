"""

all codes are written and created by John Robson Wed Mar 10, 2021

"""

from random import choice

eyes = [":", ";", "8"]
noses = ["-", "", "^"]
mouths = [")", "(", "P"]

i = 0
while i < 5:
    buf = choice(eyes) + choice(noses) + choice(mouths)
    print(buf)
    i += 1

#Vertical

cheeks = ["()","[]", "  "]
eyes = ["^^", "--", "**"]
mouths = ["_", ".", "o"]

buf = choice(cheeks)
buf = buf[0] + choice(eyes) + buf[1]
buf = buf[0:2] + choice(mouths) + buf[2::]

print(buf)