obj = [2, 4, 5, 6, 10]

for i in obj:
    print(i)

for i in obj:
    print(i * 2)

# Sum of first 5 numbers

summation = 0
for j in range(1, 6):  # range(i,j) means i to j-1
    summation = summation + j
print("The Sum is", summation)
print("The Sum is " + str(summation))

