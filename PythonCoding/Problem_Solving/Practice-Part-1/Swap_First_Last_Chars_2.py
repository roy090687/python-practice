def swap_first_last_chars(sentence):
    words = sentence.split()
    result = ""
    for word in words:
        if len(word) > 1:
            last_char = word[-1]
            middle_chars = word[1:-1]
            first_char = word[0]
            swapped_words_add = last_char + middle_chars + first_char
        else:
            swapped_words_add = word
        result += swapped_words_add + " "

    return result.strip()

text = "hello to a python world"
final = swap_first_last_chars(text)

print("After swap:", final)


