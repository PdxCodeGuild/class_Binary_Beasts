import random

def pick_6():
    ran_picks = []
    for x in range(6):
        ran_picks.append(random.randint(0, 2))
    return ran_picks

def player():
    player_picks =[]
    for x in range(6):
        player_picks.append(random.randint(0, 2))
    return player_picks

for num_picks in range(0):
    print(player())
    

        
        
    
# print(pick_6())
# print(player())
# print(match)
    






