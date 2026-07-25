def get_unique(tup):
    return list(set(tup))

def get_unique_ordered(tup):
    return list(dict.fromkeys(tup))

def get_duplicate(tup):
    seen = set()
    duplicates = set()
    for num in tup:
        if num not in seen:
            seen.add(num)
        else:
            duplicates.add(num)
    return list(duplicates)

input_tup = (2, 4, 10, 2, 1, 5, 4, 1, 3, 1, 15, 4)
unique_list = get_unique(input_tup)
unique_ordered = get_unique_ordered(input_tup)
dup_list = get_duplicate(input_tup)

print("Unique elements are: ", unique_list)
print("Unique elements in insertion order: ", unique_ordered)
print("Duplicate elements are: ", dup_list)

