"""
Cart factories for testing
"""
import factory
from cart.models import Cart
from test.factories.user_factories import UserFactory

class CartFactory(factory.django.DjangoModelFactory):
    """
    Creates Base Cart object. Cart Items will be added later in fixtures
    """
    class Meta:
        model = Cart

    cart_number = factory.Sequence(lambda n: f"cart-dsajh{n}76sdvsga")
    owner = factory.SubFactory(UserFactory, username='testuser')
    user = factory.SubFactory(UserFactory, username='testuser')
    discount = None
    shipping_method = 'standard'