import random
earnings = 0
expenses = 0
match_count = 0
match_dict = {1:4,2:7,3:100,4:50000,5:1000000,6:25000000}
possible_nums_list = list(range(1,100))
pick6_list = []
customer_ticket = []


def pick6(target_list):
    for x in range(6):
        target_list.append(random.choice(possible_nums_list))



pick6(pick6_list)

for x in range(100000):
    customer_ticket = []
    match_count = 0
    pick6(customer_ticket)
    expenses += 2
    for x in range(6):
        if pick6_list[x] == customer_ticket[x]:
            match_count += 1

    if match_count != 0:
        earnings += match_dict[match_count]

print(f"Final Balance $ {earnings - expenses} ")
print(f"ROI {(earnings - expenses)/expenses}% ")


