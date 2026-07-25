def find_duplicates(stringVal):
    counts = {}
    stringVal = stringVal.lower()
    words = stringVal.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    print("Duplicate words from a sentence with counts:")
    for word, n in counts.items():
        if n > 1:
            print(f"{word} occurs {n} times")

# Example usage
testString = "Snehasish is a good boy. Ram is a good boy."
find_duplicates(testString)

