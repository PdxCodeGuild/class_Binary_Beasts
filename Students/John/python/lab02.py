"""

all codes are written and created by John Robson Wed Mar 10, 2021

"""

import random

while True:
    noun_list = input("List 3 nouns: ").split()
    adj_list = input("List 3 emotions: ").split()
    clothing_list = input("list 3 articles of clothing: ").split()
    
    noun = random.choice(noun_list)
    adjective = random.choice(adj_list)
    clothing = random.choice(clothing_list)

    lyrics = f"""
    Be our {noun}
    Be our {noun}
    Turning 60 is {adjective}
    Tighten up your bow tie round your neck and wear your favorite {clothing}
    """
    print(lyrics);
    play_again = input("Would you like to continue? ")
    if play_again.lower() == "no":
        break