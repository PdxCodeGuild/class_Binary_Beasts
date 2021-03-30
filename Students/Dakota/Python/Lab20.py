# Lab 20
# Pick 6 random numbers using random module
import random

def pick6():
    temp_list = []
    for _ in range(6):
        temp_list.append(random.randint(1, 99))
    return temp_list


payoff = [(1, 4), (2, 7), (3, 100), (4, 50_000),
          (5, 1_000_000), (6, 25_000_000)]

winning_ticket = pick6()

def num_matches(winning, ticket):
    matches = 0
    for i,j in list(zip(winning,ticket)):
        if i == j:
            matches += 1
    return matches

expenses = 0
earnings = 0

for x in range(100_000):
    expenses += 2
    matches = 0
    random_ticket = pick6()
    matches = num_matches(winning_ticket,random_ticket)
    for m,v in payoff:
        if matches == m:
            earnings += v
    
net_winnings = earnings - expenses   
print(f'Total earnings equal to {net_winnings}')
print(f'ROI: {(earnings - expenses)/expenses}')