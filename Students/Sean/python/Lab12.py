cards = {
    'a':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
    '8':8, '9':9, '10':10, 'j':10, 'q':10, 'k':10,
}


def please_advise(x):
    hand = 0
    for card in x:
        for y in cards:
            if card == y:
                hand += cards[y]
    if 'a' in x and hand <= 10:
        hand += 10

    print(hand)
    if hand <= 16:
        return "hit"
    if hand >= 17 and hand < 21:
        return "stay"
    if hand == 21:
        return "blackjack!"
    if hand >= 22:
        return "bust!"

player_has = []

player_has.append(input("What is the first card in your hand?"))
player_has.append(input("What is the second card in your hand?"))
player_has.append(input("What is the third card in your hand?"))
print(please_advise(player_has))