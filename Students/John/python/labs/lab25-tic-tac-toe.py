"""

all codes are written and created by John Robson Sun Mar 14, 2021

"""

from string import ascii_lowercase as l
from string import ascii_uppercase as u
letters = l + u

class Player:
    def __init__(self, token):
        self.__name = self.__set_name() #by OOP principles, all properties are set to private
        self.__token = token

    def __set_name(self): #this gets called when you instantiate a new Player() object
        while True:     #it asks the user to enter a player name, cannot skip
            name = input("Please enter player name:\n").capitalize()
            if True in [x in letters for x in name]: #see line 22 - 29
                return name   #return name, this breaks loop and ends method
            
            #if True in [x in letters for x in list(name)]
            #first we loop through each letter of the input, x for x in name
            #then we check that x is a letter (declared on line 9), x in letters
            #this will return a list of True/False statements based on each letter
            #so if I enter name as "jo1" it will return a list of [True, True, False]
            #Then we check if there is ANY True statement in that list of True/False, True in [T/F List]
            #If any True exists, this returns True, otherwise it returns False
            #This method simply checks that you've typed a letter, so cannot be blank or only numbers

    def get_name(self):  #we use getter methods to retrieve our token values from outside the class
        return self.__name

    def get_token(self): #another getter
        return self.__token


class Game: # notice ALL methods are private except the play() method
            # the game class is designed to have 1 method (play()) to handle all game operations
            # this means on the outside, the ONLY method we ever need to call is game.play()
    def __init__(self, p1, p2): #by OOP principles, all properties are set to private
        self.__board_slots = [" ", " ", " ", " ", " ", " ", " ", " ", " "] #default board positions
        self.__board_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] #numbers for help menu
        self.__open_slots = [1, 2, 3, 4, 5, 6, 7, 8, 9] #tracks opens slots for help menu
        self.__players = [p1, p2] #list of Player() objects containing player info
        self.__game_over = False
        self.__winner = ""
        self.__show_info()  #display help menu when Game() is initialized

    def __show_info(self): #just displays board info (aka: how to play)
        print("Board squares are labeled 1 through 9. When it's your turn,\n" +
              "just enter a number between 1 and 9 to place your token.")
        self.__draw_board("numbers") #calls draw board to print board

    def __draw_board(self, type): #draws board based on type (either "numbers" or default)
        t = self.__board_slots
        if type == "numbers": #for a "numbers" board, it will show 1-9 instead of Xs and Os
            s = t; i = 0; t = self.__board_numbers
            while i < len(s):  #remove unavailable slots, so only available numbers show up
                t[i] = "-" if s[i] != " " else t[i]
                i += 1

        print(f" {t[0]} | {t[1]} | {t[2]}\n---|---|---\n {t[3]} | {t[4]} | {t[5]}\n---|---|---\n"\
            f" {t[6]} | {t[7]} | {t[8]}")   #print board

    def __move(self, p, pos): #this method activates the move and prints board
        self.__board_slots[pos - 1] = p.get_token()  #sets token on board
        self.__open_slots[pos - 1] = ""   #removes available slot (for numbers board)
        self.__draw_board("default")   #calls method to render board

    def __get_move(self, p): #checks input for move, with "help" and "done" options
        while True:   #loop until we get a satisfying response from player
            pos = input(
                f'{p.get_name()} - Where would you like to move? Enter "help" for help or "done" to quit. ').lower()
            if pos == "help":    #handle help request
                self.__show_info()
            elif pos == "done":  #handle done request
                self.__game_over = True
                return  #calling return in a method/func will break the loop and end the method right here
                        #break only stops the loop, it doesn't stop the method from running
            else:
                try:  #try/except in case int(pos) throws exception
                    if int(pos) in self.__open_slots:
                        self.__move(p, int(pos)) #if move available, calls move
                        return  #return to break loop and end method
                except:  #except is required for try/except
                    continue    #we are required to have code here, so we continue loop

    def __check_board(self): #checks if game over and loops through winning conditions and calls method to check them
        s = self.__board_slots
        self.__game_over = True if len(s) - len([x in ["X", "O"] for x in s if x in ["X", "O"]]) == 0 else self.__game_over
        wins = [(s[0], s[1], s[2]), (s[0], s[3], s[6]), (s[0], s[4], s[8]), (s[1], s[4], s[7]),
                       (s[2], s[4], s[6]), (s[2], s[5], s[8]), (s[3], s[4], s[5]), (s[6], s[7], s[8])]
        for x in wins: #loop through win conditions
            winner = self.__check_winning_conditions(x) #check for a winner and return winner
            if winner in self.__players: #checks that winner is actually a Player() object
                self.__winner = winner; self.__game_over = True #sets game winner and game over
                return winner #return winner, this also breaks our for x in wins loop

    def __check_winning_conditions(self, args): #checks winning conditions to see if all match and are X or O
        if all(a == args[0] and a in ["X", "O"] for a in args):
            return self.__check_winner(args[0]) #return the matching token

    def __check_winner(self, token): #match token to winner and return winner
        return self.__players[0] if self.__players[0].get_token() == token else self.__players[1]

    def play(self): #the game loop as a method on Game class
        while True:
            for p in self.__players: #for each player
                self.__get_move(p) #ask player for move (if valid, it will then call the move method and draw board)
                self.__check_board() #check board for winning conditions
                if self.__game_over:
                    if self.__winner in self.__players: #checks for a winner 
                        print(f"The winner is {self.__winner.get_name()}")
                    else:       #we could put this if/else on 1 line, but it would be too long 
                        print("No winner!")
                    return      #return None or Null to break loop, the exact same effect as "break"


def get_player(token):  #external function that generates a player
    while token not in ["X", "O"]:
        token = input("Please enter token for Player 1: (X or O):").upper()

    return Player(token) #Notice we aren't setting our Player object to a variable 
                        #instead we are just returning a new Player object
                        #We don't have to pass a name because when Player gets instantiated
                        #the constructor (__init__()) will fire a method to set a name


while True:
    print("Player 1:")
    player1 = get_player(None)  #calls our method to generate new player and we are not passing a token value
    token = "X" if player1.get_token() == "O" else "O" # we switch token from X to O and vice versa for player 2
    print("Player 2:")
    player2 = get_player(token) #generate player 2 using token from line 120

    game = Game(player1, player2) #instantiate Game object and register the players

    game.play()   #result is the "return" statement at the end of game.play()

    play = ""
    print("Game ended.")
    while play not in ["yes", "no"]:
        play = input("Play again?").lower()

    if play in ["no", "done"]:
        print("Thank you for playing. Goodbye.")
        break
