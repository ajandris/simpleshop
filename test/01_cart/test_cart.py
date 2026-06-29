import pytest
from decimal import Decimal

from cart.services import (
    check_cart_stock,
    calculate_order,
    is_coupon_valid,
    has_discount_min_subtotal_reached,
)


def test_cart_services_check_cart_stock(db, base_cart):
    """
    Test cart.
    """
    assert check_cart_stock(cart=base_cart) == (
        True,
        {},
    ), "Base Cart is not valid"


@pytest.mark.parametrize(
    "cart_fixture, expected_status, expected_errors",
    [
        ("base_cart", True, {}),
        (
            "base_cart_with_out_of_stock_product",
            False,
            {"error": "Out of stock"},
        ),
        (
            "base_cart_products_with_less_qty",
            False,
            {"error": "Not enough products"},
        ),
        (
            "base_cart_products_with_price_change",
            False,
            {"error": "Price has changed"},
        ),
    ],
)
def test_cart_services_check_cart_stock(
    db, request, cart_fixture, expected_status, expected_errors
):
    """
    Test cart.
    """
    cart_object = request.getfixturevalue(cart_fixture)
    result_status, result_errors = check_cart_stock(cart=cart_object)

    assert (result_status, result_errors) == (
        expected_status,
        expected_errors,
    ), f"Cart error: {expected_errors}"


@pytest.mark.parametrize(
    "coupon_fixture, expected_status, expected_errors",
    [
        ("coupon_no_end_date_amount", True, ""),
        ("coupon_w_end_date", True, ""),
        ("coupon_w_end_and_start_date", True, ""),
        ("coupon_expired", False, "Coupon expired"),
        ("coupon_in_future", False, "Coupon is not yet active"),
    ],
)
def test_cart_services_is_discount_valid(
    db, request, coupon_fixture, expected_status, expected_errors
):
    """
    Coupon validation
    """
    coupon = request.getfixturevalue(coupon_fixture)
    result_status, result_errors = is_coupon_valid(coupon)

    assert (result_status, result_errors) == (
        expected_status,
        expected_errors,
    ), f"Discount check: {result_errors}"


@pytest.mark.parametrize(
    "cart_fixture, expected_result",
    [
        (
            "base_cart_with_discount",
            {
                "shipping_price": Decimal("0.00"),
                "discount_value": Decimal("10.00"),
                "subtotal": Decimal("512.50"),
                "vat_percent": Decimal("20.00"),
                "vat_amount": Decimal("83.75"),
                "total": Decimal("502.50"),
            },
        ),
        (
            "base_cart_with_discount_percent",
            {
                "shipping_price": Decimal("0.00"),
                "discount_value": Decimal("51.25"),
                "subtotal": Decimal("512.50"),
                "vat_percent": Decimal("20.00"),
                "vat_amount": Decimal("76.88"),
                "total": Decimal("461.25"),
            },
        ),
        (
            "base_cart",
            {
                "shipping_price": Decimal("0.00"),
                "discount_value": Decimal("0.00"),
                "subtotal": Decimal("512.50"),
                "vat_percent": Decimal("20.00"),
                "vat_amount": Decimal("85.42"),
                "total": Decimal("512.50"),
            },
        ),
        (
            "base_cart_with_discount_1000_min_subtotal",
            {
                "shipping_price": Decimal("0.00"),
                "discount_value": Decimal("0.00"),
                "subtotal": Decimal("512.50"),
                "vat_percent": Decimal("20.00"),
                "vat_amount": Decimal("85.42"),
                "total": Decimal("512.50"),
            },
        ),
        (
            "base_cart_with_express_shipping",
            {
                "shipping_price": Decimal("8.99"),
                "discount_value": Decimal("0.00"),
                "subtotal": Decimal("512.50"),
                "vat_percent": Decimal("20.00"),
                "vat_amount": Decimal("86.92"),
                "total": Decimal("521.49"),
            },
        ),
    ],
)
def test_cart_services_calculate_cart_amounts(
    db, request, cart_fixture, expected_result
):
    """
    Calculates cart amounts like total, subtotal etc.
    """
    cart = request.getfixturevalue(cart_fixture)
    amounts = calculate_order(cart)
    amounts.pop("cart_no", None)  # not relevant for calculations
    amounts.pop("shipping_method_html", None)  # not relevant for calculations
    amounts.pop("cart_hash", None)  # used for tracking changes
    assert amounts == expected_result, "Calculation error"


