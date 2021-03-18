class BankAccount:
    def __init__(self, AccNum, Owner, Balance):
        self.AccNum = AccNum
        self.Owner = Owner
        self.Balance = Balance
    def deposit(self):
        deposit = float(input("Deposit amount: "))
        self.Balance += deposit
        print(self.Balance)
    def withdraw(self):
        withdraw = float(input("Withdraw amount: "))
        self.Balance -= withdraw
        print(self.Balance)
    def bankFees(self):
        self.Balance = Balance - (Balance * .5)
    def display(self):
        print(f"Account number: {self.AccNum}, Owner: {self.Owner}, Balance: {self.Balance}.")

s = BankAccount('1234','Sean',1000.0)

s.deposit()
s.withdraw()
s.display()