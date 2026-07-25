print("Hello")

a = 5
print(a)

# This is comment out lines in python

str1 = "Hello Roy!!"
print(str1)

b, c, d = 20, 10.45, "World"

# print("Value is "+b), this will throw error "TypeError: can only concatenate str (not "int") to str"

# To print value with print message, below is the way to use format() method
print("{} {}".format("value is ", b))

# Another way
print("The value is ", b)
print("The value is ", c)
print("The value is ", d)

# Only string value can be concatenated with the print statement message
print("Value is "+d)

# To check the Type of the variables
print(type(b))
print(type(c))
print(type(d))

# For complex number Data Type - Complex data type under parent Numeric data type
m = 200 + 3j
print("The type of the variable having value", m, "is", type(m))






