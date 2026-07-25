def get_third_largest_digit(input):
    digits = []
    for ch in input:
        if ch.isdigit():
            digits.append(ch)

    return sorted(set(digits), reverse=True)

input_string = "abc170mk266b75rts"
output = get_third_largest_digit(input_string)
print("Third largest digit is: ", output[2])
