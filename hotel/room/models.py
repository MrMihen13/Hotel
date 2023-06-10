from django.db import models

from hotel.hotel import models as hotel_models


class Room(models.Model):
    class RoomClasses(models.Choices):
        economy = 'Эконом'
        standard = 'Стандарт'
        standard_superior = 'Стандарт улучшенный'
        junior_suite = 'Полулюкс'
        luxury = 'Люкс'

    class BathroomTypes(models.Choices):
        combined = 'Совмещенный'
        separate = 'Раздельный'

    number = models.PositiveIntegerField(verbose_name='Номер')
    hotel = models.ForeignKey(hotel_models.Hotel, on_delete=models.DO_NOTHING, verbose_name='Отель')
    room_class = models.CharField(choices=RoomClasses.choices, max_length=20, verbose_name='Класс номера')
    floor = models.IntegerField(verbose_name='Этаж')
    rooms_number = models.PositiveIntegerField(verbose_name='Количество комнат')
    bathroom_type = models.CharField(choices=BathroomTypes.choices, max_length=12, verbose_name='Тип санузла')

    has_tv = models.BooleanField(verbose_name='Наличие ТВ')
    has_phone = models.BooleanField(verbose_name='Наличие телефона')
    has_air_conditioning = models.BooleanField(verbose_name='Наличие кондиционера')
    has_refrigerator = models.BooleanField(verbose_name='Наличие холодильника')
    has_balcony = models.BooleanField(verbose_name='Наличие балкона')
    is_non_smoking = models.BooleanField(verbose_name='Номер для некурящих')

    additional_amenities = models.TextField(verbose_name='Дополнительные удобства')

    price_per_day = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Стоимость за сутки')
