from collections import Counter

def first_non_repeating(s):
    counts = Counter(s)
    print("Dict is:", counts)
    for ch in s:
        if counts[ch] == 1:
            return ch
    # If no non-repeating character exists → it returns None
    # Return value when there’s nothing meaningful to return
    return None

# Example
print(first_non_repeating("swiss"))
