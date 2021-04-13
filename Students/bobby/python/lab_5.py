import random

eyes = [";", ":"] 
nose = ["<", ">"]
mouth = [")", "(", "@"]
ran_eyes = random.choice(eyes) # Randomly chooses eyes
ran_nose = random.choice(nose) # Randomly chooses nose
ran_mouth = random.choice(mouth) # Randomly chooses mouth

# Prints them individualy
print (ran_eyes) 
print (ran_nose)
print (ran_mouth)
# Prints all 3 on the same line
print (ran_eyes,ran_nose,ran_mouth)