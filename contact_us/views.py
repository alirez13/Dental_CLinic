from django.views.generic import CreateView

from .forms import ContactForm
from .models import Contact
from django.urls import reverse_lazy
from django.http import HttpResponse


class ContactCreate(CreateView):
    model = Contact
    form_class = ContactForm
    templates = 'contact_form.html'
    success_url = reverse_lazy("contact:contact")

