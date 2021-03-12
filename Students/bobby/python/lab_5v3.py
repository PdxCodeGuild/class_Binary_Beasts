import random
# Variables containing all face parts
eyes = ["^", "-", "*"] 
lcheeks = ["[", "("]
rcheeks = ["]", ")"]
mouth = ["_", "."]

ran_eyes = random.choice(eyes) # Randomly chooses eyes
ran_lcheeks = random.choice(lcheeks) # Randomly chooses left cheeks
ran_rcheeks = random.choice(rcheeks) # Randomly chooses left cheeks


ran_mouth = random.choice(mouth) # Randomly chooses mouth


print (ran_lcheeks,ran_eyes,ran_mouth,ran_eyes,ran_rcheeks) # Prints face parts in order



