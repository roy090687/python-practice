def clockwise_rotate(arr):
    arr_len = len(arr)
    max_rotate = arr_len
    count = 0
    while count < max_rotate:
        temp = arr[arr_len - 1]
        for i in range(arr_len - 1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = temp
        count += 1
        # print(arr)
        # Print the whole array in one line
        print(" ".join(str(j) for j in arr))


arr = [1, 2, 3, 4, 5]
clockwise_rotate(arr)


