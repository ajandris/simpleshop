from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from cart.services import check_cart_stock, calculate_order
from cart.models import Cart
from orders.models import Order
from orders.services import make_order, get_order_hash, email_order_created
from django.urls import reverse

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

