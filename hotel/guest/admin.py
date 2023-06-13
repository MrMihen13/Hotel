from datetime import date, timedelta

from django.contrib import admin
from rangefilter.filters import DateRangeFilterBuilder

from hotel.guest import models


@admin.register(models.Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'address', 'country', 'arrival_date', 'departure_date')
    list_filter = (
        ('arrival_date', DateRangeFilterBuilder(
            default_start=date.today(),
        )),
        ('departure_date', DateRangeFilterBuilder(
            default_end=date.today() + timedelta(days=7),
        )),
        'country'
    )
    search_fields = ('name', 'last_name', 'middle_name')
