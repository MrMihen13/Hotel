from django.contrib import admin

from hotel.guest import models


@admin.register(models.Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'hotel', 'country', 'arrival_date', 'departure_date')
