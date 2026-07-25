import json
from pathlib import Path


def get_json(file):
    with open(file, 'r') as f:
        data = json.load(f)
        return data

def get_highest_paid_employee(json_data):
    emp_sal_list = []
    departments = json_data["departments"]
    for dept in departments:
        employees = dept["employees"]
        for emp in employees:
            emp_sal_dict = {}
            emp_sal_dict["name"] = emp["name"]
            emp_sal_dict["salary"] = emp["salary"]
            emp_sal_list.append(emp_sal_dict)

    n = len(emp_sal_list)
    for i in range(n):
        for j in range(i + 1, n):
            sal1 = emp_sal_list[i].get("salary")
            sal2 = emp_sal_list[j].get("salary")
            if sal1 < sal2:
                emp_sal_list[i], emp_sal_list[j] = emp_sal_list[j], emp_sal_list[i]

    highest_salary = emp_sal_list[0]["salary"]
    highest_paid_employee = emp_sal_list[0]["name"]

    return highest_paid_employee, highest_salary

def get_highest_paid_employee_without_sorting(json_data):
    emp_sal_list = []
    departments = json_data["departments"]
    for dept in departments:
        employees = dept["employees"]
        for emp in employees:
            emp_sal_dict = {}
            emp_sal_dict["name"] = emp["name"]
            emp_sal_dict["salary"] = emp["salary"]
            emp_sal_list.append(emp_sal_dict)

    highest = max(emp_sal_list, key=lambda e: e["salary"])
    highest_salary = highest["salary"]
    highest_paid_employee = highest["name"]

    return highest_paid_employee, highest_salary

def get_salary_with_specific_employee(json_data, emp_name):
    emp_sal_list = []
    departments = json_data["departments"]
    for dept in departments:
        employees = dept["employees"]
        for emp in employees:
            emp_sal_dict = {}
            emp_sal_dict["name"] = emp["name"]
            emp_sal_dict["salary"] = emp["salary"]
            emp_sal_list.append(emp_sal_dict)

    n = len(emp_sal_list)
    sal = 0
    for i in range(n):
        name = emp_sal_list[i]["name"]
        if name == emp_name:
            sal = emp_sal_list[i]["salary"]
            break
    return sal

def get_department_budget(json_data):
    projects = json_data["projects"]
    for project in projects:
        dept = project["department"]
        budget = project["budget"]
        print(f"{dept} -> {budget}")

def verify_dept_total_salary_vs_budget(json_data):
    departments = json_data["departments"]
    projects = json_data["projects"]
    for dept in departments:
        dept_name = dept["name"]
        employees = dept["employees"]
        salary_sum = 0
        for emp in employees:
            sal = emp["salary"]
            salary_sum += sal
        for project in projects:
            dept = project["department"]
            budget = project["budget"]
            if dept == dept_name:
                if salary_sum > budget:
                    print(f"Total salary {salary_sum} exceeds the allocated budget {budget} for {dept}")
                else:
                    print(f"Total salary {salary_sum} is within the budget {budget} for {dept}")
            continue


if __name__ == "__main__":
    base_dir = Path(__file__).parent
    filepath = base_dir.parent/"sample.json"
    data = get_json(filepath)

    """ With sorting"""
    result = get_highest_paid_employee(data)
    print(f"Highest paid employee is {result[0]} with salary {result[1]}")

    """ without sorting"""
    result_without_sorting = get_highest_paid_employee_without_sorting(data)
    print(f"[Without Sorting] Highest paid employee: {result[0]} --> Salary is: {result[1]}")

    specific_emp_name = "Charlie"
    specific_salary = get_salary_with_specific_employee(data, specific_emp_name)
    print(f"{specific_emp_name} -> {specific_salary}")

    get_department_budget(data)

    verify_dept_total_salary_vs_budget(data)



