import pandas as pd

df = pd.DataFrame({
    "Name": ["John", "Alice", "Bob", "Alice", "John"],
    "Age": [25, 30, 35, 28, 25],
    "City": ["NY", "LA", "NY", "Chicago", "LA"],
    "Salary": [50000, 70000, 80000, 65000, 55000]
})

print(df)

# Problem 1: Print only the Name column
print("====== Name Column ======")
print(df["Name"])

# Problem 2: Print Name and Salary columns
print("====== Name & Salary Columns ======")
print(df[["Name", "Salary"]])

# Problem 3: Find employees whose salary is greater than 60,000
print("====== Emp Salary > 60K ======")
highest_sal_data = df[df["Salary"] > 60000][["Name", "Salary"]]
print(highest_sal_data)

# Problem 4: Find employees from NY
print("====== Emp From NY ======")
emp_data_ny = df[df["City"] == "NY"]
print(emp_data_ny)

# Problem 5: Find employees from NY whose salary is greater than 60,000
# when you combine multiple conditions in Pandas, you must wrap each condition in parentheses.
print("====== Emp From NY & Sal > 60K ======")
emp_ny_sal_greater_60K = df[(df["Salary"] > 60000) & (df["City"] == "NY")]
print(emp_ny_sal_greater_60K)

# Problem 6: Add a Bonus column
df["Bonus"] = df["Salary"] * 0.10
print("==== Print the whole DF ====")
print(df)

# Problem 7: Increase every salary by 5% (basically I am updating the existing data)
df["Salary"] = df["Salary"] * 1.05
print("==== After updating 5% hike the whole DF ====")
print(df)

