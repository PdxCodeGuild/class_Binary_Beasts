'''
Theo Cocco
Lab 12 "Black Jack"
Friday March 12, 2021
'''

cards = {'2': 2, 
'3': 3, 
'4': 4, 
'5': 5, 
'6': 6, 
'7': 7, 
'8': 8,
'9': 9,
'10': 10,
'J': 10,
'Q': 10,
'K': 10,
'A': 11,}


card1 = (input('What is your first card? '))
card2 = (input('What is your second card? '))
card3 = (input('What is your third card? '))

user_cards = [card1, card2, card3]


for card in user_cards:
    total = cards[card1] + cards[card2] + cards[card3]
    if card == 'A' and total > 21:
        cards['A'] = 1

total = cards[card1] + cards[card2] + cards[card3]

if total == 21:
    print(f'{total} Blackjack!')
elif total < 17:
    print(f'{total} Hit')
elif total > 21:
    print(f'{total} Already Busted')
elif total >= 17:
    print(f'{total} Stay')
