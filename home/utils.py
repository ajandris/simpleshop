""""
Module: utils.py
Description: Utility functions
"""

from django.utils.crypto import get_random_string


def unique_slugify(instance, slug):
    """
        Creates unique slugs
    """
    model = instance.__class__
    slug = slug.lower()
    unique_slug = slug
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = slug + "-" + get_random_string(length=4).lower()
    return unique_slug
