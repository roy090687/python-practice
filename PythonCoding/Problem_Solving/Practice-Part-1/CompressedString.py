def compressed_string(s):
    if not s:
        return " "

    compressed = []
    count = 1
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            count += 1
        else:
            compressed.append(s[i] + str(count))
            count = 1
    print(compressed)
    compressed.append(s[-1] + str(count))
    return "".join(compressed)

example = "aaaaabbbccdd"
result = compressed_string(example)
print(result)



