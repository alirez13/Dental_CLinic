from django.shortcuts import render
from .models import *


def about(request):
    return render(request, 'aboutus/about_us.html')


def dr_tahereh(request):
    tahereh = DrTahereh.objects.all()
    return render(request, 'aboutus/dr.html', context={'tahereh': tahereh})


def dr_saeed(request):
    saeed = DrTahereh.objects.all()
    return render(request, 'aboutus/saeed.html', context={'saeed': saeed})
