def login(username, password):
    if username == "admin" and password == "admin123":
        return True
    return False


def add_to_cart(is_logged_in, item):
    if not is_logged_in:
        raise Exception("User not logged in")
    return f"{item} added to cart"


def checkout(cart_item):
    if not cart_item:
        raise Exception("Cart is empty")
    return "Order placed successfully"


import pytest


def test_end_to_end_successful_order():
    is_logged_in = login("admin", "admin123")
    assert is_logged_in is True

    cart_item = add_to_cart(is_logged_in, "Laptop")
    assert "Laptop" in cart_item

    result = checkout(cart_item)
    assert result == "Order placed successfully"


def test_add_to_cart_without_login():
    with pytest.raises(Exception) as error:
        add_to_cart(False, "Mobile")

    assert "User not logged in" in str(error.value)