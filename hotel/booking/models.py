from django.db import models
from django.contrib.auth import get_user_model

from hotel.room import models as room_models

USER = get_user_model()


class Booking(models.Model):
    room = models.ForeignKey(room_models.Room, on_delete=models.DO_NOTHING, verbose_name='Номер')

    date_start = models.DateField(verbose_name='Дата начала')
    date_end = models.DateField(verbose_name='Дата конца')

    guest = models.ForeignKey(USER, on_delete=models.DO_NOTHING, verbose_name='Постоялец')

    number = models.IntegerField(verbose_name='Код бронирования')
