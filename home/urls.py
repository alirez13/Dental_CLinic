from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='main'),
    path('price', views.price, name='price')
]
