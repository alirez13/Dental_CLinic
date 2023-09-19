from django.shortcuts import render

from blog.models import *


def home(request):
    post = Article.objects.all()[:3]
    return render(request, 'home/index.html', context={'post': post})


def price(request):
    return render(request, 'home/pricing.html')
