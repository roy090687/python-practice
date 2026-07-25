sentence = "This is a sunrise view point from Darjeeling. Sunrise point is always a good view point."

sentence = sentence.lower().replace(".", "").split()
freq = {}

for word in sentence:
    if word not in freq:
        freq[word] = 1
    else:
        freq[word] += 1

my_list = list(freq.items())  # freq.items() will always return tuples. my_list will be a list of tuples.
n = len(my_list)

for i in range(n):
    for j in range(0, n-i-1):
        if my_list[j][1] > my_list[j+1][1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

sorted_freq = dict(my_list)
print(sorted_freq)

# Another one using sort
my_dict = {"a": 5, "e": 2, "d": 9, "c": 1, "b": 4}

# this is to sort based on value
def get_value(item):
    # print("called with:", item)
    return item[1]
print("---------Sorting based on values---------")
for key, value in sorted(my_dict.items(), key=get_value):
    print(f"{key} -> {value}")

# sort based on key
print("---------Sorting based on keys---------")
for key in sorted(my_dict.keys()):
    print(f"{key} -> {my_dict[key]}")


