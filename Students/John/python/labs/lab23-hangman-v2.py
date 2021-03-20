"""

all codes are written and created by John Robson Sat Mar 13, 2021

"""

import random

# Version 2
#This version was created using a Class and methods

class Hangman:
    __movie_titles = ["snakes on a plane", "kill bill", "good will hunting",
                "mad max", "spiderman", "black panther", "ex machina",
                "avengers", "inception", "toy story", "star wars",
                "wonder woman", "the notebook", "yes man", "tomb raider"]
    
    __hangman_pics = ["""
  +---+
  |   |
      |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\. |
 / \  |
      |
=========""", """
  +---+
  |   |
  O   |
./|\. |
 / \  |
      |
=========""", """
  +---+
  |   |
  O   |
./|\. |
 / \. |
      |
=========""", """
  +---+
  |   |
  O   |
./|\. |
./ \. |
      |
========="""]
    
    def __init__(self):
        self.__movie = random.choice(self.__movie_titles).upper()
        self.__answer = list(self.__movie)
        self.__board = self.__init_board()
        self.__already_guessed = []
        self.__wrong = []
        self.__guesses_remaining = 10
        self.__won = ""
        self.__guess = ""
        print("Welcome to hangman. Here's your board. Guess this movie title.")
        print('You can enter "done" at any time to exit.')
        self.__draw_hangman()
        print(self.__board)
        
    def __init_board(self):
        buf = ""
        for l in self.__answer:
            if l == " ":
                buf += "  "
            else:
                buf += "_ "
        return buf
    
    def __get_board(self):
        buf = ""
        for g in self.__answer:
            if g in self.__already_guessed:
                buf += g + " "
            else:
                if g == " ":
                    buf += "  "
                else:
                    buf += "_ "
        buf += "\n"
        buf += "Guesses remaining: " + str(self.__guesses_remaining) + "\n"
        buf += "already guessed: " + self.__get_already_guessed() + "\n"
        buf += "wrong: " + str(len(self.__wrong))
        self.__board = buf
    
    def __get_already_guessed(self):
        buf = ""
        for g in self.__already_guessed:
            if buf == "":
                buf += g
            else:
                buf += ", " + g
        return buf
    
    def __check_board(self):
        _ = "_"
        if _ not in list(self.__board):
            self.__won = True
            self.__complete_board()
    
    def __check_guess(self):
        guess = self.__guess
        self.__already_guessed.append(guess)
        boolean = False
        if len(guess) == 1:
            if guess in self.__answer:
                boolean = True
            self.__handle(boolean)
        else:
            if guess == self.__movie:
                self.__won = True
                self.__complete_board()
                return
            else:
                self.__handle(boolean)
        self.__get_board()
                
    def __handle(self, boolean):
        result = "incorrect"
        if boolean == True:
            result = "correct"
        else:
            self.__wrong.append(self.__guess)
        print(f"{self.__guess} is {result}!")
        if len(self.__wrong) >= 10:
            self.__won = False
        
    
    def __complete_board(self):
        buf = ""
        for l in self.__answer:
            buf += l + " "
        self.__board = buf
        
    def __draw_hangman(self):
        idx = len(self.__wrong)
        print(self.__hangman_pics[idx])
        
    def __draw_board(self):
        print(self.__board)
        
    def __get_guess(self):
        while True:
            guess = input(
                "Please guess a letter or entire movie title.").upper()
            if guess == "DONE":
                break
            if len(guess) == 1 or len(guess) == len(self.__answer):
                if guess in self.__already_guessed:
                    print("You already guessed that. Try again")
                else:
                    break
        self.__guess = guess
        
    def show_answer(self):
        return self.__answer
        
    def play(self):
        while True:
            self.__get_guess()
            if self.__guess == "DONE":
                return "done"
            self.__check_guess()
            self.__check_board()
            
            if type(self.__won) is bool:
                if self.__won == True:
                    self.__draw_board()
                return self.__won
            
            self.__draw_hangman()
            self.__draw_board()
            
            
def run_version2():
    while True:
        game = Hangman()
        
        won = game.play()
        
        if won == True:
            print("Good job! You won!!")
        elif won == False:
            print("Sorry, you lose. You ran out of guesses.")
            print(f"The correct answer was: {game.show_answer()}")
        else:
            print("Game ended.")
            
        play = ""
        while play != "yes" and play != "no":
            play = input("Play again?")
        
        if play == "no":
            print("Thank you for playing. Goodbye.")
            break

run_version2()