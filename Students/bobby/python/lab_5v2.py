import random

eyes = [";", ":"]
nose = ["<", ">"]
mouth = [")", "(", "@"]

# For loop that runs 5 times
for x in range(5):
    ran_eyes = random.choice(eyes)
    ran_nose = random.choice(nose)
    ran_mouth = random.choice(mouth)
    print (ran_eyes,ran_nose,ran_mouth)




