"""

all codes are written and created by John Robson Sat Mar 20, 2021

"""

from string import ascii_letters as letters

class Player:
    def __init__(self, token, i):
        self.__name = self.__set_name(i)
        self.__token = token

    def __set_name(self, i):
        name = input(f"Please enter Player {i} name (letters only): ").capitalize()
        return name if all([x in letters for x in name]) else self.__set_name(i)

    def get_name(self):
        return self.__name

    def get_token(self):
        return self.__token


class Game:
    def __init__(self):
        self.__board_slots = list(" " * 9)
        self.__board_numbers = list(map(str, list(range(1, 10))))
        self.__open_slots = list(range(1, 10))
        self.__players = []
        self.__over = False
        self.__winner = ""
        self.__set_players(None, 1)
        self.__show_info()

    def __set_players(self, token, i):
        while token not in ["X", "O"]:
            token = input(
                f"Please enter token for Player {i}: (X or O):").upper()
        token2 = "X" if token == "O" else "O"
        self.__players.append(Player(token, i))
        while len(self.__players) < 2:
            self.__set_players(token2, i+1)

    def __show_info(self):
        print("Board squares are labeled 1 through 9. When it's your turn,\n" +
              "just enter a number between 1 and 9 to place your token.")
        self.__draw_board("nums")

    def __draw_board(self, type):
        t = self.__board_slots
        if type == "nums":
            s = t; i = 0; t = self.__board_numbers
            while i < len(s):
                t[i] = "-" if s[i] != " " else t[i]
                i += 1

        print(f" {t[0]} | {t[1]} | {t[2]}\n---|---|---\n {t[3]} | {t[4]} | {t[5]}\n---|---|---\n"\
            f" {t[6]} | {t[7]} | {t[8]}")

    def __move(self, p, pos):
        self.__board_slots[pos - 1] = p.get_token()
        self.__open_slots[pos - 1] = ""
        self.__draw_board("")

    def __get_move(self, p):
        while True:
            pos = input(f'{p.get_name()} - Where would you like to move? Enter "help" for help or "done" to quit. ').lower()
            if pos == "help":
                self.__show_info()
            elif pos == "done":
                self.__over = True
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
        self.__over = True if len(s) - len([x in ["X", "O"] for x in s]) == 0 else self.__over
        wins = [s[0:3], s[3:6], s[6:9], s[0:7:3], s[1:8:3], s[2:9:3], s[2:7:2], s[0:9:4]]
        for w in wins:
            winner = self.__check_winning_conditions(w)
            if winner in self.__players:
                self.__winner = winner; self.__over = True

    def __check_winning_conditions(self, args):
        return self.__check_winner(args[0]) if all(a == args[0] and a in ["X", "O"] for a in args) else ""

    def __check_winner(self, token):
        return self.__players[0] if self.__players[0].get_token() == token else self.__players[1]

    def play(self):
        while True:
            for p in self.__players:
                self.__get_move(p)
                self.__check_board()
                if self.__over:
                    if self.__winner in self.__players:
                        print(f"The winner is {self.__winner.get_name()}")
                    else:
                        print("No winner!")
                    print("Game ended.")
                    return

while True:
    Game().play()

    play = ""
    while play not in ["yes", "no"]:
        play = input("Play again?").lower()

    if play in ["no", "done"]:
        print("Thank you for playing. Goodbye.")
        break
