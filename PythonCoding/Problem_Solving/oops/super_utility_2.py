class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        Shape.__init__(self, color, is_filled)   # direct call
        self.radius = radius

class Square(Shape):
    def __init__(self, color, is_filled, length):
        super().__init__(color, is_filled)    # using super()
        self.length = length

class Triangle(Shape):
    def __init__(self, color, is_filled, length, height):
        super().__init__(color, is_filled)
        self.length = length
        self.height = height

    def describe(self):
        super().describe()
        print(f"The area of Triangle is {0.5 * self.length * self.height}cm^2")

shapes = [
    Circle("red", True, 2),
    Square(color="blue", is_filled=False, length=4),
    Triangle("yellow", True, length=3, height=5)
]

for shape in shapes:
    shape.describe()
    print("------------------")

print("========== Another Way ==========")
# another way of printing all
for shape in shapes:
    # Common attributes
    print(shape.color, shape.is_filled)

    # Extra attributes depending on type
    if isinstance(shape, Circle):
        print(f"For Circle: Radius is {shape.radius}")
        shape.describe()
    elif isinstance(shape, Square):
        print(f"For Square: Length is {shape.length}")
        shape.describe()
    elif isinstance(shape, Triangle):
        print(f"For Triangle: Length is {shape.length} and Height is {shape.height}")
        shape.describe()

    print("--------------------------")





