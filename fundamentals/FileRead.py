file = open('C://Users//SNEHASISH//PycharmProjects//PythonPracticeAutomation//test.txt')

# byte wise character printing
# print(file.read(8))

# To print line by line at a time. But don't mix read() and readline() method both together.
# It might not provide the answer. One at a time.
print(file.readline())
print(file.readline())

# Method 1: While loop to print all the lines in a file one by one. "" is to check the end of file.
line = file.readline()
while line != "":
    print(line)
    line = file.readline()

# Method 2: Using for loop and readlines() method
# readlines() will give all the file values in list format. Using for loop just fetch values from list one by one
for line in file.readlines():
    print(line)

file.close()
