from abc import ABC, abstractmethod

class Animal(ABC):   # Abstract class
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):   # Abstract method
        pass

    def eat(self):
        print("Animal eating")

class Dog(Animal):   # Concrete class
    def sound(self):   # Implementation of abstract method
        print(f"{self.name} barks")

    def eat(self):
        super().eat()
        print("Dog eating")

class Cat(Animal):   # Concrete class
    def sound(self):
        print(f"{self.name} meows")

# Usage
d = Dog("Tommy")
d.sound()   # Output: Tommy barks
d.eat()

c = Cat("Kitty")
c.sound()   # Output: Kitty meows
