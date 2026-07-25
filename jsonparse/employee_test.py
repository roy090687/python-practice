employee_list = {
  "company": "TechCorp",
  "employees": {
    "emp1": {
      "id": 1,
      "name": "Leanne Graham",
      "email": "Sincere@april.biz"
    },
    "emp2": {
      "id": 2,
      "name": "Ervin Howell",
      "email": "Shanna@melissa.tv"
    },
    "emp3": {
      "id": 3,
      "name": "Clementine Bauch",
      "email": "Nathan@yesenia.net"
    }
  }
}

def extractAllEmails(data):
    emails = []
    employees = data["employees"]
    for emp in employees:
        print(emp)
        emails.append(employees[emp]["email"])

    return emails

def extract_all_emails_2nd(data):
    emails = []
    employees = data["employees"]

    # Loop over values (nested JSON objects)
    for emp in employees.values():
        emails.append(emp["email"])

    return emails


print(extractAllEmails(employee_list))

print(extract_all_emails_2nd(employee_list))
