"""

all codes are written and created by John Robson Sat Mar 13, 2021

"""

import random

# Version 1
#This version was created using functions only

movie_titles = ["snakes on a plane", "kill bill", "good will hunting",
                "mad max", "spiderman", "black panther", "ex machina",
                "avengers", "inception", "toy story", "star wars",
                "wonder woman", "the notebook", "yes man", "tomb raider"]
hangman_pics = ["""
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


def run_version1():

    movie = random.choice(movie_titles).upper()
    answer = list(movie)
    already_guessed = []
    wrong = []

    def init_board():
        board = ""
        for l in answer:
            if l == " ":
                board += "  "
            else:
                board += "_ "
        return board

    def check_guess(guess):
        already_guessed.append(guess)
        if len(guess) == 1:
            if guess not in answer:
                handle_wrong(guess)
            else:
                handle_right(guess)
            board = update_board()
            return board
        else:
            if guess == movie:
                return True
            else:
                handle_wrong(guess)
                board = update_board()
                return board

    def check_board():
        board = update_board()
        _ = "_"
        if _ not in list(board):
            return True

    def handle_right(guess):
        print(f"The letter {guess} was found! Good job!")

    def handle_wrong(guess):
        print(f"{guess} is not correct.")
        wrong.append(guess)

    def get_already_guessed():
        buf = ""
        for g in already_guessed:
            if buf == "":
                buf += g
            else:
                buf += ", " + g
        return buf

    def update_board():
        board = ""
        for g in answer:
            if g in already_guessed:
                board += g + " "
            else:
                if g == " ":
                    board += "  "
                else:
                    board += "_ "
        board += "\n"
        board += "Guesses remaining: " + str(get_guesses_remaining()) + "\n"
        board += "already guessed: " + get_already_guessed() + "\n"
        board += "wrong: " + str(len(wrong))
        return board

    def complete_board():
        buf = ""
        for l in answer:
            buf += l + " "
        return buf

    def draw_hangman():
        idx = len(wrong)
        hangman_pics[idx]

    def get_guess():
        while True:
            guess = input(
                "Please guess a letter or entire movie title.").upper()
            if guess == "DONE":
                return guess
            if len(guess) == 1 or len(guess) == len(answer):
                if guess in already_guessed:
                    print("You already guessed that. Try again")
                else:
                    return guess

    def get_guesses_remaining():
        return 10 - len(wrong)

    def play():
        board = init_board()
        print("Welcome to hangman. Here's your board. Guess this movie title.")
        pic = draw_hangman()
        print(pic)
        print(board)

        while True:
            guess = get_guess()
            if guess == "DONE":
                return False
            response = check_guess(guess)
            check = check_board()
            if check == True:
                response = True
            pic = draw_hangman()
            print(pic)
            if len(wrong) >= 10:
                response = False

            if response == False:
                print("Sorry, you lose. You ran out of guesses.")
                print(f"The correct answer was: {movie}")
                break
            elif response == True:
                print(complete_board())
                print("Good job! You won!!")
                break
            else:
                print(response)

    return play()

while True:

    print('Welcome. You can type "done" at any time to exit.')
    
    play = run_version1()
    if play == False:
        print("Game ended.")
    
    while play != "yes" and play != "no":
        play = input("Play again?")
    
    if play == "no" or play == "done":
        print("Thank you for playing. Goodbye.")
        break