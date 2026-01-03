"""
Cart fixtures for pytest
"""
import pytest
from test.factories.cart_factories import Cart, CartFactory


def add_coupon_to_cart(cart, coupon):
    cart.discount = coupon
    cart.save()

def remove_coupon_from_cart(cart):
    cart.discount = None
    cart.save()


def add_cart_items(cart, items):
    """
    Adds products to cart
    :param cart: The current Cart
    :param items: The products to add to cart
    """
    from cart.models import CartItem

    for prod in items.values():
        CartItem.objects.create(
            cart=cart,
            user=prod.user,
            qty=prod.stock,
            price=prod.price,
            product=prod
        )

@pytest.fixture
def base_cart(db, base_cart_products):
    """
    Base cart fixture for a cart to compare with
    """
    cart = CartFactory()
    add_cart_items(cart, base_cart_products)
    return cart

@pytest.fixture
def base_cart_with_discount(db, base_cart_products, coupon_no_end_date_amount):
    """
    Base cart with discount coupon
    """
    cart = CartFactory(discount=coupon_no_end_date_amount)
    add_cart_items(cart, base_cart_products)
    return cart

@pytest.fixture
def base_cart_with_55_amount(db, cart_products_55_amount, coupon_no_end_date_amount):
    """
    Base cart with discount coupon
    """
    cart = CartFactory(discount=coupon_no_end_date_amount)
    add_cart_items(cart, cart_products_55_amount)
    return cart

@pytest.fixture
def base_cart_with_55_amount_percent_discount(db, cart_products_55_amount, coupon_no_end_date_percent):
    """
    Base cart with discount coupon and cart subtotal of GBP 55.00
    """
    cart = CartFactory(discount=coupon_no_end_date_percent)
    add_cart_items(cart, cart_products_55_amount)
    return cart


@pytest.fixture
def cart_with_100_subtotal_and_percent_discount(db, products_subtotal_100, coupon_no_end_date_percent):
    """
    Base cart with discount coupon and cart subtotal of GBP 55.00
    """
    cart = CartFactory(discount=coupon_no_end_date_percent)
    add_cart_items(cart, products_subtotal_100)
    return cart
