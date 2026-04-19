"""
Orders URLs
"""

from django.urls import path
from . import views

urlpatterns = [
    path("myorders/", views.orders_list, name="order-list"),
    path(
        "order_detail/<str:order_no>/",
        views.orders_details,
        name="order-detail",
    ),
]
