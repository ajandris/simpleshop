"""
Product URLs configuration
"""

from django.urls import path
from . import views

urlpatterns = [
    path('add/<slug:slug>', views.add_product, name='add-to-cart'),
    path('pay/<slug:slug>', views.pay_now, name='pay-now'),
    path('', views.view_cart, name='cart'),
]
