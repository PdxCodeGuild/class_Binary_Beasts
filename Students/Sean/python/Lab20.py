import random

def pick6(x):
    expenses = 0
    earnings = 0
    for i in range(x):
        ticket = []
        lucky6 = []
        while len(lucky6) < 6:
            lucky6.append(random.randint(1,99))
        #print(f"lucky 6: {lucky6}")

        expenses -= 2

        #print(f"Balance: {bal}")

        while len(ticket) < 6:
            ticket.append(random.randint(1,99))
        #print(f"Your ticket: {ticket}")

        matches = 0
        for i in range(len(ticket)):
            if ticket[i] == lucky6[i]:
                matches += 1
        #print(f"Lucky 6 matches: {matches}")

        if matches == 1:
            earnings += 4
        elif matches == 2:
            earnings += 7
        elif matches == 3:
            earnings += 100
        elif matches == 4:
            earnings += 50000
        elif matches == 5:
            earnings += 1000000
        elif matches == 6:
            earnings += 25000000
    print(f"Your earnings were: {earnings}")
    print(f"Your end balance: {expenses + earnings}")
    print(f"Your ROI for the 100,000 tickets was {(earnings - expenses) / expenses}")

pick6(100000)