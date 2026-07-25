import array

# declare and initialize an array in python
# arr = array.array('i', [10, 20, 15, 2, 23, 90, 67])

def peak_elements():
    arr = array.array('i', [])
    n = int(input("Enter how many numbers you want to insert to the array: "))

    for i in range(n):
        val = int(input())
        arr.append(val)

    if n == 1:
        print(arr[0])
        return

    if n == 2 and arr[0] > arr[1]:
        print(arr[0])
        return

    print("==== Peak elements are ====")
    for i in range(1, n - 1):
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            print(arr[i])

    if arr[n - 1] >= arr[n - 2]:
        print(arr[n - 1])

peak_elements()
