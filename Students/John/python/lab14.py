"""

all codes are written and created by John Robson Thu Mar 11, 2021

"""

# Version 1

from os import replace


def run_version1(num):
    teens = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    teen_words = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
                  "seventeen", "eighteen", "nineteen"]
    ones = ["one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine"]
    tens = ["twenty", "thirty", "fourty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

    def convert_to_word(num):
        if num in teens:
            return teen_words[teens.index(num)]
        elif num < 10:
            return ones[num - 1]
        elif num % 10 == 0:
            return tens[num//10 - 2]
        else:
            return tens[num//10 - 2] + "-" + ones[num % 10 - 1]

    return convert_to_word(num)

# Version 2


def run_version2(num):
    teens = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    teen_words = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
                  "seventeen", "eighteen", "nineteen"]
    ones = ["one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine"]
    tens = ["twenty", "thirty", "fourty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]
    h = "-hundred"

    def convert_to_word(num):
        buf = ""
        if num % 100 == 0:
            return ones[num // 100 - 1] + h
        elif num > 100:
            buf += ones[num // 100 - 1] + h + " and "
            num = num % 100
        if num in teens:
            buf += teen_words[teens.index(num)]
        elif num < 10:
            buf += ones[num - 1]
        elif num % 10 == 0:
            buf += tens[num // 10 - 2]
        else:
            buf += tens[num // 10 - 2] + "-" + ones[num % 10 - 1]
        return buf

    return convert_to_word(num)

# Version 3


def run_version3(num):

    def convert_to_roman(num):
        roms = ["M", "CM", "D", "CD", "C", "XC",
                "L", "XL", "X", "IX", "V", "IV", "I"]
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numeral = ""
        i = 0
        while num > 0:
            for x in range(num // vals[i]):
                numeral += roms[i]
                num -= vals[i]
            i += 1
        return numeral

    return convert_to_roman(num)


# Version 4

def run_version4(time):

    time = time.split(":")
    h = time[0]
    m = time[1]

    if int(h) > 0:
        h = run_version1(int(h))
        if h == "one":
            h += " hour and "
        else:
            h += " hours and "
    else:
        h = "no hours and "

    if int(m) > 0:
        m = run_version1(int(m))
        if m == "one":
            m += " minute"
        else:
            m += " minutes"
    else:
        m = "no minutes"
            

    return h + m


versions = [run_version1, run_version2, run_version3, run_version4]

while True:
    strategy = 0

    print('Welcome. You can type "done" at any time to exit.')

    while strategy < 1 or strategy > 4:
        strategy = int(input("Which version would you like to run: 1 - 4"))
        if strategy == "done":
            break
        
    if strategy == "done":
        break
    
    num = 0
    h = -1
    m = -1
    
    if strategy == 1:
        while num < 1 or num > 99 or type(num) is not int:
            num = int(input("Please enter a number 1 - 99:"))
    elif strategy == 2:
        while num < 1 or num > 999 or type(num) is not int:
            num = int(input("Please enter a number 1 - 999:"))
    elif strategy == 3:
        while num < 1 or num > 99:
            num = int(input("Please enter a number 1 - 99:"))
    elif strategy == 4:
        while h < 0 or num > 99 or type(h) is not int:
            h = int(input("Number of hours (0 - 24):"))
        h = str(h)
        h += ":"
        while m < 0 or m > 59 or type(m) is not int:
            m = int(input("Number of minutes (0 - 59):"))
        num = h + str(m)
        print("You entered: " + num)

    strategy = versions[strategy - 1]

    print(strategy(num))
    
    