def get_unique(input):
    return set(input)

def get_unique_sorted(input):
    return sorted(set(input))

def get_duplicate(input):
    seen = set()
    dup = set()
    for val in input:
        if val not in seen:
            seen.add(val)
        else:
            dup.add(val)
    return dup


question = [2, 4, 10, 2, 1, 5, 4, 1, 3, 1, 15, 4]

unique = get_unique(question)
unique_sorted = get_unique_sorted(question)
print(unique)
print(unique_sorted)

duplicate = get_duplicate(question)
print("Duplicate: ", duplicate)


