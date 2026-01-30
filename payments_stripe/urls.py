"""
Stripe payment URLs
"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('stripe_payment_intent/<str:cart_no>/', views.create_payment_intent,
         name='stripe-payment-intent'),
    path('pk/', views.get_stripe_publishable_key, name='stripe-pk'),
    path('process_payment/', views.complete_payment, name='complete-stripe-payment'),
]
