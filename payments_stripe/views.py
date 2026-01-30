import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from orders.models import Order
from cart.models import Cart

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_payment_intent(request, cart_no):
    from cart.services import calculate_order
    cart = Cart.objects.filter(cart_number=cart_no).first()
    order = Order.objects.filter(cart_no=cart_no).first()

    order_no = '' if order is None else order.order_number

    if cart is None:
        return JsonResponse({'error': 'No cart'}, status=403)

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
    redirect_status = request.GET.get('redirect_status', '')

    if redirect_status == 'succeeded':
        return redirect('payment-success')
    else:
        return redirect('payment-failed')
