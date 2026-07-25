input = "4r3a2j"   # o/p: rrrraaajj
n = len(input)
sb = []
for i in range(0, n-1):
    if input[i].isdigit():
        number = int(input[i])
        next_char = input[i+1]
        for j in range(number):
            sb.append(next_char)

output = "".join(sb)
print("Decompressed version is:", output)

