def reverse_words(sentence):
    words = sentence.split()
    print("List is:", words)
    reversed_words = []
    for word in words:
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)
    result = " ".join(reversed_words)
    return result

testSentence = "Hello World QA"
print(reverse_words(testSentence))






