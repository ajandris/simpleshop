import pytest
from django.contrib.auth.models import User

@pytest.fixture
def user(db):
    """Creates a test user."""
    return User.objects.create_user(username='testuser', password='password123')

