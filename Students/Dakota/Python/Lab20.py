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
matches = 0

def num_matches(winning, ticket):
    for i,j in list(zip(winning,ticket)):
        if i == j:
            matches += 1
    print(matches) 

for x in range(10):
    net_winnings = 0
    expenses = 0
    earnings = 0
    random_ticket = pick6()
    num_matches(winning_ticket,random_ticket)


# define variables
# Keep as few local variables, keep variables within functions or loops
# digits = string.digits
# computer_number = ''
# ticket_number = ''
# count = 1000
# output = digits
# ticket = 2

# randomly pick winner ticket
# for x in range(7):
#     count += 1
#     if x > 1:
#         computer_output = random.choice(output)
#         computer_number += computer_output
# winner = list(computer_number)
# print(f'The winning numbers are {winner}')
# #randomly pick user ticket
# for y in range(7):
#     if y > 1:
#         ticket_output = random.choice(output)
#         ticket_number += ticket_output
# ticket_number_list = list(ticket_number)
# print(f'Your ticket numbers are {ticket_number_list}')

# for i,j in enumerate(ticket_number_list):
#     if j == ticket_number_list:
#         print(f'You have no matches, sorry!')
#     if j in winner:
#         print(f'You have 1 match, you win {ticket * 2}')
