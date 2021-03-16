class Person:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(amount):
        self.balance += amount
        return True

    def withdrawal(amount):
        self.balance -= amount
        return True

    def bank_fees():
        self.balance = self.balance * .05

    def display(self):
        print(self.account_number,self.name,self.balance)

    


p1 = Person(104532, "John Smith", 8675309)


p1.display()