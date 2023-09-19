from django.db import models


class Contact(models.Model):
    fullname = models.CharField(max_length=100, verbose_name='نام کامل')
    phone = models.CharField(max_length=11, verbose_name=' تلفن همراه', null=True)
    message = models.TextField(max_length=400, verbose_name='متن پیام')


    def __str__(self):
        return f"{self.fullname}  => {self.message}"


    class Meta:
        verbose_name = 'پیغام'
        verbose_name_plural = 'پیغام ها'
