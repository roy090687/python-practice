import requests

def get_response():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    return response

def get_highest_avg_ratings():
    response = get_response()
    category_ratings = {}
    if response.status_code == 200:
        data = response.json()
        # Category as key and the values as list of rate values.
        for product in data:
            category = product["category"]
            if category not in category_ratings:
                category_ratings[category] = []
            category_ratings[category].append(product["rating"]["rate"])

        # Calculate avg_ratings for each category and store in a dict
        avg_ratings = {}
        for category, ratings in category_ratings.items():
            avg_rating = sum(ratings)/len(ratings)
            avg_ratings[category] = avg_rating

        # Calculate highest avg rating for the corresponding category
        highest_category = None
        highest_avg_rating = 0
        for cat, avg in avg_ratings.items():
            if avg > highest_avg_rating:
                highest_category = cat
                highest_avg_rating = avg

        # You could replace the manual loop with Python’s max() for brevity
        # highest_category = max(avg_ratings, key=avg_ratings.get)
        # highest_avg_rating = avg_ratings[highest_category]
        formatted_rating = format(highest_avg_rating, ".2f")
        print(f"{highest_category} : {formatted_rating}")


def get_top_3_expensive_products():
    response = get_response()
    products_list = []
    if response.status_code == 200:
        data = response.json()
        for product in data:
            product_prices = {}
            product_prices["title"] = product["title"]
            product_prices["price"] = product["price"]
            products_list.append(product_prices)

        # Sorting descending order based on price by comparing each maps inside the list
        list_length = len(products_list)
        for i in range(list_length):
            for j in range(i+1, list_length):
                price1 = products_list[i].get("price")
                price2 = products_list[j].get("price")
                if price1 < price2:
                    products_list[i], products_list[j] = products_list[j], products_list[i]

        # Extract top 3
        print("Top 3 most expensive products:")
        for i in range(3):
            title = products_list[i]["title"]
            price = products_list[i]["price"]
            print(f"{title}: {price}")

get_highest_avg_ratings()
get_top_3_expensive_products()
