scores = {"Alice": 95, "Bob": 87, "Charlie": 72}

highest_emp = max(scores, key=scores.get)
highest_salary = scores[highest_emp]

print(f"Highest paid employee is {highest_emp} with salary {highest_salary}")


nums = [10, 5, 7, 23, 15, 40, 11, 3]
highest_nam = max(nums)
min_num = min(nums)
print(highest_nam)
print(min_num)

strings = ["Alice", "Tom", "Priya", "Snehasish", "Sanchari", "Amit", "Bob"]
max_str = max(strings)
min_str = min(strings)
print(max_str)
print(min_str)

