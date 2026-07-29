arr = [1, 2, 3, 4, 5]
n = len(arr)
count = 0

while count < n:
    temp = arr[n-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = temp
    count += 1
    # print(" ".join(map(str, arr)))
    print(*arr)  # *arr is is positional argument unpacking

