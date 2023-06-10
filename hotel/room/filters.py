import coreapi
from datetime import date

from django_filters import filterset
from django_filters.filters import BaseInFilter
from django.db.models import QuerySet, Q

from hotel.booking import models as booking_models
from hotel.room import models as room_models


def get_free_rooms(rooms: QuerySet[room_models.Room],
                   date_start: str = date.today(), date_end: str = None) -> QuerySet[room_models.Room]:
    if date_start and date_end:
        free_rooms_ids = booking_models.Booking.objects.filter(
            Q(date_start__lt=date_start, date_end__lt=date_start) | Q(date_start__gt=date_start, date_end__gt=date_end)
        ).values_list('room_id', flat=True)
        return rooms.filter(id__in=free_rooms_ids)

    free_rooms_ids = booking_models.Booking.objects.filter(
        Q(date_start__lt=date_start, date_end__lt=date_start) | Q(date_start__gt=date_start)
    ).values_list('room_id', flat=True)
    return rooms.filter(id__in=free_rooms_ids)


class RoomDateFilter(BaseInFilter):
    class FilterField:
        name: str
        description: str

        def __init__(self, name, description):
            self.name = name
            self.description = description

    filterset_base = filterset.FilterSet
    start_date = FilterField(name='start', description='start date')
    end_date = FilterField(name='end', description='end date')

    def filter_queryset(self, request, rooms, view):
        date_start = request.GET.get(self.start_date.name)
        date_end = request.GET.get(self.end_date.name)

        if date_start and date_end:
            return get_free_rooms(rooms=rooms, date_start=date_start, date_end=date_end)

        if date_start and not date_end:
            return get_free_rooms(rooms=rooms, date_start=date_start)

        return get_free_rooms(rooms=rooms)

    def get_schema_fields(self, view):
        return [
            coreapi.Field(
                name=self.start_date.name,
                required=False,
                location="query",
                description=self.start_date.description,
            ),
            coreapi.Field(
                name=self.end_date.name,
                required=False,
                location="query",
                description=self.end_date.description,
            )
        ]
