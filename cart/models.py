from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum, F, DecimalField

from products.models import Product


# Create your models here.


class Coupon(models.Model):
    code = models.CharField(max_length=30, verbose_name="Coupon")
    min_subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Minimum Subtotal",
                                       default=0, null=False, blank=False)
    value = models.DecimalField(verbose_name="Coupon value", max_digits=20, decimal_places=2)
    # percent or amount
    type = models.CharField(max_length=30, verbose_name="Coupon type", db_comment='amount or percent')
    # null -> no restriction
    effective_from = models.DateField(verbose_name="Coupon start date", null=True, blank=True)
    # null -> no restriction
    effective_to = models.DateField(verbose_name="Coupon end date", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='DateTime when record created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='DateTime when record was updated')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                             verbose_name="Last changes user", null=False, blank=False)

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'coupons'
        db_table_comment = 'Coupons'
        verbose_name = "Coupon"
        verbose_name_plural = "Coupons"
        ordering = ['-effective_from', 'effective_to', '-created_at']


class Cart(models.Model):
    cart_number = models.CharField(max_length=32, verbose_name='Cart ID', unique=True)
    # Owner None means it is an anonymous cart
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Cart owner",
                              related_name="owner", null=True, blank=True)
    shipping_method = models.CharField(max_length=50, verbose_name='Shipping method', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='DateTime when record created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='DateTime when record was updated')
    # User None means it is anonymous cart
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                             verbose_name="Last changes user", null=True, blank=True)

    discount = models.ForeignKey(Coupon, on_delete=models.DO_NOTHING,
                                 verbose_name="Active Discount", null=True, blank=True)

    def __str__(self):
        return self.cart_number

    class Meta:
        db_table = 'cart'
        db_table_comment = 'Shopping cart'
        verbose_name = "Cart"
        verbose_name_plural = "Carts"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name="Cart", related_name="cartitems")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")
    qty = models.PositiveIntegerField(verbose_name="Quantity", default=1, null=False, blank=False)
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2,
                                default=0.01, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='DateTime when record created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='DateTime when record was updated')
    # User None means it is anonymous cart
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                             verbose_name="Last changes user", null=True, blank=True)

    class Meta:
        db_table = 'cart_item'
        db_table_comment = 'Cart items'
        verbose_name = "Cart item"
        verbose_name_plural = "Cart items"


class Shipping(models.Model):
    title = models.CharField(verbose_name="Shipping title", max_length=50, unique=True)
    code = models.CharField(max_length=50, verbose_name="Shipping code", unique=True)
    text_html = models.CharField(verbose_name="Shipping text", max_length=150, blank=False)
    price = models.DecimalField(verbose_name="Shipping price", max_digits=10, decimal_places=2,
                                default=4.99, null=False, blank=False)
    discount_threshold = models.DecimalField(verbose_name="Shipping discount threshold", max_digits=10,
                                             decimal_places=2, default=10000.00, null=False, blank=False)
    price_discounted = models.DecimalField(verbose_name="Discounted shipping price", max_digits=10, decimal_places=2,
                                           default=0.00, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='DateTime when record created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='DateTime when record was updated')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                             verbose_name="Last changes user", null=False, blank=False)

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'shipping'
        db_table_comment = 'Shipping rates'
        verbose_name = "Shipping rate"
        verbose_name_plural = "Shipping rates"

