from django.contrib import admin

from hotel.hotel import models


@admin.register(models.Hotel)
class RoomModels(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')


@admin.register(models.Country)
class RoomModels(admin.ModelAdmin):
    list_display = ('name', )
