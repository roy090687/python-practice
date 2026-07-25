""" In the Vector new‑object approach, while returning a new Vector object, you need to overload __str__() to control how it prints.
The output may look like a tuple (x, y), but it’s actually a string representation of the object, not a real tuple."""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload +
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Overload -
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # Overload ==
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1 + v2)   # calls __add__ → (6, 8)
print(v2 - v1)   # calls __sub__ → (2, 2)
print(v1 == v2)  # calls __eq__ → False
