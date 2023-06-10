from rest_framework import serializers

from hotel.room import models
from hotel.hotel.serializers import HotelSerializer


class RoomSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(read_only=True)

    class Meta:
        model = models.Room
        fields = (
            'number',
            'hotel',
            'room_class',
            'floor',
            'rooms_number',
            'bathroom_type',
            'has_tv',
            'has_phone',
            'has_air_conditioning',
            'has_refrigerator',
            'has_balcony',
            'is_non_smoking',
            'additional_amenities',
            'price_per_day',
        )
