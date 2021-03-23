def valid8(x):

    CC_number = []

    for i in x:
        CC_number.append(i)

    for i in range(0,len(CC_number)):
        CC_number[i] = int(CC_number[i])

    check_digit = CC_number[-1]
    CC_number.pop()
    CC_number.reverse()
    reverse = 0

    for i, e in enumerate(CC_number):
        if i % 2 == 0:
           CC_number[i] = e*2

    for i, e in enumerate(CC_number):
        if e > 9:
            CC_number[i] = e-9
    print(CC_number)
    sum_digits = []
    sum_digits.append(sum(CC_number))
    print(sum_digits)

    #Need to get second digit only
    if sum_digits[0] == check_digit[0]:
        return True
    else:
        return False



while True:
    try:
        x = input("Enter your credit card number to validate: ")
    except Exception as exc:
        print(exc)

    print(f"Credit card validity: {valid8(x)}")
    break