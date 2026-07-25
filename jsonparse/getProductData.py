import requests

def getResponse():
    url = 'https://dummyjson.com/carts/1'
    response = requests.get(url)
    return response

def get_specific_product_price():
    response = getResponse()
    discountedTotal = None
    if response.status_code == 200:
        data = response.json()
        products = data.get("products", [])
        for prod in products:
            if prod.get("title") == "Generic Motorcycle":
                discountedTotal = prod.get("discountedTotal")
    return discountedTotal

def listAllDiscountPercentage():
    response = getResponse()
    allDiscountPercentage = []
    if response.status_code == 200:
        data = response.json()
        products = data.get("products", [])
        for prod in products:
            if "discountPercentage" in prod:
                allDiscountPercentage.append(prod.get("discountPercentage"))

    return allDiscountPercentage

# Print a specific product discounted price
discountedPrice = get_specific_product_price()
print("Discounted Total: ", discountedPrice)

# Print a list of all the discount percentage values
allDiscountPercentage = listAllDiscountPercentage()
print("List is: ", allDiscountPercentage)




