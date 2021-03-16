class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def length_input(self):
        length = int(input("Enter length: "))
        self.length = length
    def width_input(self):
        width = int(input("Enter width: "))
        self.width = width
    def display(self):
        print(f"Length: {self.length}\nWidth: {self.width}\nArea: {self.width * self.length}")

class parallel(rectangle):
    def __init__(self, height, *args):
        super().__init__(*args)
        self.height = height
    def height_input(self):
        height = int(input("Enter height: "))
        self.height = height
    def volume(self):
        print(f"Volume: {self.length * self.width * self.height}")

r = rectangle(0,0)

r.length_input()
r.width_input()
r.display()

p = parallel(0,0,0)

p.length_input()
p.width_input()
p.height_input()
p.display()
p.volume()