from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login', views.UserLogin.as_view(), name='login'),
    path('register', views.UserRegister.as_view(), name='register'),
    path('check_otp', views.CheckOtp.as_view(), name='check_otp'),
    path('address_add', views.AddressAddView.as_view(), name='address_add'),
    path('logout', views.userlogout, name='logout'),
]
