
cards = {
    "a": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "j": 10,
    "q": 10,
    "k": 10
}

print("Welcome to Blackjack")
card_1 = input("Enter your first card (a thru k) ")
card_2 = input("Enter your second card (a thru k) ")
card_3 = input("Enter your third card (a thru k) ")

hand = cards[card_1] + cards[card_2] + cards[card_3]

if hand < 17:
    print(f"{hand} Hit")
elif hand >= 17 and hand < 21:
    print(f"{hand} Stay")
elif hand == 21:
    print(f"{hand} Blackjack")
else:
    print(f"{hand} You Busted")
 
 
   