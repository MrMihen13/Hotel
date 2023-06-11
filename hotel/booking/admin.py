from django.contrib import admin

from hotel.booking import models


@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('number', 'room', 'date_start', 'date_end')

    def save_model(self, request, obj, form, change):
        super().save_model(self, request, obj, form)
