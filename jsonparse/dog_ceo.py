import requests

# Call Dog API
response = requests.get("https://dog.ceo/api/breeds/image/random")
statusCode = response.status_code

# Verify HTTP status code
print(statusCode)
assert statusCode == 200

# Parse JSON response
data = response.json()
body_url = data["message"]

# Verify image URL starts with https://
print(body_url)
assert body_url.startswith("https://")

# Verify URL ends with .jpg.
assert body_url.endswith(".jpg")

# Extract the breed name from the URL.
parts = body_url.split('/')
index = parts.index("breeds")
breed_name = parts[index + 1]
print(breed_name)

# Verify status is "success".
status = data["status"]
assert status == "success"
print(status)
