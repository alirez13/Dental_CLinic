from django.urls import path
from .views import ContactCreate

app_name = 'contact'

urlpatterns = [
    path("contact", ContactCreate.as_view(), name="contact"),
   # path("thanks/", thanks, name="thanks"),
]