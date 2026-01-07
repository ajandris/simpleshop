"""
Cart service functions
"""
from datetime import date
from decimal import Decimal, ROUND_HALF_UP

from django.db.models import F, Sum

from cart.models import Cart, CartItem, Coupon, Shipping

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


def calculate_order(cart_no):
    """
    Calculates the order amounts
    """
    VAT = Decimal('20.00')
    cart = Cart
    try:
        cart = Cart.objects.get(cart_number=cart_no)
    except Cart.DoesNotExist:
        return {}

    shipping = None
    if cart.shipping_method is None:
        shipping = Shipping.objects.order_by('discount_threshold').first()
    else:
        shipping = Shipping.objects.filter(code=cart.shipping_method).first()

    cart_sub_total = CartItem.objects.filter(cart=cart).aggregate(
        total=Sum(F('price') * F('qty'))
    )

    ship_price = 5.00
    if Decimal(str(cart_sub_total['total'])) > Decimal(str(shipping.discount_threshold)):
        ship_price = shipping.price_discounted
    else:
        ship_price = shipping.price

    discount_amount = Decimal('0.00')
    if cart.discount_id is not None:
        disc = Coupon.objects.filter(id=cart.discount_id).first()
        if disc is not None:
            if disc.type == 'percent':
                discount_amount = disc.value * Decimal(str(cart_sub_total['total'])) / 100
            elif disc.type == 'amount':
                discount_amount = disc.value

    ord = dict()
    ord['cart_no'] = cart_no
    ord['shipping_price'] = ship_price
    ord['shipping_method_html'] = shipping.text_html
    ord['discount_value'] = Decimal(str(discount_amount)).quantize(
                                    Decimal("0.01"), rounding=ROUND_HALF_UP)
    ord['subtotal'] = Decimal(str(cart_sub_total['total']))
    ord['vat_percent'] = VAT
    ord['vat_amount'] = Decimal(str((Decimal(str(cart_sub_total['total'])) -
                                    Decimal(str(discount_amount))) * VAT / (100 - VAT))).quantize(
                                    Decimal("0.01"), rounding=ROUND_HALF_UP)

    ord['total'] = Decimal(str(ord.get('subtotal') - ord.get('discount_value') + ord.get('shipping_price'))).quantize(
                                    Decimal("0.01"), rounding=ROUND_HALF_UP)

    return ord

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