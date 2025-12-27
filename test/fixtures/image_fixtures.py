import pytest

from products.models import Images

@pytest.fixture
def default_image(db, user):
    """
    Placeholder image
    """
    image = Images.objects.create(
        name='placeholder',
        url='images/000_product_placeholder.png',
        user=user,
    )
    return image
