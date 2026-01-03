"""
Profile URLs
"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('process_payment/', views.process_payment, name='process-payment'),
]