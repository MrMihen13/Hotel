from django.db import models

from hotel.room import models as room_models
from hotel.guest import models as guest_models


class Booking(models.Model):
    room = models.ForeignKey(room_models.Room, on_delete=models.DO_NOTHING, verbose_name='Номер')

    date_start = models.DateField(verbose_name='Дата начала')
    date_end = models.DateField(verbose_name='Дата конца')

    guest = models.ForeignKey(guest_models.Guest, on_delete=models.DO_NOTHING, verbose_name='Постоялец')

    number = models.CharField(max_length=8, verbose_name='Код бронирования', editable=False)
