
class Person:
    def __init__(self, name, age):
        self.name = str(name)
        self.age = str(age)

    def display(self):
        return self.name, self.age

class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = str(section)
    def dis_student(self):
        return self.name, self.age, self.section

student = Student(name="Bobby", age="52", section="A-1")
print(student.dis_student())