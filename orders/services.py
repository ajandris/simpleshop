import hashlib
from cart.services import calculate_order

from cart.models import Cart
from orders.models import Order, OrderStatuses, OrderItem
from cart.models import Shipping
from simpleshop import settings


def create_order(cart: Cart) -> Order:
    """
    Creates a new Order from a cart
    To create full order, user make_order(). It adds addresses and other necessary information to the order
    """
    cart_totals = calculate_order(cart)
    order_status = OrderStatuses.objects.get(code='PENDING')
    order = Order.objects.create(
        cart_no=cart.cart_number,
        discount_amount=cart_totals['discount_value'],
        total=cart_totals['total'],
        owner=cart.owner,
        subtotal=cart_totals['subtotal'],
        vat_included=cart_totals['vat_amount'],
        billing_address='Billing Address',
        shipping_address='Shipping Address',
        shipping_price=cart_totals['shipping_price'],
        status=order_status,
        user=cart.owner
    )
    order.save()

    for item in cart.cartitem_set.all():
        order_item=OrderItem.objects.create(
            order=order,
            sku=item.product.sku,
            item=item.product.title,
            quantity=item.qty,
            unit_price=item.price,
            user=cart.owner
        )
        order_item.save()

    return order


def re_build_order(order_to_rebuild: Order, cart: Cart) -> Order:
    """
    Rebuilds existing order based on a cart.
    @return True if cart has not been changed
    To create full order, user make_order(). It adds addresses and other necessary information to the order
    """
    cart_totals = calculate_order(cart)

    print("Cart Totals: ", cart_totals)

    order = order_to_rebuild
    order.cart_no = cart.cart_number
    order.discount_amount = cart_totals['discount_value']
    order.total = cart_totals['total']
    order.owner = cart.owner
    order.subtotal = cart_totals['subtotal']
    order.vat_included = cart_totals['vat_amount']
    order.billing_address = 'Billing Address'
    order.shipping_address = 'Shipping Address'
    order.shipping_price = cart_totals['shipping_price']
    order.status = OrderStatuses.objects.get(code='PENDING')
    order.user = cart.owner
    order.save()

    # delete all order items to replace with actual cart items
    OrderItem.objects.filter(order=order).delete()

    for item in cart.cartitem_set.all():
        order_item = OrderItem.objects.create(
            order=order,
            sku=item.product.sku,
            item=item.product.title,
            quantity=item.qty,
            unit_price=item.price,
            user=cart.owner
        )
        order_item.save()

    return order

def make_order(request, cart: Cart) -> Order:
    """
    Order creation master function, which serves creating a new order based on a cart and
    recreating an existing order with order_no and based on a Cart.
    If order_no provided does not have associated order, a new order is created.
    """

    order = Order()
    existing_order = Order.objects.filter(cart_no=cart.cart_number).first()

    if existing_order is None:
        order = create_order(cart)
    else:
        order = re_build_order(existing_order, cart)

    # Add addresses
    post = request.POST
    address = f"{post.get('address_line1', '')}"
    if post.get('address_line2', '') == '':
        address += ","
    else:
        address += f" {post.get('address_line2', '')},"

    address += f"\n{post.get('city', '')},"
    if post.get('state', '') != '':
        address += f"\n{post.get('state', '')},"
    address += f"\n{post.get('zip', '')}"
    address += f"\n{post.get('country', '')}"

    order.billing_name = f"{post.get('first_name', '')}"
    order.billing_surname = f"{post.get('last_name', '')}"
    order.billing_address = address

    order.shipping_name = f"{post.get('first_name', '')}"
    order.shipping_surname = f"{post.get('last_name', '')}"
    order.shipping_address = address

    shipping = Shipping.objects.get(code=cart.shipping_method)
    order.shipping_method = shipping.title

    order.save()

    return order


def get_order_hash(order: Order) -> str:
    item_signatures = []

    for item in order.orderitem_set.all():
        sig = f"{item.sku}:{item.quantity}:{item.unit_price}"
        item_signatures.append(sig)
    item_signatures.sort()

    full_signature = "|".join(item_signatures)
    hash_str = hashlib.sha256(full_signature.encode()).hexdigest()
    return hash_str


def render_email_order_created_content(order: Order) -> (str, str, str):
    """
    Makes Order Created email Subject and Body Text and Body HTML content
    """
    from django.template.loader import render_to_string

    subject = f"Order #{order.order_no} Created [The Olde Christmas Market]"

    text_template = 'emails/order_receipt_confirmation_text.html'
    text = render_to_string(text_template, context={"order": order})

    html_template = 'emails/order_receipt_confirmation_html.html'
    html = render_to_string(html_template, context={"order":order})

    return subject, text, html


def email_order_created(order: Order):
    from django.core.mail import EmailMultiAlternatives

    subject, text, html = render_email_order_created_content(order)

    email = EmailMultiAlternatives(subject, text, settings.EMAIL_HOST_USER, to=['andris.jancevskis@gmail.com'])
    email.attach_alternative(html, "text/html")
    email.send()

    return 0