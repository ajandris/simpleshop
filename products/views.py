from decimal import Decimal, InvalidOperation

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Images, ProductImages


# Create your views here.

def catalogue(request, slug):
    template = 'products/catalogue.html'

    cat = get_object_or_404(Category, slug=slug)

    prod = Product.objects.filter(category=cat).order_by("id", "-updated_at")

    min_price_raw = request.GET.get("min")
    max_price_raw = request.GET.get("max")

    # Apply filters safely
    if min_price_raw:
        try:
            prod = prod.filter(price__gte=Decimal(min_price_raw))
        except InvalidOperation:
            pass  # ignore bad input
    if max_price_raw:
        try:
            prod = prod.filter(price__lte=Decimal(max_price_raw))
        except InvalidOperation:
            pass

    # Pagination
    paginator = Paginator(prod, 12)  # 12 per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Build querystring without 'page' so links preserve filters
    params = request.GET.copy()
    params.pop("page", None)
    qs_without_page = params.urlencode()

    context = {
        "page_obj": page_obj,
        "min_price": min_price_raw or "",
        "max_price": max_price_raw or "",
        "qs_without_page": qs_without_page,
        "category": cat,
    }

    return render(request, template_name=template, context=context)

def products(request):

    template = 'products/products.html'

    prod = Product.objects.all().order_by("id", "-updated_at")

    min_price_raw = request.GET.get("min")
    max_price_raw = request.GET.get("max")

    # Apply filters safely
    if min_price_raw:
        try:
            prod = prod.filter(price__gte=Decimal(min_price_raw))
        except InvalidOperation:
            pass  # ignore bad input
    if max_price_raw:
        try:
            prod = prod.filter(price__lte=Decimal(max_price_raw))
        except InvalidOperation:
            pass

    # Pagination
    paginator = Paginator(prod, 12)  # 12 per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Build querystring without 'page' so links preserve filters
    params = request.GET.copy()
    params.pop("page", None)
    qs_without_page = params.urlencode()

    context = {
        "page_obj": page_obj,
        "min_price": min_price_raw or "",
        "max_price": max_price_raw or "",
        "qs_without_page": qs_without_page
    }

    return render(request, template_name=template, context=context)


def product_detail(request, slug):
    template = "products/product_details.html"
    product = get_object_or_404(Product, slug=slug)
    # Build gallery: primary image first, then extras (unique by URL)
    sql = """select im.* 
                from products p 
                    left join product_images pi on (p.id = pi.product_id)
                    left join images im on (pi.image_id = im.id)
                where p.slug = %s
                order by pi.number_in_gallery
            """
    images = Images.objects.raw(sql, [slug])
    gallery = []
    if images is None:
        gallery.append(product.image.url)
    else:
        for img in images:
            if img.url is not None and img.url.url not in gallery:
                gallery.append(img.url.url)
    context = {
        "product": product,
        "gallery": gallery,
    }

    return render(request, template_name=template, context=context)
