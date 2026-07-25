def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


numbers = [5, 10, 3, 20, 18, 8]
bubble_sort(numbers)

print("Sorted Array is:")
for num in numbers:
    print(num, end=" ")


