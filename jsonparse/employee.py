# Your JSON data
employee_list = {
    "employee": [
        {
            "name": "Ram",
            "age": 29,
            "hobbies": ["Running", "Dancing", "Swimming"],
            "children": [
                {"name": "Bobby", "age": 10},
                {"name": "Sityan", "age": 9}
            ]
        },
        {
            "name": "Priya",
            "age": 34,
            "hobbies": ["Painting", "Reading", "Yoga"],
            "children": []
        },
        {
            "name": "Amit",
            "age": 41,
            "hobbies": ["Cycling", "Chess", "Cooking"],
            "children": [
                {"name": "Neha", "age": 12}
            ]
        },
        {
            "name": "Sara",
            "age": 27,
            "hobbies": ["Photography", "Traveling", "Blogging"],
            "children": [
                {"name": "Leo", "age": 6},
                {"name": "Mia", "age": 4}
            ]
        }
    ]
}

# -------------------------------
# 1. Employees older than 28 years
# -------------------------------
employees_above_28 = []   # empty list to collect names

# Loop through each employee
for emp in employee_list["employee"]:
    # Check age condition
    if emp["age"] > 28:
        # Add employee name to the list
        employees_above_28.append(emp["name"])

print("Employees older than 28:", employees_above_28)

# -------------------------------
# 2. Children younger than 10 years
# -------------------------------
children_below_10 = []   # empty list to collect child names

# Loop through each employee
for emp in employee_list["employee"]:
    # Loop through children of this employee
    for child in emp.get("children", []):
        # Check age condition
        if child["age"] < 10:
            # Add child name to the list
            children_below_10.append(child["name"])

print("Children younger than 10:", children_below_10)
