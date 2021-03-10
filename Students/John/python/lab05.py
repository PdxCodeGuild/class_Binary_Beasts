import random

eyes = [":", ";", "8"]
noses = ["-", "", "^"]
mouths = [")", "(", "P"]

i = 0
while i < 5:
    buf = random.choice(eyes)
    buf += random.choice(noses)
    buf += random.choice(mouths)
    print(buf)
    i = i + 1
    
    
    
#Vertical

eyes = ["^^", "--", "**"]
mouths = ["_", ".", "o"]

buf = random.choice(eyes)
buf = buf[0] + random.choice(mouths) + buf[1]

print(buf)