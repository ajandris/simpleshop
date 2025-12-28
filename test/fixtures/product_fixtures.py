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
    products = dict()
    prod1 = ProductFactory(price=12.50, stock=10)
    prod2 = ProductFactory(price=10, stock=5)
    prod3 = ProductFactory(price=22.50, stock=15)
    products['prod1'] = prod1
    products['prod2'] = prod2
    products['prod3'] = prod3
    return products

@pytest.fixture
def cart_products_with_out_of_stock_product(
        db, base_cart_products):
    """
    Cart Item products with out-of-stock product
    """
    products = base_cart_products
    products['prod1'].title = 'Sold Out Item'
    products['prod1'].stock = 0
    products['prod1'].save()
    return products


@pytest.fixture
def cart_products_with_less_qty(
        db, base_cart_products):
    """
    Cart Item products with less quantity than in cart but not out of
    """
    products = base_cart_products
    products['prod2'].stock = 3
    products['prod2'].save()
    return products


@pytest.fixture
def cart_products_with_price_change(
        db, base_cart_products):
    products = base_cart_products
    products['prod1'].price = 15
    products['prod1'].save()
    return products
