class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False

p1 = Person("Ram", 32)
p2 = Person("Priya", 29)

print(p1 > p2)
