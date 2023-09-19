from django.contrib import admin
from .models import *


admin.site.register(Category)
admin.site.register(Author)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'show_image')
    list_editable = ("title",)
    list_filter = ('title',)
    search_fields = ('title',)
    fields = ('author',
              'category', 'title', 'one_body', 'do_you_know', 'two_body', 'image', 'image1', 'image2', 'image3',
              'date')
    readonly_fields = ['date']


admin.site.register(Like)
