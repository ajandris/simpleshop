from django.contrib.auth.models import User
import factory
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        # This tells factory_boy to look for an existing category with this name
        django_get_or_create = ('username',)

    username = "testuser"
    password = "password123@."