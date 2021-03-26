#Lab Credit Card 

credit_card = "4556737586899855"

def doubled(c):
    for i in range(len(c)):
        if i%2 == 0:
            c[i] = int(c[i])*2
    return c

def over_nine(c):
    for i in c:
        if int(i) > 9:
            c[c.index(i)] = int(i)-9
    return c

def verify_card(card):
    c = list(card)
    c.pop()
    c.reverse()
    c = doubled(c)
    c = over_nine(c)
    c = sum([int(x) for x in c])
    return 'Valid' if c%10 == int(card[-1]) else 'Not Valid'

print(verify_card(credit_card))
