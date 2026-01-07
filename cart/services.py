"""
Cart service functions
"""
from datetime import datetime, date
from decimal import Decimal

from cart.models import Cart, CartItem, Coupon


def check_cart_stock(cart: Cart):
    """
    Checks stock levels and prices.
    Returns: (bool: is_valid, dict: errors)
    """
    failed_items = dict()
    for item in cart.cartitem_set.all():
        if item.product.stock == 0:
            failed_items["error"] = "Out of stock"
            return False, failed_items
        elif item.qty > item.product.stock:
            failed_items["error"] = "Not enough products"
            return False, failed_items

        if Decimal(str(item.price)) != Decimal(str(item.product.price)):
            failed_items["error"] = "Price has changed"
            return False, failed_items

    return True, {}


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


def is_coupon_valid(coupon: Coupon) -> (bool, str):
    """
    Checks if cart subtotal is larger or equal to minimum of coupon threshold
    """
    today = date.today()
    if coupon.effective_from and coupon.effective_from > today:
        return False, "Coupon is not yet active"

    if coupon.effective_to and coupon.effective_to < today:
        return False, "Coupon expired"

    return True, ""


def has_discount_min_subtotal_reached(cart_with_active_coupon: Cart) -> (bool, str):
    """
    Checks if cart subtotal is larger or equal to coupon threshold.
    """
    if cart_with_active_coupon.discount.min_subtotal < get_cart_subtotal(cart_with_active_coupon):
        return False, f"Cart subtotal should be larger or equal to {cart_with_active_coupon.discount.min_subtotal}"
    return True, ""