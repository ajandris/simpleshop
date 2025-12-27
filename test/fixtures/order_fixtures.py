import pytest
from products.models import Product, Category


@pytest.fixture
def product_out_of_stock(db, user, default_image, product_category):
    """Creates demo product with stock=0 for tests"""

    zero_stock_product = Product.objects.create(
        title="Sold Out Item",
        price=10.00,
        stock=0,
        user=user,
        image=default_image,
        category=product_category
    )

    return zero_stock_product
