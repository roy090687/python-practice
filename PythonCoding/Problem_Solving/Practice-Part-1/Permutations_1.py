from itertools import permutations

# Input string
s = "abc"

# Generate all permutations
perm_list = permutations(s)

# Print each permutation
print("Permutations of", s, ":")
for perm in perm_list:
    # join tuple into string
    print("".join(perm))
