"""
Payments in general URLs
"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('stripe/', include('payments_stripe.urls')),
    path('test/', views.test, name='stripe_test'),
    path('payment_success/', views.payment_success, name='payment-success'),
    path('payment_failed/', views.payment_failed, name='payment-failed'),
]
