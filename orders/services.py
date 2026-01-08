from typing import Type

from django.shortcuts import redirect
from django.urls import reverse

from cart.models import Cart
from orders.models import Order


def create_order(cart: Cart) -> Type[Order]:
    """
    Creates a new Order from a cart
    """
    order = Order

    return order


def validate_order(cart: Cart) -> bool:
    """
    Validates order against cart.
    @return True if cart has not been changed
    """

    return False