from user_input import user_input


def test_user(): 

    assert user_input("no") == "That's ok. Come back for a new cocktail recipes whenever you like!"
    assert user_input("yes") == 'True'