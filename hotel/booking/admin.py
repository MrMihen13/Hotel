from datetime import date, timedelta

from random import choice
from string import ascii_uppercase

from rangefilter.filters import DateRangeFilterBuilder
from django.contrib import admin

from hotel.booking import models


@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('number', 'room', 'date_start', 'date_end')
    readonly_fields = ('number', )
    search_fields = ('number', 'room__number')
    list_filter = (
        ('date_start', DateRangeFilterBuilder(
            default_start=date.today(),
        )),
        ('date_end', DateRangeFilterBuilder(
            default_end=date.today() + timedelta(days=7),
        )),
    )

    def save_model(self, request, obj, form, change):
        obj.number = "".join(choice(ascii_uppercase + '1234567890') for i in range(8))
        super().save_model(request, obj, form, change)
