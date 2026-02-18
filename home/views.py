import requests

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages
from allauth.account.models import EmailAddress
from collections import defaultdict

from home.models import Profile, Address
from products.models import Category, Product
from simpleshop import settings


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
    return redirect(request, 'profile_generalinfo')

@login_required
def profile_generalinfo(request):
    """
    Profile General info tab
    """
    user = get_user_model().objects.get(username=request.user.username)
    user_profile, created = Profile.objects.\
        get_or_create(owner=user,
                      defaults={
                          'name': user.first_name,
                          'surname': user.last_name,
                          'email': user.email,
                          'user': user,
                      })
    if created:
        user_profile.save()
    if request.method == 'POST':
        user.first_name = request.POST.get('name')
        user.last_name = request.POST.get('surname')
        user.save()
        user_profile.name = request.POST.get('name')
        user_profile.surname = request.POST.get('surname')
        user_profile.save()
    template = 'home/profile_generalinfo.html'
    a_user = get_user_model()
    user = a_user.objects.filter(username=request.user.username).values().first()
    email = EmailAddress.objects.filter(user_id=request.user.id).values().first()

    context = {
        "active_menu": 'general-info',
        "user_data": user,
        "email": email['email']
    }
    return render(request, template, context)

@login_required
def profile_security(request):
    """
    Profile Security tab
    """
    template = 'home/profile_security.html'
    context = {
        "active_menu": 'profile-security',
    }

    return render(request, template, context)

@login_required
def profile_addresses(request):
    """
    Profile Address management tab
    """
    user = get_user_model().objects.get(username=request.user.username)
    user_profile, created = Profile.objects.\
        get_or_create(owner=user,
                      defaults={
                          'name': user.first_name,
                          'surname': user.last_name,
                          'email': user.email,
                          'user': user,
                      })
    if created:
        user_profile.save()

    addresses = Address.objects.filter(profile=user_profile).order_by('-is_default')
    template = 'home/profile_addresses.html'
    context = {
        "active_menu": 'profile-addresses',
        "addresses": addresses,
    }

    return render(request, template, context)

@login_required
def profile_addresses_new(request):
    """
    New Address in Profile
    """
    user = get_user_model().objects.get(username=request.user.username)
    user_profile, created = Profile.objects.\
        get_or_create(owner=user,
                      defaults={
                          'name': user.first_name,
                          'surname': user.last_name,
                          'email': user.email,
                          'user': user,
                      })
    if created:
        user_profile.save()

    template = 'home/profile_addresses_new.html'
    context = {
        "active_menu": 'profile-addresses',
    }
    return render(request, template, context)

@login_required
def profile_addresses_add(request):
    """
    Add Address in Profile
    """
    user = get_user_model().objects.get(username=request.user.username)
    user_profile, created = Profile.objects.\
        get_or_create(owner=user,
                      defaults={
                          'name': user.first_name if not None else '',
                          'surname': user.last_name if not None else '',
                          'email': user.email,
                          'user': user,
                      })
    if created:
        user_profile.save()

    if request.method == 'POST':
        address_count = Address.objects.filter(profile=user_profile).count()
        print('Address Count', address_count)
        address = Address.objects.create(
            profile=user_profile,
            is_default=(address_count == 0),
            address_line1=request.POST.get('address_line1'),
            address_line2=request.POST.get('address_line2'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            postal_code=request.POST.get('postcode'),
            country=request.POST.get('country'),
            user=user
        )
        address.save()
        messages.success(request, 'Address Created')

    return redirect('profile_addresses')

@login_required
def profile_addresses_edit_show(request):
    """
    Edit form for Address in Profile
    """
    user = get_user_model().objects.get(username=request.user.username)
    user_profile, created = Profile.objects.\
        get_or_create(owner=user,
                      defaults={
                          'name': user.first_name,
                          'surname': user.last_name,
                          'email': user.email,
                          'user': user,
                      })
    if created:
        user_profile.save()

    address = get_object_or_404(Address, id=int(request.POST.get('address_id', 0)),profile=user_profile)
    template = 'home/profile_addresses_edit.html'
    context = {
        "active_menu": 'profile-addresses',
        "address": address,
    }
    return render(request, template, context)

@login_required
def profile_addresses_edit(request):
    """
    Edit Address in Profile
    """
    if request.method == 'POST':
        user = get_user_model().objects.get(username=request.user.username)
        user_profile, created = Profile.objects.\
            get_or_create(owner=user,
                          defaults={
                              'name': user.first_name,
                              'surname': user.last_name,
                              'email': user.email,
                              'user': user,
                          })
        if created:
            user_profile.save()

        address_id = int(request.POST.get('address_id'))
        addr = get_object_or_404(Address, id=address_id, profile=user_profile)

        addr.address_line1 = request.POST.get('address_line1')
        addr.address_line2 = request.POST.get('address_line2')
        addr.city = request.POST.get('city')
        addr.state = request.POST.get('state')
        addr.postal_code = request.POST.get('postcode')
        addr.country = request.POST.get('country')
        addr.user = user
        addr.save()

        messages.success(request, "Address Updated")

    return redirect('profile_addresses')


@login_required
def profile_addresses_delete(request):
    """
    Edit Address in Profile
    """
    if request.method == 'POST':
        user = get_user_model().objects.get(username=request.user.username)
        user_profile, created = Profile.objects.\
            get_or_create(owner=user,
                          defaults={
                              'name': user.first_name,
                              'surname': user.last_name,
                              'email': user.email,
                              'user': user,
                          })
        if created:
            user_profile.save()

        address_id = int(request.POST.get('address_id'))
        addr = get_object_or_404(Address, id=address_id, profile=user_profile)
        addr.delete()

        messages.success(request, "Address deleted")

    return redirect('profile_addresses')



@login_required
def profile_addresses_make_default(request):
    """
    Make Default Address in Profile
    """
    if request.method == 'POST':
        user = get_user_model().objects.get(username=request.user.username)
        user_profile, created = Profile.objects.\
            get_or_create(owner=user,
                          defaults={
                              'name': user.first_name,
                              'surname': user.last_name,
                              'email': user.email,
                              'user': user,
                          })
        if created:
            user_profile.save()

        address_id = int(request.POST.get('address_id'))
        addr = get_object_or_404(Address, id=address_id, profile=user_profile)
        addresses = Address.objects.filter(profile=user_profile)

        for address in addresses:
            address.is_default = (address == addr)
            address.save()

        messages.success(request, 'Default address changed')

    return redirect('profile_addresses')

def about(request):
    return render(request, 'home/about.html')

def writeme(request):
    ctx = {
        "site_key": settings.RECAPTCHA_SITE_KEY,
    }
    if request.method == "POST":
        recaptcha_response = request.POST.get('g-recaptcha-response')

        data = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }

        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if not result.get('success'):
            messages.error(request, "reCAPTCHA failed. Please try again.")
            return render(request, 'home/contact_form.html', context=ctx)

        # Process form normally
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # send message
        send_mail(
            subject="News from [The Olde Christmas Market] Contact Form",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )

        # Save, email, or handle message here
        messages.success(request, "Thank you! Your message has been sent.")

    return render(request, 'home/contact_form.html', context=ctx)
