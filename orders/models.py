import uuid

from django.contrib.auth.models import User
from django.db import models


class OrderStatuses(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    inserted_at = models.DateTimeField(auto_now_add=True, verbose_name='DateTime when record inserted')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='DateTime when record updated')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'order_statuses'
        verbose_name = 'Order Status'
        verbose_name_plural = 'Order Statuses'

class Order(models.Model):
    order_no = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False, blank=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='order_owner')
    order_date = models.DateTimeField(auto_now_add=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=False, blank=False,
                                   verbose_name='Subtotal Calculated')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=False, blank=False,
                                verbose_name='Order Total Calculated')
    vat_included = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=False, blank=False,
                                       verbose_name='Included VAT Calculated')
    currency = models.CharField(max_length=3, default='GBP', verbose_name='Order Currency', null=False,
                                blank=False)
    cart_no = models.CharField(max_length=100, verbose_name='Cart Number', null=False, blank=False)
    billing_address = models.TextField(null=False, blank=False)
    shipping_address = models.TextField(null=False, blank=False)
    billing_name = models.CharField(max_length=50, null=False, blank=False)
    billing_surname = models.CharField(max_length=50, null=False, blank=False)
    shipping_name = models.CharField(max_length=50, null=False, blank=False)
    shipping_surname = models.CharField(max_length=50, null=False, blank=False)
    shipping_method = models.CharField(max_length=30, null=False, blank=False)
    shipping_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    status = models.ForeignKey(OrderStatuses, on_delete=models.DO_NOTHING)

    inserted_at = models.DateTimeField(auto_now_add=True, verbose_name='DateTime when record inserted')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='DateTime when record updated')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='order_user_records')

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"Order {self.order_no}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    sku = models.CharField(max_length=50, null=False, blank=False)
    item = models.TextField(null=False, blank=False)
    quantity = models.PositiveIntegerField(null=False, blank=False)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    inserted_at = models.DateTimeField(auto_now_add=True, verbose_name='DateTime when record inserted')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='DateTime when record updated')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.sku

    def line_amount(self):
        return self.quantity * self.unit_price

    class Meta:
        db_table = 'order_items'
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'