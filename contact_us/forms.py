from calendar import calendar

from django import forms
from django.forms import ModelForm
from django.forms import Textarea
from .models import Contact



class ContactForm(ModelForm):
    fullname = forms.CharField(required=True,max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                 label=' نام و نام خانوادگی')
    phone = forms.CharField(required=True,max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                 label=' تلفن شما')

    message = forms.CharField(required=True,max_length=50, widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'پیام خود را بنویسید'}), label='پیام')

    # last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #
    # class Meta:
    #     model = User
    #     fields = ('fullname', 'email', 'city')

    class Meta:
        model = Contact
        fields = ["fullname", "phone","message", ]
        widgets = {
            "message": Textarea(
                attrs={
                    "placeholder": "Would love to talk about Philip K. Dick"
                }
            )
        }
