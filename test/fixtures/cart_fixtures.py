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

    for prod in items:
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