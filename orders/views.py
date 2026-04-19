from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from orders.models import Order


@login_required
def orders_list(request):
    """
    View function to display a list of orders.
    """
    template = "orders/orders_list.html"
    orders = Order.objects.filter(owner=request.user).order_by("-order_date")

    context = {"orders": orders}

    return render(request, template_name=template, context=context)


@login_required
def orders_details(request, order_no):
    """
    View function to display details of a specific order.
    """
    template = "orders/order_details.html"
    order = get_object_or_404(Order, order_no=order_no)

    context = {"order": order}

    return render(request, template_name=template, context=context)
