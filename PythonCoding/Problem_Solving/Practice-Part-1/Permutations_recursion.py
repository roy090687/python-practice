def get_permutations(s, prefix=" "):
    if len(s) == 0:
        print(prefix)
    else:
        for i in range(len(s)):
            new_prefix = prefix + s[i]
            remaining = s[:i] + s[i+1:]
            get_permutations(remaining, new_prefix)

# Example
st = "abc"
print("Permutations of", st, ':')
get_permutations(st) # prefix automatically takes the default " "
