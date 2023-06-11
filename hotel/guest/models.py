from django.db import models

from hotel.hotel import models as hotel_models
from hotel.room import models as room_models


class Guest(models.Model):
    room = models.ForeignKey(room_models.Room, on_delete=models.DO_NOTHING, verbose_name='Номер в отеле')

    name = models.CharField(max_length=128, verbose_name='Имя')
    last_name = models.CharField(max_length=128, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=123, verbose_name='Отчество')

    country = models.ForeignKey(hotel_models.Country, on_delete=models.DO_NOTHING, verbose_name='Страна')
    hotel = models.ForeignKey(hotel_models.Hotel, on_delete=models.DO_NOTHING, verbose_name='Отель')

    passport_series = models.DecimalField(max_digits=6, decimal_places=0, verbose_name='Серия паспорта')
    passport_number = models.DecimalField(max_digits=6, decimal_places=0, verbose_name='Номер паспорта')
    passport_date_issue = models.DateField(verbose_name='Дата выдачи паспорта')
    passport_place_issue = models.TextField(verbose_name='Место выдачи паспорта')

    arrival_date = models.DateField(verbose_name='Дата приезда')
    departure_date = models.DateField(verbose_name='Дата отъезда')

    def __str__(self):
        return f'{self.room} {self.name} {self.last_name}'

    class Meta:
        verbose_name = 'Постоялец'
        verbose_name_plural = 'Постояльцы'
