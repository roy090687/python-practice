# Python List can have multiple values with similar or different data types
values = [1, 2, "roy", 10.5, 100]

print(values[0])   # o/p: 1
print(values[2])   # o/p: roy

print(values[-1])  # To get the last index value, o/p: 100

# Sub list
print(values[1:3])  # o/p: [2, 'roy']

values.insert(3, 'hello')
print(values)  # o/p: [1, 2, 'roy', 'hello', 10.5, 100]

# Update and Delete
values[2] = "ROY"
del values[0]
print(values)  # o/p: [2, 'ROY', 'hello', 10.5, 100]

# Add the value at the end
values.append("End")
print(values)   # o/p: [2, 'ROY', 'hello', 10.5, 100, 'End']



