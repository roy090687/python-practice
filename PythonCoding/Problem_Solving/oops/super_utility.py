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

circle = Circle("red", True, 2)
square = Square(color="red", is_filled=False, length=4)
triangle = Triangle("yellow", True, length=3, height=5)

print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")
circle.describe()

print("================================")

print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.length}cm")
print(f"{triangle.height}cm")
triangle.describe()



