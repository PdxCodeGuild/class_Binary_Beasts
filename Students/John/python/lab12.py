"""

all codes are written and created by John Robson Wed Mar 10, 2021

"""

import random

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K"]


def getValue(card):
    if card == "J" or card == "Q" or card == "K":
        return 10
    elif card == "A":
        return 11
    else:
        return card


def checkAces(cards):
    ace = ""
    sum = 0
    index = 0
    for card in cards:
        if card == "A" and ace != "found":
            ace = "found"
            cards[index] = 1
            sum += 1
        else:
            sum += getValue(card)
        index += 1
        
    if sum > 21 and ace == "found":
        checkAces(cards)

    return cards

def getAdvice(cards):
    hand = 0
    for card in cards:
        hand += getValue(card)
        
    if hand > 21:
        hand = 0
        cards = checkAces(cards)
        
        for card in cards:
            hand += getValue(card)
        
        
    print("Your hand is " + str(hand))
    
    if hand > 21:
        print("Already Busted")
    elif hand == 21:
        print("Blackjack!")
    elif hand >= 17:
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
        
    getAdvice(hand)
    
    if input("Play again?").lower() == "no":
        break
                
