'''
Theo Cocco
Object Oriented Programming Lab
Monday, March 15, 2021
'''

# Bank Account Class

'''
class BankAccount:
    def __init__(self, accountnumber, name, balance):
        self.accountnumber = accountnumber
        self.name = name
        self.balance = balance
    def deposit(self, x):
        self.balance = self.balance + x
    def withdrawl(self, x):
        self.balance = self.balance - x
    def bankfees(self):
        self.balance = self.balance - (.05 * self.balance)
    def display(self):
        return (f'Welcome {self.name}, your account number is: {self.accountnumber}, and your balance is {self.balance}')

account1 = BankAccount(555, 'Theo', 1000000000.50)
account1.deposit(10000)
account1.withdrawl(5000)
account1.bankfees()

print(account1.display())
# Welcome Theo, your account number is: 555, and your balance is 950004750.475
'''

# Rectangle Class

"""
class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def perimeter(self):
        p = 2 * (self.l + self.w)
        return p
    def area(self):
        a = self.l * self.w
        return a
    def display(self):
        return (f'''
        Length: {self.l}
        Width: {self.w}
        Perimeter: {self.perimeter()}
        Area: {self.area()}''')

rectangle1 = Rectangle(5,6)

print(rectangle1.display())
'''
        Length: 5
        Width: 6
        Perimeter: 22
        Area: 30
'''

class Parallelepipede(Rectangle):
    def __init__(self, h, *args):
        super().__init__(*args)
        self.h = h
    def volume(self):
        v = self.l * self.w * self.h
        return v
    def display(self):
        return (f'''
        Length: {self.l}
        Width: {self.w}
        Perimeter: {self.perimeter()}
        Area: {self.area()}
        Volume: {self.volume()}''')

parallelepipede1 = Parallelepipede(7,6,6)

print(parallelepipede1.display())
'''
        Length: 6
        Width: 6
        Perimeter: 24
        Area: 36
        Volume: 252
'''
"""

# Person Class

"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        return (f'Name: {self.name}, Age: {self.age}')

theo = Person('Theo', 27)

print(theo.display())

# Name: Theo, Age: 27

class Student(Person):
    def __init__(self, section, *args):
        super().__init__(*args)
        self.section = section
    def display(self):
        return (f'Name: {self.name}, Age: {self.age}, Section: {self.section}')

ares = Student('Band', 'Ares', 7)

print(ares.display())

# Name: Ares, Age: 7, Section: Band
"""