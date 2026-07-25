def decompress_string_single_multi_digit(input):
    result = ""
    num = ""
    for ch in input:
        if ch.isdigit():
            num += ch
        else:
            result += ch * int(num)
            num = ""
    return result

input1 = "4r3a2j"
input2 = "12x3y2z"

output1 = decompress_string_single_multi_digit(input1)
output2 = decompress_string_single_multi_digit(input2)

print("Decompressed version for single digit is:", output1)
print("Decompressed version for multi digits is:", output2)
