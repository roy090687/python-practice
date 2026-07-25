class ReverseNumber:

    def reverse(self, num):
        reverse = 0
        while num > 0:
            digit = num % 10
            reverse = (reverse * 10) + digit
            num = num // 10
        return reverse


number = int(input("Enter a Number"))
obj = ReverseNumber()
print("The reversed number is ", obj.reverse(number))

