# Loop through all users and print each user’s full name (firstName + lastName), their company name, and the city of their company’s address.

import requests

def getResponse():
    url = 'https://dummyjson.com/users'
    response = requests.get(url)
    return response

def getUserFullNames():
    response = getResponse()
    if response.status_code == 200:
        data = response.json()
        for user in data.get("users", []):
            user_id = user.get("id")
            full_name = f"{user.get('firstName')} {user.get('lastName')}"
            company_name = user.get("company", {}).get("name")
            dept_name = user.get("company", {}).get("department")
            city_name = user.get("company", {}).get("address", {}).get("city")
            print(f"ID: {user_id} -> Full Name: {full_name} - Company: {company_name} - Dept: {dept_name} - City: {city_name}")


getUserFullNames()
