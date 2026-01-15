from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from cart.services import check_cart_stock, calculate_order
from cart.models import Cart
from orders.models import Order
from orders.services import make_order, get_order_hash

@login_required
def process_payment(request):
    """
    Process payment from checkout
    """
    cart_no = request.session.get('cart_number')
    cart = None
    if cart_no:
        cart = Cart.objects.get(cart_number=cart_no)
    else:
        messages.error(request, 'Your cart is empty')
        return redirect('cart')

    # check/ validate cart items against warehouse
    rez, msg = check_cart_stock(cart)
    if not rez:
        messages.error(request, "Item quantities or price have been changed")
        return redirect('cart')

    # check/ validate cart itself against user changes
    totals = calculate_order(cart_no)
    checkout_hash = request.POST.get('checkout_hash')

    if checkout_hash != totals['cart_hash']:
        messages.error(request, "Your cart has been changed. Please review your cart before payment.")
        return redirect('cart')

    # create order
    order = make_order(request, cart)

    if checkout_hash != get_order_hash(order):
        messages.error(request, "There is a difference between the cart and the created order. \
                        Please contact the Customer Support")
        return redirect('cart')



    # log order

    # process payment

    # moch process for development

    card_num = request.POST.get('card_number', '')
    card_month = request.POST.get('expiry_month', '')
    card_year = request.POST.get('expiry_year', '')
    card_cvc = request.POST.get('cvc', '')
    payment_amount = order.total

    if card_num == '111111':
        payment_successful = True
        template = 'orders/payment_success.html'
        context = {
            'order_number': order.order_no
        }
        # delete cart and number in sessions
        cart.delete()
        request.session.pop('cart_number', None)
        request.session.modified = True
    else:
        payment_successful = False
        template = 'orders/payment_failed.html'

    return render(request, template_name=template, context=context)


@login_required
def orders_list(request):
    template = 'orders/orders_list.html'
    orders = Order.objects.filter(owner=request.user).order_by('-order_date')

    context = {
        'orders': orders
    }

    return render(request, template_name=template, context=context)


@login_required
def orders_details(request, order_no):
    template = 'orders/order_details.html'
    order = get_object_or_404(Order, order_no=order_no)

    context = {
        'order': order
    }

    return render(request, template_name=template, context=context)
