import re

# 1st Example
def regex_pattern_count(input, pattern):
    if re.match(pattern, input): # instead of 'match' we can use 'search' also i.e "re.search(pattern, input)"
        print("Pattern Matched")
        matches = re.findall(pattern, input)
        print(matches) # return a list
        count = len(matches)
    else:
        print("Invalid Pattern")
        return
    return count

# Example
input_str = "aadhaarYmmz"
match_pattern = "aa"
count_matched_pattern = regex_pattern_count(input_str, match_pattern)
print(f"Count of matched pattern '{match_pattern}' is: {count_matched_pattern}")

# 2nd Example
txt = "Order numbers: 123, 456, and 789"
digits = re.findall("\d+", txt) # \d+ means one or more digits
print(digits)


