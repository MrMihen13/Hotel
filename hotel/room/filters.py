import coreapi

from django_filters import filterset
from django_filters.filters import BaseInFilter
from django.db.models import QuerySet, Q

from hotel.room import models as room_models
from hotel.booking import utils


def get_free_rooms(
        rooms: QuerySet[room_models.Room], date_start: str = None, date_end: str = None) -> QuerySet[room_models.Room]:
    occupied_rooms_ids = utils.get_bookings(date_start=date_start, date_end=date_end).values_list('room_id', flat=True)
    return rooms.filter(~Q(id__in=occupied_rooms_ids))


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

        return get_free_rooms(rooms=rooms, date_start=date_start, date_end=date_end)

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
