from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from hotel.room import models, serializers
from hotel.room import filters as room_filters


class ListRoomAPIView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.RoomSerializer
    queryset = models.Room.objects.all()

    filter_backends = [room_filters.RoomDateFilter, DjangoFilterBackend, filters.SearchFilter, ]
    filterset_fields = [
        'has_tv',
        'has_phone',
        'has_air_conditioning',
        'has_refrigerator',
        'has_balcony',
    ]
    search_fields = ['number', ]
