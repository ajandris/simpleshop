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
    order_no = models.CharField(max_length=50, unique=True)
    order_date = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=3)
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
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.order_no

    def total_amount(self):
        """
        Total order amount calculated
        @return PositiveInteger in the smallest units
        """
        total = 0
        items = OrderItem.objects.filter(order_id=self.id)
        for item in items:
            total += item.line_amount()
        return total

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
        return self.quantity * self.unit_price * 100