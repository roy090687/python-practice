import re

def matching_pair_count(word):
    word = word.lower() # convert to lowercase
    pairs = []
    n = len(word)

    # collect consecutive duplicate pairs
    for i in range(n - 1):
        if word[i] == word[i+1]:
            pairs.append(word[i]+word[i+1])
        # use regex to count occurrences of each pair
        counts = {}
        for pair in set(pairs): # unique pairs only
            matches = re.findall(pair, word)
            counts[pair] = len(matches)
    return counts

result = matching_pair_count("Successful Aadhaar")
print(result)



