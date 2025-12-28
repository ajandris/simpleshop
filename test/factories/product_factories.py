import factory

from products.models import Product
from test.factories.category_factories import CategoryFactory
from test.factories.image_factories import ImagesFactory
from test.factories.user_factories import UserFactory

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Sequence(lambda n: f"Product {n}")
    sku = factory.Sequence(lambda n: f"SKU-{n}")
    category = factory.SubFactory(CategoryFactory, title="Default Category")
    image = factory.SubFactory(ImagesFactory, name="Placeholder")
    user = factory.SubFactory(UserFactory, username="testuser")