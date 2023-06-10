from rest_framework import serializers

from hotel.hotel import models


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hotel
        fields = '__all__'
