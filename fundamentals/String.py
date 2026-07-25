str1 = "MakeMyTrip.com"
str2 = 'Make'
str3 = " great "

print(str1[1])
print(str1[0:4])  # if you want a specific substring. Destination always (n-1)

print(str2 in str1)  # To check a specific string is present in an another string or not

# Split operation
values = str1.split(".")
print(values)
print(values[0])

# Concatenation
print(str1 + str2)

# Strip operation. It's like trim which removes white spaces from the beginning and end
# In python we have also lstrip() and rstrip() methods which remove only left space and right space accordingly

print(str3.strip())
print(str3.lstrip())
print(str3.rstrip())



