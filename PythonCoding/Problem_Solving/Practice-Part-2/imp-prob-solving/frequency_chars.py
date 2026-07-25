def solution_with_dict(input):
    freq = {}
    for ch in input:
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] = freq[ch] + 1

    for key, value in freq.items():
        print(f"{key} -> {value}")

    print("======== Sorted/Alphabetic order ========")
    # sorted or alphabetic order output
    for key in sorted(freq.keys()):
        print(f"{key} -> {freq[key]}")

def solution_without_dict(input):
    n = len(input)
    chars = [''] * n   # n empty string slots
    freq = [0] * n    # n zeros
    count = 0
    for ch in input:
        flag = False
        for i in range(count):
            if chars[i] == ch:
                freq[i] += 1
                flag = True
                break
        if not flag:
            chars[count] = ch
            freq[count] = 1
            count += 1

    # sorting to get alphabetic way output
    for i in range(count):
        for j in range(i+1, count):
            if chars[i] > chars[j]:
                charTemp = chars[i]
                chars[i] = chars[j]
                chars[j] = charTemp

                countTemp = freq[i]
                freq[i] = freq[j]
                freq[j] = countTemp

    for i in range(count):
        print(f"{chars[i]} : {freq[i]}")


input = "snehasish"
solution_with_dict(input)

print("======== 2nd Approach ========")
solution_without_dict(input)

