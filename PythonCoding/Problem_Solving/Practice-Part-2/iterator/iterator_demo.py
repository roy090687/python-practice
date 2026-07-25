nums = [7, 5, 10, 9, 8]

it = iter(nums)

# 1st way
print(it.__next__())
print(it.__next__())

# 2nd way
print(next(it))
