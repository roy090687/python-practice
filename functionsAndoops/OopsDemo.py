# normal class level variables are called as class variable
# constructor level or object level variables are knows as instance variable
# constructor should be declared as __init__ in python
# If no constructor is mentioned, then default constructor will be invoked
# this program shows the example of parameterized constructor
# no new keyword required for object creation

class OopsDemo:
    num = 100  # class variable

    def __init__(self, a, b):
        print("Inside Constructor")
        self.firstNumber = a
        self.secondNumber = b

    def getData(self):
        print("Inside Get Data")

    def summation(self):
        # self.num cab be written as OopsDemo.num also as num is a class level variable
        return self.firstNumber + self.secondNumber + self.num

    def multiply(self, x, y):
        z = x * y
        print(z)


print("***** First Object *****")
obj = OopsDemo(2, 3)
obj.getData()
print(obj.summation())
obj.multiply(2.5, 2)

print("***** Second Object *****")
obj1 = OopsDemo(4, 5)
obj1.getData()
result = obj1.summation()
print(result)
obj1.multiply(10, 2)

