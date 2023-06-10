from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название страны')


class Hotel(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название отеля')
    address = models.TextField(verbose_name='Адрес отеля')
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, verbose_name='Страна')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
