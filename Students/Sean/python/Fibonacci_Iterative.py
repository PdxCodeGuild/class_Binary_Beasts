def Fibon(n):
    fib_list = []
    for i in range(n):
        if len(fib_list) < n:
            if len(fib_list) < 2:
                fib_list.append(1)
                continue
            fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list

while True:
    try:
        print(Fibon(int(input("Please enter the number of numbers you'd like in your fibonacci sequence. \n> "))))
    except Exception as exc:
        print("Please enter a valid number.")