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
        self.__draw_board("numbers")

    def __draw_board(self, type):
        t = self.__board_slots
        if type == "numbers":
            s = t; i = 0; t = self.__board_numbers
            while i < len(s):
                t[i] = "-" if s[i] != " " else t[i]
                i += 1

        print(f" {t[0]} | {t[1]} | {t[2]}\n---|---|---\n {t[3]} | {t[4]} | {t[5]}\n---|---|---\n"\
            f"{t[6]} | {t[7]} | {t[8]}")

    def __move(self, p, pos):
        token = p.get_token()
        self.__board_slots[pos - 1] = token
        self.__open_slots[pos - 1] = ""
        self.__draw_board("slot")

    def __get_move(self, p):
        player = p.get_name()
        while True:
            pos = input(
                f'{player} - Where would you like to move? Enter "help" for help or "done" to quit.').lower()
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
        self.__game_over = True if len(s) - len([x in ["X", "O"] for x in s if x in ["X", "O"]]) == 0 else False
        wins = [(s[0], s[1], s[2]), (s[0], s[3], s[6]), (s[0], s[4], s[8]), (s[1], s[4], s[7]),
                       (s[2], s[4], s[6]), (s[2], s[5], s[8]), (s[3], s[4], s[5]), (s[6], s[7], s[8])]
        for x in wins:
            winner = self.__check_winning_conditions(x[0], x[1], x[2])
            if winner in self.__players:
                self.__winner = winner; self.__game_over = True
                return winner

    def __check_winning_conditions(self, *args):
        if all(a == args[0] and a in ["X", "O"] for a in args):
            return self.__check_winner(args[0])

    def __check_winner(self, token):
        return self.__players[0] if self.__players[0].get_token() == token else self.__players[1]

    def play(self):
        while True:
            for p in self.__players:
                self.__get_move(p)
                self.__check_board()
                if self.__game_over:
                    if self.__winner in self.__players:
                        name = self.__winner.get_name()
                        print(f"The winner is {name}")
                    else:
                        print("It's a tie game!")
                    return


def get_player(token):
    while token not in ["X", "O"]:
        token = input("Please enter token for Player 1: (X or O):").upper()

    return Player(token)


while True:
    print("Player 1:")
    player1 = get_player(None)
    token = "X" if player1.get_token() == "O" else "O"
    print("Player 2:")
    player2 = get_player(token)

    game = Game(player1, player2)

    result = game.play()

    if result == "done":
        print("Game ended.")

    play = ""
    while play != "yes" and play != "no":
        play = input("Play again?").lower()

    if play == "no":
        print("Thank you for playing. Goodbye.")
        break
