"""
Product URLs configuration
"""

from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_product, name='add-to-cart'),
    path('remove/', views.remove_from_cart, name='remove-from-cart'),
    path('pay/<sku>', views.pay_now, name='pay-now'),
    path('', views.view_cart, name='cart'),
]
