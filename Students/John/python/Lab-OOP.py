#Bank Account

class Bank_Account:
    def __init__(self, account_number, name, balance):
       self.account_number = account_number
       self.name = name
       self.balance = balance
       
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount
        
    def bank_fees(self):
        self.balance *= 1.05
        
    def display(self):
        print(self.balance)


#Rectangle

class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w
        
    def calc_perimeter(self):
        self.perimeter = self.length * 2 + self.width * 2
        
    def calc_area(self):
        self.area = self.length * self.width
        
    def display(self):
        print(f"Length: {self.length}, Height: {self.width}, Perimeter: {self.perimeter}, Area: {self.area}")
    
class Parallelepipede(Rectangle):
    def __init__(self, h, *args):
        super().__init__(*args)
        self.height = h
    
    def calc_volume(self):
        self.volume = self.length * self.width * self.height
        

#Person

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
class Student(Person):
    def __init__(self, section, *args):
        super().__init__(*args)
        self.section = section
        
    def display_student(self):
        print(f"Name: {self.name}, Age: {self.age}, Section: {self.section}")