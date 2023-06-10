from rest_framework import serializers

from hotel.guest import models


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Guest
        fields = '__all__'
