input = "sd4t51ry7"
char = []
digit = []
for ch in input:
    if ch.isdigit():
        digit.append(int(ch))
    else:
        char.append(ch)

print(char)
print(digit)
