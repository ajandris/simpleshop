from django.contrib.auth.models import User
from django.db import models

from products.models import Product


# Create your models here.

class Cart(models.Model):
    cart_number = models.CharField(max_length=32, verbose_name='Cart ID', unique=True)
    discount_code = models.CharField(max_length=20, null=False, blank=True, verbose_name="Discount Code")
    # Owner None means it is anonymous cart
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Cart owner",
                              related_name="owner", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='DateTime when record created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='DateTime when record was updated')
    # User None means it is anonymous cart
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                             verbose_name="Last changes user", null=True, blank=True)

    class Meta:
        db_table = 'cart'
        db_table_comment = 'Shopping cart'
        verbose_name = "Cart"
        verbose_name_plural = "Carts"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name="Cart")
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
