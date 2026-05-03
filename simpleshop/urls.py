"""
URL configuration for simpleshop project.
"""

from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path, include

handler404 = "home.errors.custom_404"

urlpatterns = [
    path("products/", include("products.urls")),
    path("cart/", include("cart.urls")),
    path("orders/", include("orders.urls")),
    path("payment/", include("payments.urls")),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
else:
    from django.urls import re_path
    from django.views.static import serve
    from django.utils.cache import patch_cache_control

    def cached_serve(request, path, document_root=None, show_indexes=False):
        response = serve(request, path, document_root, show_indexes)
        # Cache media files for 1 year
        patch_cache_control(response, public=True, max_age=31536000)
        return response
    
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', cached_serve, {'document_root': settings.MEDIA_ROOT}),
    ]
