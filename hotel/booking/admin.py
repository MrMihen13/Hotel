from django.contrib import admin

from hotel.booking import models


@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('number', 'room', 'date_start', 'date_end')
