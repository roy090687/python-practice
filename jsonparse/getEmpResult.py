import json

def get_json(filename):
    with open(filename, 'r') as f:
        json_data = json.load(f)
    return json_data

output = get_json('D:/Udemy Python APIAutomation - RahulShetty/PythonPracticeAutomation/emp.json')
print(output)

# Bob's Fraud Detection project status
print(output["employees"][1]["projects"][1]["status"])

# Dynamically
emp_data = output.get("employees", [])
for item in emp_data:
    for proj in item.get("projects", []):
        if proj.get("name") == "Fraud Detection":
            print("Fraud Detection status:", proj.get("status"))









