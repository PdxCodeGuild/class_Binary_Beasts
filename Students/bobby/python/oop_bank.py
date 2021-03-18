
class Bank_Account:
    def __init__(self, account_number, name, balance):
        self.account_number = int(account_number)
        self.name = str(name)
        self.balance = float(balance)

    def deposit(self, add_deposit): # need add_deposit because it is new info not in Bank_Account otherwise just (self) is needed
        self.balance = self.balance + add_deposit

    def withdrawl(self, withdrawl):
        self.balance = self.balance - withdrawl

    def bank_fees(self, bank_fees):
        self.balance = self.balance *.05

johns_account = Bank_Account(account_number="12543", name="Jonathon Bixby", balance="400")
bobbys_account = Bank_Account(account_number="54321", name="Bobby Estes", balance="100")
while True:
    print("Welcome to the bank!")
    trans = input("What transaction would you like to perform: account number, name, balance or none to quit ")

    if trans == "none":
        print("Goodbye")
        break

    elif trans == ("account number"):
        print("Your account number is: ", bobbys_account.account_number)

    elif trans == ("name"):
        print("Your name is: ", bobbys_account.name)

    elif trans == ("balance"):
        print("Your balance is: ", bobbys_account.balance)





# johns_account.withdrawl(100)
# print("John's balance is: ", johns_account.balance)


# bobbys_account.deposit(100)
# print("Bobby's balance is: ",bobbys_account.balance)
