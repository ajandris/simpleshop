"""
Defining fixtures
"""
import pytest

pytest_plugins = [
    "test.fixtures.coupon_fixtures",
    "test.fixtures.cart_fixtures",
    "test.fixtures.product_fixtures",
    "test.fixtures.user_fixtures",
    "test.fixtures.order_fixtures",
    # "test.fixtures.payment_fixtures",
]

@pytest.fixture(scope="session", autouse=True)
def init_data(django_db_setup, django_db_blocker):
    """
    This function waits for the plugins to be loaded, so it can use the factories defined in them.
    """
    with django_db_blocker.unblock():
        # Shipping methods
        from cart.models import Shipping
        from django.contrib.auth.models import User

        usr, _ = User.objects.get_or_create(
            username='testuser',
            defaults={'is_staff': True}
        )
        if usr.password == "":
            usr.set_password("password123")
            usr.save()

        Shipping.objects.create(
            title="Standard",
            code='standard',
            text_html="Standard (3-5 days)",
            price=3.99,
            discount_threshold=50.00,
            price_discounted=0.00,
            user=usr
        )
        Shipping.objects.create(
            title="Express",
            code='express',
            text_html="Express (1-2 days)",
            price=8.99,
            discount_threshold=10000.00,
            price_discounted=8.99,
            user=usr
        )
        Shipping.objects.create(
            title="Tracked",
            code='tracked',
            text_html="Tracked (2-3 days)",
            price=4.99,
            discount_threshold=10000.00,
            price_discounted=4.99,
            user=usr
        )

        # EOF Shipping methods
