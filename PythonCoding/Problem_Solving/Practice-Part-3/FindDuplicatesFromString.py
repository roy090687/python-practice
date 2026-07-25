def find_duplicates(stringVal):
    counts = {}
    stringVal = stringVal.lower()
    for ch in stringVal:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    print("Duplicate characters with counts:")
    for ch, n in counts.items():
        if n > 1:
            print(f"{ch} occurs {n} times")

testString = "SnehasisH"
find_duplicates(testString)

