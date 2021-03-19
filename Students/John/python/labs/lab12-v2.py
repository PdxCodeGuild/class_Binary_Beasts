"""

all codes are written and created by John Robson Wed Mar 10, 2021

"""

#Version 2
#This version was built using Classes

import random

class Card:
    def __init__(self, name):
        self.name = str(name)
        self.__get_value(name)
    
    def __get_value(self, name):
        try:
            self.value = int(name)
        except:
            if self.name in ["J", "Q", "K"]:
                self.value = 10
            else:
                self.value = 11
    
    def __repr__(self):
        return self.name 

class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.__calc_value()
        
    def __calc_value(self):
        value = 0
        for card in self.cards:
            value += card.value
        self.value = value
    
    def __flip_aces(self):
        for card in self.cards:
            if card.name == "A" and self.value > 21:
                card.value = 1
                self.__calc_value()
                self.__flip_aces()
                
    def __get_advice(self):
        if self.value > 21:
            return "Already Busted"
        elif self.value == 21:
            return "Blackjack!"
        elif self.value >= 17:
            return "Stay"
        else:
            return "Hit"
                
    def play_hand(self):
        if self.value > 21:
            self.__flip_aces()
            
        return self.__get_advice()
    
    def __repr__(self):
        return f"Hand: {self.cards}, Value: {self.value}"
        
        

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K"]

while True:
    print("Welcome to blackjack") 
    
    hand = []
    i = 0
    while i < 3:
        card = Card(random.choice(cards))
        hand.append(card)
        i += 1
        
    hand = Hand(hand)
    advice = hand.play_hand()
    
    print(hand)
    print(advice)
    
    if input("Play again?").lower() == "no":
        break
                
