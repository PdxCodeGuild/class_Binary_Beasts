#Lab11
money = (input('Welcome to the Change Maker 5000 (tm)/nEnter a dollar amount: '))
float_money = float(money)
quarter = .25
dime = .10
nickel = .05
penny = .01
while True:
    if float_money > quarter:
        quarters = float_money//quarter
        print(quarters)
        break
    elif float_money > dime:
        dimes = float_money//dime
        print(dimes)
    elif float_money > nickel:
        dimes = float_money//nickel
        print(nickel)
    elif float_money > penny:
        dimes = float_money//penny
        print(penny)