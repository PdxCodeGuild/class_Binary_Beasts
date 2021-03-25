import requests
import smtplib, ssl
import string
from bs4 import BeautifulSoup
import webbrowser
from twilio.rest import Client
import getpass

account_sid = "ACcf4157aa5ff6399764b81d6044fdfb65"
auth_token = "b4df4f4963402380dc5d1dc4678fdde5"
client = Client(account_sid, auth_token)
uppers = string.ascii_uppercase

hangman = ['''
x-----
|
|
|
|
x-------''','''
x-----
|    |
|
|
|
x-------''','''
x-----
|    |
|    O
|
|
x-------''','''
x-----
|    |
|    O
|   /
|
x-------''','''
x-----
|    |
|    O
|   /|
|
x-------''','''
x-----
|    |
|    O
|   /|
|
x-------''','''
x-----
|    |
|    O
|   /|\\
|
x-------''','''
x-----
|    |
|    O
|   /|\\
|   /
x-------''','''
x-----
|    |
|    O
|   /|\\
|   / \\
x-------''',]

# random wikipedia article hangman, with description info as reward?

def RetrieveWord():
    # Pull a random animal from wikipedia
    url = "https://en.wikipedia.org/wiki/Special:Random"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find(id="firstHeading")
    links = [item['href'] if item.get('href') is not None else item['src'] for item in soup.select('[href^="http"], [src^="http"]') ]

    # Finds just the header from the wikipedia page, and turns it into uppercase ASCII
    random_word = title.string
    random_word = random_word.upper()

    # Filters out everything except ASCII characters
    random_word = ''.join(filter(uppers.__contains__,random_word))
    return random_word, links

def ShowBoard(incorrect_guesses,correct_guesses):
    # Creates and prints a blank space for every character in the random word from Wikipedia
    blank = '_' * len(random_word)
    print(f"{hangman[len(incorrect_guesses)]}")
    print(f"Incorrect guesses: {incorrect_guesses}")
    print(f"Correct guesses: {correct_guesses}")
    for i in range(len(random_word)):
        if random_word[i] in correct_guesses:
            blank = blank[:i] + random_word[i] + blank[i+1:]
    for i in blank:
        print(i, end=' ')
    print()

def RetrieveGuess(guesses):
    # Collects a single-character guess from the user
    while True:
        guess = input("Please guess a letter:\n> ").upper()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in guesses:
            print("You've already guessed that!")
        elif guess not in uppers:
            print("Please enter a letter.")
        else:
            return guess

def PlayAgain():
    # Asks if the user wants to play again
    print("Do you want to play again? (y/n)")
    return input().lower()

def email():
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = 'codersontesting@gmail.com'
    receiver_email = 'seanwilcox@comcast.net'
    pw = input("Enter your password: ")
    message = f"""
        Subject: Hello from Sean.

        This message is the wikipedia page you requested:
        {links[0]}"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, pw)
        server.sendmail(sender_email, receiver_email, message)
# Defines the global lists necessary to run
response = ''
incorrect_guesses = ''
correct_guesses = ''
random_word, links = RetrieveWord()
game_over = False
win_condition = False

while True:
    # Prints the board
    ShowBoard(incorrect_guesses,correct_guesses)

    # Retrieves the guess
    guess = RetrieveGuess(incorrect_guesses + correct_guesses)

    # Runs the guess through the game, finding whether or not it's in the word
    if guess in random_word:
        correct_guesses += guess
        for i in range(len(random_word)):
            if random_word[i] not in correct_guesses:
                win_condition = False
                break
            else:
                win_condition = True

    else:
        incorrect_guesses = guess + incorrect_guesses

    # If game is over, win or lose
    if win_condition == True:
        print(f"Yes! The secret word was {random_word}")
        info = input(f"Do you want me to send you more info about {random_word}? (y/n)\n")
        if info == 'y':
            email()    
        again = PlayAgain()

        if again == 'y':
            response = ''
            incorrect_guesses = ''
            correct_guesses = ''
            win_condition = False
            random_word, response = RetrieveWord()
        else:
            break

    if len(incorrect_guesses) == len(hangman):
        print("Game over.")
        game_over = True

    if game_over == True:
        print("You lose.")
        again = PlayAgain()
        if again == 'y':
            response = ''
            incorrect_guesses = ''
            correct_guesses = ''
            game_over = False
            random_word, response = RetrieveWord()
        else:
            break