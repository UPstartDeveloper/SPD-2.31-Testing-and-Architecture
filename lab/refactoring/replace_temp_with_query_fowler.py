# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace temp with query
# Code snippet. Not runnable.


def get_discount_factor(base_price):
    discount_factor = 0.98
    if base_price > 1000:
        discount_factor = 0.95
    return discount_factor


def get_price():
    base_price = quantity * item_price
    discount_factor = get_discount_factor(base_price)
    return base_price * discount_factor
