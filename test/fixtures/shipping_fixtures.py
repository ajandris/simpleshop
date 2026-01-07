from decimal import Decimal

import pytest
from test.factories.user_factories import UserFactory

from cart.models import Shipping

@pytest.fixture
def shipping_standard(db):
    Shipping.objects.create(
        title='Standard',
        code='standard',
        text_html='Standard (3-5) days',
        price=Decimal(str('4.99')),
        discount_threshold=Decimal(str('50.00')),
        price_discounted=Decimal(str('0.00')),
        user=UserFactory(username='testuser')
    )

@pytest.fixture
def shipping_express(db):
    Shipping.objects.create(
        title='Express',
        code='express',
        text_html='Express (1-2) days',
        price=Decimal(str('8.99')),
        discount_threshold=Decimal(str('10000.00')),
        price_discounted=Decimal(str('9.99')),
        user=UserFactory(username='testuser')
    )