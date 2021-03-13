print('Welcome to the change maker 3000!')

while True:
    dollars = float(input('Enter a dollar amount: '))
    quarters = dollars // .25
    dimes = (dollars - (quarters * .25)) // .10
    nickels = (dollars - (quarters * .25) - (dimes * .10)) // .05
    pennies = (dollars - (quarters * .25) - (dimes * .10) - (nickels * .05)) // .01
    print(f'{int(quarters)} quarters, {int(dimes)} dimes, {int(nickels)} nickels, {int(pennies)} pennies.')
    again = input('Would you like to try again? Enter "no" to quit: ')
    if again == 'no':
        break
