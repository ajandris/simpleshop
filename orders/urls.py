"""
Orders URLs
"""
from django.urls import path
from . import views

urlpatterns = [
    path('process_payment/', views.process_payment, name='process-payment'),
    path('myorders/', views.orders_list, name='order-list'),
    path('order_detail/<str:order_no>/', views.orders_details, name='order-detail'),
    path('cart_validation/<str:cart_no>/', views.cart_validation, name='cart-validation'),
]