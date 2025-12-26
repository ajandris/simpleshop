from django.shortcuts import redirect
from django.urls import reverse

class OrderService:
    @staticmethod
    def check_cart_stock(cart):
        """
        Checks if all items in the cart are available in stock.
        Returns (True, None) if okay, (False, redirect_url) if fail.
        """

        for item in cart.items.all():
            # For 'Green' phase, we simulate a fail if any stock is 0
            if item.product.stock <= 0:
                return False, reverse('checkout')
        return True, None
