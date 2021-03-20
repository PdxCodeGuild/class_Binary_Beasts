"""

all codes are written and created by John Robson Sat Mar 20, 2021

"""

#This is the commented version -- see other version for clean code

from string import ascii_letters as letters

class Player:
    def __init__(self, token, i): #i usually stands for "iteration", it's a counter. i here represents player number
        self.__name = self.__set_name(i) #immediately calls __set_name() method
        self.__token = token    #standard OOP principles: private variables! (you cannot call player.__token from outside)

    def __set_name(self, i):
        name = input(
            f"Please enter Player {i} name (letters only): ").capitalize()
        return name if all([x in letters for x in name]) else self.__set_name(i) #a little tricky, but basically
                            #this says "return name" if every letter in the name is in the list of all letters or else 
                            #we call this method again (this is called recursion) so it repeats until name is acceptable

    def get_name(self):  #normal "getter" method, used to get private variables from the outside
        return self.__name

    def get_token(self):    #normal "getter", call player.get_token() from outside to get token name
        return self.__token


class Game:
    def __init__(self):
        self.__board_slots = list(" " * 9)  #generates [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.__board_numbers = list(map(str, list(range(1, 10))))  #generates ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.__open_slots = list(range(1, 10))  #generates [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.__players = [] #empty list, required for line 46 when we append new players
        self.__over = False
        self.__winner = ""
        self.__set_players(None, 1)  #call this method as soon as Game() is instantiated
        self.__show_info()     #call after we establish players

    def __set_players(self, token, i):  #default token is "none" (from line 38), i is our player number
        while token not in ["X", "O"]:
            token = input(f"Please enter token for Player {i}: (X or O):").upper()
        token2 = "X" if token == "O" else "O" #switch tokens for player 2
        self.__players.append(Player(token, i)) #add player to list (we dont a variable to Player(), no need to)
        while len(self.__players) < 2:  #while less than 2 players, call this method again
            self.__set_players(token2, i+1) #next time this method runs, it has a token, so it skips lines 42 and 43
                                            #we also increase i to represent player 2
    def __show_info(self):
        print("Board squares are labeled 1 through 9. When it's your turn,\n" +
              "just enter a number between 1 and 9 to place your token.")
        self.__draw_board("nums") #we pass nums to draw a board of numbers instead a default game board

    def __draw_board(self, type):
        t = self.__board_slots  #default slots from line 32
        if type == "nums":
            s = t; i = 0; t = self.__board_numbers
            while i < len(s):               #basically we are looking for tokens on our board and replacing the number
                t[i] = "-" if s[i] != " " else t[i]     #on our number board with a dash (-) to represent unavailability
                i += 1

        print(f" {t[0]} | {t[1]} | {t[2]}\n---|---|---\n {t[3]} | {t[4]} | {t[5]}\n---|---|---\n"\
            f" {t[6]} | {t[7]} | {t[8]}")       #print out our board

    def __move(self, p, pos): #p = player, pos = position
        self.__board_slots[pos - 1] = p.get_token()     #set token on our board
        self.__open_slots[pos - 1] = "" #removes slot on our open slots list
        self.__draw_board("")

    def __get_move(self, p):    #p = player
        while True:
            pos = input(f'{p.get_name()} - Where would you like to move? Enter "help" for help or "done" to quit. ').lower()
            if pos == "help":   #check "help" condition
                self.__show_info()
            elif pos == "done":     #check "done" condition
                self.__over = True
                return      #return will immediately break loop and end entire method right here
            else:
                try:    #if not "done" or "help" we check if pos can be casted as an int and if it is an open slot
                    if int(pos) in self.__open_slots:
                        self.__move(p, int(pos))        #if true, call __move()
                        return
                except:     #except is required for syntax. we dont really need it for our case
                    continue        #so we just put "continue" to go to the next cycle in the loop

    def __check_board(self):
        s = self.__board_slots
        self.__over = True if len(s) - len([x in ["X", "O"] for x in s]) == 0 else self.__over
            #This just checks if the board is full or not if amount of tokens = board size, game over
            #this is a ternary statement (A if B else C) with a list comprehension [A for A in B]
            #if length of board slots minus length (amount) of tokens in board slots == 0
            #then set self.__over to True else we leave self.__over as it is
            #(we don't want to set to false in case it's already true)
        
        wins = [s[0:3], s[3:6], s[6:9], s[0:7:3], s[1:8:3], s[2:9:3], s[2:7:2], s[0:9:4]]
            #s[0:3] returns [s[0], s[1], s[2]] (3 is the upper limit and gets excluded, so no s[3]
            #s[0:7:3] returns indices of s between 0 to 6 adding 3 each time, so [s[0], s[3], s[6]]
        for w in wins:
            winner = self.__check_winning_conditions(w) #this will return a player if there is a winner, else ""
            if winner in self.__players:        #this just checks if the winner is a player (not "")
                self.__winner = winner; self.__over = True

    def __check_winning_conditions(self, args):
        return self.__check_winner(args[0]) if all(a == args[0] and a in ["X", "O"] for a in args) else ""
            #a few things going on here. This is a giant ternary statement (A if B else C)
            #which returns a method __check_winner() if true or "" if false
            #the if condition is a function (all()) that takes a list comprehension [A for A in B] as a parameter
            #the list comprehension checks if all a values are equal to the first value and is an X or O
            #this returns a list of True and False values, like this [True, True, False, True, False]
            #the all() method returns True if all are True or False if 1 or more are False

    def __check_winner(self, token):
        return self.__players[0] if self.__players[0].get_token() == token else self.__players[1]
            #another ternary statement (A if B else C)
            #if player 1's token matches winning token, return player 1, else return player 2

    def play(self): #this is the ONLY public (non-private) method of our Game class, thus the only
        while True:                     #method we can call from the outside
            for p in self.__players:    #for each player (p)
                self.__get_move(p)      #get the move and pass the player as a parameter
                self.__check_board()    #check the board for winning conditions or full condition
                if self.__over:         
                    if self.__winner in self.__players:
                        print(f"The winner is {self.__winner.get_name()}")
                    else:
                        print("No winner!")
                    print("Game ended.")
                    return      #return to end the game loop

while True:             #here's our outside world. Notice it's very minimal
    Game().play()       #I don't set Game() to a variable (game = Game()) because there's no need
                        #Game() will instantiate a new Game() object and the .play() will
                        #call the .play() method of our game which controls the entire game flow: no nested while loops!

    play = ""
    while play not in ["yes", "no"]:
        play = input("Play again?").lower()

    if play in ["no", "done"]:
        print("Thank you for playing. Goodbye.")
        break
