from django.contrib import admin

from cart.models import Cart, CartItem, Coupon, Shipping


# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_number', 'discount', 'owner')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'qty', 'price', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'type', 'value', 'effective_from', 'effective_to', 'created_at', 'updated_at', 'user')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'text_html', 'price', 'discount_threshold', 'price_discounted',
                    'created_at', 'updated_at', 'user')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('code',)