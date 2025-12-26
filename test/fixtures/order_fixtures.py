import pytest
from .user_fixtures import user
from products.models import Product, Images, Category


@pytest.fixture
def product_out_of_stock(db, user):
    """Creates demo product with stock=0 for tests"""

    image = Images.objects.create(
        id=1,
        name='placeholder',
        url='images/000_product_placeholder.png',
        user=user,
    )

    category = Category.objects.create(
        id=1,
        title="Christmas Decorations",
        slug="christmas-decorations",
        description="Christmas Decorations",
        image=image,
        user=user,
    )

    zero_stock_product = Product.objects.create(
        title="Sold Out Item",
        price=10.00,
        stock=0,
        user=user,
        image=image,
        category=category
    )

    return zero_stock_product
