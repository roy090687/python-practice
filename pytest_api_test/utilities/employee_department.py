import json

class Employee:
    def get_json(self, file):
        with open(file) as f:
            json_data = json.load(f)
            return json_data

    def get_highest_paid_employee(self, json_data):
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

    def get_salary_with_specific_employee(self, json_data, emp_name):
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

    def get_department_budget(self, json_data):
        projects = json_data["projects"]
        for project in projects:
            dept = project["department"]
            budget = project["budget"]
            print(f"{dept} -> {budget}")

    def verify_dept_total_salary_vs_budget(self, json_data):
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
                    if salary_sum > budget :
                        print(f"Total salary {salary_sum} exceeds the allocated budget {budget} for {dept}")
                    else :
                        print(f"Total salary {salary_sum} is within the budget {budget} for {dept}")
                continue
