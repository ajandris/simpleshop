############################################################
#  Cart models
############################################################
from django.contrib.auth.models import User
from django.db import models

from products.models import Product

# Create your models here.


class Coupon(models.Model):
    """
    Coupon model
    """

    code = models.CharField(
        max_length=30, verbose_name="Coupon", db_comment="Coupon code"
    )
    min_subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Minimum Subtotal",
        default=0,
        null=False,
        blank=False,
        db_comment="Minimum subtotal",
    )
    value = models.DecimalField(
        verbose_name="Coupon value",
        max_digits=20,
        decimal_places=2,
        db_comment="Coupon value",
    )
    # percent or amount
    type = models.CharField(
        max_length=30,
        verbose_name="Coupon type",
        db_comment="amount or percent",
    )
    # null -> no restriction
    effective_from = models.DateField(
        verbose_name="Coupon start date",
        null=True,
        blank=True,
        db_comment="Coupon effective from",
    )
    # null -> no restriction
    effective_to = models.DateField(
        verbose_name="Coupon end date",
        null=True,
        blank=True,
        db_comment="Coupon effective to",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="DateTime when record created",
        db_comment="DateTime when record created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="DateTime when record was updated",
        db_comment="DateTime when record was updated",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name="Last changes user",
        null=False,
        blank=False,
        db_comment="The user who made last change",
    )

    def __str__(self):
        """
        Returns the string representation of the model instance.
        """
        return self.code

    class Meta:
        db_table = "coupons"
        db_table_comment = "Coupons"
        verbose_name = "Coupon"
        verbose_name_plural = "Coupons"
        ordering = ["-effective_from", "effective_to", "-created_at"]


class Cart(models.Model):
    """
    Cart model
    """

    cart_number = models.CharField(
        max_length=32,
        verbose_name="Cart ID",
        unique=True,
        db_comment="Cart ID",
    )
    # Owner None means it is an anonymous cart
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Cart owner",
        related_name="owner",
        null=True,
        blank=True,
        db_comment="Cart owner",
    )
    shipping_method = models.CharField(
        max_length=50,
        verbose_name="Shipping method",
        null=True,
        blank=True,
        db_comment="Shipping method",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="DateTime when record created",
        db_comment="DateTime when record created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="DateTime when record was updated",
        db_comment="DateTime when record was updated",
    )
    # User None means it is anonymous cart
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name="Last changes user",
        null=True,
        blank=True,
        db_comment="Last changes user",
    )

    discount = models.ForeignKey(
        Coupon,
        on_delete=models.DO_NOTHING,
        verbose_name="Active Discount",
        null=True,
        blank=True,
        db_comment="Active Discount",
    )

    def __str__(self):
        """
        Returns the string representation of the model instance.
        """
        return self.cart_number

    class Meta:
        db_table = "cart"
        db_table_comment = "Shopping cart"
        verbose_name = "Cart"
        verbose_name_plural = "Carts"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, verbose_name="Cart", db_comment="Cart"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Product",
        db_comment="Product",
    )
    qty = models.PositiveIntegerField(
        verbose_name="Quantity",
        default=1,
        null=False,
        blank=False,
        db_comment="Quantity",
    )
    price = models.DecimalField(
        verbose_name="Price",
        max_digits=10,
        decimal_places=2,
        default=0.01,
        null=False,
        blank=False,
        db_comment="Price",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="DateTime when record created",
        db_comment="DateTime when record created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="DateTime when record was updated",
        db_comment="DateTime when record was updated",
    )
    # User None means it is anonymous cart
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name="Last changes user",
        null=True,
        blank=True,
        db_comment="Last changes user",
    )

    class Meta:
        db_table = "cart_item"
        db_table_comment = "Cart items"
        verbose_name = "Cart item"
        verbose_name_plural = "Cart items"


class Shipping(models.Model):
    title = models.CharField(
        verbose_name="Shipping title",
        max_length=50,
        unique=True,
        db_comment="Shipping title",
    )
    code = models.CharField(
        max_length=50,
        verbose_name="Shipping code",
        unique=True,
        db_comment="Shipping code",
    )
    text_html = models.CharField(
        verbose_name="Shipping text",
        max_length=150,
        blank=False,
        db_comment="Shipping text",
    )
    price = models.DecimalField(
        verbose_name="Shipping price",
        max_digits=10,
        decimal_places=2,
        default=4.99,
        null=False,
        blank=False,
        db_comment="Shipping price",
    )
    discount_threshold = models.DecimalField(
        verbose_name="Shipping discount threshold",
        max_digits=10,
        decimal_places=2,
        default=10000.00,
        null=False,
        blank=False,
        db_comment="Shipping discount threshold",
    )
    price_discounted = models.DecimalField(
        verbose_name="Discounted shipping price",
        max_digits=10,
        decimal_places=2,
        default=0.00,
        null=False,
        blank=False,
        db_comment="Discounted shipping price",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="DateTime when record created",
        db_comment="DateTime when record created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="DateTime when record was updated",
        db_comment="DateTime when record was updated",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name="Last changes user",
        null=False,
        blank=False,
        db_comment="Last changes user",
    )

    def __str__(self):
        """
        Returns the string representation of the model instance.
        """
        return self.code

    class Meta:
        db_table = "shipping"
        db_table_comment = "Shipping rates"
        verbose_name = "Shipping rate"
        verbose_name_plural = "Shipping rates"
