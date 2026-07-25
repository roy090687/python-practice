import requests

def get_response():
    url = "https://jsonplaceholder.typicode.com/users?utm_source=chatgpt.com"
    response = requests.get(url)
    return response

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def validate_returned_user_count():
    exp_returned_user = 10
    count = 0
    response = get_response()
    if response.status_code == 200:
        data = response.json()
        dict_number = len(data)
        for i in range(0, dict_number):
            user = data[i]["username"]
            if user:
                count += 1
    assert exp_returned_user == count
    print(f"Assertion passed: {count} users returned")

def validate_non_empty_email():
    valid_email_count = 0
    dict_number = 0
    response = get_response()
    if response.status_code == 200:
        data = response.json()
        dict_number = len(data)
        for i in range(0, dict_number):
            email = data[i].get("email")
            if email:
                valid_email_count += 1
    assert valid_email_count == dict_number
    print("No email is empty")

def validate_user_address_geo_company():
    response = get_response()
    username = []
    if response.status_code == 200:
        data = response.json()
        dict_number = len(data)
        for i in range(0, dict_number):
            address = data[i]["address"]
            company = data[i]["company"]
            username.append(data[i]["username"])
            if address and company:
                geo = address["geo"]
                if geo:
                    lat = geo["lat"]
                    lng = geo["lng"]
                    assert is_numeric(lat), f"Latitude is not numeric: {lat}"
                    assert is_numeric(lng), f"Longitude is not numeric: {lng}"
        assert len(username) == len(set(username)), "Duplicate usernames found!"
        print("All validations are successful!")

# Another way of validation
def validate_user_address_geo_company_part2():
    response = get_response()
    assert response.status_code == 200, \
        f"Expected status code 200 but got {response.status_code}"

    data = response.json()
    username_list = []

    for i in range(len(data)):

        # Validate mandatory keys
        assert "address" in data[i], \
            f"Address key missing for user id {data[i]['id']}"

        assert "company" in data[i], \
            f"Company key missing for user id {data[i]['id']}"

        assert "geo" in data[i]["address"], \
            f"Geo key missing for user id {data[i]['id']}"

        username_list.append(data[i]["username"])

        lat = data[i]["address"]["geo"]["lat"]
        lng = data[i]["address"]["geo"]["lng"]

        assert is_numeric(lat), \
            f"Latitude is not numeric: {lat}"

        assert is_numeric(lng), \
            f"Longitude is not numeric: {lng}"

    # Validate duplicate usernames
    assert len(username_list) == len(set(username_list)), \
        "Duplicate usernames found!"

    print("Address, geo, company and username validations successful!")


validate_returned_user_count()
validate_non_empty_email()
validate_user_address_geo_company()
validate_user_address_geo_company_part2()

