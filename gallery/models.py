from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from blog.models import Category, Author


class Post_Tahere(models.Model):
    category = models.ManyToManyField(Category, verbose_name='دسته بندی')
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name='علت مراجعه بیمار')
    one_body = models.CharField(max_length=200, null=True, blank=True, verbose_name=' توضیح مختصر از مشکل بیمار')
    two_body = models.CharField(max_length=100, null=True, blank=True, verbose_name=' کار های انجام شده بر روی بیمار')
    image = models.ImageField(upload_to='image/gallery', verbose_name='درج عکس اصلی', blank=True)
    image1 = models.ImageField(upload_to='image/gallery', verbose_name='درج عکس 1', null=True, blank=True)
    image2 = models.ImageField(upload_to='image/gallery', verbose_name='درج عکس 2', null=True, blank=True)
    image3 = models.ImageField(upload_to='image/gallery', verbose_name='درج عکس 3', null=True, blank=True)
    before = models.ImageField(upload_to='image/gallery', verbose_name='قبل', null=True, blank=True)
    after = models.ImageField(upload_to='image/gallery', verbose_name='بعد', null=True, blank=True)

    class Meta:
        verbose_name = 'نمونه کار دکتر '
        verbose_name_plural = 'نمونه کارهای دکتر '

    def get_absolute_url(self):
        return reverse('gallery:photo_detail_dr', args=[self.title])

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="60px" height="50px" >')

    def __str__(self):
        return f"{self.title} - {self.one_body[:30]}"





class Video(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name='موضوع فیلم')
    doctor = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='دکتر مربوطه', null=True)
    one_body = models.CharField(max_length=200, null=True, blank=True, verbose_name=' توضیحات راجب فیلم')
    cover = models.ImageField(upload_to='image/cover', verbose_name='تصویر پیشنمایش', null=True)
    video = models.FileField(upload_to='video/gallery', verbose_name='درج ویدئو ', blank=True)

    class Meta:
        verbose_name = 'فیلم'
        verbose_name_plural = 'فیلم ها'

    def get_absolute_url(self):
        return reverse('gallery:video_detail', args=[self.title])

    def __str__(self):
        return f"{self.title} - {self.one_body[:30]}"


class Like(models.Model):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='like', verbose_name='کاربر')
    post = models.ForeignKey(Post_Tahere, on_delete=models.CASCADE, related_name='like', verbose_name='مقاله')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.phone} - {self.post.title}'
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'پسند'
        verbose_name_plural = 'پسند ها'

