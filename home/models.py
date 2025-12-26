from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile_owner')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Name")
    surname = models.CharField(max_length=100, blank=True, null=True, verbose_name="Name")
    email = models.EmailField(max_length=100, blank=False, null=False, verbose_name="email")
    inserted_at = models.DateTimeField(auto_now_add=True, verbose_name='DateTime when record inserted')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='DateTime when record updated')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'profile'
        db_table_comment = 'User profiles'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

class Address(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_default = models.BooleanField(default=False, verbose_name="Is default")
    address_line1 = models.CharField(max_length=250, null=False, blank=False, verbose_name="Address line 1")
    address_line2 = models.CharField(max_length=250, null=True, blank=True, verbose_name="Address line 2")
    city = models.CharField(max_length=100, null=False, blank=False, verbose_name="City")
    state = models.CharField(max_length=100, null=True, blank=True, verbose_name="State/ province")
    country = models.CharField(max_length=2, null=False, blank=False,
                               verbose_name="Country", default="GB")
    postal_code = models.CharField(max_length=10, null=True, blank=False, verbose_name="Postal Code")
    for_shipping = models.BooleanField(default=True, verbose_name="Shipping Address")
    for_billing = models.BooleanField(default=True, verbose_name="Billing Address")
    inserted_at = models.DateTimeField(auto_now_add=True, verbose_name='DateTime when record inserted')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='DateTime when record updated')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'address'
        db_table_comment = 'User Addresses'
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


class BaseLog(models.Model):
    LEVEL_CHOICES = [('INFO', 'Info'), ('WARN', 'Warning'), ('ERR', 'Error')]

    inserted_at = models.DateTimeField(auto_now_add=True, verbose_name='DateTime when record inserted')
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='INFO')
    action = models.CharField(max_length=255)
    order_reference = models.CharField(max_length=100, null=True, blank=True)
    data = models.JSONField(null=True, blank=True)  # Stores request/response snippets

    class Meta:
        abstract = True