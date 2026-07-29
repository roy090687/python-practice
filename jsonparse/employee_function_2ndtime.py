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
            "hobbies": ["Photography", "Traveling", "Blogging", "Dancing"],
            "children": [
                {"name": "Leo", "age": 6},
                {"name": "Mia", "age": 4}
            ]
        }
    ]
}

# -------------------------------------------
# Function 1: Employees older than a given age
# --------------------------------------------
def get_employees_above_age(data, age_limit):
    emp_name = []
    employees = data["employee"]
    for emp in employees:
        if emp["age"] > age_limit:
            emp_name.append(emp["name"])

    return emp_name

print("======== Employees Above Age ========")
emp_names = get_employees_above_age(employee_list, 28)
print(emp_names)

# ------------------------------------------
# Function 2: Children younger than a given age
# -------------------------------------------
def get_children_below_age(data, age_limit):
    children_name = []
    employees = data["employee"]
    for emp in employees:
        for child in emp["children"]:
            if child["age"] < age_limit:
                children_name.append(child["name"])

    return children_name

print("======== Children Below Age ========")
children_names = get_children_below_age(employee_list, 10)
print(children_names)

# -------------------------------------
# Function 3: Group employees by hobbies
# --------------------------------------
def group_emp_by_hobbies(data):
    emp_hobby = {}
    employees = data["employee"]
    for emp in employees:
        for hobby in emp["hobbies"]:
            if hobby not in emp_hobby:
                emp_hobby[hobby] = []
            emp_hobby[hobby].append(emp["name"])
    return emp_hobby

print("======== Hobby Employee Map ========")
emp_hobbies_group = group_emp_by_hobbies(employee_list)
for hobby, names in emp_hobbies_group.items():
    print(hobby, ":", names)

# -------------------------------------------------------------------
# Function 4: Sorted employees with their age - Using Sorted Function
# --------------------------------------------------------------------
def sort_employees_with_age_sorted_fn(data):
    emp_age = {}
    employees = data["employee"]
    for emp in employees:
        emp_age[emp["name"]] = emp["age"]

    emp_age_list = list(emp_age.items())
    sorted_emp = sorted(emp_age_list, key=lambda e: e[1])
    for name, age in sorted_emp:
        print(name, ":", age)

print("======== Sorted Employee By Age ========")
sort_employees_with_age_sorted_fn(employee_list)

# -------------------------------------------------------------------
# Function 4: Sorted employees with their age - Using Manual Sorting
# --------------------------------------------------------------------
def sort_manually_employees_with_age(data):
    emp_age = {}
    employees = data["employee"]
    for emp in employees:
        emp_age[emp["name"]] = emp["age"]

    emp_age_list = list(emp_age.items())
    n = len(emp_age_list)
    for i in range(n):
        for j in range(i+1, n):
            if emp_age_list[i][1] > emp_age_list[j][1]:
                emp_age_list[i], emp_age_list[j] = emp_age_list[j], emp_age_list[i]

    for name, age in emp_age_list:
        print(name, ":", age)

print("======== Manual Sorting Employee By Age ========")
sort_manually_employees_with_age(employee_list)
