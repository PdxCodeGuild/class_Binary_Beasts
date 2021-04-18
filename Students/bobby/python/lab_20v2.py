import random

pick_6 =[]
for x in range (6):
    pick_6.append(random.randint(0, 100))
# print(pick_6)

def player_picks():
    pl_tik =[]
    for x in range (6):
        pl_tik.append(random.randint(0, 100))
    # print(pl_tik)
    return pl_tik

def earn_calc(match, earnings):
    if match == 0:
        earnings -= 2
    if match == 1:
        earnings += 4
    if match == 2:
        earnings += 7
    if match == 3:
        earnings += 100
    if match == 4:
        earnings += 50000
    if match == 5:
        earnings += 1000000
    if match == 6:
        earnings += 25000000
    # print(f"match {match}")
    return earnings
        
count = 0
earnings = 0
total = 0

for x in range(100000):
    count += 1
    match = 0
    play = player_picks()
    for i in range(len(pick_6)):
        if pick_6[i] == play[i]:            
            match +=1
    total += earn_calc(match, earnings)
expenses = total - (count * 2)
roi = (total - expenses) / expenses
print(f"earnings= {total}")
print(f"expenses= {expenses}")
print((f"ROI= {int(roi * 100)}"))
            
