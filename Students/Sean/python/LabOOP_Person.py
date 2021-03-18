class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class student(person):
    def __init__(self, section, *args):
        super().__init__(*args)
        self.section = section
    def displayStudent(self):
        print(f"Name: {self.name}\nAge: {self.age}\nSection: {self.section}")

p = person("Sean", 18)
s = student("Math","Sara",19)

p.display()
s.displayStudent()