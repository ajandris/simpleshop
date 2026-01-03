import factory
from products.models import Category
from test.factories.user_factories import UserFactory
from test.factories.image_factories import ImagesFactory

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        django_get_or_create = ('title',)

    title = "Default Category"
    user = factory.SubFactory(UserFactory, username="testuser")
    image = factory.SubFactory(ImagesFactory, name="Placeholder")
