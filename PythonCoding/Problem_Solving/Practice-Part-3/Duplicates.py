def print_duplicates(arr):
    seen = {}
    duplicates = {}

    for num in arr:
        if num in seen:
            seen[num] += 1
            duplicates[num] = seen[num]
        else:
            seen[num] = 1
    # Print duplicates with counts
    print(seen)
    print(duplicates)
    if duplicates:
        print("Duplicate numbers with counts:")
        for num, count in duplicates.items():
            print(f"{num} occurs {count} times")
    else:
        print("No duplicates found")

# Example usage
arr = [1, 2, 3, 4, 2, 7, 8, 3, 1, 9, 5, 2]
print_duplicates(arr)
