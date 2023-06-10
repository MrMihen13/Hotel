from django.contrib import admin

from hotel.room import models


@admin.register(models.Room)
class RoomModels(admin.ModelAdmin):
    list_display = ('number', 'room_class', 'price_per_day')
