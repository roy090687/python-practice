import requests
class RandomUserApiTest:

    def get_response(self):
        response = requests.get("https://randomuser.me/api/")
        return response

    def printUserFullName(self, response):
        # response = self.get_response()
        full_name = None
        if response.status_code == 200:
            data = response.json()
            first_name = data["results"][0]["name"]["first"]
            last_name = data["results"][0]["name"]["last"]
            full_name = first_name + " " + last_name

        return full_name

    def getGender(self, response):
        data = response.json()
        gender = data["results"][0]["gender"]
        assert gender in ("male", "female")
        return gender

    def verifyAgeDOB(self, response):
        data = response.json()
        dob_age = data["results"][0]["dob"]["age"]
        assert dob_age > 18
        return dob_age

    def verifyEmail(self, response):
        data = response.json()
        email = data["results"][0]["email"]
        assert '@' in email, f"Invalid email {email}"
        return email

    def verifyLatAndLongNotEmpty(self, response):
        data = response.json()
        lat = data["results"][0]["location"]["coordinates"]["latitude"]
        long = data["results"][0]["location"]["coordinates"]["longitude"]
        assert lat is not None, f"latitude is empty"
        assert long is not None, f"longitude is empty"
        return lat, long


user = RandomUserApiTest()
response = user.get_response()
full_name = user.printUserFullName(response)
gender = user.getGender(response)
dob_age = user.verifyAgeDOB(response)
email = user.verifyEmail(response)
lat_long = user.verifyLatAndLongNotEmpty(response)

print(full_name)
print(gender)
print(dob_age)
print(email)
print(f"Latitude is {lat_long[0]} and Longitude is {lat_long[1]}")




