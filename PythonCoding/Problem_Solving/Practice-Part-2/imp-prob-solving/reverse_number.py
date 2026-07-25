number = 12467
rev = 0

while number > 0:
    digit = number % 10
    rev = digit + (rev * 10)
    number //= 10

print("reversed number is:", rev)
