from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="profile_owner",
        db_comment="Profile owner",
    )
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Name",
        db_comment="Name",
    )
    surname = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Surname",
        db_comment="Surname",
    )
    email = models.EmailField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name="email",
        db_comment="email",
    )
    inserted_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="DateTime when record inserted",
        db_comment="DateTime when record inserted",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="DateTime when record updated",
        db_comment="DateTime when record updated",
    )
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, db_comment="User"
    )

    class Meta:
        db_table = "profile"
        db_table_comment = "User profiles"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


class Address(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, db_comment="Profile"
    )
    is_default = models.BooleanField(
        default=False, verbose_name="Is default", db_comment="Is default"
    )
    address_line1 = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        verbose_name="Address line 1",
        db_comment="Address line 1",
    )
    address_line2 = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name="Address line 2",
        db_comment="Address line 2",
    )
    city = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="City",
        db_comment="City",
    )
    state = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="State/ province",
        db_comment="State/ province",
    )
    country = models.CharField(
        max_length=2,
        null=False,
        blank=False,
        verbose_name="Country",
        default="GB",
        db_comment="Country",
    )
    postal_code = models.CharField(
        max_length=10,
        null=True,
        blank=False,
        verbose_name="Postal Code",
        db_comment="Postal Code",
    )
    for_shipping = models.BooleanField(
        default=True,
        verbose_name="Shipping Address",
        db_comment="Shipping Address",
    )
    for_billing = models.BooleanField(
        default=True,
        verbose_name="Billing Address",
        db_comment="Billing Address",
    )
    inserted_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="DateTime when record inserted",
        db_comment="DateTime when record inserted",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="DateTime when record updated",
        db_comment="DateTime when record updated",
    )
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, db_comment="User"
    )

    class Meta:
        db_table = "address"
        db_table_comment = "User Addresses"
        verbose_name = "Address"
        verbose_name_plural = "Addresses"


class BaseLog(models.Model):
    LEVEL_CHOICES = [("INFO", "Info"), ("WARN", "Warning"), ("ERR", "Error")]

    inserted_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="DateTime when record inserted",
        db_comment="DateTime when record inserted",
    )
    level = models.CharField(
        max_length=10,
        choices=LEVEL_CHOICES,
        default="INFO",
        db_comment="Level",
    )
    action = models.CharField(max_length=255, db_comment="Action")
    order_reference = models.CharField(
        max_length=100, null=True, blank=True, db_comment="Order reference"
    )
    # Stores request/response snippets
    data = models.JSONField(null=True, blank=True, db_comment="Data")

    class Meta:
        abstract = True
