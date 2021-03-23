#Lab11
while True:
    money = (input('Welcome to the Change Maker 5000 (tm)/nEnter a dollar amount: '))
    float_money = float(money)
    quarter = .25
    dime = .10
    nickel = .05
    penny = .01
    if float_money > quarter:
        quarters = float_money//quarter
        if quarters > 0 or quarters == 0:
            dimes = (float_money-(quarter*quarters))//dime
            if dimes > 0 or dimes == 0 :
                nickels = ((float_money-((quarter*quarters)+(dime*dimes))))//nickel
                if nickels > 0 or nickels == 0:
                    pennies = (float_money-((quarter*quarters)+(dime*dimes)+(nickel*nickels)))//penny
                    print(f'{int(quarters)} Quarters, {int(dimes)} Dimes, {int(nickels)} Nickels, and {int(pennies)} Pennies.')
                    more_change = (input('Would you like make more change?: '))
                    if more_change == 'yes':
                        continue
                    else:
                        print('Enjoy the rest of your day')
                        break