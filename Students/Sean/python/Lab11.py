def changer(x):
    change = []
    change.append(x // coins[0][1])
    remainder = x % coins[0][1]

    change.append(remainder // coins[1][1])
    remainder = remainder % coins [1][1]

    change.append(remainder // coins[2][1])
    remainder = remainder % coins[2][1]

    change.append(remainder // coins[3][1])
    remainder = remainder % coins[3][1]

    change.append(remainder // coins[4][1])

    return change



coins = [
    ('half-dollar', .50),
    ('quarter', .25),
    ('dime', .10),
    ('nickel', .05),
    ('penny', .01),
]

cash = 4.49
converted = changer(cash)
print(
    f"""Converted {cash} into
    {converted[0]} {coins[0][0]}(s)
    {converted[1]} {coins[1][0]}(s)
    {converted[2]} {coins[2][0]}(s)
    {converted[3]} {coins[3][0]}(s)
    {converted[4]} {coins[4][0]}(s)
    """)