def test_coupon_minimal_subtotal_threshold_under(db, base_cart_with_discount):
    """
    False if cart subtotal is less than discount threshold
    """
    cart = base_cart_with_discount
    cart.discount.min_subtotal = Decimal("100.00")
    cart.discount.save()
    result, msg = has_discount_min_subtotal_reached(cart)
    assert result is True, msg


def test_coupon_minimal_subtotal_threshold_even(
    db, cart_with_100_subtotal_and_percent_discount
):
    """
    True if cart subtotal is more or even than discount threshold
    """
    cart = cart_with_100_subtotal_and_percent_discount
    cart.discount.min_subtotal = Decimal("100.00")
    cart.discount.save()
    result, msg = has_discount_min_subtotal_reached(cart)
    assert result is True, msg


def test_coupon_minimal_subtotal_threshold_over(
    db, cart_with_100_subtotal_and_percent_discount
):
    """
    True if cart subtotal is more or even than discount threshold
    """
    cart = cart_with_100_subtotal_and_percent_discount
    cart.discount.min_subtotal = Decimal("200.00")
    cart.discount.save()
    result, msg = has_discount_min_subtotal_reached(cart)
    assert result is False, msg


def test_checkout_empty_cart(client, db, user):
    """
    If cart exists but there are no cart items, delete cart,
    clear the cart_number from the session, and redirect to the cart page.
    """
    from django.urls import reverse
    from cart.models import Cart
    from home.models import Profile

    # Ensure profile exists for the user
    Profile.objects.create(owner=user, user=user, email=user.email)

    client.force_login(user)

    # Create a cart without any items
    cart = Cart.objects.create(cart_number="test_empty_cart_no", owner=user, user=user)

    session = client.session
    session["cart_number"] = "test_empty_cart_no"
    session.save()

    response = client.get(reverse("checkout"))

    # Assert redirect to cart page
    assert response.status_code == 302
    assert response.url == reverse("cart")

    # Verify the cart was deleted from DB
    assert not Cart.objects.filter(cart_number="test_empty_cart_no").exists()

    # Verify the session has been cleared of the cart_number
    assert "cart_number" not in client.session


def test_checkout_empty_cart_post(client, db, user):
    """
    If a user submits a POST request to checkout (e.g. from cart page form submission)
    but the cart items are missing in DB, it should delete the cart,
    clear session and redirect back to cart, instead of throwing AttributeError 500.
    """
    from django.urls import reverse
    from cart.models import Cart
    from home.models import Profile

    Profile.objects.create(owner=user, user=user, email=user.email)
    client.force_login(user)

    cart = Cart.objects.create(cart_number="test_empty_cart_no", owner=user, user=user)

    session = client.session
    session["cart_number"] = "test_empty_cart_no"
    session.save()

    response = client.post(reverse("checkout"), {
        "sku-testproduct": "1",
        "shipping": "standard"
    })

    # Assert redirect to cart page and no 500 error
    assert response.status_code == 302
    assert response.url == reverse("cart")

    # Verify database cleanup
    assert not Cart.objects.filter(cart_number="test_empty_cart_no").exists()
    assert "cart_number" not in client.session


def test_checkout_creates_profile_if_missing(client, db, user):
    """
    If a user visits checkout but doesn't have a Profile object, it should be created automatically,
    rather than raising a 404 error.
    """
    from django.urls import reverse
    from home.models import Profile

    client.force_login(user)

    # Verify profile does not exist initially
    assert not Profile.objects.filter(owner=user).exists()

    response = client.get(reverse("checkout"))

    # It should not return a 404. Since the cart is empty, it will redirect (302) to cart.
    assert response.status_code == 302
    assert response.url == reverse("cart")

    # Verify the profile was automatically created
    assert Profile.objects.filter(owner=user).exists()

