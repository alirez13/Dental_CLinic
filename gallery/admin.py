from django.contrib import admin
from .models import *


@admin.register(Post_Tahere)
class Post_DrAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'show_image')
    list_editable = ("title",)
    list_filter = ('title',)
    search_fields = ('title',)
    fields = (
        'category', 'title', 'one_body', 'two_body', 'image', 'image1', 'image2', 'image3', 'before', 'after',)




@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title')
    list_editable = ("title",)
    list_filter = ('title',)
    search_fields = ('title',)
    fields = ('doctor', 'title', 'one_body','cover','video')

admin.site.register(Like)
