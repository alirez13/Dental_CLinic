# Generated by Django 4.2 on 2023-09-17 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_like_post_alter_like_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='cover',
            field=models.ImageField(null=True, upload_to='image/cover', verbose_name='تصویر پیشنمایش'),
        ),
    ]
