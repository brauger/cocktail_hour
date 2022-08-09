from user_input import user_input
from cocktail_api import cocktail_input

def test_user(): 

    assert user_input("no") == "That's ok. Come back for a new cocktail recipes whenever you like!"
    assert user_input("yes") == 'True'

def test_cocktail(): 

    assert cocktail_input("https://www.thecocktaildb.com/api/json/v1/1/random.php") == 'True'
    assert cocktail_input("") == 'False'    