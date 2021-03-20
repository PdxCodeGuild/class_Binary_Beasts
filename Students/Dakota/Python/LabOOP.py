#Lab OOP
#Create Bank Account Class 
class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    def Deposit(self, total):
        self.balance = total
        print('You are depositing', self.balance, 'into your account')
    def Withdrawal(self, total):
        self.balance = self.balance - total
        print('You are withdrawaling', self.balance, 'from your account')
    def bankFee(self, total):
        bankFees = self.balance * 0.05
        print('You will be charged', bankFees, 'from your account')
    def display(self):
        print('You current balance for', self.name, 'is', self.balance)
bank = BankAccount('Bank Account 42', '42 checkings', 100000)

bank.Deposit(500)
bank.Withdrawal(200)
bank.bankFee(500)
bank.display()

#Rectangle Class 
class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = int(lenght)
        self.width = int(width)
    def Perimeter(self):
        self.perimeter = 2*(self.lenght + self.width)
        print('The perimeter of your rectangle is', self.perimeter)
    def Area(self):
        self.area = self.lenght * self.width
        print('The area of your rectangle is', self.area)
    def display(self, Rectangle):
        print('Lenght is: ',self.lenght, 'Width is: ',self.width, 'Perimeter is: ',self.perimeter, 'Area is: ', self.area)
    def Parallelepipede(self, Rectangle, height):
        self.height = height
        self.volume = self.lenght * self.width * self.height
        print('The Parallelepipede is: ', self.volume)
rect = Rectangle(4,2)
rect.Perimeter()
rect.Area()
rect.display(rect)
rect.Parallelepipede(rect,2)

#Person Class
class Person:
    def __init__(self, name, age):
        self.name = str(name)
        self.age = str(age)
    def display(self):
         print(self.name + ' ' + self.age)
class Student(Person):
    def __init__(self, section):
        self.section = str(section)    
    def displayStudent(self):
        return self.name + ' ' + self.age + ' ' + self.section

person = Person('Dakota', '31')
section = displayStudent('Masters')
person.display()
section.displayStudent()
