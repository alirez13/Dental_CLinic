from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog', views.blog, name='blog'),
    path('detail/<str:title>', views.BlogDetail.as_view(), name='detail'),
    path('search', views.search, name='search'),
    path('blog/like/<int:pk>', views.likes, name='like')
]
