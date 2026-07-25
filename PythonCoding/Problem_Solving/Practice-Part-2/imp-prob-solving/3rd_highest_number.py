import sys

input_list = [2, 5, 14, 10, 41, 20, 20, 30, 41, 22, 9]
first = second = third = float('-inf')

if len(input_list) < 3:
    print("Invalid input")
    sys.exit()  # stops execution here

for num in input_list:
    if num > first:
        third = second
        second = first
        first = num
    elif num > second and num != first:
        third = second
        second = num
    elif num > third and num != second and num != first:
        third = num

print("Third highest number is: ", third)

