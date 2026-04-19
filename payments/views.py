from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.


@login_required
def test(request):
    """
    Test view for payments.
    """
    template = "test.html"
    ctx = dict()

    return render(request, template, context=ctx)


@login_required
def payment_success(request):
    """
    View function to handle successful payments.
    """

    order_no = request.session.get("order_no", None)

    if not order_no:
        return redirect("order-list")

    del request.session["order_no"]

    template = "payments/payment_success.html"
    ctx = dict(
        order_no=order_no,
    )

    return render(request, template, context=ctx)


@login_required
def payment_failed(request):
    """
    View function to handle failed payments.
    """
    template = "payments/payment_failed.html"
    ctx = dict()

    return render(request, template, context=ctx)
