def print_duplicates(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    print("Duplicate numbers with counts:")
    for num, count in counts.items():
        if count > 1:
            print(f"{num} occurs {count} times")

# Example usage
arr = [1, 2, 3, 4, 2, 7, 8, 3, 1, 9, 5, 5, 3]
print_duplicates(arr)

