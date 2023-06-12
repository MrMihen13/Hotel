from rangefilter.filters import NumericRangeFilterBuilder
from django.contrib import admin

from hotel.room import models


@admin.register(models.Room)
class RoomModels(admin.ModelAdmin):
    list_display = ('number', 'room_class', 'price_per_day')
    search_fields = ('number', )
    list_filter = (
        ('price_per_day', NumericRangeFilterBuilder()),
        ('rooms_number', NumericRangeFilterBuilder(
            default_start=2
        )),
        ('floor', NumericRangeFilterBuilder()),
        'room_class', 'bathroom_type',
        'has_tv', 'has_phone', 'has_air_conditioning',
        'has_refrigerator', 'has_balcony', 'is_non_smoking',
    )
