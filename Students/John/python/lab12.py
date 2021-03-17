"""

all codes are written and created by John Robson Wed Mar 10, 2021

"""

import random

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K"]


def get_value(card):
    if card == "J" or card == "Q" or card == "K":
        return 10
    elif card == "A":
        return 11
    else:
        return card


def check_aces(hand):
    index = 0
    for card in hand:
        sum = 0
        for c in hand:
            sum += get_value(c)
        if card == "A" and sum > 21:
            hand[index] = 1
            check_aces(hand)
        index += 1
    
    return hand, sum

def get_advice(hand):
    sum = 0
    for card in hand:
        sum += get_value(card)
        
    if sum > 21:
        hand, sum = check_aces(hand)
        
    print("Your hand is " + str(sum))
    
    if sum > 21:
        print("Already Busted")
    elif sum == 21:
        print("Blackjack!")
    elif sum >= 17:
        print("Stay")
    else:
        print("Hit")
        
while True:
    print("Welcome to blackjack") 
    print("Your cards are:")
    
    hand = []
    i = 0
    while i < 3:
        card = random.choice(cards)
        print(card)
        hand.append(card)
        i += 1
    
    if input("Play again?").lower() == "no":
        break
                
