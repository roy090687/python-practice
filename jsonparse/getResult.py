import requests

def get_results():
    url = "https://dummyjson.com/products/1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json() # Parse JSON response. `data` returns dictionary.
        reviews = data.get("reviews", [])
        emails = []
        for review in reviews:
            if "reviewerEmail" in review:
                emails.append(review["reviewerEmail"])
        # Print results
        print("Reviewer Emails:", emails)
        print("====== Below are email id's =======")
        print(emails[0])
        for email in emails:
            print("Email is:- ", email)
    else:
        print("Failed to fetch data. Status code:", response.status_code)

get_results()


