import pytest
from test.factories.user_factories import UserFactory

@pytest.fixture
def user(db):
    return UserFactory.create(username='testuser')
