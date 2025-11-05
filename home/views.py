from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model
from allauth.account.models import EmailAddress
from collections import defaultdict
from products.models import Category, Product


# Create your views here.

def index(request):
    template = 'home/index.html'

    categories = list(Category.objects.filter(is_featured=True).order_by('title'))
    products = Product.objects.filter(category__in=categories).order_by('category__title', '-inserted_at')

    top_by_cat = defaultdict(list)
    for p in products:
        bucket = top_by_cat[p.category_id]
        if len(bucket) < 8:
            bucket.append(p)

    # attach for template convenience (no extra queries)
    cat_map = {c.id: c for c in categories}
    for cid, items in top_by_cat.items():
        setattr(cat_map[cid], 'top_products', items)

    cont = {'categories': categories}

    return render(request, template, context=cont)

@login_required
def profile(request):
    if request.method == 'POST':
        if request.POST.get('action') == 'general_info':
            user = get_user_model().objects.get(username=request.user.username)
            user.first_name = request.POST.get('name')
            user.last_name = request.POST.get('surname')
            user.save()

    template = 'home/profile.html'
    a_user = get_user_model()
    user = a_user.objects.filter(username=request.user.username).values().first()
    email = EmailAddress.objects.filter(user_id=request.user.id).values().first()

    context = {
        "user_data": user,
        "email": email
    }
    return render(request, template, context=context)