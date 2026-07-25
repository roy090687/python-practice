def calculate_third_largest(input):
    first = second = third = float('-inf')
    n = len(input)
    if n < 3:
        print("Invalid input")
        return
    for num in input:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second and num != first:
            third = second
            second = num
        elif num > third and num != second and num != first:
            third = num

    return third

input_list = [2, 5, 14, 10, 41, 20, 30, 41, 22, 9]
# input_set = set(input_list)

print("Third largest number is: ", calculate_third_largest(input_list))






