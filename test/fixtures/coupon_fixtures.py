import pytest
from datetime import datetime, timedelta
from cart.models import Coupon
from test.factories.user_factories import UserFactory

@pytest.fixture
def coupon_no_end_date_amount(db):
    # Discounts
    return Coupon.objects.create(
        code='valid_coupon1',
        value=10,
        # percent or amount
        type='amount',
        # null -> no restriction
        effective_from=None,
        # null -> no restriction
        effective_to=None,
        user=UserFactory(username='testuser')
    )

@pytest.fixture
def coupon_no_end_date_percent(db):
    # Discounts
    return Coupon.objects.create(
        code='valid_coupon2',
        value=10,
        # percent or amount
        type='percent',
        # None -> no restriction
        effective_from=None,
        # None -> no restriction
        effective_to=None,
        user=UserFactory(username='testuser')
    )

@pytest.fixture
def coupon_w_end_date(db):
    # Discounts
    today = datetime.now().date()
    offset = timedelta(days=100)
    end_date = today + offset
    return Coupon.objects.create(
        code='valid_coupon3',
        value=10,
        # percent or amount
        type='amount',
        # None -> no restriction
        effective_from=None,
        # None -> no restriction
        effective_to=end_date,
        user=UserFactory(username='testuser')
    )

@pytest.fixture
def coupon_w_end_and_start_date(db):
    # Discounts
    today = datetime.now().date()
    offset = timedelta(days=100)
    start_date = today - offset
    end_date = today + offset
    return Coupon.objects.create(
        code='valid_coupon4',
        value=10,
        # percent or amount
        type='amount',
        # None -> no restriction
        effective_from=start_date,
        # None -> no restriction
        effective_to=end_date,
        user=UserFactory(username='testuser')
    )

@pytest.fixture
def coupon_expired(db):
    # Discounts
    today = datetime.now().date()
    offset = timedelta(days=100)
    end_date = today - timedelta(days=5)
    start_date = today - offset
    return Coupon.objects.create(
        code='expired_coupon',
        value=10,
        # percent or amount
        type='amount',
        # None -> no restriction
        effective_from=start_date,
        # None -> no restriction
        effective_to=end_date,
        user=UserFactory(username='testuser')
    )

@pytest.fixture
def coupon_future(db):
    # Discounts
    today = datetime.now().date()
    offset = timedelta(days=100)
    start_date = today + timedelta(days=5)
    end_date = today + offset

    return Coupon.objects.create(
        code='future_coupon',
        value=10,
        # percent or amount
        type='amount',
        # None -> no restriction
        effective_from=start_date,
        # None -> no restriction
        effective_to=end_date,
        user=UserFactory(username='testuser')
    )
