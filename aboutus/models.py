from django.db import models


class DrTahereh(models.Model):
    bio = models.CharField(max_length=1000, null=True, verbose_name='بیوگرافی')
    image = models.ImageField(upload_to='dr_tahereh')
    resume = models.ImageField(upload_to='dr_tahereh/resume')
    resume1 = models.ImageField(upload_to='dr_tahereh/resume')
    resume2 = models.ImageField(upload_to='dr_tahereh/resume')
    resume3 = models.ImageField(upload_to='dr_tahereh/resume')
    resume4 = models.ImageField(upload_to='dr_tahereh/resume')
    resume5 = models.ImageField(upload_to='dr_tahereh/resume')

    class Meta:
        verbose_name = 'دکتر طاهره'
        verbose_name_plural = 'دکتر طاهره'


class DrSaeed(models.Model):
    bio = models.CharField(max_length=1000, null=True, verbose_name='بیوگرافی')
    image = models.ImageField(upload_to='dr_Saeed')
    resume = models.ImageField(upload_to='dr_Saeed/resume')
    resume1 = models.ImageField(upload_to='dr_Saeed/resume')
    resume2 = models.ImageField(upload_to='dr_Saeed/resume')
    resume3 = models.ImageField(upload_to='dr_Saeed/resume')
    resume4 = models.ImageField(upload_to='dr_Saeed/resume')
    resume5 = models.ImageField(upload_to='dr_Saeed/resume')

    class Meta:
        verbose_name = 'دکتر سعید'
        verbose_name_plural = 'دکتر سعید'
