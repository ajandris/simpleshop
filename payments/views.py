from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def test(request):
    template = 'test.html'
    ctx = dict()

    return render(request, template, context=ctx)

@login_required
def payment_success(request):
    template = 'payments/payment_success.html'
    ctx = dict()

    return render(request, template, context=ctx)


@login_required
def payment_failed(request):
    template = 'payments/payment_failed.html'
    ctx = dict()

    return render(request, template, context=ctx)
