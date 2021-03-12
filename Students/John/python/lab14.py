"""

all codes are written and created by John Robson Wed Mar 10, 2021

"""

# Version 1


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

    print(convert_to_word(num))


# Version 2


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

    print(convert_to_word(num))