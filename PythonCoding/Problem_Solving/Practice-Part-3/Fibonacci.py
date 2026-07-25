n = int(input("Enter the number of terms: "))

# assign first 2 numbers
a = 0
b = 1

print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    temp_a = a
    temp_b = b
    a = temp_b
    b = temp_a + temp_b
