'''
Theo Cocco
Thursday March 25, 2021
Lab 18, ATM
'''

class ATM:
    def __init__(self, balance, apr):
        self.balance = 0
        self.apr = 0.1

    def balance(self):
        return self.balance

    def deposit(self, x):
        self.balance += x
    
    def __check_withdrawl__(self, x):
        if self.balance - x >= 0:
            return True
        else: 
            return False
         
    def withdraw(self, x):
        if __check_withdrawl__(x) == True:
            self.balance -= x
        else: 
            False
    
    def calc_interest(self):
        return self.balance * self.apr

atm = ATM(0, 0.1)
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
        if atm.withdraw(amount) == False:
            print('Insufficient funds')
        else:
            atm.withdraw(amount)
            print(f'Withdrew ${amount}')
    elif command == 'interest':
        amount = atm.calc_interest()
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')