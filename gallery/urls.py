from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('gallery_post_d', views.post_dr, name='post_dr'),
    path('gallery_video', views.video, name='video'),
    path('gallery_post_detail_tahere/<str:title>', views.PostDetailDR.as_view(), name='photo_detail_dr'),
    path('gallery_video_detail/<str:title>', views.VideoDetail.as_view(), name='video_detail'),

    path('like/<int:pk>/', views.like, name='like')
]
