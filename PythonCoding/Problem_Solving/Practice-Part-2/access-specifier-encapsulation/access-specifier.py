class Student:

    def __init__(self, name, roll, age):
        self.name = name  # public instance variable
        self._roll = roll  # protected instance variable
        self.__age = age   # private instance variable

    def display(self):
        print(f"Hey, Myself {self.name}")

class Child(Student):
    pass

c1 = Child("Snehasish", 5, 30)

print(c1.name)
print(c1._roll)
# print(c1.__age) # private can't be accessed directly
print(c1._Student__age)

