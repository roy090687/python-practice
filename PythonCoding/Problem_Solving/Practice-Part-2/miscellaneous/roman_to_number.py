def convert_roman_to_number(input):
    input = input.upper()
    n = len(input)
    result = 0

    dict = {}
    dict['I'] = 1
    dict['V'] = 5
    dict['X'] = 10
    dict['L'] = 50
    dict['C'] = 100
    dict['D'] = 500

    for i in range(n):
        current_roman_val = dict[input[i]]
        if i < n - 1:
            next_roman_val = dict[input[i + 1]]
            if current_roman_val < next_roman_val:
                result -= current_roman_val
            else:
                result += current_roman_val
        else:
            result += current_roman_val

    return result

roman_str = input("Enter the roman string: ")
output = convert_roman_to_number(roman_str)
print(f"{roman_str} -> {output}")
