#lab 12
playing_cards = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10, 'Q':10, 'K':10}
p1 = input('What is your first card?: ')
p2 = input('What is your second card?: ')
p3 = input('What is your third card?: ')

p1_int = int(playing_cards[p1])
p2_int = int(playing_cards[p2])
p3_int = int(playing_cards[p3])
p_total = p1_int + p2_int + p3_int

if p_total < 17:
    print('Hit.')
elif p_total > 17 and p_total < 21:
    print('Stay,')
elif p_total == 21:
    print('Blackjack!')
elif p_total > 21:
    print('Already busted.')