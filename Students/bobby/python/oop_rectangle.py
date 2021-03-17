
class Rectangle:
    def __init__(self, length, width):
        self.length = int(length)
        self.width = int(width)

    def calc_perimeter(self):
        perimeter = self.length*2 + self.width*2
        return perimeter

    def calc_area(self):
        area = self.length * self.width
        return area
    def display(self):
        return self.length, self.width,self.calc_perimeter(), self.calc_area()

class Parallel(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = int(height)

    def calc_volume (self):
        return self.length * self.width * self.height # Deleted variable ( not realy needed for this as I did above)John helped me with this
        




rect_size = Rectangle(length="10", width="10")
parallel = Parallel(length="10", width="10", height="10") # Can also pass integers

print(rect_size.length)
print(rect_size.width)
print(rect_size.calc_perimeter()) # Always use open parenthesis when calling a method
print(rect_size.calc_area())
print(rect_size.display())
print(parallel.calc_volume())