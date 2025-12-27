import pytest
from django.urls import reverse

# Note: Will need to import your models once they exist
# from orders.services import OrderService

@pytest.mark.django_db
def test_order_fails_if_stock_insufficient(client, user, product_out_of_stock):
    """
    RED: Test that the order process stops and redirects if stock is low.
    """
    # 1. Setup: User is logged in and has a cart with an item
    client.force_login(user)

    # 2. Action: User clicks the "Pay" button trigger
    response = client.post(reverse('pay-now'))

    # 3. Assert: Should redirect back to checkout with an error message
    assert response.status_code == 302
    assert response.url == reverse('checkout')

    # Optional: Verify a log was created in the payments log table
    # assert PaymentLog.objects.filter(action="STOCK_CHECK_FAILURE").exists()
