from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Эл.почта")
    avatar = models.ImageField(upload_to='users/avatars', blank=True, null=True, verbose_name='Аватар',
                              help_text='Загрузити фотографию')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона', help_text='Введите номер телефона', blank=True, null=True)
    city = models.CharField(max_length=40, verbose_name="Город", blank=True, null=True,
                               help_text="Введите город проживания")