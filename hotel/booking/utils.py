from datetime import date, datetime, timedelta

from django.db.models import QuerySet, Q

from hotel.booking import models


def __get_date_list(date_start: str = date.today(), date_end: str = None) -> list:
    dates_list = list()

    if isinstance(date_start, str):
        date_start = datetime.strptime(date_start, '%Y-%m-%d').date()

    if not date_end:
        return [date_start]

    date_end = datetime.strptime(date_end, '%Y-%m-%d').date()

    while date_start <= date_end:
        dates_list.append(date_start)
        date_start += timedelta(days=1)

    return dates_list


def get_bookings(
        bookings: QuerySet[models.Booking] = models.Booking.objects.all(),
        date_start: str = date.today(), date_end: str = None) -> QuerySet[models.Booking]:
    if not date_start:
        date_start = date.today()

    if date_end:
        return bookings.filter(
            Q(date_start__in=__get_date_list(date_start=date_start, date_end=date_end)) |
            Q(date_end__in=__get_date_list(date_start=date_start, date_end=date_end))
        )
    return bookings.filter(Q(date_start__lt=date_start, date_end__gt=date_start))


def check_booking_availability(date_start: str = date.today(), date_end: str = None) -> bool:
    return not get_bookings(date_start=date_start, date_end=date_end).exists()
