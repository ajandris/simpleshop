import stripe
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from cart.services import check_cart_stock, calculate_order
from orders.models import Order, OrderStatuses
from cart.models import Cart
from orders.services import make_order, update_order_status, email_order_created

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_payment_intent(request, cart_no):
    from cart.services import calculate_order
    cart = Cart.objects.filter(cart_number=cart_no).first()
    order = Order.objects.filter(cart_no=cart_no).first()

    order_no = '' if order is None else order.order_no

    if cart is None:
        messages.error(request, 'No cart found')
        return redirect('cart')

    amounts = calculate_order(cart.cart_number)
    amount_to_pay = int(amounts['total'] * 100)

    try:
        # Create a PaymentIntent with the cart amount
        intent = stripe.PaymentIntent.create(
            amount=amount_to_pay,  # Stripe uses pence/cents
            currency='gbp',
            metadata={'order_no': order_no,
                      'cart_no': cart_no,
                      },
        )

        return JsonResponse({
            'clientSecret': intent.client_secret
        })
    except Exception as e:
        print(e)
        return JsonResponse({'error': str(e)}, status=403)


@csrf_exempt
def get_stripe_publishable_key(request):
    if request.method == 'POST':
        pk = settings.STRIPE_PUBLIC_KEY
    else:
        pk = ''
    resp = {
        'pk': pk,
    }

    return JsonResponse(resp)


@csrf_exempt
def create_payment_intent_test(request):
    try:
        # Create a PaymentIntent with the order amount and currency
        # Amount is in pence (e.g., 2000 = £20.00)
        intent = stripe.PaymentIntent.create(
            amount=2000,
            currency='gbp',
            automatic_payment_methods={
                'enabled': True,
            },
        )
        return JsonResponse({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=403)

@csrf_exempt
def complete_payment(request):
    """
    Actions after Stripe authorization is complete
    """
    redirect_status = request.GET.get('redirect_status', '')
    payment_intent = request.GET.get('payment_intent')
    request.session['payment_intent'] = payment_intent

    pi = stripe.PaymentIntent.retrieve(
        payment_intent,
        expand=[
            "charges.data.balance_transaction",
            "charges.data.payment_method_details",
            "payment_method",
            "customer",
        ]
    )

    order_no = pi.payment_method.metadata.get('order_number')
    order = Order.objects.get(order_no=order_no)

    if redirect_status == 'succeeded':
        request.session['order_no'] = order_no
        update_order_status(order, OrderStatuses.objects.get(code='PAID'))

        # Send email
        email_order_created(order)

        # Clean up
        Cart.objects.filter(cart_number=request.session['cart_number']).delete()
        del request.session['cart_number']
        del request.session['payment_intent']

        return redirect('payment-success')
    else:
        # Never reached as Stripe gives error messages in the payment form and stops authorization
        update_order_status(order, OrderStatuses.objects.get(code='PAYMENT_FAILED'))
        return redirect('payment-failed')

@csrf_exempt
def get_order(request):
    """
    Gets order for JSON response.
    If validation fails, redirects to cart with error message.
    """

    resp = dict()

    cart_no = request.session.get('cart_number')
    cart = None
    if cart_no:
        cart = Cart.objects.get(cart_number=cart_no)
    else:
        messages.error(request, 'Your cart has been emptied.')
        return redirect('cart')

    # check/ validate cart items against warehouse
    rez, msg = check_cart_stock(cart)
    if not rez:
        messages.error(request, 'Item quantities or price have been changed.')
        return redirect('cart')

    # check/ validate cart itself against user changes
    totals = calculate_order(cart_no)
    checkout_hash = request.POST.get('checkout_hash')

    if checkout_hash != totals['cart_hash']:
        messages.error(request, 'Your cart has been changed. Please check other browser tabs.')
        redirect('cart')

    order = make_order(request, cart)

    return JsonResponse({
        'order_no': order.order_no,
        'email': order.email,
    })