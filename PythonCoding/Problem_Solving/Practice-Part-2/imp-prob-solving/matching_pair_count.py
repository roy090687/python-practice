import re

def regex_matching_count(word, regex):
    matches = re.findall(regex, word)
    count = len(matches)
    return count

def get_matching_pair_count(input):
    input = input.lower()
    n = len(input)
    my_set = set()
    for i in range(n-1):
        if input[i] == input[i+1]:
            sb = input[i] + input[i+1]
            my_set.add(sb)

    for pair in my_set:
        total_count = regex_matching_count(input, pair)
        print(f"{pair} : {total_count}")

test_input = "Successful Aadhaar"
print("====== Matching pair and its count ======")
get_matching_pair_count(test_input)

# Another Example

input_str = "aadhaarymmz"
match_pattern = "aa"
matches = re.findall(match_pattern, input_str)
print(f"Count of {match_pattern} is {len(matches)}")

