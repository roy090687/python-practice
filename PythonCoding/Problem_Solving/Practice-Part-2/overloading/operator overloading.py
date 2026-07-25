class ComplexNumber:

    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary

    def __add__(self, other):
        return f"{self.r + other.r} + {self.i + other.i}i"

    def __sub__(self, other):
        return str(self.r - other.r) + " " + str(self.i - other.i) + "i"

c1 = ComplexNumber(3, 5)
c2 = ComplexNumber(4, 2)

print(c1 + c2)

print(c1 - c2)

