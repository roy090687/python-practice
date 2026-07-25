num = int(input("Enter a Number"))
# print(var)

flag = False

if num > 2:
    for i in range(2, (num//2)+1):
        if (num % i) == 0:
            flag = True
            break
else:
    print(num, "is not a prime number")

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
