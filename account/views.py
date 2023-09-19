import requests
import ghasedakpack
from uuid import uuid4
from .models import Otp
from .models import User
from random import randint
from django.views import View
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm, OtpForm, AddressCreationForm

SMS = ghasedakpack.Ghasedak('')


class UserLogin(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', context={'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                form.add_error('phone', "شماره تلفن نامعتبر")
        else:
            form.add_error('phone', 'اطلاعات نامعتبر')

        return render(request, 'account/login.html', context={'form': form})


class UserRegister(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'account/register.html', context={'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            randcode = randint(1000, 9999)
            cd = form.cleaned_data
            SMS.verification({'receptor': '09900480112', 'type': '1', 'template': randcode, 'param1': '1234'})
            token = str(uuid4())
            Otp.objects.create(phone=cd['phone'], code=randcode, token=token)
            print(randcode)
            return redirect(reverse('account:check_otp') + f'?token={token}')

        else:
            form.add_error('phone', 'اطلاعات نامعتبر')

        return render(request, 'account/register.html', context={'form': form})


class CheckOtp(View):
    def get(self, request):
        form = OtpForm()
        return render(request, 'account/check_otp.html', context={'form': form})

    def post(self, request):
        token = request.GET.get('token')
        form = OtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code=cd['code'], token=token).exists():
                otp = Otp.objects.get(token=token)
                user, is_created = User.objects.get_or_create(phone=otp.phone)
                login(request, user)
                otp.delete()
                return redirect("/")

        else:
            form.add_error('code', 'اطلاعات نامعتبر')

        return render(request, 'account/check_otp.html', context={'form': form})


def userlogout(request):
    logout(request)
    return redirect("/")


class AddressAddView(View):
    def post(self, request):
        form = AddressCreationForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)
            return render(request, 'account/addressadd.html', context={'form': form})

    def get(self, request):
        form = AddressCreationForm()
        return render(request, 'account/addressadd.html', context={'form': form})
