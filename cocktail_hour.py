

api_key = ("1")

def generate_cocktail_hour(name):
    url = f"www.thecocktaildb.com/api/json/v1/{api_key}/search.php?s={name}"