import uuid

from django.contrib.auth.models import User
from django.db import models


class OrderStatuses(models.Model):
    code = models.CharField(max_length=50, unique=True, db_comment="Code")
    name = models.CharField(max_length=50, db_comment="Name")
    description = models.TextField(
        null=True, blank=True, db_comment="Description"
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

    def __str__(self):
        """
        Returns the string representation of the model instance.
        """
        return self.code

    class Meta:
        db_table = "order_statuses"
        db_table_comment = "Order Statuses"
        verbose_name = "Order Status"
        verbose_name_plural = "Order Statuses"


class Order(models.Model):
    order_no = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        null=False,
        blank=True,
        db_comment="Order no",
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name="order_owner",
        db_comment="Owner",
    )
    order_date = models.DateTimeField(
        auto_now_add=True, db_comment="Order date"
    )
    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        null=False,
        blank=False,
        verbose_name="Subtotal Calculated",
        db_comment="Subtotal Calculated",
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        null=False,
        blank=False,
        verbose_name="Order Total Calculated",
        db_comment="Order Total Calculated",
    )
    vat_included = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        null=False,
        blank=False,
        verbose_name="Included VAT Calculated",
        db_comment="Included VAT Calculated",
    )
    currency = models.CharField(
        max_length=3,
        default="GBP",
        verbose_name="Order Currency",
        null=False,
        blank=False,
        db_comment="Order Currency",
    )
    cart_no = models.CharField(
        max_length=100,
        verbose_name="Cart Number",
        null=False,
        blank=False,
        db_comment="Cart Number",
    )
    billing_address = models.TextField(
        null=False, blank=False, db_comment="Billing address"
    )
    shipping_address = models.TextField(
        null=False, blank=False, db_comment="Shipping address"
    )
    billing_name = models.CharField(
        max_length=50, null=False, blank=False, db_comment="Billing name"
    )
    billing_surname = models.CharField(
        max_length=50, null=False, blank=False, db_comment="Billing surname"
    )
    shipping_name = models.CharField(
        max_length=50, null=False, blank=False, db_comment="Shipping name"
    )
    shipping_surname = models.CharField(
        max_length=50, null=False, blank=False, db_comment="Shipping surname"
    )
    shipping_method = models.CharField(
        max_length=30, null=False, blank=False, db_comment="Shipping method"
    )
    shipping_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        db_comment="Shipping price",
    )
    email = models.EmailField(
        max_length=254,
        null=True,
        blank=True,
        verbose_name="Email",
        db_comment="Email to send order status updates",
    )
    discount_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        default=0,
        db_comment="Discount amount",
    )
    status = models.ForeignKey(
        OrderStatuses, on_delete=models.DO_NOTHING, db_comment="Status"
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
        User,
        on_delete=models.DO_NOTHING,
        related_name="order_user_records",
        db_comment="User",
    )

    class Meta:
        db_table = "orders"
        db_table_comment = "Orders"
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        """
        Returns the string representation of the model instance.
        """
        return f"Order {self.order_no}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, db_comment="Order"
    )
    sku = models.CharField(
        max_length=50, null=False, blank=False, db_comment="Sku"
    )
    item = models.TextField(null=False, blank=False, db_comment="Item")
    quantity = models.PositiveIntegerField(
        null=False, blank=False, db_comment="Quantity"
    )
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        db_comment="Unit price",
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

    def __str__(self):
        """
        Returns the string representation of the model instance.
        """
        return self.sku

    def line_amount(self):
        """
        Calculates the total amount for an order line item.
        """
        return self.quantity * self.unit_price

    class Meta:
        db_table = "order_items"
        db_table_comment = "Order Items"
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"
