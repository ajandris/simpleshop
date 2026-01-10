from orders.models import Order, OrderItem
from cart.services import calculate_order
from orders.services import create_order, get_order_hash, re_build_order

def test_create_order(base_cart_with_discount):
    cart = base_cart_with_discount
    cart_totals = calculate_order(cart.cart_number)

    order = create_order(cart.cart_number)

    assert cart_totals['cart_hash'] == get_order_hash(order), "The cart and the order hashes are different"


def test_re_build_order(base_order_with_discount, base_cart_with_discount_1000_min_subtotal):
    cart = base_cart_with_discount_1000_min_subtotal
    cart_totals = calculate_order(cart.cart_number)

    orders = Order.objects.filter(order_no=base_order_with_discount.order_no)
    order = orders[0]

    rebuilt_order = re_build_order(order, cart)

    assert cart_totals['cart_hash'] == get_order_hash(rebuilt_order), \
        "The cart and the rebuilt order hashes are different"
