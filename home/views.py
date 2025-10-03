from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

def index(request):
    template = 'home/index.html'
    return render(request, template)

@login_required
def profile(request):
    template = 'home/profile.html'
    context = {

    }
    return render(request, template, context=context)