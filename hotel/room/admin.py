from rangefilter.filters import NumericRangeFilterBuilder

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.db.models import Q

from hotel.room import models
from hotel.room import filters
from hotel.booking import utils


@admin.register(models.Room)
class RoomModels(admin.ModelAdmin):
    list_display = ('number', 'room_class', 'price_per_day')
    search_fields = ('number',)

    class FreeRoomsFilter(admin.SimpleListFilter):
        title = 'Вид комнаты'
        parameter_name = 'free_rooms_filter'

        def lookups(self, request, model_admin):
            return (
                ('free_rooms', _('Свободные комнаты')),
                ('occupied_rooms', _('Занятые комнаты')),
            )

        def queryset(self, request, queryset):
            if self.value() == 'free_rooms':
                return filters.get_free_rooms(rooms=queryset)
            if self.value() == 'occupied_rooms':
                return queryset.filter(Q(id__in=utils.get_bookings().values_list('room_id', flat=True)))
            return queryset

    list_filter = (
        FreeRoomsFilter,
        ('price_per_day', NumericRangeFilterBuilder()),
        ('rooms_number', NumericRangeFilterBuilder(
            default_start=2
        )),
        ('floor', NumericRangeFilterBuilder()),
        'room_class', 'bathroom_type',
        'has_tv', 'has_phone', 'has_air_conditioning',
        'has_refrigerator', 'has_balcony', 'is_non_smoking',
    )
