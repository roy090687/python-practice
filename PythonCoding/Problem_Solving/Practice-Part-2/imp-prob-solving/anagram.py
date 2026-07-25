def check_anagram(first, second):
    n1 = len(first)
    n2 = len(second)
    if n1 != n2:
        return "Not Anagram"
    for ch in first:
        index = second.find(ch)
        if index == -1:
            return "Not Anagram"
        second = second[:index] + second[index+1:]
    return second

first_string = input("Enter first string: ")
second_string = input("Enter second string: ")

output = check_anagram(first_string, second_string)
if len(output) == 0:
    print("Both Strings are Anagram")
else:
    print("Not Anagram")
