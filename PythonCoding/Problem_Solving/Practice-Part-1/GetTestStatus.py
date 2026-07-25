test_results = [
    {"test": "LoginTest", "status": "Passed"},
    {"test": "SignupTest", "status": "Failed"},
    {"test": "PaymentTest", "status": "Passed"},
    {"test": "ProfileUpdateTest", "status": "Skipped"}
]

test_status_dict = {}

for result in test_results:
    key = result["test"]
    value = result["status"]
    test_status_dict[key] = value

print("Final Test Status Dictionary:")
print(test_status_dict)

print("========= Final Result =========")
for key, value in test_status_dict.items():
    print(key, ':', value)
    print("-------------------------")

# Accessing specific test status
print("Login Test Status:", test_status_dict["LoginTest"])

