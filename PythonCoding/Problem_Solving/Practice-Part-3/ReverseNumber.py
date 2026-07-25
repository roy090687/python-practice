number = int(input("Enter a Number"))
reverse = 0
while number > 0:
    digit = number % 10
    reverse = (reverse * 10) + digit
    number = number//10

print("The final reversed number is ", reverse)
