import pandas as pd

""" 1st Example """
employees = [
    {"Name": "John", "Salary": 50000},
    {"Name": "Alice", "Salary": 70000},
    {"Name": "Bob", "Salary": 80000}
]

print("----------------- 1st Example -----------------")
df = pd.DataFrame(employees)
print(df)

# Find employees whose salary is greater than 60,000
print("====== Emp Salary > 60K ======")
emp_sal_greater_60k = df[df["Salary"] > 60000]
print(emp_sal_greater_60k)

""" 2nd Example """
# Here the concept is: If you have a single JSON object (Python dictionary) and you want to use Pandas as a single row,
# the most common and recommended approach is to wrap it inside a list.
employee1 = {
    "Name": "Alice",
    "Salary": 70000,
    "City": "LA"
}

df1 = pd.DataFrame([employee1])
print("----------------- 2nd Example -----------------")
print(df1)

