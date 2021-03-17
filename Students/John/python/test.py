class Rectangle:
    def __init__(self, length, width):
        self.length = int(length)
        self.width = int(width)
    def calc_perimeter(self):
        perimeter = (self.length*2 + self.width*2)
        return perimeter
rect_size = Rectangle(length="10", width="10")
# print("The perimeter of the rectangle is ", Rectangle.perimeter)
print(rect_size.length)
print(rect_size.width)
print(rect_size.calc_perimeter())