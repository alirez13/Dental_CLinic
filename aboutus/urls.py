from django.urls import path
from . import views

app_name = 'about_ua'

urlpatterns = [
    path('about_us', views.about, name='about_us'),
    path('dr_tahereh', views.dr_tahereh, name='dr_tahereh'),
    path('dr_saeed', views.dr_saeed, name='dr_saeed'),
]
