from datetime import date
from decimal import Decimal

import pytest

from cart.services import check_cart_stock, calculate_cart_amounts, \
                          is_coupon_valid, has_discount_min_subtotal_reached

def test_cart_services_check_cart_stock(db, base_cart):
    """
    Test cart.
    """
    assert check_cart_stock(cart=base_cart) == (True, {}), "Base Cart is not valid"

@pytest.mark.parametrize("cart_fixture, expected_status, expected_errors", [
    ("base_cart", True, {}),
    ("base_cart_with_out_of_stock_product", False, {"error": "Out of stock"}),
    ("base_cart_products_with_less_qty", False, {"error": "Not enough products"}),
    ("base_cart_products_with_price_change", False, {"error": "Price has changed"}),
])
def test_cart_services_check_cart_stock(db, request, cart_fixture, expected_status, expected_errors):
    """
    Test cart.
    """
    cart_object = request.getfixturevalue(cart_fixture)
    result_status, result_errors = check_cart_stock(cart=cart_object)

    assert (result_status, result_errors) == (expected_status, expected_errors), f"Cart error: {expected_errors}"


@pytest.mark.parametrize("coupon_fixture, expected_status, expected_errors", [
    ("coupon_no_end_date_amount", True, ""),
    ("coupon_w_end_date", True, ""),
    ("coupon_w_end_and_start_date", True, ""),
    ("coupon_expired", False, "Coupon expired"),
    ("coupon_in_future", False, "Coupon is not yet active"),
])
def test_cart_services_is_discount_valid(db, request, coupon_fixture, expected_status, expected_errors):
    """
    Coupon validation
    """
    coupon = request.getfixturevalue(coupon_fixture)
    result_status, result_errors = is_coupon_valid(coupon)

    assert (result_status, result_errors) == (expected_status, expected_errors), f"Discount check: {result_errors}"


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
    # assert amounts == expected_result, "Calculation error"


def test_coupon_minimal_subtotal_threshold_under(db, base_cart_with_discount):
    cart = base_cart_with_discount
    cart.discount.min_subtotal = Decimal('100.00')
    cart.discount.save()
    result, msg = has_discount_min_subtotal_reached(cart)
    assert result is False, msg

def test_coupon_minimal_subtotal_threshold_over(db, cart_with_100_subtotal_and_percent_discount):
    cart = cart_with_100_subtotal_and_percent_discount
    cart.discount.min_subtotal = Decimal('100.00')
    cart.discount.save()
    result, msg = has_discount_min_subtotal_reached(cart)
    assert result is True, msg

