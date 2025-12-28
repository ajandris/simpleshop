import factory
from products.models import Category
from test.factories.user_factories import UserFactory


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        django_get_or_create = ('title',)

    title = "Default Category"
    user = factory.SubFactory(UserFactory(username="testuser"))