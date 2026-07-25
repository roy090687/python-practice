# input = 1223494455

number = int(input("Enter a number: "))
freq = [0] * 10

while number != 0:
    n = number % 10
    freq[n] += 1
    number //= 10

for i in range(len(freq)):
    if freq[i] > 0:
        print(f"{i} -> {freq[i]}")

print("======== 2nd Approach ========")
# using dict approach
dict = {}
input_number = 1223494455
while input_number != 0:
    n = input_number % 10
    if n not in dict:
        dict[n] = 1
    else:
        dict[n] += 1
    input_number //= 10

for key in sorted(dict.keys()):
    print(f"{key} -> {dict[key]}")
