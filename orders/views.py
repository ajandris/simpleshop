from django.shortcuts import render

def process_payment(request):
    """
    Process payment from checkout
    """

    # check/ validate cart

    # create order
    # log order

    # process payment

    # template = 'orders/payment_failed.html'
    template = 'orders/payment_success.html'

    return render(request, template_name=template)
