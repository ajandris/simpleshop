"""
Profile URLs
"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('writeme/', views.writeme, name='contact-form'),
    path('profile/', views.profile_generalinfo, name='profile'),
    path('profile/generalinfo/', views.profile_generalinfo, name='profile_generalinfo'),
    path('profile/security/', views.profile_security, name='profile_security'),
    path('profile/addresses/', views.profile_addresses, name='profile_addresses'),
    path('profile/addresses/new/', views.profile_addresses_new, name='profile_addresses_new'),
    path('profile/addresses/add/', views.profile_addresses_add, name='profile_addresses_add'),
    path('profile/addresses/edit_show/', views.profile_addresses_edit_show, name='profile_addresses_edit_show'),
    path('profile/addresses/edit/', views.profile_addresses_edit, name='profile_addresses_edit'),
    path('profile/addresses/delete/', views.profile_addresses_delete, name='profile_addresses_delete'),
    path('profile/addresses/makedefault/', views.profile_addresses_make_default, name='profile_addresses_make_default'),
]
