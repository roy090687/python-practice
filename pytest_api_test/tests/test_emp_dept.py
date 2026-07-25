import pytest
from pathlib import Path
from pytest_api_test.utilities.employee_department import Employee

emp = Employee()

@pytest.fixture()
def json_data():
    emp = Employee()
    base_dir = Path(__file__).parent
    filepath = base_dir.parent/'resources'/'test.json'
    data = emp.get_json(filepath)
    return data

def test_get_highest_paid_employee(json_data):
    emp_data = emp.get_highest_paid_employee(json_data)
    highest_paid_employee = emp_data[0]
    highest_salary = emp_data[1]
    assert highest_paid_employee == "Bob"
    assert highest_salary == 270000
    print(f"Highest paid employee is {highest_paid_employee} with salary {highest_salary}")


def test_get_salary_with_specific_employee(json_data):
    specific_emp_name = "Charlie"
    salary = emp.get_salary_with_specific_employee(json_data, specific_emp_name)
    assert salary == 72000

def test_get_department_budget(json_data):
    emp.get_department_budget(json_data)

def test_verify_dept_total_salary_vs_budget(json_data):
    emp.verify_dept_total_salary_vs_budget(json_data)
