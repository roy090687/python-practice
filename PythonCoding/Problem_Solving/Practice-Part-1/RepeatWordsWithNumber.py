import re

def repeat_words_with_numbers(input):
    result = []
    pattern = "([A-Za-z]+)(\d+)"
    matches = re.findall(pattern, input)

    for word, num in matches:
        count = int(num)
        result.append(word * count) # repeat the word 'count' times
    print(result)
    return "".join(result)

# Example
input_str = "alpha10Bita2Gama0"
output = repeat_words_with_numbers(input_str)
print(output)
