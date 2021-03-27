def Fibon(n):
    if n == 0 or n == 1:
        return 1
    return Fibon(n-1) + Fibon(n-2)











while True:
    try:
        print(Fibon(int(input("Please enter the number of numbers you'd like in your fibonacci sequence. \n> "))))
    except Exception as exc:
        print("Please enter a valid number.")