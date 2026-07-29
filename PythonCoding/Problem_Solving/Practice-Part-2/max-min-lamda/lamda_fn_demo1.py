emp_sal_list = [
    {"name": "Alice", "salary": 95000},
    {"name": "Bob", "salary": 87000},
    {"name": "Charlie", "salary": 72000}
]

highest = max(emp_sal_list, key=lambda e: e["salary"])
print(highest)
lowest = min(emp_sal_list, key=lambda e: e["salary"])

print("Highest:", highest)
print("Lowest:", lowest)

top_emp = highest["name"]
top_sal = highest["salary"]

print("Highest paid employee: ", top_emp)
print("Highest salary: ", top_sal)

