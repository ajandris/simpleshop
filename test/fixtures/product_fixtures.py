"""
Product fixtures for pytest
"""
import pytest
from test.factories.product_factories import ProductFactory


@pytest.fixture
def base_cart_products(db):
    """
    Products to be in a base cart to test against
    """
    prod1 = ProductFactory(price=12.50, stock=10)
    prod2 = ProductFactory(price=10, stock=5)
    prod3 = ProductFactory(price=22.50, stock=15)
    products = [prod1, prod2, prod3]
    return products


@pytest.fixture
def cart_products_with_price_change(
        db, base_cart_products):
    products = base_cart_products
    products[0].price = 15
    products[0].save()
    return products


@pytest.fixture
def cart_products_55_amount(
        db):
    prod1 = ProductFactory(price=5.50, stock=10)
    products = [prod1,]
    return products

@pytest.fixture
def products_subtotal_100(db):
    """
    Products to be in a base cart to test against
    """
    prod1 = ProductFactory(price=2.50, stock=10)
    prod2 = ProductFactory(price=7.50, stock=10)
    products = [prod1, prod2]
    return products
