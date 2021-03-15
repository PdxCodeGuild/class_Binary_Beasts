"""

all codes are written and created by John Robson Sun Mar 14, 2021

"""

#Version 2
#This version was created a Class and methods

import random

class LCR():
    __players = []
    __center_pot = 0
    __no_chips = []
    __won = False
    __die = []
    __rolls = []
    
    def __init__(self):
        self.__center_pot = 0
        self.__no_chips = []
        self.__won = False
        self.__rolls = []
        self.__die = ["L", "C", "R", 1, 1, 1]
        print("Welcome to LCR. Please enter players to begin.")
        self.__init_players()
        
    def __init_players(self):
        names = []
        while True:
            name = input('Please enter player name or "done" when finished adding players.\n')
            if name == "done" and len(self.__players) >= 3:
                break
            if name == "done":
                print("At least 3 players are required to begin. Please enter more players.")
                continue
            self.__players.append({"name": name, "chips": 3})
            names.append(name)
        print("The players are: ")
        print(names)
    
    def __roll_die(self):
        self.__rolls.append(random.choice(self.__die))

    def __pass_chip(self, p, d):
        i = self.__players.index(p)
        if i == len(self.__players) - 1:
            i = -1
        if d == "L":
            d = -1
        elif d == "R":
            d = 1
        from_p = self.__players[i]
        from_p["chips"] -= 1
        to_p = {}
        if type(d) is int:
            to_p = self.__players[i + d]
            to_p["chips"] += 1
        else:
            self.__center_pot += 1
            
    def __check_chips(self):
        self.__no_chips = []
        for p in self.__players:
            if p["chips"] == 0:
                self.__no_chips.append(p)
    
    def __display_winner(self):
        for p in self.__players:
            if p["chips"] > 0:
                p["chips"] += self.__center_pot
                name = p["name"]
                chips = p["chips"]
                print(f"The winner is {name} with {chips} chips.")

    def play(self):
        while not self.__won:
            for p in self.__players:
                chips = p["chips"]
                self.__rolls = []
                while chips > 0:
                    self.__roll_die()
                    chips -= 1
                for r in self.__rolls:
                    if type(r) is str:
                        self.__pass_chip(p, r)
                self.__check_chips()
                if len(self.__no_chips) == len(self.__players) - 1:
                    self.__display_winner()
                    self.__won = True
                    break

while True:
    game = LCR()
    
    game.play()
    
    again = ""
    while again != "yes" and again != "no":
        again = input("Play again?")
    
    if again == "no":
        print("Game ended. Goodbye")
        break