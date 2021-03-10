import random

list_of_eyes = ["^","-","*"]
#list_of_noses = [""]
list_of_mouths = ["__", "_", "."]
generated_emoticon = ""
loop_count = 0
while loop_count != 5:
    generated_emoticon = random.choice(list_of_eyes)
    generated_emoticon += random.choice(list_of_mouths)
    generated_emoticon += random.choice(list_of_eyes)
    print(str(loop_count + 1) + "   " + generated_emoticon + " \n")
    loop_count += 1

