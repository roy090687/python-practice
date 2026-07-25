def reverse(s):
    reverse_str = ""
    for ch in s:
        reverse_str = ch + reverse_str
    return reverse_str

text = "Hello"
print("Reversed String is:", reverse(text))

# Palindrome check
revString = reverse(text)
if text.lower() == revString.lower():
    print("PALINDROME")
else:
    print("NOT PALINDROME")

