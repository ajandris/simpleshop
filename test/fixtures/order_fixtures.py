import factory
import pytest
from orders.models import Order, OrderItem
from cart.services import calculate_order
from test.factories.order_statuses_factories import OrderStatusFactory
@pytest.fixture
def base_order_with_discount(db, base_cart_with_discount):
    cart = base_cart_with_discount
    cart_totals = calculate_order(cart)

    order = Order.objects.create(
        order_no='ORD-jhafafwnwhjdf',
        cart_no=cart.cart_number,
        discount_amount=cart_totals['discount_value'],
        owner=cart.owner,
        subtotal=cart_totals['subtotal'],
        vat_included=cart_totals['vat_amount'],
        billing_address='Billing Address',
        shipping_address='Shipping Address',
        shipping_price=cart_totals['shipping_price'],
        status=OrderStatusFactory(code='PENDING'),
        user=cart.owner
    )

    for item in cart.cartitem_set.all().order_by('id'):
        OrderItem.objects.create(
            order=order,
            sku=item.product.sku,
            item=item.product.title,
            quantity=item.qty,
            unit_price=item.price,
            user=cart.owner
        )

    return order
