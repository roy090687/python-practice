class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes sound")

class Mammal(Animal):
    def eat(self):
        print(f"{self.name} eats ")

    def sleep(self):
        print(f"{self.name} sleeps ")

class Dog(Mammal):
    def sound(self): # overriding Animal
        super().sound() # call parent (Animal)
        print("Woof!")


d = Dog("Tommy")
d.sound()
d.eat()
d.sleep()


