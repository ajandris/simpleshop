from decimal import Decimal

import pytest

from cart.models import Cart
from cart.services import check_cart_stock, is_discount_valid, calculate_cart_amounts, \
                          is_coupon_active_with_cart_minimum_value

def test_cart_services_check_cart_stock(db, base_cart):
    """
    Test cart.
    """
    assert check_cart_stock(cart=base_cart) == (True, {}), "Base Cart is not valid"

@pytest.mark.parametrize("cart_fixture, expected_status, expected_errors", [
    ("base_cart", True, {}),
    ("cart_with_out_of_stock_product", False, {"error": "Out of stock"}),
    ("cart_products_with_less_qty", False, {"error": "Not enough products"}),
    ("cart_products_with_price_change", False, {"error": "Price changed"}),
])
def test_cart_services_check_cart_stock(db, cart_fixture, expected_status, expected_errors):
    """
    Test cart.
    """
    assert check_cart_stock(cart=cart_fixture) == (expected_status, expected_errors), "Cart error"


@pytest.mark.parametrize("coupon_fixture, expected_status, expected_errors", [
    ("coupon_no_end_date_amount", True, {}),
    ("coupon_w_end_date", True, {}),
    ("coupon_w_end_and_start_date", True, {}),
    ("coupon_expired", False, {"error": "Coupon expired"}),
    ("coupon_in_future", False, {"error": "Coupon is not yet active"}),
])
def test_cart_services_is_discount_valid(db, coupon_fixture, expected_status, expected_errors):
    """
    Coupon validation
    """
    assert is_discount_valid(coupon_fixture) == (expected_status, expected_errors), "Discount check"


@pytest.mark.parametrize("cart_fixture, expected_result", [
    ("base_cart", {                 # Amounts need to recalculate before each test
        'shipping_price': 111,
        'shipping_method_html': 111,
        'discount_value': 111,
        'subtotal': 111,
        'vat_percent': Decimal(20.00),
        'vat_amount': 111,
        'total': 111111
        }),
    ("base_cart", {  # Amounts need to recalculate before each test
        'shipping_price': 111,
        'shipping_method_html': 111,
        'discount_value': 111,
        'subtotal': 111,
        'vat_percent': Decimal(20.00),
        'vat_amount': 111,
        'total': 111111
    }),
])
def test_cart_services_calculate_cart_amounts(db, cart_fixture, expected_result):
    """
    Calculates cart amounts like total, subtotal etc.
    """

    amounts = calculate_cart_amounts(cart_fixture)
    assert amounts == expected_result, "Calculation error"

def test_is_coupon_active_with_cart_minimum_value(db, base_cart_with_discount):
    base_cart_with_discount.discount.min_subtotal = Decimal('100.00')
    base_cart_with_discount.discount.save()
    result, msg = is_coupon_active_with_cart_minimum_value(base_cart_with_discount)
    assert result is True, msg

    base_cart_with_discount.discount = None
    base_cart_with_discount.save()
    result, msg = is_coupon_active_with_cart_minimum_value(base_cart_with_discount)
    assert result is True, msg


def test_is_coupon_active_with_cart_minimum_value_subtotal_100(db, cart_with_100_subtotal_and_percent_discount):
    cart_with_100_subtotal_and_percent_discount.discount.min_subtotal = Decimal('100.00')
    cart_with_100_subtotal_and_percent_discount.discount.save()
    result, msg = is_coupon_active_with_cart_minimum_value(cart_with_100_subtotal_and_percent_discount)
    assert result is True, msg
