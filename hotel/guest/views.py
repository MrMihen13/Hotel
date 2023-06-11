from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from hotel.guest import serializers, models


class ListGuestAPIView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.GuestSerializer
    queryset = models.Guest.objects.all()
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['arrival_date', 'departure_date']