# default, positional, keyword, arbitrary [positional, keyword]
def greet(name, dept):
    print(f"Hi {name}")
    print(f'Are you from {dept} dept?')

def foo(name, subject, dept='CS'): #default argument
    print(f"Hi {name}")
    print(f'Do you teach {subject}?')
    print(f'Are you from {dept} dept?')

greet('Roy', 'CS')
print("=================================")
greet('Roy', dept='CS')
print("=================================")
greet(name='Roy', dept='CS')
print("=================================")
greet(dept='CS', name='Roy')
print("=================================")
foo('Roy', 'Python')
print("=================================")
foo('Roy', 'Python', 'ECE')
print("=================================")
foo('Roy', subject='Python')

# arbitrary positional arguments
def add(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print(f'Sum is {sum}')

add(5, 7, 10)

# *args **kwargs


