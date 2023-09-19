from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from DR_Alizadeh import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('', include('home.urls')),
    path('', include('blog.urls')),
    path('', include('gallery.urls')),
    path('', include('account.urls')),
    path('', include('contact_us.urls')),
    path('', include('aboutus.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
