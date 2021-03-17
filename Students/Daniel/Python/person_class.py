class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def display(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self, name, age, section):
        self.name = name
        self.age = age
        self.section = section

    def display(self):
        print(self.name, self.age, self.section)


p1 = Person("Heather", 29)
p1.display()

s1 = Student("Daniel", 31, "HR")
s1.display()