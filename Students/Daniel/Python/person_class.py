class Person:
    def __init__(self, name, age):
        name = self.name
        age = self.age
        

    def display(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self, name, age, section):
        name = self.name
        age = self.age
        section = self.section

    def display(self):
        print(self.name, self.age, self.section)


p1 = Person("Heather", 29,"HR")