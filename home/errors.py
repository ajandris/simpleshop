"""
Custom errror handling
"""

from django.shortcuts import render


def custom_404(request, exception):
    """
    Custom 404 error handler view.
    """
    template = "error_pages/404.html"
    return render(
        request,
        template,
        {"message": "The page you are looking for does not exist."},
        status=404,
    )
