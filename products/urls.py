"""
Product URLs configuration
"""


from django.urls import path
from . import views

urlpatterns = [
    path('catalogue/<slug:slug>/', views.catalogue, name='catalogue'),
    path('<slug:slug>/', views.product_detail, name='product-detail'),
    path('', views.products, name='products'),
]
