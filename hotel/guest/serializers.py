from rest_framework import serializers

from hotel.guest import models
from hotel.hotel import serializers as hotel_serializers
from hotel.room import serializers as room_serializers


class GuestSerializer(serializers.ModelSerializer):
    room = room_serializers.RoomSerializer(read_only=True)
    hotel = hotel_serializers.HotelSerializer(read_only=True)
    country = hotel_serializers.CountrySerializer(read_only=True)

    class Meta:
        model = models.Guest
        fields = (
            'room',

            'name',
            'last_name',
            'middle_name',

            'country',
            'hotel',

            'passport_series',
            'passport_number',
            'passport_date_issue',
            'passport_place_issue',

            'arrival_date',
            'departure_date',
        )
