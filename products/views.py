from decimal import Decimal, InvalidOperation

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Images

# Create your views here.


def catalogue(request, slug):
    """
    View function to display the product catalogue.
    """
    template = "products/catalogue.html"

    cat = get_object_or_404(Category, slug=slug)

    prod = None

    search_criteria = request.GET.get("q")
    min_price_raw = request.GET.get("min")
    max_price_raw = request.GET.get("max")

    # Apply filters safely
    if search_criteria:
        try:
            prod = Product.objects.filter(
                Q(category=cat),
                Q(sku=search_criteria.upper())
                | Q(title__icontains=search_criteria)
                | Q(short_description__icontains=search_criteria)
                | Q(description__icontains=search_criteria)
                | Q(tags__icontains=search_criteria)
                | Q(category__title__icontains=search_criteria)
                | Q(category__description__icontains=search_criteria),
            ).distinct()

        except InvalidOperation:
            pass
    else:
        prod = Product.objects.filter(category=cat).order_by(
            "id", "-updated_at"
        )

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
        "search_criteria": search_criteria or "",
        "qs_without_page": qs_without_page,
        "category": cat,
    }

    return render(request, template_name=template, context=context)


def products(request):
    """
    View function to display a list of products based on filters.
    """

    template = "products/products.html"

    prod = None

    search_criteria = request.GET.get("q")
    min_price_raw = request.GET.get("min")
    max_price_raw = request.GET.get("max")

    # Apply filters safely
    if search_criteria:
        try:
            prod = Product.objects.filter(
                Q(sku=search_criteria.upper())
                | Q(title__icontains=search_criteria)
                | Q(short_description__icontains=search_criteria)
                | Q(description__icontains=search_criteria)
                | Q(tags__icontains=search_criteria)
                | Q(category__title__icontains=search_criteria)
                | Q(category__description__icontains=search_criteria)
            ).distinct()

        except InvalidOperation:
            pass
    else:
        prod = Product.objects.all().order_by("id", "-updated_at")

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
        "search_criteria": search_criteria or "",
        "qs_without_page": qs_without_page,
    }

    return render(request, template_name=template, context=context)


def product_detail(request, slug):
    """
    View function to display the details of a specific product.
    """
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
        if product.image.name.lower() == 'placeholder':
            gallery.append(product.image.url.url)
        else:
            for img in images:
                if img.url.url is not None and img.url.url not in gallery:
                    gallery.append(img.url.url)
    context = {
        "product": product,
        "gallery": gallery,
    }

    return render(request, template_name=template, context=context)
