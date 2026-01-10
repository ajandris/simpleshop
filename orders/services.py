from typing import Type

from django.shortcuts import redirect
from django.urls import reverse

from cart.models import Cart
from orders.models import Order


def create_order(cart: Cart) -> Order:
    """
    Creates a new Order from a cart
    """
    order = Order()

    return order


def re_build_order(order_to_rebuild: Order, cart: Cart) -> Order:
    """
    Rebuilds existing order based on a cart.
    @return True if cart has not been changed
    """
    order = Order()

    return order


def get_order_hash(order: Order) -> str:
    hash_str = ""
    return hash_str
