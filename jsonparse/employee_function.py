# JSON data
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
            "hobbies": ["Painting", "Reading", "Yoga", "Running"],
            "children": []
        },
        {
            "name": "Amit",
            "age": 41,
            "hobbies": ["Cycling", "Chess", "Cooking", "Traveling"],
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
# Function 1: Employees older than a given age
# -------------------------------
def get_employees_above_age(data, age_limit):
    result = []
    print(type(data))
    for emp in data["employee"]:
        if emp["age"] > age_limit:
            result.append(emp["name"])
    return result

# -------------------------------
# Function 2: Children younger than a given age
# -------------------------------
def get_children_below_age(data, age_limit):
    result = []
    for emp in data["employee"]:
        for child in (emp.get("children") or []):
            if child["age"] < age_limit:
                result.append(child["name"])
    return result

# -------------------------------
# Function 3: Group employees by hobbies
# -------------------------------
def group_employees_by_hobbies(data):
    hobby_map = {}  # dictionary to store hobby -> list of employees

    # Loop through each employee
    for emp in data["employee"]:
        # Loop through each hobby of the employee
        for hobby in emp.get("hobbies" or []):
            # If hobby not yet in dictionary, initialize with empty list
            if hobby not in hobby_map:
                hobby_map[hobby] = []
            # Add employee name to the hobby list
            hobby_map[hobby].append(emp["name"])
    return hobby_map

# ---------------------------------
# Function 4: Sorted employees with their age
# ---------------------------------
def get_sorted_employee(data):
    """ Returns a list of (name, age) tuples sorted by age in ascending order using bubble sort (no built-in sort). """
    employees = []
    for emp in data["employee"]:
        employees.append((emp['name'], emp['age']))
        print("TEST", employees)

    n = len(employees)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            # Check based on age
            if employees[j][1] > employees[j+1][1]:
                # Swap the tuples
                temp = employees[j]
                employees[j] = employees[j+1]
                employees[j + 1] = temp
    return employees

# ----------------------------
# Function 5: Print results
# -----------------------------
def print_results():
    # Call each helper function
    employees = get_employees_above_age(employee_list, 28)
    children = get_children_below_age(employee_list, 10)
    hobby_groups = group_employees_by_hobbies(employee_list)
    sorted_emp = get_sorted_employee(employee_list)
    #
    # Print results one by one
    print("Employees older than 28:", employees)
    print("Children younger than 10:", children)
    print("Employees grouped by hobbies:")
    # Loop through hobby_groups dictionary
    for hobby, emp_names in hobby_groups.items():
        print(f"{hobby}: {emp_names}")
    # Sorted employees ascending order based on age
    print("======= Sorted List =======")
    for name, age in sorted_emp:
        print(f"{name} - {age}")

# -------------------------------
# Call the main function
# -------------------------------
print_results()

