import factory
from products.models import Product
from test.factories.category_factories import CategoryFactory
from test.factories.image_factories import ImagesFactory


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
        # This tells factory_boy to look for an existing category with this name
        django_get_or_create = ('category',)

    title = factory.Sequence(lambda n: f"Product {n}")
    category = factory.SubFactory(CategoryFactory, title="Default Category")
    image = factory.SubFactory(ImagesFactory(name="Placeholder"))