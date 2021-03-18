
coins = [
    ("half-dollar", .50),
    ("qtr", .25),
    ("dim", .10),
    ("nic", .05),
    ("pen", .01)
]
def mk_chng(dol_amt, coin_val):
    num_coins = dol_amt // coin_val
    return int(num_coins)

print ("Welcome")
dol_amt = float(input("Enter a dollar amount: "))

for coin in coins:
    num_coins = mk_chng(dol_amt, coin[1])
    dol_amt -= round(num_coins * coin[1],2)
    print(f"{coin[0]} = {num_coins}")


