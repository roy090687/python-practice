from itertools import permutations

s = "abc"
perm_list = permutations(s)

all_perms = []
for p in perm_list:
    word = " ".join(p)
    all_perms.append(word)

print("Permutations of", s, ":")
print(all_perms)

