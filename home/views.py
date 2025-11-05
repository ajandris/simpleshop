from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model
from allauth.account.models import EmailAddress

from products.models import Category


# Create your views here.

def index(request):
    template = 'home/index.html'

    categories = Category.objects.filter(is_featured=True).order_by('title')
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