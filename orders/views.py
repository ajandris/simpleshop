from django.contrib import messages
from django.shortcuts import render, redirect
from cart.services import check_cart_stock, calculate_order
from cart.models import Cart

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


    # log order

    # process payment

    # template = 'orders/payment_failed.html'
    template = 'orders/payment_success.html'

    return render(request, template_name=template)
