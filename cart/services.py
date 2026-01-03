"""
Cart service functions
"""
from decimal import Decimal

from cart.models import Cart, CartItem


def check_cart_stock(cart):
    """
    Checks stock levels and prices.
    Returns: (bool: is_valid, dict: errors)
    """
    failed_items = dict()

    return len(failed_items) != 0, failed_items

def is_discount_valid(coupon):
    """
    Checks if the attached discount is still active.
    Returns: (bool: is_valid, dict: fail_info)
    """
    fail_info = dict()

    return len(fail_info) == 0, fail_info

def calculate_cart_amounts(cart) -> dict:
    """
    Calculates the cart amounts such as total, subtotal, VAT, shipping etc.
    Returns: (dict: amounts)
    """
    from decimal import Decimal

    VAT = Decimal('20.00')

    amounts = {
        'shipping_price': 0,
        'shipping_method_html': 0,
        'discount_value': 0,
        'subtotal': 0,
        'vat_percent': VAT,
        'vat_amount': 0,
        'total': 0
    }

    return amounts

def get_cart_subtotal(cart: Cart) -> Decimal:
    result = Decimal('0.00')
    cart_items = CartItem.objects.filter(cart=cart)
    for item in cart_items:
        result += item.qty * Decimal(str(item.price))

    return result


def is_coupon_active_with_cart_minimum_value(cart: Cart) -> (bool, str):
    """
    Checks if cart subtotal is larger or equal to minimum of coupon threshold
    """
    if cart.discount is None:
        return True, "No coupon attached"

    if cart.discount.min_subtotal > get_cart_subtotal(cart):
        return False, f"Discount starts from cart subtotal of £{cart.discount.min_subtotal}"
    else:
        return True, "Discount can be calculated"
