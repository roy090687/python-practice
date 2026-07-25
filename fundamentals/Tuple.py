values = (2, 10.6, "Hello")

print("the first value is", values[0])
print("the last value is", values[2])

# As tuple is immutable, it won't allow modification of any existing value

# values[2] = "HELLO" --> TypeError: 'tuple' object does not support item assignment

print(values)
