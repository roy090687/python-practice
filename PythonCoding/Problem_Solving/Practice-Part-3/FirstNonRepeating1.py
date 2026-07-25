def first_non_repeating(s):
    counts = {}
    for ch in s:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    print("Dict is:", counts)
    for ch in s:
        if counts[ch] == 1:
            return ch

# Example
print(first_non_repeating("swiss"))

