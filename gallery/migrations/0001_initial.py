# Generated by Django 4.2 on 2023-09-17 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='موضوع فیلم')),
                ('one_body', models.CharField(blank=True, max_length=200, null=True, verbose_name=' توضیحات راجب فیلم')),
                ('cover', models.ImageField(upload_to='image/cover', verbose_name='تصویر پیشنمایش')),
                ('video', models.FileField(blank=True, upload_to='video/gallery', verbose_name='درج ویدئو ')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.author', verbose_name='دکتر مربوطه')),
            ],
            options={
                'verbose_name': 'فیلم',
                'verbose_name_plural': 'فیلم ها',
            },
        ),
        migrations.CreateModel(
            name='Post_Tahere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='علت مراجعه بیمار')),
                ('one_body', models.CharField(blank=True, max_length=200, null=True, verbose_name=' توضیح مختصر از مشکل بیمار')),
                ('two_body', models.CharField(blank=True, max_length=100, null=True, verbose_name=' کار های انجام شده بر روی بیمار')),
                ('image', models.ImageField(blank=True, upload_to='image/gallery', verbose_name='درج عکس اصلی')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='image/gallery', verbose_name='درج عکس 1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='image/gallery', verbose_name='درج عکس 2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='image/gallery', verbose_name='درج عکس 3')),
                ('before', models.ImageField(blank=True, null=True, upload_to='image/gallery', verbose_name='قبل')),
                ('after', models.ImageField(blank=True, null=True, upload_to='image/gallery', verbose_name='بعد')),
                ('category', models.ManyToManyField(to='blog.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'نمونه کار دکتر طاهره',
                'verbose_name_plural': 'نمونه کارهای دکتر طاهره',
            },
        ),
        migrations.CreateModel(
            name='Post_Saeid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='علت مراجعه بیمار')),
                ('one_body', models.CharField(blank=True, max_length=200, null=True, verbose_name=' توضیح مختصر از مشکل بیمار')),
                ('two_body', models.CharField(blank=True, max_length=100, null=True, verbose_name=' کار های انجام شده بر روی بیمار')),
                ('image', models.ImageField(blank=True, upload_to='image/gallery', verbose_name='درج عکس اصلی')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='image/gallery', verbose_name='درج عکس 1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='image/gallery', verbose_name='درج عکس 2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='image/gallery', verbose_name='درج عکس 3')),
                ('before', models.ImageField(blank=True, null=True, upload_to='image/gallery', verbose_name='قبل')),
                ('after', models.ImageField(blank=True, null=True, upload_to='image/gallery', verbose_name='بعد')),
                ('category', models.ManyToManyField(to='blog.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'نمونه کار دکتر سعید',
                'verbose_name_plural': 'نمونه کارهای دکتر سعید',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='gallery.post_tahere', verbose_name='مقاله')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'پسند',
                'verbose_name_plural': 'پسند ها',
                'ordering': ('-created_at',),
            },
        ),
    ]
