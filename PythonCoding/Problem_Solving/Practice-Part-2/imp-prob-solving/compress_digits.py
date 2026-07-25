def compress_digit(number):
    str_val = str(number)
    sb = []   # acts like StringBuilder

    digit_map = {}

    # Count digits in order
    for ch in str_val:
        if ch in digit_map:
            digit_map[ch] += 1
        else:
            digit_map[ch] = 1

    # Build compressed string
    for key, value in digit_map.items():
        sb.append(key)
        sb.append(str(value))

    print(sb)

    return "".join(sb)


# Example usage
number = 1112233444555
output = compress_digit(number)
print("Compressed version:", output)
