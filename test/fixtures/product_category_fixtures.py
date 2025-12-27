import pytest
from products.models import Category

@pytest.fixture
def product_category(db, user, default_image):
    category = Category.objects.create(
        title="Christmas Decorations",
        slug="christmas-decorations",
        description="Christmas Decorations",
        image=default_image,
        user=user,
    )
    return category