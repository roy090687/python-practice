def get_second_highest_number(input):
    first = second = float('-inf')
    if len(input) < 2:
        return "Invalid input"

    for num in input:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second

input_list = [2]
print("Second highest number is: ", get_second_highest_number(input_list))

