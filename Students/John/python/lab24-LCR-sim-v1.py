"""

all codes are written and created by John Robson Sun Mar 14, 2021

"""

#Version 1
#This version was created using only functions

import random

def init_players():
    players = []
    names = []
    while True:
        name = input('Please enter player name or "done" when finished adding players.\n')
        if name == "done" and len(players) >= 3:
            break
        if name == "done":
            print("At least 3 players are required to begin. Please enter more players.")
            continue
        players.append({"name": name, "chips": 3})
        names.append(name)
        
    print("The players are: ")
    print(names)
    return players

def roll_die():
    die = ["L", "C", "R", 1, 1, 1]
    return random.choice(die)

def pass_chip(players, player, dir):
    idx = players.index(player)
    if idx == len(players) - 1:
        idx = -1
    if dir == "L":
        dir = -1
    elif dir == "R":
        dir = 1
    from_d = players[idx]
    from_d["chips"] -= 1
    to_d = {}
    if type(dir) is int:
        to_d = players[idx + dir]
        to_d["chips"] += 1
    else:
        return "c"
    
def check_chips(players):
    lst = []
    for p in players:
        if p["chips"] == 0:
            lst.append(p)
    return lst

def get_winner(players, pot):
    for p in players:
        if p["chips"] > 0:
            p["chips"] += pot
            return p
    
    
def play():
    
    print("Welcome to LCR. Please enter players to begin.")
    players = init_players()
    center_pot = 0
    no_chips = []
    won = False
    
    while not won:
        for p in players:
            chips = p["chips"]
            roll = []
            while chips > 0:
                roll.append(roll_die())
                chips -= 1
            for r in roll:
                if type(r) == str:
                    result = pass_chip(players, p, r)
                    if result == "c":
                        center_pot += 1
            no_chips = check_chips(players)
            if len(no_chips) == len(players) - 1:
                winner = get_winner(players, center_pot)
                name = winner["name"]
                chips = winner["chips"]
                print(f"The winner is {name} with {chips} chips.")
                won = True
                break
        if won == True:
            break
            
while True:
    play()
    
    again = ""
    while again != "yes" and again != "no":
        again = input("Play again?")
    
    if again == "no":
        print("Game ended. Goodbye")
        break