while True:
    print("Welcome to the Change Maker 5000 (tm) ")
    dollar_amount = float(input("Enter a dollar amount: "))
    dollar_amount = round(dollar_amount,2)
    coins = {'half-dollar': .50, 'quarter': .25, 'dime':.10, 'nickel':.05, 'penny':.01}
    change = 0.0
    user_choice = ""

    while dollar_amount != 0.0:     
        for k,v in coins.items():
            change = dollar_amount // v
            if k == "penny":                                     #handling special case where float does not return 0. Will research further later.
                dollar_amount = int(dollar_amount - (change*v))
            else:
                dollar_amount = dollar_amount - (change*v)
            if change != 0.0:
                print(f"{k}:  {change} ")
    user_choice = input("Would you like to make more change? Enter Y for yes and N for no: ")
    if user_choice == "N":
        break
