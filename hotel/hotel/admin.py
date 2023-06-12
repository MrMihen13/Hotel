from django.contrib import admin

from hotel.hotel import models


@admin.register(models.Hotel)
class RoomModels(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'country')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('country__name', )


@admin.register(models.Country)
class RoomModels(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
