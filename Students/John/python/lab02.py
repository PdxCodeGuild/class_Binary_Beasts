"""

all codes are written and created by John Robson Wed Mar 10, 2021

"""

import random

while True:
    nounlist = input("List 3 nouns: ").split()
    adjlist = input("List 3 emotions: ").split()
    clothinglist = input("list 3 articles of clothing: ").split()
    
    noun = random.choice(nounlist)
    adjective = random.choice(adjlist)
    clothing = random.choice(clothinglist)

    lyrics = f"""
    Be our {noun}
    Be our {noun}
    Turning 60 is {adjective}
    Tighten up your bow tie round your neck and wear your favorite {clothing}
    """
    print(lyrics);
    playAgain = input("Would you like to continue? ")
    if playAgain.lower() == "no":
        break