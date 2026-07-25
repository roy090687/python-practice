def my_decorator(func):

    def wrapper():
        print("Before the functions runs")
        func()
        print("After the functions runs")

    return wrapper

@my_decorator
def say_hello():
    print("Hello Snehasish")

say_hello()
