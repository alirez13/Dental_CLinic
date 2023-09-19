from django.db import models
from account.models import User
from django.urls import reverse
from django.utils.html import format_html



class Author(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='دکتر')

    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسندگان'

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=50, null=True, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title
    

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='نویسنده', null=True)
    category = models.ManyToManyField(Category, verbose_name='دسته بندی', null=True)
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name='عنوان')
    one_body = models.CharField(max_length=1000, null=True, blank=True, verbose_name='متن اولیه')
    do_you_know = models.CharField(max_length=1000, null=True, blank=True, verbose_name='آیا میدانید')
    two_body = models.CharField(max_length=1000, null=True, blank=True, verbose_name='متن دوم')
    image = models.ImageField(upload_to='image/articles', verbose_name='درج عکس اصلی')
    image1 = models.ImageField(upload_to='image/articles', verbose_name='درج عکس 1', null=True)
    image2 = models.ImageField(upload_to='image/articles', verbose_name='درج عکس 2', null=True)
    image3 = models.ImageField(upload_to='image/articles', verbose_name='درج عکس 3', null=True)
    date = models.DateField(auto_now=True, verbose_name='زمان انتشار', null=True)

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.title])

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="60px" height="50px" >')

    def __str__(self):
        return f"{self.title} - {self.one_body[:30]}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='لایک کننده', related_name='likes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes', null=True,
                                verbose_name='مقاله')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'

    def __str__(self):
        return f"{self.user} - {self.article.title}"
