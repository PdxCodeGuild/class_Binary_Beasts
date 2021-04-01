"""

all codes are written and created by John Robson Fri Mar 12, 2021

"""

#Version 1 and 2

class ATM:
    
    def __init__(self):
        self.__balance = 0
        self.__interest_rate = 0.0002
        self.__history = []
        
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount
        self.__add_to_history("Deposit: $" + str(amount))
        
    def check_withdrawal(self, amount):
        return self.__balance - amount >= 0
        
    def withdraw(self, amount):
        self.__balance -= amount
        self.__add_to_history("Withdrawal: $" + str(amount))
        
    def calc_interest(self):
        return self.__balance * self.__interest_rate
        
    def __add_to_history(self, transaction):
        self.__history.append(transaction)

    def view_history(self):
        return self.__history

atm = ATM()
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.balance()
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount)
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest()
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'history':
        history = atm.view_history()
        print(history)
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('history - show history')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')