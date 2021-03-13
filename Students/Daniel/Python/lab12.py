card_points = {"A": 1, "2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
user_input = input("Please enter 3 playing cards separated by a comma: ").upper()

user_input = user_input.replace(" ","")
user_input = list(user_input.split(","))
points = 0
for card in user_input:
    points += card_points[card]

if points < 17:
    print("Hit")
elif 17 <=points < 21:
    print("Stay")
elif points == 21:
    print("Blackjack!")
else:
    print("Already Busted")

