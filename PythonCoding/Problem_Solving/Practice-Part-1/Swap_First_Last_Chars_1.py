def swap_first_last_chars(sentence):
    """Swap first and last character from each word of a sentence"""
    words = sentence.split()
    swapped_words = []
    for word in words:
        if len(word) > 1:
            last_char = word[-1]
            middle_chars = word[1:-1]
            first_char = word[0]
            swapped_words_add = last_char + middle_chars + first_char
        else:
            swapped_words_add = word

        swapped_words.append(swapped_words_add)
    return " ".join(swapped_words)

text = "hello to a python world"
result = swap_first_last_chars(text)

print("Original sentence: ", text)
print("After swap: ", result)



