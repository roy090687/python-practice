def addOddNumbers(arr):
    total = 0
    for num in arr:
        if num % 2 != 0:
            total += num
    return total

arr = [1, 2, 3, 4, 5, 6, 7]
print("The sum of odd numbers: ", addOddNumbers(arr))

