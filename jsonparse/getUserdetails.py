# Using Python, retrieve the company name, the department, and the city of the company address for this user.

import requests

def getResponse():
    url = 'https://dummyjson.com/users/1'
    response = requests.get(url)
    return response

def get_user_details():
    response = getResponse()
    if response.status_code == 200:
        data = response.json()
        company = data.get("company")
        if data.get("firstName") == "Emily":
            print("Company Name: ", company.get("name"))
            print("Dept name: ", company.get("department"))
            address = company.get("address")
            print("City: ", address.get("city"))
            print("State Code: ", address.get("stateCode"))


get_user_details()




