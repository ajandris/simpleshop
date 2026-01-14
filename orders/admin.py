from django.contrib import admin

from orders.models import Order, OrderItem, OrderStatuses


# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_no', 'order_date', 'subtotal', 'total', 'vat_included', 'currency', 'cart_no',
                    'billing_address', 'shipping_address', 'billing_name', 'billing_surname', 'shipping_name',
                    'shipping_surname', 'shipping_method', 'shipping_price', 'discount_amount', 'status',
                    'inserted_at', 'updated_at', 'user', 'owner'
    )
    readonly_fields = ('order_no', 'order_date', 'subtotal', 'total', 'vat_included', 'currency', 'cart_no',
                    'billing_address', 'shipping_address', 'billing_name', 'billing_surname', 'shipping_name',
                    'shipping_surname', 'shipping_method', 'shipping_price', 'discount_amount', 'status',
                    'inserted_at', 'updated_at', 'user', 'owner'
    )

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
                    'order', 'sku', 'item', 'quantity', 'unit_price',
                    'inserted_at', 'updated_at', 'user'
    )
    readonly_fields = (
                    'order', 'sku', 'item', 'quantity', 'unit_price',
                    'inserted_at', 'updated_at', 'user'
    )

@admin.register(OrderStatuses)
class OrderStatusesAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'description', 'inserted_at', 'updated_at', 'user')
    readonly_fields = ('inserted_at', 'updated_at',)
