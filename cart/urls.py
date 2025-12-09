"""
Product URLs configuration
"""

from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_product, name='add-to-cart'),
    path('remove/', views.remove_from_cart, name='remove-from-cart'),
    path('update/', views.update_cart, name='update-cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('pay/', views.pay_now, name='pay-now'),
    path('coupon/add/', views.add_coupon, name='coupon-add'),
    path('coupon/remove/', views.remove_coupon, name='coupon-remove'),
    path('', views.view_cart, name='cart'),
]
