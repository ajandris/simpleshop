"""
URL configuration for simpleshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
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
