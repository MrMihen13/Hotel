from rest_framework import serializers


class AvailabilityBookingSerializers(serializers.Serializer):
    is_available = serializers.BooleanField()
