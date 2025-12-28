import factory
from products.models import Images
from test.factories.user_factories import UserFactory

class ImagesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Images
        django_get_or_create = ('name',)

    name = "Placeholder"
    url = 'images/000_product_placeholder.png',
    user = factory.SubFactory(UserFactory, username="testuser"),
