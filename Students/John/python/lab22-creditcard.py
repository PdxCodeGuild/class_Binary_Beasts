"""

all codes are written and created by John Robson Fri Mar 12, 2021

"""

#Version 1 (functions only)

def get_card_number():
    while True:
        try:
            card = input('Please enter your 16 digit card number or "skip" to use default number')
            if card == "skip":
                return ""
            card = int(card)
            card = str(card)
            if len(card) == 16:
                return str(card)
        except:
            continue
        
def break_into_list(c):
    return list(c)

def remove_last_digit(c):
    c.pop()
    return c

def reverse_order(c):
    c.reverse()
    return c

def double_numbers(c):
    i = 0
    while i < len(c):
        if i % 2 == 0:
            c[i] = int(c[i]) * 2
        i += 1
    return c

def reduce_high_numbers(c):
    for n in c:
        if int(n) > 9:
            c[c.index(n)] = int(n) - 9
    return c

def sum_all_digits(c):
    sum = 0
    for n in c:
        sum += int(n)
    return sum

def get_last_digit(c):
    if type(c) is int:
        return c % 10
    if type(c) is str:
        return c[len(c) - 1]
    
def verify_results(c, d):
    if c == int(d):
        return "Valid"
    else:
        return "Invalid"

def run_version1():
    card = get_card_number()
    if card == "":
        card = "4556737586899855"
    
    c = break_into_list(card)
    c = remove_last_digit(c)
    c = reverse_order(c)
    c = double_numbers(c)
    c = reduce_high_numbers(c)
    c = sum_all_digits(c)
    c = get_last_digit(c)
    card_last = get_last_digit(card)
    print(verify_results(c, card_last))
    


#Version 2 (Class and methods)
#Verification runs once, then deletes itself. Must verify every time you want verification

class Card():
    __number = "4556737586899855"
    __verify = "Verification Required"
    
    def get_num(self):
        return self.__number
    
    def set_number(self, card):
        self.__number = card
        
    def verify(self):
        temp_verification = self.__break_into_list()
        self.__verify = "Verification Required"
        return temp_verification
        
    def __break_into_list(self):
        self.__verify = list(self.__number)
        return self.__remove_last_digit()

    def __remove_last_digit(self):
        self.__verify.pop()
        return self.__reverse_order()

    def __reverse_order(self):
        self.__verify.reverse()
        return self.__double_numbers()

    def __double_numbers(self):
        i = 0
        while i < len(self.__verify):
            if i % 2 == 0:
                self.__verify[i] = int(self.__verify[i]) * 2
            i += 1
        return self.__reduce_high_numbers()

    def __reduce_high_numbers(self):
        for n in self.__verify:
            if int(n) > 9:
                self.__verify[self.__verify.index(n)] = int(n) - 9
        return self.__sum_all_digits()

    def __sum_all_digits(self):
        sum = 0
        for n in self.__verify:
            sum += int(n)
        self.__verify = sum
        return self.__get_last_digit()

    def __get_last_digit(self):
        self.__verify = self.__verify % 10
        return self.__get_last_card_digit()
            
    def __get_last_card_digit(self):
        self.__verify = list(str(self.__verify))
        self.__verify.append(self.__number[len(self.__number) - 1])
        return self.__verify_results()
        
    def __verify_results(self):
        if self.__verify[0] == self.__verify[1]:
            self.__verify = "Card Valid"
        else:
            self.__verify = "Card Invalid"
        return self.__show_verification_results()
        
    def __show_verification_results(self):
        return self.__verify
            
      
def run_version2():
    card = Card()
    
    num = get_card_number()
    if num != "":
        card.set_number(num)
    verification = card.verify()
    
    print(verification)
    
versions = [run_version1, run_version2]

while True:
    strategy = 0

    print('Welcome. You can type "done" at any time to exit.')
    
    m = len(versions)

    while strategy not in range(1, m + 1):
        try:
            strategy = input(f"Which version would you like to run: 1 - {m}")
            if strategy == "done":
                break
            strategy = int(strategy)
        except:
            continue
        if strategy == "done":
            break

    strategy = versions[strategy - 1]

    strategy()