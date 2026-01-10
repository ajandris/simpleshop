import factory
from orders.models import OrderStatuses
from test.factories.user_factories import UserFactory

class OrderStatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderStatuses
        django_get_or_create = ('code',)

    code = "PENDING"
    name = 'Pending order'
    description = 'Order created, waiting for payment'
    user = factory.SubFactory(UserFactory, username="testuser")
