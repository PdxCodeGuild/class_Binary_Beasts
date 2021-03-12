import random

plays = {
    'rock':['lizard','scissors'],
    'paper':['rock','spock'],
    'scissors':['paper','spock'],
    'lizard':['spock','paper'],
    'spock':['scissors','rock'],
    }

def play(u):
    com = random.choice(list(plays))
    if u in plays[com]:
        outcome = f"{u} beats {com}. You win."
        return outcome

    elif com in plays[u]:
        outcome = f"{com} beats {u}. You lose."
        return outcome
    
    else:
        outcome = f"You both chose {com}. That's a tie."
        return outcome

while True:
    user = input("Please enter 'rock', 'paper', 'scissors', 'lizard', or 'spock'.\nEnter 'done' when you've had enough.\n> ")
    if user == 'done':
        break
    elif user in plays:
        outcome = play(user)
        print(outcome)
    else:
        continue