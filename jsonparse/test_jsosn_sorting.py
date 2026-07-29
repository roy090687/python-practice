import pytest

def test_sort_employees():
    employees = [
        {"emp_name": "Snehasish", "salary": 75000},
        {"emp_name": "Rahul", "salary": 65000},
        {"emp_name": "Priya", "salary": 82000},
        {"emp_name": "Arjun", "salary": 55000},
        {"emp_name": "Meera", "salary": 70000}
    ]
    sorted_emp = sorted(employees, key=lambda e: e["salary"], reverse=True)
    print(sorted_emp)
    for emp in sorted_emp:
        print(emp["emp_name"], ":", emp["salary"])

def test_sort_employees_manually():
    employees = [
        {"emp_name": "Snehasish", "salary": 75000},
        {"emp_name": "Rahul", "salary": 65000},
        {"emp_name": "Priya", "salary": 82000},
        {"emp_name": "Arjun", "salary": 55000},
        {"emp_name": "Meera", "salary": 70000}
    ]
    n = len(employees)
    for i in range(n):
        for j in range(i+1, n):
            sal1 = employees[i]["salary"]
            sal2 = employees[j]["salary"]
            if sal1 > sal2:
                employees[i], employees[j] = employees[j], employees[i]
    for emp in employees:
        print(emp["emp_name"], ":", emp["salary"])

def test_sort_employees_pure_json():
    scores = {"Alice": 95, "Bob": 87, "Charlie": 60, "Roy": 72}
    sorted_items = sorted(scores.items(), key=lambda x: x[1])
    for name, value in sorted_items:
        print(name, ":", value)
