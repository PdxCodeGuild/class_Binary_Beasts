"""

all codes are written and created by John Robson Sun Mar 14, 2021

"""

class Player:
    
    def __init__(self, token):
        self.__set_name()
        self.__token = token
        
    def __set_name(self):
        while True:
            name = input("Please enter player name:\n").capitalize()
            if name != "":
                self.__name = name
                break
    
    def get_name(self):
        return self.__name
    
    def get_token(self):
        return self.__token
            
class Game:
    
    def __init__(self, p1, p2):
        self.__board_slots = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.__board_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.__open_slots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.__players = [p1, p2]
        self.__game_over = False
        self.__winner = ""
        self.__board = ""
        self.__show_info()
        
    def __show_info(self):
        print("Board squares are labeled 1 through 9. When it's your turn, \n" + 
            "just enter a number between 1 and 9 to place your token.")
        self.__repr__("numbers")
        
    def __repr__(self, type):
        t = self.__board_slots
        if type == "numbers":
            s = t
            t = self.__board_numbers
            i = 0
            while i < len(s):
                if s[i] != " ":
                    t[i] = "-"
                i += 1
            
        self.__board = " " + t[0] + " | " + t[1] + " | " + t[2] + "\n"
        self.__board += "---|---|---\n"
        self.__board += " " + t[3] + " | " + t[4] + " | " + t[5] + "\n"
        self.__board += "---|---|---\n"
        self.__board += " " + t[6] + " | " + t[7] + " | " + t[8] + "\n"
        print(self.__board)
        
    def __move(self, p, pos):
        token = p.get_token()
        self.__board_slots[pos - 1] = token
        self.__open_slots[pos - 1] = ""
        self.__repr__("slot")
        
    def __get_move(self, p):
        player = p.get_name()
        while True:
            pos = input(f'{player} - Where would you like to move? Enter "help" for help or "done" to quit.').lower()
            if pos == "help":
                self.__show_info()
            elif pos == "done":
                self.__game_over = True
                return
            else:
                try:
                    if int(pos) in self.__open_slots:
                        self.__move(p, int(pos))
                        return
                except:
                    continue
    
    def __check_board(self):
        s = self.__board_slots
        open = len(s) - len([x for x in s if x in ["X", "O"]])
        if open == 0:
            self.__game_over = True
        if s[0] == s[1] == s[2] and s[0] != " " or \
            s[0] == s[3] == s[6] and s[0] != " " or \
            s[0] == s[4] == s[8] and s[0] != " ":
                self.__check_winner(s[0])
                
        elif s[1] == s[4] == s[7] and s[1] != " ":
                self.__check_winner(s[1])
        
        elif s[2] == s[4] == s[6] and s[2] != " " or \
            s[2] == s[4] == s[6] and s[2] != " " or \
            s[2] == s[5] == s[8] and s[2] != " ":
                self.__check_winner(s[2])
                
        elif s[3] == s[4] == s[5] and s[3] != " ":
                self.__check_winner(s[3])
            
        elif s[6] == s[7] == s[8] and s[6] != " ":
                self.__check_winner(s[6])
            
    def __check_winner(self, token):
            self.__game_over = True
            p1 = self.__players[0]
            p2 = self.__players[1]
            if token == p1.get_token():
                self.__winner = p1
            else:
                self.__winner = p2        
                    
    def play(self):
        while True:
            for p in self.__players:
                self.__get_move(p)
                self.__check_board()
                check = self.__game_over
                if check:
                    w = self.__winner
                    if w != "":
                        name = w.get_name()
                        print(f"The winner is {name}")
                    else:
                        print("It's a tie game!")
                    return
                

def get_player(token):
    while token not in ["X", "O"]:
        token = input("Please enter token for Player 1: (X or O):").upper()
        
    return Player(token)

while True:
    token = ""
    player1 = get_player(token)
    token = "X"
    if player1.get_token() == "X":
        token = "O"
    player2 = get_player(token)
    
    game = Game(player1, player2)
    
    result = game.play()
    
    if result == "done":
        print("Game ended.")
    
    play = ""
    while play != "yes" and play != "no":
        play = input("Play again?")
        
    if play == "no":
        print("Thank you for playing. Goodbye.")
        break