class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self. width = width


    def perimeter(self):
        return (2*(self.length * self.width))
    
    def area(self):
        return (self.length * self.width)

    def display(self):
        print(self.perimeter())
        print(self.area())

r1 = Rectangle(45, 2)

r1.display()
